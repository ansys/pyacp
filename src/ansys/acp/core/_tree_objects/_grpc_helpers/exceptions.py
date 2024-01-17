from collections.abc import Iterator
from contextlib import contextmanager

from grpc import RpcError, StatusCode

STATUS_CODE_TO_EXCEPTION_TYPE = {
    StatusCode.INVALID_ARGUMENT: ValueError,
    StatusCode.NOT_FOUND: LookupError,
    StatusCode.ALREADY_EXISTS: RuntimeError,
    StatusCode.DEADLINE_EXCEEDED: TimeoutError,
    StatusCode.PERMISSION_DENIED: PermissionError,
    StatusCode.UNAUTHENTICATED: PermissionError,
    StatusCode.FAILED_PRECONDITION: RuntimeError,
    StatusCode.OUT_OF_RANGE: LookupError,
    StatusCode.UNIMPLEMENTED: NotImplementedError,
    StatusCode.UNAVAILABLE: ConnectionError,
    StatusCode.DATA_LOSS: RuntimeError,
    StatusCode.ABORTED: RuntimeError,
    StatusCode.INTERNAL: RuntimeError,
    StatusCode.UNKNOWN: RuntimeError,
}


@contextmanager
def wrap_grpc_errors() -> Iterator[None]:
    """Wrap gRPC errors in Python exceptions.

    This context manager will catch gRPC errors and re-raise them as Python
    exceptions with simpler error messages. The original error message will
    still be available in the traceback.
    """
    try:
        yield
    except RpcError as exc:
        status = exc.code().value[1].upper()
        details = exc.details().split("\n", 1)[0].strip()
        exception_type = STATUS_CODE_TO_EXCEPTION_TYPE.get(exc.code(), RuntimeError)
        raise exception_type(f"{details} (RPC status code {status})") from exc
