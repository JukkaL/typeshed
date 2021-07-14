from psycopg2._psycopg import (
    BINARY as BINARY,
    Binary as Binary,
    DATETIME as DATETIME,
    DataError as DataError,
    DatabaseError as DatabaseError,
    Date as Date,
    DateFromTicks as DateFromTicks,
    Error as Error,
    IntegrityError as IntegrityError,
    InterfaceError as InterfaceError,
    InternalError as InternalError,
    NUMBER as NUMBER,
    NotSupportedError as NotSupportedError,
    OperationalError as OperationalError,
    ProgrammingError as ProgrammingError,
    ROWID as ROWID,
    STRING as STRING,
    Time as Time,
    TimeFromTicks as TimeFromTicks,
    Timestamp as Timestamp,
    TimestampFromTicks as TimestampFromTicks,
    Warning as Warning,
    __libpq_version__ as __libpq_version__,
    apilevel as apilevel,
    paramstyle as paramstyle,
    threadsafety as threadsafety,
)
from typing import Any

def connect(dsn: Any | None = ..., connection_factory: Any | None = ..., cursor_factory: Any | None = ..., **kwargs): ...
