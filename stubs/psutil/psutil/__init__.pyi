import os
import sys
from ._common import (
    AIX as AIX,
    AccessDenied as AccessDenied,
    BSD as BSD,
    CONN_CLOSE as CONN_CLOSE,
    CONN_CLOSE_WAIT as CONN_CLOSE_WAIT,
    CONN_CLOSING as CONN_CLOSING,
    CONN_ESTABLISHED as CONN_ESTABLISHED,
    CONN_FIN_WAIT1 as CONN_FIN_WAIT1,
    CONN_FIN_WAIT2 as CONN_FIN_WAIT2,
    CONN_LAST_ACK as CONN_LAST_ACK,
    CONN_LISTEN as CONN_LISTEN,
    CONN_NONE as CONN_NONE,
    CONN_SYN_RECV as CONN_SYN_RECV,
    CONN_SYN_SENT as CONN_SYN_SENT,
    CONN_TIME_WAIT as CONN_TIME_WAIT,
    Error as Error,
    FREEBSD as FREEBSD,
    LINUX as LINUX,
    MACOS as MACOS,
    NETBSD as NETBSD,
    NIC_DUPLEX_FULL as NIC_DUPLEX_FULL,
    NIC_DUPLEX_HALF as NIC_DUPLEX_HALF,
    NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN,
    NoSuchProcess as NoSuchProcess,
    OPENBSD as OPENBSD,
    OSX as OSX,
    POSIX as POSIX,
    POWER_TIME_UNKNOWN as POWER_TIME_UNKNOWN,
    POWER_TIME_UNLIMITED as POWER_TIME_UNLIMITED,
    STATUS_DEAD as STATUS_DEAD,
    STATUS_DISK_SLEEP as STATUS_DISK_SLEEP,
    STATUS_IDLE as STATUS_IDLE,
    STATUS_LOCKED as STATUS_LOCKED,
    STATUS_PARKED as STATUS_PARKED,
    STATUS_RUNNING as STATUS_RUNNING,
    STATUS_SLEEPING as STATUS_SLEEPING,
    STATUS_STOPPED as STATUS_STOPPED,
    STATUS_TRACING_STOP as STATUS_TRACING_STOP,
    STATUS_WAITING as STATUS_WAITING,
    STATUS_WAKING as STATUS_WAKING,
    STATUS_ZOMBIE as STATUS_ZOMBIE,
    SUNOS as SUNOS,
    TimeoutExpired as TimeoutExpired,
    WINDOWS as WINDOWS,
    ZombieProcess as ZombieProcess,
)
from typing import Any

if sys.platform == "linux":
    from ._pslinux import (
        IOPRIO_CLASS_BE as IOPRIO_CLASS_BE,
        IOPRIO_CLASS_IDLE as IOPRIO_CLASS_IDLE,
        IOPRIO_CLASS_NONE as IOPRIO_CLASS_NONE,
        IOPRIO_CLASS_RT as IOPRIO_CLASS_RT,
    )
if sys.platform == "win32":
    from ._psutil_windows import (
        ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
        BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
        HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
        IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
        NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
        REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
    )
    from ._pswindows import (
        CONN_DELETE_TCB as CONN_DELETE_TCB,
        IOPRIO_VERYLOW as IOPRIO_VERYLOW,
        IOPRIO_LOW as IOPRIO_LOW,
        IOPRIO_NORMAL as IOPRIO_NORMAL,
        IOPRIO_HIGH as IOPRIO_HIGH,
        win_service_iter as win_service_iter,
        CONN_DELETE_TCB as CONN_DELETE_TCB,
        AF_LINK as AF_LINK,
    )

if sys.platform == "linux":
    PROCFS_PATH: str
AF_LINK: Any
version_info: Any
__version__: Any

class Process:
    def __init__(self, pid: Any | None = ...) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    @property
    def pid(self): ...
    def oneshot(self) -> None: ...
    def as_dict(self, attrs: Any | None = ..., ad_value: Any | None = ...): ...
    def parent(self): ...
    def parents(self): ...
    def is_running(self): ...
    def ppid(self): ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def status(self): ...
    def username(self): ...
    def create_time(self): ...
    def cwd(self): ...
    def nice(self, value: Any | None = ...): ...
    def uids(self): ...
    def gids(self): ...
    def terminal(self): ...
    def num_fds(self): ...
    if sys.platform != "darwin":
        def io_counters(self): ...
        def ionice(self, ioclass: Any | None = ..., value: Any | None = ...): ...
    if sys.platform == "linux":
        def rlimit(self, resource, limits: Any | None = ...): ...
    if sys.platform != "darwin":
        def cpu_affinity(self, cpus: Any | None = ...): ...
    if sys.platform == "linux":
        def cpu_num(self): ...
    def environ(self): ...
    if sys.platform == "win32":
        def num_handles(self): ...
    def num_ctx_switches(self): ...
    def num_threads(self): ...
    def threads(self): ...
    def children(self, recursive: bool = ...): ...
    def cpu_percent(self, interval: Any | None = ...): ...
    def cpu_times(self): ...
    def memory_info(self): ...
    def memory_info_ex(self): ...
    def memory_full_info(self): ...
    def memory_percent(self, memtype: str = ...): ...
    if sys.platform != "darwin":
        def memory_maps(self, grouped: bool = ...): ...
    def open_files(self): ...
    def connections(self, kind: str = ...): ...
    def send_signal(self, sig) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def wait(self, timeout: Any | None = ...): ...

class Popen(Process):
    def __init__(self, *args, **kwargs) -> None: ...
    def __dir__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs): ...
    def __getattribute__(self, name): ...
    def wait(self, timeout: Any | None = ...): ...

def pids(): ...
def pid_exists(pid): ...
def process_iter(attrs: Any | None = ..., ad_value: Any | None = ...): ...
def wait_procs(procs, timeout: Any | None = ..., callback: Any | None = ...): ...
def cpu_count(logical: bool = ...): ...
def cpu_times(percpu: bool = ...): ...
def cpu_percent(interval: Any | None = ..., percpu: bool = ...): ...
def cpu_times_percent(interval: Any | None = ..., percpu: bool = ...): ...
def cpu_stats(): ...
def cpu_freq(percpu: bool = ...): ...

getloadavg = os.getloadavg

def virtual_memory(): ...
def swap_memory(): ...
def disk_usage(path): ...
def disk_partitions(all: bool = ...): ...
def disk_io_counters(perdisk: bool = ..., nowrap: bool = ...): ...
def net_io_counters(pernic: bool = ..., nowrap: bool = ...): ...
def net_connections(kind: str = ...): ...
def net_if_addrs(): ...
def net_if_stats(): ...
if sys.platform == "linux":
    def sensors_temperatures(fahrenheit: bool = ...): ...
    def sensors_fans(): ...
if sys.platform != "win32":
    def sensors_battery(): ...
def boot_time(): ...
def users(): ...

if sys.platform == "linux":
    RLIMIT_AS: Any
    RLIMIT_CORE: Any
    RLIMIT_CPU: Any
    RLIMIT_DATA: Any
    RLIMIT_FSIZE: Any
    RLIMIT_LOCKS: Any
    RLIMIT_MEMLOCK: Any
    RLIMIT_MSGQUEUE: Any
    RLIMIT_NICE: Any
    RLIMIT_NOFILE: Any
    RLIMIT_NPROC: Any
    RLIMIT_RSS: Any
    RLIMIT_RTPRIO: Any
    RLIMIT_SIGPENDING: Any
    RLIMIT_STACK: Any
    RLIM_INFINITY: Any
