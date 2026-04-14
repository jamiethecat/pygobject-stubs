from typing import Final
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GObject

T = TypeVar("T")

MAJOR_VERSION: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
VERSION_S: Final = "0.2.14"

def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_resource() -> Gio.Resource: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object ManetteDevice

    Signals from ManetteDevice:
      event (ManetteEvent)
      button-press-event (ManetteEvent)
      button-release-event (ManetteEvent)
      absolute-axis-event (ManetteEvent)
      hat-axis-event (ManetteEvent)
      disconnected ()

    Signals from GObject:
      notify (GParam)
    """
    def get_device_type(self) -> DeviceType: ...
    def get_guid(self) -> str: ...
    def get_mapping(self) -> str | None: ...
    def get_name(self) -> str: ...
    def has_input(self, type: int, code: int) -> bool: ...
    def has_rumble(self) -> bool: ...
    def has_user_mapping(self) -> bool: ...
    def remove_user_mapping(self) -> None: ...
    def rumble(
        self, strong_magnitude: int, weak_magnitude: int, milliseconds: int
    ) -> bool: ...
    def save_user_mapping(self, mapping_string: str) -> None: ...
    def supports_mapping(self) -> bool: ...

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Event(GObject.GBoxed):
    def get_absolute(self) -> tuple[bool, int, float]: ...
    def get_button(self) -> tuple[bool, int]: ...
    def get_device(self) -> Device: ...
    def get_event_type(self) -> EventType: ...
    def get_hardware_code(self) -> int: ...
    def get_hardware_index(self) -> int: ...
    def get_hardware_type(self) -> int: ...
    def get_hardware_value(self) -> int: ...
    def get_hat(self) -> tuple[bool, int, int]: ...
    def get_time(self) -> int: ...

class Monitor(GObject.Object):
    """
    :Constructors:

    ::

        Monitor(**properties)
        new() -> Manette.Monitor

    Object ManetteMonitor

    Signals from ManetteMonitor:
      device-connected (ManetteDevice)
      device-disconnected (ManetteDevice)

    Signals from GObject:
      notify (GParam)
    """
    def iterate(self) -> MonitorIter: ...
    @classmethod
    def new(cls) -> Monitor: ...

class MonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MonitorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class MonitorIter(GObject.GBoxed):
    def next(self) -> tuple[bool, Device]: ...

class DeviceType(GObject.GEnum):
    GENERIC = 0
    STEAM_DECK = 1

class EventType(GObject.GEnum):
    EVENT_ABSOLUTE = 2
    EVENT_BUTTON_PRESS = 0
    EVENT_BUTTON_RELEASE = 1
    EVENT_HAT = 3
    EVENT_NOTHING = -1
