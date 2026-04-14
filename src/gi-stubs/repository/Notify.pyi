from typing import Any
from typing import Final
from typing import TypeVar

from collections.abc import Callable
from collections.abc import Sequence

from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

EXPIRES_DEFAULT: Final[int]
EXPIRES_NEVER: Final[int]
NOTIFICATION_HINT_ACTION_ICONS: Final = "action-icons"
NOTIFICATION_HINT_CATEGORY: Final = "category"
NOTIFICATION_HINT_DESKTOP_ENTRY: Final = "desktop-entry"
NOTIFICATION_HINT_IMAGE_DATA: Final = "image-data"
NOTIFICATION_HINT_IMAGE_DATA_LEGACY: Final = "image_data"
NOTIFICATION_HINT_IMAGE_PATH: Final = "image-path"
NOTIFICATION_HINT_IMAGE_PATH_LEGACY: Final = "image_path"
NOTIFICATION_HINT_RESIDENT: Final = "resident"
NOTIFICATION_HINT_SOUND_FILE: Final = "sound-file"
NOTIFICATION_HINT_SOUND_NAME: Final = "sound-name"
NOTIFICATION_HINT_SUPPRESS_SOUND: Final = "suppress-sound"
NOTIFICATION_HINT_TRANSIENT: Final = "transient"
NOTIFICATION_HINT_URGENCY: Final = "urgency"
NOTIFICATION_HINT_X: Final = "x"
NOTIFICATION_HINT_Y: Final = "y"
VERSION_MAJOR: Final[int]
VERSION_MICRO: Final[int]
VERSION_MINOR: Final[int]

def get_app_icon() -> str: ...
def get_app_name() -> str: ...
def get_server_caps() -> list[str]: ...
def get_server_info() -> tuple[bool, str, str, str, str]: ...
def init(app_name: str | None = None) -> bool: ...
def is_initted() -> bool: ...
def set_app_icon(app_icon: str | None = None) -> None: ...
def set_app_name(app_name: str) -> None: ...
def uninit() -> None: ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)
        new(summary:str, body:str=None, icon:str=None) -> Notify.Notification

    Object NotifyNotification

    Signals from NotifyNotification:
      closed ()

    Properties from NotifyNotification:
      id -> gint: ID
        The notification ID
      app-name -> gchararray: Application name
        The application name to use for this notification
      app-icon -> gchararray: Application icon
        The application icon to use for this notification as filename or icon theme-compliant name
      summary -> gchararray: Summary
        The summary text
      body -> gchararray: Message Body
        The message body text
      icon-name -> gchararray: Icon Name
        The icon filename or icon theme-compliant name
      closed-reason -> gint: Closed Reason
        The reason code for why the notification was closed

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        app_icon: str | None
        app_name: str | None
        body: str
        closed_reason: int
        icon_name: str
        id: int
        summary: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        app_icon: str | None = ...,
        app_name: str | None = ...,
        body: str = ...,
        icon_name: str = ...,
        id: int = ...,
        summary: str = ...,
    ) -> None: ...
    def add_action(
        self, action: str, label: str, callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def clear_actions(self) -> None: ...
    def clear_hints(self) -> None: ...
    def close(self) -> bool: ...
    def do_closed(self) -> None: ...
    def get_activation_app_launch_context(self) -> Gio.AppLaunchContext | None: ...
    def get_activation_token(self) -> str | None: ...
    def get_closed_reason(self) -> int: ...
    @classmethod
    def new(
        cls, summary: str, body: str | None = None, icon: str | None = None
    ) -> Notification: ...
    def set_app_icon(self, app_icon: str | None = None) -> None: ...
    def set_app_name(self, app_name: str | None = None) -> None: ...
    def set_category(self, category: str) -> None: ...
    def set_hint(self, key: str, value: GLib.Variant | None = None) -> None: ...
    def set_hint_byte(self, key: str, value: int) -> None: ...
    def set_hint_byte_array(self, key: str, value: Sequence[int]) -> None: ...
    def set_hint_double(self, key: str, value: float) -> None: ...
    def set_hint_int32(self, key: str, value: int) -> None: ...
    def set_hint_string(self, key: str, value: str) -> None: ...
    def set_hint_uint32(self, key: str, value: int) -> None: ...
    def set_icon_from_pixbuf(self, icon: GdkPixbuf.Pixbuf) -> None: ...
    def set_image_from_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_urgency(self, urgency: Urgency) -> None: ...
    def show(self) -> bool: ...
    def update(
        self, summary: str, body: str | None = None, icon: str | None = None
    ) -> bool: ...

class NotificationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotificationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def closed(self) -> Callable[[Notification], None]: ...

class ClosedReason(GObject.GEnum):
    API_REQUEST = 3
    DISMISSED = 2
    EXPIRED = 1
    UNDEFIEND = 4
    UNDEFINED = 4
    UNSET = -1

class Urgency(GObject.GEnum):
    CRITICAL = 2
    LOW = 0
    NORMAL = 1
