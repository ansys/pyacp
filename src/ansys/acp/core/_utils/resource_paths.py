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

"""Helper functions for dealing with Resource Paths."""

__all__ = ["join"]


def join(*parts: str) -> str:
    """Join parts of a Resource Path into a single string.

    Join parts of a Resource Path by slashes, ensuring that there are no
    double slashes in the result. Leading and trailing slashes are removed.
    """
    return "/".join(parts).replace("//", "/").strip("/")


def to_parts(path: str) -> tuple[str, ...]:
    """Get a tuple representation of the given path."""
    return tuple(path.split("/"))


def common_path(*paths: str) -> str:
    """Get the partial path that all input paths have in common."""
    common_parts = []
    for path_parts in zip(*[to_parts(p) for p in paths]):
        first_path_part = path_parts[0]
        if all(part == first_path_part for part in path_parts):
            common_parts.append(first_path_part)
        else:
            break
    return "/".join(common_parts)
