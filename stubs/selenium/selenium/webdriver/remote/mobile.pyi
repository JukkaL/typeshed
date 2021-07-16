from typing import Any

from .command import Command as Command

class Mobile:
    class ConnectionType:
        mask: Any
        def __init__(self, mask) -> None: ...
        @property
        def airplane_mode(self): ...
        @property
        def wifi(self): ...
        @property
        def data(self): ...
    ALL_NETWORK: Any
    WIFI_NETWORK: Any
    DATA_NETWORK: Any
    AIRPLANE_MODE: Any
    def __init__(self, driver) -> None: ...
    @property
    def network_connection(self): ...
    def set_network_connection(self, network): ...
    @property
    def context(self): ...
    @property
    def contexts(self): ...
    @context.setter
    def context(self, new_context) -> None: ...
