# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections.abc import Callable
from functools import wraps
from typing import Concatenate, TypeAlias, TypeVar

from packaging.version import parse as parse_version
from typing_extensions import ParamSpec

from .protocols import Readable

T = TypeVar("T", bound=Readable)
P = ParamSpec("P")
R = TypeVar("R")
_WRAPPED_T: TypeAlias = Callable[Concatenate[T, P], R]


def supported_since(
    version: str | None, err_msg_tpl: str | None = None
) -> Callable[[_WRAPPED_T[T, P, R]], _WRAPPED_T[T, P, R]]:
    """Mark a TreeObjectBase method as supported since a specific server version.

    Raises an exception if the current server version does not match the required version.
    If either the given `version` or the server version is `None`, the decorator does nothing.

    Parameters
    ----------
    version :
        The server version since which the method is supported. If ``None``, the
        decorator does nothing.
    err_msg_tpl :
        A custom error message template. If ``None``, a default error message is used.
    """
    if version is None:
        # return a trivial decorator if no version is specified
        def trivial_decorator(func: _WRAPPED_T[T, P, R]) -> _WRAPPED_T[T, P, R]:
            return func

        return trivial_decorator

    required_version = parse_version(version)

    def decorator(func: _WRAPPED_T[T, P, R]) -> _WRAPPED_T[T, P, R]:
        @wraps(func)
        def inner(self: T, /, *args: P.args, **kwargs: P.kwargs) -> R:
            server_version = self._server_version
            # If the object is not stored, we cannot check the server version.
            if server_version is not None:
                if server_version < required_version:
                    if err_msg_tpl is None:
                        err_msg = (
                            f"The '{func.__name__}' method is only supported since version {version} "
                            f"of the ACP gRPC server. The current server version is {server_version}."
                        )
                    else:
                        err_msg = err_msg_tpl.format(
                            required_version=required_version, server_version=server_version
                        )
                    raise RuntimeError(err_msg)
            return func(self, *args, **kwargs)

        return inner

    return decorator
