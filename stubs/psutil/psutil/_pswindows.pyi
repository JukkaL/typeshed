import enum
from ._common import (
    AccessDenied as AccessDenied,
    ENCODING as ENCODING,
    ENCODING_ERRS as ENCODING_ERRS,
    NoSuchProcess as NoSuchProcess,
    TimeoutExpired as TimeoutExpired,
    conn_tmap as conn_tmap,
    conn_to_ntuple as conn_to_ntuple,
    debug as debug,
    isfile_strict as isfile_strict,
    memoize as memoize,
    parse_environ_block as parse_environ_block,
    usage_percent as usage_percent,
)
from ._psutil_windows import (
    ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
    BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
    HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
    IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
    NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
    REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
)
from typing import Any, NamedTuple

msg: str
__extra__all__: Any
CONN_DELETE_TCB: str
ERROR_PARTIAL_COPY: int
PYPY: Any
AF_LINK: int
AddressFamily: Any
TCP_STATUSES: Any

class Priority(enum.IntEnum):
    ABOVE_NORMAL_PRIORITY_CLASS: Any
    BELOW_NORMAL_PRIORITY_CLASS: Any
    HIGH_PRIORITY_CLASS: Any
    IDLE_PRIORITY_CLASS: Any
    NORMAL_PRIORITY_CLASS: Any
    REALTIME_PRIORITY_CLASS: Any

IOPRIO_VERYLOW: int
IOPRIO_LOW: int
IOPRIO_NORMAL: int
IOPRIO_HIGH: int

class IOPriority(enum.IntEnum):
    IOPRIO_VERYLOW: int
    IOPRIO_LOW: int
    IOPRIO_NORMAL: int
    IOPRIO_HIGH: int

pinfo_map: Any

class scputimes(NamedTuple):
    user: Any
    system: Any
    idle: Any
    interrupt: Any
    dpc: Any

class svmem(NamedTuple):
    total: Any
    available: Any
    percent: Any
    used: Any
    free: Any

class pmem(NamedTuple):
    rss: Any
    vms: Any
    num_page_faults: Any
    peak_wset: Any
    wset: Any
    peak_paged_pool: Any
    paged_pool: Any
    peak_nonpaged_pool: Any
    nonpaged_pool: Any
    pagefile: Any
    peak_pagefile: Any
    private: Any

pfullmem: Any

class pmmap_grouped(NamedTuple):
    path: Any
    rss: Any

pmmap_ext: Any

class pio(NamedTuple):
    read_count: Any
    write_count: Any
    read_bytes: Any
    write_bytes: Any
    other_count: Any
    other_bytes: Any

def convert_dos_path(s): ...
def py2_strencode(s): ...
def getpagesize(): ...
def virtual_memory(): ...
def swap_memory(): ...

disk_io_counters: Any

def disk_usage(path): ...
def disk_partitions(all): ...
def cpu_times(): ...
def per_cpu_times(): ...
def cpu_count_logical(): ...
def cpu_count_physical(): ...
def cpu_stats(): ...
def cpu_freq(): ...
def getloadavg(): ...
def net_connections(kind, _pid: int = ...): ...
def net_if_stats(): ...
def net_io_counters(): ...
def net_if_addrs(): ...
def sensors_battery(): ...
def boot_time(): ...
def users(): ...
def win_service_iter() -> None: ...
def win_service_get(name): ...

class WindowsService:
    def __init__(self, name, display_name) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def name(self): ...
    def display_name(self): ...
    def binpath(self): ...
    def username(self): ...
    def start_type(self): ...
    def pid(self): ...
    def status(self): ...
    def description(self): ...
    def as_dict(self): ...

pids: Any
pid_exists: Any
ppid_map: Any

def is_permission_err(exc): ...
def convert_oserror(exc, pid: Any | None = ..., name: Any | None = ...): ...
def wrap_exceptions(fun): ...
def retry_error_partial_copy(fun): ...

class Process:
    pid: Any
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def ppid(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    def memory_maps(self) -> None: ...
    def kill(self): ...
    def send_signal(self, sig) -> None: ...
    def wait(self, timeout: Any | None = ...): ...
    def username(self): ...
    def create_time(self): ...
    def num_threads(self): ...
    def threads(self): ...
    def cpu_times(self): ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def cwd(self): ...
    def open_files(self): ...
    def connections(self, kind: str = ...): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def ionice_get(self): ...
    def ionice_set(self, ioclass, value) -> None: ...
    def io_counters(self): ...
    def status(self): ...
    def cpu_affinity_get(self): ...
    def cpu_affinity_set(self, value): ...
    def num_handles(self): ...
    def num_ctx_switches(self): ...
