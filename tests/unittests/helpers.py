# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

from typing import Any, Optional, TypeVar

__all__ = ["check_property"]

T = TypeVar("T")


def check_property(obj: Any, *, name: str, value: T, set_value: Optional[T] = None):
    assert hasattr(obj, name), f"Object '{obj}' has no property named '{name}'"
    assert (
        getattr(obj, name) == value
    ), f"Test of property '{name}' failed! value '{getattr( obj, name )}' instead of '{value}'."
    if set_value is not None:
        setattr(obj, name, set_value)
        assert (
            getattr(obj, name) == set_value
        ), f"Setter of property '{name}' failed! value '{getattr(obj, name)}' instead of '{value}'."
