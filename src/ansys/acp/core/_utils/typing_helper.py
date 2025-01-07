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

"""Helpers for defining type annotations."""
import enum
import os
from typing import TYPE_CHECKING, Union

__all__ = ["PATH", "StrEnum"]

PATH = Union[str, os.PathLike[str]]

# For Python 3.10 and below, emulate the behavior of StrEnum by
# inheriting from str and enum.Enum.
# Note that this does *not* work on Python 3.11+, since the default
# Enum format method has changed and will not return the value of
# the enum member.
# When type checking, always use the Python 3.10 workaround, otherwise
# the StrEnum resolves as 'Any'.
if TYPE_CHECKING:  # pragma: no cover

    class StrEnum(str, enum.Enum):
        """String enum."""

else:
    try:
        from enum import StrEnum
    except ImportError:

        import enum

        class StrEnum(str, enum.Enum):
            """String enum."""

            pass
