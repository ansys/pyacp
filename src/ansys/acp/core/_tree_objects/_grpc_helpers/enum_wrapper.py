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
