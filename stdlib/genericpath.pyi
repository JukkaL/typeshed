import os
from _typeshed import AnyPath, BytesPath, StrPath, SupportsLessThanT
from typing import List, Sequence, Tuple, Union, overload
from typing_extensions import Literal

# All overloads can return empty string. Ideally, Literal[""] would be a valid
# Iterable[T], so that Union[List[T], Literal[""]] could be used as a return
# type. But because this only works when T is str, we need Sequence[T] instead.
@overload
def commonprefix(m: Sequence[StrPath]) -> str: ...
@overload
def commonprefix(m: Sequence[BytesPath]) -> Union[bytes, Literal[""]]: ...
@overload
def commonprefix(m: Sequence[List[SupportsLessThanT]]) -> Sequence[SupportsLessThanT]: ...
@overload
def commonprefix(m: Sequence[Tuple[SupportsLessThanT, ...]]) -> Sequence[SupportsLessThanT]: ...
def exists(path: AnyPath) -> bool: ...
def getsize(filename: AnyPath) -> int: ...
def isfile(path: AnyPath) -> bool: ...
def isdir(s: AnyPath) -> bool: ...

# These return float if os.stat_float_times() == True,
# but int is a subclass of float.
def getatime(filename: AnyPath) -> float: ...
def getmtime(filename: AnyPath) -> float: ...
def getctime(filename: AnyPath) -> float: ...
def samefile(f1: AnyPath, f2: AnyPath) -> bool: ...
def sameopenfile(fp1: int, fp2: int) -> bool: ...
def samestat(s1: os.stat_result, s2: os.stat_result) -> bool: ...
