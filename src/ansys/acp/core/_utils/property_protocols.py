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

from __future__ import annotations

from typing import Generic, Protocol, TypeVar

GetValueT_co = TypeVar("GetValueT_co", covariant=True)
SetValueT_contra = TypeVar("SetValueT_contra", contravariant=True)


class ReadOnlyProperty(Generic[GetValueT_co], Protocol):
    """Interface definition for read-only properties.

    The main purpose of this protocol is to improve the type hints for
    properties which are created from helper functions.
    """

    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co: ...


class ReadWriteProperty(Generic[GetValueT_co, SetValueT_contra], Protocol):
    """Interface definition for read-write properties.

    The main purpose of this protocol is to improve the type hints for
    properties which are created from helper functions.
    """

    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co: ...

    def __set__(self, obj: object, value: SetValueT_contra) -> None: ...
