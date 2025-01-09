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

from collections.abc import Callable, Mapping
import types
from typing import Any

__all__ = ["wrap_to_string_enum"]

from ansys.acp.core._utils.typing_helper import StrEnum

# mypy doesn't understand this dynamically created Enum, so we have to
# fall back to 'Any'.
_StrEnumT = Any


def wrap_to_string_enum(
    class_name: str,
    proto_enum: Any,
    module: str,
    *,
    key_converter: Callable[[str], str] = lambda val: val,
    value_converter: Callable[[str], str] = lambda val: val.lower(),
    doc: str,
    explicit_value_list: tuple[int, ...] | None = None,
    extra_aliases: Mapping[str, tuple[str, str]] = types.MappingProxyType({}),
) -> tuple[_StrEnumT, Callable[[_StrEnumT], int], Callable[[int], _StrEnumT]]:
    """Create a string Enum with the same keys as the given protobuf Enum.

    Values of the enum are the keys, converted to lowercase.

    Parameters
    ----------
    key_converter :
        A callable which converts the protobuf field names to the string enum field names.
    value_converter :
        A callable which converts the protobuf field names to the string enum values.
    doc :
        The docstring of the enum.
    explicit_value_list :
        A list of values that should be included in the enum. If None, all values are included.
    extra_aliases :
        Allows defining additional fields in the enum which correspond to the same protobuf value.
        The keys are the primary enum field values, and the values are tuples of the alias field name
        and the alias field value.
        Note that the alias will not be used when converting from the protobuf value to the string
        enum: the primary field name will be used instead.

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
        if explicit_value_list is not None:
            if pb_value not in explicit_value_list:
                continue
        enum_key = key_converter(key)
        enum_value = value_converter(key)
        fields.append((enum_key, enum_value))
        to_pb_conversion_dict[enum_value] = pb_value
        from_pb_conversion_dict[pb_value] = enum_value
    for primary_enum_value, (alias_enum_key, alias_enum_value) in extra_aliases.items():
        fields.append((alias_enum_key, alias_enum_value))
        to_pb_conversion_dict[alias_enum_value] = to_pb_conversion_dict[primary_enum_value]

    res_enum: _StrEnumT = StrEnum(class_name, fields, module=module)  # type: ignore
    res_enum.__doc__ = doc

    def to_pb_conversion_func(val: _StrEnumT) -> int:
        val = res_enum(val)  # generates a nicer error if 'val' is not a valid enum value
        return to_pb_conversion_dict[val]

    def from_pb_conversion_func(val: int) -> _StrEnumT:
        return res_enum(from_pb_conversion_dict[val])

    return (
        res_enum,
        to_pb_conversion_func,
        from_pb_conversion_func,
    )
