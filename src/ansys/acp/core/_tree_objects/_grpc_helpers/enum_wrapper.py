from enum import Enum
from typing import Any, Callable, Dict

__all__ = ["wrap_to_string_enum"]


# mypy doesn't understand this dynamically created Enum, so we have to
# fall back to 'Any'.
def wrap_to_string_enum(
    class_name: str,
    proto_enum: Any,
    module: str,
    *,
    key_converter: Callable[[str], str] = lambda val: val,
    value_converter: Callable[[str], str] = lambda val: val.lower(),
) -> Any:
    """Create a string Enum with the same keys as the given protobuf Enum.

    Values of the enum are the keys, converted to lowercase.

    Returns
    :
        A tuple containing
        - the string enum
        - a conversion function from string enum to protobuf
        - a conversion function from protobuf to string enum
    """
    fields = []
    to_pb_conversion_dict: Dict[Any, int] = {}
    from_pb_conversion_dict: Dict[int, Any] = {}
    for key, pb_value in proto_enum.items():
        enum_key = key_converter(key)
        enum_value = value_converter(key)
        fields.append((enum_key, enum_value))
        to_pb_conversion_dict[enum_value] = pb_value
        from_pb_conversion_dict[pb_value] = enum_value

    res_enum = Enum(class_name, fields, type=str, module=module)  # type: ignore

    def to_pb_conversion_func(val: res_enum) -> int:
        return to_pb_conversion_dict[val]

    def from_pb_conversion_func(val: int) -> res_enum:
        return res_enum(from_pb_conversion_dict[val])

    return (
        res_enum,
        to_pb_conversion_func,
        from_pb_conversion_func,
    )
