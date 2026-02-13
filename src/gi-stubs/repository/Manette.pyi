import typing

from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

MAJOR_VERSION: int = 1
MICRO_VERSION: int = 0
MINOR_VERSION: int = 0
VERSION_S: str = "1.0.alpha"

def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object ManetteDevice

    Signals from ManetteDevice:
      disconnected ()
      button-pressed (ManetteButton)
      button-released (ManetteButton)
      absolute-axis-changed (ManetteAxis, gdouble)
      unmapped-button-pressed (guint)
      unmapped-button-released (guint)
      unmapped-absolute-axis-changed (guint, gdouble)
      unmapped-hat-axis-changed (guint, gchar)

    Signals from GObject:
      notify (GParam)
    """
    def get_current_event_time(self) -> int: ...
    def get_device_type(self) -> DeviceType: ...
    def get_guid(self) -> str: ...
    def get_mapping(self) -> typing.Optional[str]: ...
    def get_name(self) -> str: ...
    def has_axis(self, axis: Axis) -> bool: ...
    def has_button(self, button: Button) -> bool: ...
    def has_input(self, type: int, code: int) -> bool: ...
    def has_rumble(self) -> bool: ...
    def has_user_mapping(self) -> bool: ...
    def remove_user_mapping(self) -> None: ...
    def rumble(
        self, strong_magnitude: float, weak_magnitude: float, milliseconds: int
    ) -> bool: ...
    def save_user_mapping(self, mapping_string: str) -> None: ...
    def supports_mapping(self) -> bool: ...

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """

    parent_class: GObject.ObjectClass = ...

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
    def list_devices(self) -> list[Device]: ...
    @classmethod
    def new(cls) -> Monitor: ...

class MonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MonitorClass()
    """

    parent_class: GObject.ObjectClass = ...

class Axis(GObject.GEnum):
    LEFT_TRIGGER = 4
    LEFT_X = 0
    LEFT_Y = 1
    RIGHT_TRIGGER = 5
    RIGHT_X = 2
    RIGHT_Y = 3

class Button(GObject.GEnum):
    DPAD_DOWN = 1
    DPAD_LEFT = 2
    DPAD_RIGHT = 3
    DPAD_UP = 0
    EAST = 7
    LEFT_PADDLE1 = 15
    LEFT_PADDLE2 = 16
    LEFT_SHOULDER = 11
    LEFT_STICK = 13
    MISC1 = 19
    MISC2 = 20
    MISC3 = 21
    MISC4 = 22
    MISC5 = 23
    MISC6 = 24
    MODE = 10
    NORTH = 4
    RIGHT_PADDLE1 = 17
    RIGHT_PADDLE2 = 18
    RIGHT_SHOULDER = 12
    RIGHT_STICK = 14
    SELECT = 8
    SOUTH = 5
    START = 9
    TOUCHPAD = 25
    WEST = 6

class DeviceType(GObject.GEnum):
    GENERIC = 0
    STEAM_DECK = 1
