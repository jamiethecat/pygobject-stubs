import typing

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

WALLPAPER_TARGET_BOTH: int = 0

class InputCapturePointerBarrier(GObject.Object):
    """
    :Constructors:

    ::

        InputCapturePointerBarrier(**properties)

    Object XdpInputCapturePointerBarrier

    Properties from XdpInputCapturePointerBarrier:
      x1 -> gint: Pointer barrier x offset
        The pointer barrier x offset in logical pixels
      x2 -> gint: Pointer barrier x offset
        The pointer barrier x offset in logical pixels
      y1 -> gint: Pointer barrier y offset
        The pointer barrier y offset in logical pixels
      y2 -> gint: Pointer barrier y offset
        The pointer barrier y offset in logical pixels
      id -> guint: Pointer barrier unique id
        The id assigned to this barrier by the caller
      is-active -> gboolean: true if active, false otherwise
        true if active, false otherwise

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        id: int
        is_active: bool
        x1: int
        x2: int
        y1: int
        y2: int

    props: Props = ...
    def __init__(
        self, id: int = ..., x1: int = ..., x2: int = ..., y1: int = ..., y2: int = ...
    ) -> None: ...

class InputCapturePointerBarrierClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputCapturePointerBarrierClass()
    """

    parent_class: GObject.ObjectClass = ...

class InputCaptureSession(GObject.Object):
    """
    :Constructors:

    ::

        InputCaptureSession(**properties)

    Object XdpInputCaptureSession

    Signals from XdpInputCaptureSession:
      zones-changed (GVariant)
      activated (guint, GVariant)
      deactivated (guint, GVariant)
      disabled (GVariant)

    Signals from GObject:
      notify (GParam)
    """
    def connect_to_eis(self) -> int: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def get_session(self) -> Session: ...
    def get_zones(self) -> list[InputCaptureZone]: ...
    def release(self, activation_id: int) -> None: ...
    def release_at(
        self, activation_id: int, cursor_x_position: float, cursor_y_position: float
    ) -> None: ...
    def set_pointer_barriers(
        self,
        barriers: list[InputCapturePointerBarrier],
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def set_pointer_barriers_finish(
        self, result: Gio.AsyncResult
    ) -> list[InputCapturePointerBarrier]: ...

class InputCaptureSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputCaptureSessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class InputCaptureZone(GObject.Object):
    """
    :Constructors:

    ::

        InputCaptureZone(**properties)

    Object XdpInputCaptureZone

    Properties from XdpInputCaptureZone:
      width -> guint: zone width
        The zone width in logical pixels
      height -> guint: zone height
        The zone height in logical pixels
      x -> gint: zone x offset
        The zone x offset in logical pixels
      y -> gint: zone y offset
        The zone y offset in logical pixels
      zone-set -> guint: zone set number
        The zone_set number when this zone was retrieved
      is-valid -> gboolean: validity check
        True if this zone is currently valid

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        height: int
        is_valid: bool
        width: int
        x: int
        y: int
        zone_set: int

    props: Props = ...
    def __init__(
        self,
        height: int = ...,
        is_valid: bool = ...,
        width: int = ...,
        x: int = ...,
        y: int = ...,
        zone_set: int = ...,
    ) -> None: ...

class InputCaptureZoneClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputCaptureZoneClass()
    """

    parent_class: GObject.ObjectClass = ...

class Parent(GObject.GBoxed):
    def copy(self) -> Parent: ...
    def free(self) -> None: ...

class Portal(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Portal(**properties)
        initable_new() -> Xdp.Portal or None
        new() -> Xdp.Portal

    Object XdpPortal

    Signals from XdpPortal:
      spawn-exited (guint, guint)
      session-state-changed (gboolean, XdpLoginSessionState)
      update-available (gchararray, gchararray, gchararray)
      update-progress (guint, guint, guint, XdpUpdateStatus, gchararray, gchararray)
      location-updated (gdouble, gdouble, gdouble, gdouble, gdouble, gdouble, gchararray, gint64, gint64)
      notification-action-invoked (gchararray, gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    def access_camera(
        self,
        parent: typing.Optional[Parent],
        flags: CameraFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def access_camera_finish(self, result: Gio.AsyncResult) -> bool: ...
    def add_notification(
        self,
        id: str,
        notification: GLib.Variant,
        flags: NotificationFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def add_notification_finish(self, result: Gio.AsyncResult) -> bool: ...
    def compose_email(
        self,
        parent: typing.Optional[Parent],
        addresses: typing.Optional[typing.Sequence[str]],
        cc: typing.Optional[typing.Sequence[str]],
        bcc: typing.Optional[typing.Sequence[str]],
        subject: typing.Optional[str],
        body: typing.Optional[str],
        attachments: typing.Optional[typing.Sequence[str]],
        flags: EmailFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def compose_email_finish(self, result: Gio.AsyncResult) -> bool: ...
    def create_input_capture_session(
        self,
        parent: typing.Optional[Parent],
        capabilities: InputCapability,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def create_input_capture_session_finish(
        self, result: Gio.AsyncResult
    ) -> InputCaptureSession: ...
    def create_remote_desktop_session(
        self,
        devices: DeviceType,
        outputs: OutputType,
        flags: RemoteDesktopFlags,
        cursor_mode: CursorMode,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def create_remote_desktop_session_finish(
        self, result: Gio.AsyncResult
    ) -> Session: ...
    def create_remote_desktop_session_full(
        self,
        devices: DeviceType,
        outputs: OutputType,
        flags: RemoteDesktopFlags,
        cursor_mode: CursorMode,
        persist_mode: PersistMode,
        restore_token: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def create_screencast_session(
        self,
        outputs: OutputType,
        flags: ScreencastFlags,
        cursor_mode: CursorMode,
        persist_mode: PersistMode,
        restore_token: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def create_screencast_session_finish(self, result: Gio.AsyncResult) -> Session: ...
    def dynamic_launcher_get_desktop_entry(self, desktop_file_id: str) -> str: ...
    def dynamic_launcher_get_icon(
        self,
        desktop_file_id: str,
        out_icon_format: typing.Optional[str] = None,
        out_icon_size: typing.Optional[int] = None,
    ) -> GLib.Variant: ...
    def dynamic_launcher_install(
        self, token: str, desktop_file_id: str, desktop_entry: str
    ) -> bool: ...
    def dynamic_launcher_launch(
        self, desktop_file_id: str, activation_token: str
    ) -> bool: ...
    def dynamic_launcher_prepare_install(
        self,
        parent: typing.Optional[Parent],
        name: str,
        icon_v: GLib.Variant,
        launcher_type: LauncherType,
        target: typing.Optional[str],
        editable_name: bool,
        editable_icon: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def dynamic_launcher_prepare_install_finish(
        self, result: Gio.AsyncResult
    ) -> GLib.Variant: ...
    def dynamic_launcher_request_install_token(
        self, name: str, icon_v: GLib.Variant
    ) -> str: ...
    def dynamic_launcher_uninstall(self, desktop_file_id: str) -> bool: ...
    def get_settings(self) -> Settings: ...
    def get_supported_notification_options(self) -> GLib.Variant: ...
    def get_user_information(
        self,
        parent: typing.Optional[Parent],
        reason: typing.Optional[str],
        flags: UserInformationFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def get_user_information_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    @classmethod
    def initable_new(cls) -> typing.Optional[Portal]: ...
    def is_camera_present(self) -> bool: ...
    def location_monitor_start(
        self,
        parent: typing.Optional[Parent],
        distance_threshold: int,
        time_threshold: int,
        accuracy: LocationAccuracy,
        flags: LocationMonitorFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def location_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def location_monitor_stop(self) -> None: ...
    @classmethod
    def new(cls) -> Portal: ...
    def open_directory(
        self,
        parent: Parent,
        uri: str,
        flags: OpenUriFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def open_directory_finish(self, result: Gio.AsyncResult) -> bool: ...
    def open_file(
        self,
        parent: typing.Optional[Parent],
        title: str,
        filters: typing.Optional[GLib.Variant],
        current_filter: typing.Optional[GLib.Variant],
        choices: typing.Optional[GLib.Variant],
        flags: OpenFileFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def open_file_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def open_pipewire_remote_for_camera(self) -> int: ...
    def open_uri(
        self,
        parent: Parent,
        uri: str,
        flags: OpenUriFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def open_uri_finish(self, result: Gio.AsyncResult) -> bool: ...
    def pick_color(
        self,
        parent: typing.Optional[Parent] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def pick_color_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def prepare_print(
        self,
        parent: typing.Optional[Parent],
        title: str,
        settings: typing.Optional[GLib.Variant],
        page_setup: typing.Optional[GLib.Variant],
        flags: PrintFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def prepare_print_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def print_file(
        self,
        parent: typing.Optional[Parent],
        title: str,
        token: int,
        file: str,
        flags: PrintFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def print_file_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remove_notification(self, id: str) -> None: ...
    def request_background(
        self,
        parent: typing.Optional[Parent],
        reason: typing.Optional[str],
        commandline: typing.Optional[typing.Sequence[str]],
        flags: BackgroundFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def request_background_finish(self, result: Gio.AsyncResult) -> bool: ...
    @staticmethod
    def running_under_flatpak() -> bool: ...
    @staticmethod
    def running_under_sandbox() -> bool: ...
    @staticmethod
    def running_under_snap() -> bool: ...
    def save_file(
        self,
        parent: typing.Optional[Parent],
        title: str,
        current_name: typing.Optional[str],
        current_folder: typing.Optional[str],
        current_file: typing.Optional[str],
        filters: typing.Optional[GLib.Variant],
        current_filter: typing.Optional[GLib.Variant],
        choices: typing.Optional[GLib.Variant],
        flags: SaveFileFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def save_file_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def save_files(
        self,
        parent: typing.Optional[Parent],
        title: str,
        current_name: typing.Optional[str],
        current_folder: typing.Optional[str],
        files: GLib.Variant,
        choices: typing.Optional[GLib.Variant],
        flags: SaveFileFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def save_files_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def session_inhibit(
        self,
        parent: typing.Optional[Parent],
        reason: typing.Optional[str],
        flags: InhibitFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def session_inhibit_finish(self, result: Gio.AsyncResult) -> int: ...
    def session_monitor_query_end_response(self) -> None: ...
    def session_monitor_start(
        self,
        parent: typing.Optional[Parent],
        flags: SessionMonitorFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def session_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def session_monitor_stop(self) -> None: ...
    def session_uninhibit(self, id: int) -> None: ...
    def set_background_status(
        self,
        status_message: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def set_background_status_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_wallpaper(
        self,
        parent: typing.Optional[Parent],
        uri: str,
        flags: WallpaperFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def set_wallpaper_finish(self, result: Gio.AsyncResult) -> bool: ...
    def spawn(
        self,
        cwd: str,
        argv: typing.Sequence[str],
        fds: typing.Optional[typing.Sequence[int]],
        map_to: typing.Optional[typing.Sequence[int]],
        env: typing.Optional[typing.Sequence[str]],
        flags: SpawnFlags,
        sandbox_expose: typing.Optional[typing.Sequence[str]] = None,
        sandbox_expose_ro: typing.Optional[typing.Sequence[str]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def spawn_finish(self, result: Gio.AsyncResult) -> int: ...
    def spawn_signal(self, pid: int, signal: int, to_process_group: bool) -> None: ...
    def take_screenshot(
        self,
        parent: typing.Optional[Parent],
        flags: ScreenshotFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def take_screenshot_finish(self, result: Gio.AsyncResult) -> str: ...
    def trash_file(
        self,
        path: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def trash_file_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_install(
        self,
        parent: Parent,
        flags: UpdateInstallFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def update_install_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_monitor_start(
        self,
        flags: UpdateMonitorFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def update_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_monitor_stop(self) -> None: ...

class PortalClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PortalClass()
    """

    parent_class: GObject.ObjectClass = ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)

    Object XdpSession

    Signals from XdpSession:
      closed ()

    Signals from GObject:
      notify (GParam)
    """
    def close(self) -> None: ...
    def connect_to_eis(self) -> int: ...
    def get_devices(self) -> DeviceType: ...
    def get_persist_mode(self) -> PersistMode: ...
    def get_restore_token(self) -> typing.Optional[str]: ...
    def get_session_state(self) -> SessionState: ...
    def get_session_type(self) -> SessionType: ...
    def get_streams(self) -> GLib.Variant: ...
    def keyboard_key(self, keysym: bool, key: int, state: KeyState) -> None: ...
    def open_pipewire_remote(self) -> int: ...
    def pointer_axis(self, finish: bool, dx: float, dy: float) -> None: ...
    def pointer_axis_discrete(self, axis: DiscreteAxis, steps: int) -> None: ...
    def pointer_button(self, button: int, state: ButtonState) -> None: ...
    def pointer_motion(self, dx: float, dy: float) -> None: ...
    def pointer_position(self, stream: int, x: float, y: float) -> None: ...
    def start(
        self,
        parent: typing.Optional[Parent] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def touch_down(self, stream: int, slot: int, x: float, y: float) -> None: ...
    def touch_position(self, stream: int, slot: int, x: float, y: float) -> None: ...
    def touch_up(self, slot: int) -> None: ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class Settings(GObject.Object):
    """
    :Constructors:

    ::

        Settings(**properties)

    Object XdpSettings

    Signals from XdpSettings:
      changed (gchararray, gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    def read_all_values(
        self, namespaces: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> GLib.Variant: ...
    def read_string(
        self,
        namespace: str,
        key: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> str: ...
    def read_uint(
        self,
        namespace: str,
        key: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> int: ...
    def read_value(
        self,
        namespace: str,
        key: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> GLib.Variant: ...

class SettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SettingsClass()
    """

    parent_class: GObject.ObjectClass = ...

class BackgroundFlags(GObject.GFlags):
    ACTIVATABLE = 2
    AUTOSTART = 1
    NONE = 0

class CursorMode(GObject.GFlags):
    EMBEDDED = 2
    HIDDEN = 1
    METADATA = 4

class DeviceType(GObject.GFlags):
    KEYBOARD = 1
    NONE = 0
    POINTER = 2
    TOUCHSCREEN = 4

class InhibitFlags(GObject.GFlags):
    IDLE = 8
    LOGOUT = 1
    SUSPEND = 4
    USER_SWITCH = 2

class InputCapability(GObject.GFlags):
    KEYBOARD = 1
    NONE = 0
    POINTER = 2
    TOUCHSCREEN = 4

class LauncherType(GObject.GFlags):
    APPLICATION = 1
    WEBAPP = 2

class OpenFileFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class OpenUriFlags(GObject.GFlags):
    ASK = 1
    NONE = 0
    WRITABLE = 2

class OutputType(GObject.GFlags):
    MONITOR = 1
    NONE = 0
    VIRTUAL = 4
    WINDOW = 2

class RemoteDesktopFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class ScreencastFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class ScreenshotFlags(GObject.GFlags):
    INTERACTIVE = 1
    NONE = 0

class SpawnFlags(GObject.GFlags):
    CLEARENV = 1
    LATEST = 2
    NONE = 0
    NO_NETWORK = 8
    SANDBOX = 4
    WATCH = 16

class WallpaperFlags(GObject.GFlags):
    BACKGROUND = 1
    LOCKSCREEN = 2
    NONE = 0
    PREVIEW = 4

class ButtonState(GObject.GEnum):
    PRESSED = 1
    RELEASED = 0

class CameraFlags(GObject.GEnum):
    NONE = 0

class DiscreteAxis(GObject.GEnum):
    HORIZONTAL_SCROLL = 0
    VERTICAL_SCROLL = 1

class EmailFlags(GObject.GEnum):
    NONE = 0

class KeyState(GObject.GEnum):
    PRESSED = 1
    RELEASED = 0

class LocationAccuracy(GObject.GEnum):
    CITY = 2
    COUNTRY = 1
    EXACT = 5
    NEIGHBORHOOD = 3
    NONE = 0
    STREET = 4

class LocationMonitorFlags(GObject.GEnum):
    NONE = 0

class LoginSessionState(GObject.GEnum):
    ENDING = 3
    QUERY_END = 2
    RUNNING = 1

class NotificationFlags(GObject.GEnum):
    NONE = 0

class PersistMode(GObject.GEnum):
    NONE = 0
    PERSISTENT = 2
    TRANSIENT = 1

class PrintFlags(GObject.GEnum):
    NONE = 0

class SaveFileFlags(GObject.GEnum):
    NONE = 0

class SessionMonitorFlags(GObject.GEnum):
    NONE = 0

class SessionState(GObject.GEnum):
    ACTIVE = 1
    CLOSED = 2
    INITIAL = 0

class SessionType(GObject.GEnum):
    INPUT_CAPTURE = 2
    REMOTE_DESKTOP = 1
    SCREENCAST = 0

class UpdateInstallFlags(GObject.GEnum):
    NONE = 0

class UpdateMonitorFlags(GObject.GEnum):
    NONE = 0

class UpdateStatus(GObject.GEnum):
    DONE = 2
    EMPTY = 1
    FAILED = 3
    RUNNING = 0

class UserInformationFlags(GObject.GEnum):
    NONE = 0
