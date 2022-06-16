from ansys.api.acp.v0.enum_types_pb2 import StatusType


def status_type_to_string(value: int) -> str:
    if value < len(StatusType.keys()):
        return StatusType.keys()[value]

    raise RuntimeError(f"StatusType: {value} exceeds the limit of defined types!")
