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

from collections.abc import Callable, Iterable
from typing import Any, Concatenate, TypeAlias, TypeVar
from weakref import WeakValueDictionary

from typing_extensions import ParamSpec, Self

__all__ = ["ObjectCacheMixin", "constructor_with_cache"]

# Making the cache key type a TypeVar would require higher-kinded TypeVars,
# a feature not (yet) supported by the Python type system. See
#   https://github.com/python/typing/issues/548
# So for now, we alias it to 'Any'
_CACHE_KEY_T: TypeAlias = Any


class ObjectCacheMixin:
    """Mixin class to add an instance cache.

    Adds a cache to the class, enabling constructors decorated with
    ``constructor_with_cache`` to return an existing object instead of
    creating a new instance.
    """

    __slots__: Iterable[str] = ("__weakref__",)

    _OBJECT_CACHE: WeakValueDictionary[_CACHE_KEY_T, Self]

    def __init_subclass__(cls: type[Self]) -> None:
        cls._OBJECT_CACHE = WeakValueDictionary()
        super().__init_subclass__()

    @staticmethod
    def _cache_key_valid(key: _CACHE_KEY_T) -> bool:
        raise NotImplementedError("The _cache_key_valid implementation is missing")


T = TypeVar("T", bound=ObjectCacheMixin, covariant=True)
P = ParamSpec("P")

_WRAPPED_T: TypeAlias = Callable[Concatenate[type[T], P], T]


def constructor_with_cache(
    key_getter: Any, raise_on_invalid_key: bool = True
) -> Callable[[_WRAPPED_T[T, P]], _WRAPPED_T[T, P]]:
    """Enable using the object cache in a constructor classmethod.

    Parameters
    ----------
    key_getter :
        Returns the cache key, given the arguments to the constructor classmethod.
    raise_on_invalid_key :
        Whether an invalid key should be ignored, or raise an exception.
    """

    def decorator(func: _WRAPPED_T[T, P]) -> _WRAPPED_T[T, P]:
        def inner(cls: type[T], /, *args: P.args, **kwargs: P.kwargs) -> T:
            key = key_getter(*args, **kwargs)
            if cls._cache_key_valid(key):
                try:
                    return cls._OBJECT_CACHE[key]
                except KeyError:
                    pass
            else:
                if raise_on_invalid_key:
                    raise ValueError(f"Cache key '{key}' is invalid.")
            instance = func(cls, *args, **kwargs)
            cls._OBJECT_CACHE[key] = instance
            return instance

        return inner

    return decorator
