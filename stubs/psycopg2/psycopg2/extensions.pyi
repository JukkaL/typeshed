from psycopg2._json import register_default_json as register_default_json, register_default_jsonb as register_default_jsonb
from psycopg2._psycopg import (
    AsIs as AsIs,
    BINARYARRAY as BINARYARRAY,
    BOOLEAN as BOOLEAN,
    BOOLEANARRAY as BOOLEANARRAY,
    BYTES as BYTES,
    BYTESARRAY as BYTESARRAY,
    Binary as Binary,
    Boolean as Boolean,
    Column as Column,
    ConnectionInfo as ConnectionInfo,
    DATE as DATE,
    DATEARRAY as DATEARRAY,
    DATETIMEARRAY as DATETIMEARRAY,
    DECIMAL as DECIMAL,
    DECIMALARRAY as DECIMALARRAY,
    DateFromPy as DateFromPy,
    Diagnostics as Diagnostics,
    FLOAT as FLOAT,
    FLOATARRAY as FLOATARRAY,
    Float as Float,
    INTEGER as INTEGER,
    INTEGERARRAY as INTEGERARRAY,
    INTERVAL as INTERVAL,
    INTERVALARRAY as INTERVALARRAY,
    ISQLQuote as ISQLQuote,
    Int as Int,
    IntervalFromPy as IntervalFromPy,
    LONGINTEGER as LONGINTEGER,
    LONGINTEGERARRAY as LONGINTEGERARRAY,
    Notify as Notify,
    PYDATE as PYDATE,
    PYDATEARRAY as PYDATEARRAY,
    PYDATETIME as PYDATETIME,
    PYDATETIMEARRAY as PYDATETIMEARRAY,
    PYDATETIMETZ as PYDATETIMETZ,
    PYDATETIMETZARRAY as PYDATETIMETZARRAY,
    PYINTERVAL as PYINTERVAL,
    PYINTERVALARRAY as PYINTERVALARRAY,
    PYTIME as PYTIME,
    PYTIMEARRAY as PYTIMEARRAY,
    QueryCanceledError as QueryCanceledError,
    QuotedString as QuotedString,
    ROWIDARRAY as ROWIDARRAY,
    STRINGARRAY as STRINGARRAY,
    TIME as TIME,
    TIMEARRAY as TIMEARRAY,
    TimeFromPy as TimeFromPy,
    TimestampFromPy as TimestampFromPy,
    TransactionRollbackError as TransactionRollbackError,
    UNICODE as UNICODE,
    UNICODEARRAY as UNICODEARRAY,
    Xid as Xid,
    adapt as adapt,
    adapters as adapters,
    binary_types as binary_types,
    connection as connection,
    cursor as cursor,
    encodings as encodings,
    encrypt_password as encrypt_password,
    get_wait_callback as get_wait_callback,
    libpq_version as libpq_version,
    lobject as lobject,
    new_array_type as new_array_type,
    new_type as new_type,
    parse_dsn as parse_dsn,
    quote_ident as quote_ident,
    register_type as register_type,
    set_wait_callback as set_wait_callback,
    string_types as string_types,
)
from psycopg2._range import Range as Range
from typing import Any

ISOLATION_LEVEL_AUTOCOMMIT: int
ISOLATION_LEVEL_READ_UNCOMMITTED: int
ISOLATION_LEVEL_READ_COMMITTED: int
ISOLATION_LEVEL_REPEATABLE_READ: int
ISOLATION_LEVEL_SERIALIZABLE: int
ISOLATION_LEVEL_DEFAULT: Any
STATUS_SETUP: int
STATUS_READY: int
STATUS_BEGIN: int
STATUS_SYNC: int
STATUS_ASYNC: int
STATUS_PREPARED: int
STATUS_IN_TRANSACTION = STATUS_BEGIN
POLL_OK: int
POLL_READ: int
POLL_WRITE: int
POLL_ERROR: int
TRANSACTION_STATUS_IDLE: int
TRANSACTION_STATUS_ACTIVE: int
TRANSACTION_STATUS_INTRANS: int
TRANSACTION_STATUS_INERROR: int
TRANSACTION_STATUS_UNKNOWN: int

def register_adapter(typ, callable) -> None: ...

class SQL_IN:
    def __init__(self, seq) -> None: ...
    def prepare(self, conn) -> None: ...
    def getquoted(self): ...

class NoneAdapter:
    def __init__(self, obj) -> None: ...
    def getquoted(self, _null: bytes = ...): ...

def make_dsn(dsn: Any | None = ..., **kwargs): ...

JSON: Any
JSONARRAY: Any
JSONB: Any
JSONBARRAY: Any
k: Any
