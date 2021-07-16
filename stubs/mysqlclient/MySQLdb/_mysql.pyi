from typing import Any, ClassVar, overload

import MySQLdb._exceptions

version_info: tuple

class DataError(MySQLdb._exceptions.DatabaseError): ...
class DatabaseError(MySQLdb._exceptions.Error): ...
class Error(MySQLdb._exceptions.MySQLError): ...
class IntegrityError(MySQLdb._exceptions.DatabaseError): ...
class InterfaceError(MySQLdb._exceptions.Error): ...
class InternalError(MySQLdb._exceptions.DatabaseError): ...
class MySQLError(Exception): ...
class NotSupportedError(MySQLdb._exceptions.DatabaseError): ...
class OperationalError(MySQLdb._exceptions.DatabaseError): ...
class ProgrammingError(MySQLdb._exceptions.DatabaseError): ...
class Warning(Warning, MySQLdb._exceptions.MySQLError): ...

class connection:
    client_flag: ClassVar[member_descriptor] = ...
    converter: ClassVar[member_descriptor] = ...
    open: ClassVar[member_descriptor] = ...
    port: ClassVar[member_descriptor] = ...
    server_capabilities: ClassVar[member_descriptor] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _get_native_connection(self, *args, **kwargs) -> Any: ...
    def affected_rows(self, *args, **kwargs) -> Any: ...
    def autocommit(self, *args, **kwargs) -> Any: ...
    def change_user(self, *args, **kwargs) -> Any: ...
    def character_set_name(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    def commit(self, *args, **kwargs) -> Any: ...
    def dump_debug_info(self, *args, **kwargs) -> Any: ...
    def errno(self, *args, **kwargs) -> Any: ...
    def error(self, *args, **kwargs) -> Any: ...
    def escape(obj, dict) -> Any: ...
    @overload
    def escape_string(s) -> Any: ...
    @overload
    def escape_string(s) -> Any: ...
    @overload
    def escape_string(s) -> Any: ...
    def field_count(self, *args, **kwargs) -> Any: ...
    def fileno(self, *args, **kwargs) -> Any: ...
    def get_autocommit(self, *args, **kwargs) -> Any: ...
    def get_character_set_info(self, *args, **kwargs) -> Any: ...
    def get_host_info(self, *args, **kwargs) -> Any: ...
    def get_proto_info(self, *args, **kwargs) -> Any: ...
    def get_server_info(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def insert_id(self, *args, **kwargs) -> Any: ...
    def kill(self, *args, **kwargs) -> Any: ...
    @overload
    def next_result() -> Any: ...
    @overload
    def next_result() -> Any: ...
    def ping() -> Any: ...
    def query(self, *args, **kwargs) -> Any: ...
    def read_query_result(self, *args, **kwargs) -> Any: ...
    def rollback(self, *args, **kwargs) -> Any: ...
    def select_db(self, *args, **kwargs) -> Any: ...
    def send_query(self, *args, **kwargs) -> Any: ...
    def set_character_set(self, *args, **kwargs) -> Any: ...
    def set_server_option(option) -> Any: ...
    def shutdown(self, *args, **kwargs) -> Any: ...
    def sqlstate(self, *args, **kwargs) -> Any: ...
    def stat(self, *args, **kwargs) -> Any: ...
    def store_result(self, *args, **kwargs) -> Any: ...
    @overload
    def string_literal(obj) -> Any: ...
    @overload
    def string_literal(obj) -> Any: ...
    @overload
    def string_literal(obj) -> Any: ...
    def thread_id(self, *args, **kwargs) -> Any: ...
    def use_result(self, *args, **kwargs) -> Any: ...
    def warning_count(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class result:
    converter: ClassVar[member_descriptor] = ...
    has_next: ClassVar[member_descriptor] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def data_seek(n) -> Any: ...
    def describe(self, *args, **kwargs) -> Any: ...
    def fetch_row(self, *args, **kwargs) -> Any: ...
    def field_flags(self, *args, **kwargs) -> Any: ...
    def num_fields(self, *args, **kwargs) -> Any: ...
    def num_rows(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

def connect(*args, **kwargs) -> Any: ...
def debug(*args, **kwargs) -> Any: ...
def escape(obj, dict) -> Any: ...
@overload
def escape_string(s) -> Any: ...
@overload
def escape_string(s) -> Any: ...
@overload
def escape_string(s) -> Any: ...
def get_client_info() -> Any: ...
@overload
def string_literal(obj) -> Any: ...
@overload
def string_literal(obj) -> Any: ...
@overload
def string_literal(obj) -> Any: ...
