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

from typing import Any, Callable

__all__ = ["wrap_to_string_enum"]

from ansys.acp.core._typing_helper import StrEnum


# mypy doesn't understand this dynamically created Enum, so we have to
# fall back to 'Any'.
def wrap_to_string_enum(
    class_name: str,
    proto_enum: Any,
    module: str,
    *,
    key_converter: Callable[[str], str] = lambda val: val,
    value_converter: Callable[[str], str] = lambda val: val.lower(),
    doc: str,
) -> tuple[StrEnum, Callable[[StrEnum], int], Callable[[int], StrEnum]]:
    """Create a string Enum with the same keys as the given protobuf Enum.

    Values of the enum are the keys, converted to lowercase.

    Returns
    -------
    :
        A tuple containing
        - the string enum
        - a conversion function from string enum to protobuf
        - a conversion function from protobuf to string enum
    """
    fields = []
    to_pb_conversion_dict: dict[Any, int] = {}
    from_pb_conversion_dict: dict[int, Any] = {}
    for key, pb_value in proto_enum.items():
        enum_key = key_converter(key)
        enum_value = value_converter(key)
        fields.append((enum_key, enum_value))
        to_pb_conversion_dict[enum_value] = pb_value
        from_pb_conversion_dict[pb_value] = enum_value

    res_enum = StrEnum(class_name, fields, module=module)
    res_enum.__doc__ = doc

    def to_pb_conversion_func(val: StrEnum) -> int:
        return to_pb_conversion_dict[val]

    def from_pb_conversion_func(val: int) -> StrEnum:
        return res_enum(from_pb_conversion_dict[val])

    return (
        res_enum,
        to_pb_conversion_func,
        from_pb_conversion_func,
    )
