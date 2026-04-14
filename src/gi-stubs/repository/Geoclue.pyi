from typing import Any
from typing import Protocol
from typing import TypeVar

from collections.abc import Callable

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

def client_interface_info() -> Gio.DBusInterfaceInfo: ...
def client_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def location_interface_info() -> Gio.DBusInterfaceInfo: ...
def location_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def manager_interface_info() -> Gio.DBusInterfaceInfo: ...
def manager_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...

class Client(GObject.GInterface, Protocol):
    """
    Interface GClueClient

    Signals from GObject:
      notify (GParam)
    """
    def call_start(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_start_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_start_sync(self, cancellable: Gio.Cancellable | None = None) -> bool: ...
    def call_stop(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_stop_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_stop_sync(self, cancellable: Gio.Cancellable | None = None) -> bool: ...
    def complete_start(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_stop(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def emit_location_updated(self, arg_old: str, arg_new: str) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ClientIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_start(self) -> Callable[[Client, Gio.DBusMethodInvocation], bool]: ...
    @property
    def handle_stop(self) -> Callable[[Client, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_active(self) -> Callable[[Client], bool]: ...
    @property
    def get_desktop_id(self) -> Callable[[Client], str | None]: ...
    @property
    def get_distance_threshold(self) -> Callable[[Client], int]: ...
    @property
    def get_location(self) -> Callable[[Client], str | None]: ...
    @property
    def get_requested_accuracy_level(self) -> Callable[[Client], int]: ...
    @property
    def get_time_threshold(self) -> Callable[[Client], int]: ...
    @property
    def location_updated(self) -> Callable[[Client, str, str], None]: ...

class ClientProxy(
    Gio.DBusProxy, Client, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        ClientProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.ClientProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.ClientProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ClientProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ClientProxy

    Object GClueClientProxy

    Signals from GClueClient:
      handle-start (GDBusMethodInvocation) -> gboolean
      handle-stop (GDBusMethodInvocation) -> gboolean
      location-updated (gchararray, gchararray)

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo | None
        g_interface_name: str
        g_name: str | None
        g_name_owner: str | None
        g_object_path: str
        active: bool
        desktop_id: str
        distance_threshold: int
        location: str
        requested_accuracy_level: int
        time_threshold: int
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ClientProxyPrivate: ...
    def __init__(
        self,
        *,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo | None = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        active: bool = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        location: str = ...,
        requested_accuracy_level: int = ...,
        time_threshold: int = ...,
    ) -> None: ...
    @staticmethod
    def create(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_full_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
    @staticmethod
    def create_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...

class ClientProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ClientProxyPrivate(GObject.GPointer): ...

class ClientSkeleton(Gio.DBusInterfaceSkeleton, Client, Gio.DBusInterface):
    """
    :Constructors:

    ::

        ClientSkeleton(**properties)
        new() -> Geoclue.ClientSkeleton

    Object GClueClientSkeleton

    Signals from GClueClient:
      handle-start (GDBusMethodInvocation) -> gboolean
      handle-stop (GDBusMethodInvocation) -> gboolean
      location-updated (gchararray, gchararray)

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        active: bool
        desktop_id: str
        distance_threshold: int
        location: str
        requested_accuracy_level: int
        time_threshold: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ClientSkeletonPrivate: ...
    def __init__(
        self,
        *,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        active: bool = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        location: str = ...,
        requested_accuracy_level: int = ...,
        time_threshold: int = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> ClientSkeleton: ...

class ClientSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ClientSkeletonPrivate(GObject.GPointer): ...

class Location(GObject.GInterface, Protocol):
    """
    Interface GClueLocation

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class LocationIface(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accuracy(self) -> Callable[[Location], float]: ...
    @property
    def get_altitude(self) -> Callable[[Location], float]: ...
    @property
    def get_description(self) -> Callable[[Location], str | None]: ...
    @property
    def get_heading(self) -> Callable[[Location], float]: ...
    @property
    def get_latitude(self) -> Callable[[Location], float]: ...
    @property
    def get_longitude(self) -> Callable[[Location], float]: ...
    @property
    def get_speed(self) -> Callable[[Location], float]: ...
    @property
    def get_timestamp(self) -> Callable[[Location], GLib.Variant | None]: ...

class LocationProxy(
    Gio.DBusProxy, Location, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        LocationProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.LocationProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.LocationProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.LocationProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.LocationProxy

    Object GClueLocationProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo | None
        g_interface_name: str
        g_name: str | None
        g_name_owner: str | None
        g_object_path: str
        accuracy: float
        altitude: float
        description: str
        heading: float
        latitude: float
        longitude: float
        speed: float
        timestamp: GLib.Variant
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> LocationProxyPrivate: ...
    def __init__(
        self,
        *,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo | None = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        accuracy: float = ...,
        altitude: float = ...,
        description: str = ...,
        heading: float = ...,
        latitude: float = ...,
        longitude: float = ...,
        speed: float = ...,
        timestamp: GLib.Variant = ...,
    ) -> None: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> LocationProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> LocationProxy: ...

class LocationProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class LocationProxyPrivate(GObject.GPointer): ...

class LocationSkeleton(Gio.DBusInterfaceSkeleton, Location, Gio.DBusInterface):
    """
    :Constructors:

    ::

        LocationSkeleton(**properties)
        new() -> Geoclue.LocationSkeleton

    Object GClueLocationSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accuracy: float
        altitude: float
        description: str
        heading: float
        latitude: float
        longitude: float
        speed: float
        timestamp: GLib.Variant

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> LocationSkeletonPrivate: ...
    def __init__(
        self,
        *,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accuracy: float = ...,
        altitude: float = ...,
        description: str = ...,
        heading: float = ...,
        latitude: float = ...,
        longitude: float = ...,
        speed: float = ...,
        timestamp: GLib.Variant = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> LocationSkeleton: ...

class LocationSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class LocationSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.GInterface, Protocol):
    """
    Interface GClueManager

    Signals from GObject:
      notify (GParam)
    """
    def call_add_agent(
        self,
        arg_id: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_add_agent_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_add_agent_sync(
        self, arg_id: str, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def call_create_client(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_create_client_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_create_client_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str]: ...
    def call_delete_client(
        self,
        arg_client: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_delete_client_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_delete_client_sync(
        self, arg_client: str, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def call_get_client(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_client_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_get_client_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str]: ...
    def complete_add_agent(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_create_client(
        self, invocation: Gio.DBusMethodInvocation, client: str
    ) -> None: ...
    def complete_delete_client(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_get_client(
        self, invocation: Gio.DBusMethodInvocation, client: str
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ManagerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_add_agent(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation, str], bool]: ...
    @property
    def handle_create_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation], bool]: ...
    @property
    def handle_delete_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation, str], bool]: ...
    @property
    def handle_get_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_available_accuracy_level(self) -> Callable[[Manager], int]: ...
    @property
    def get_in_use(self) -> Callable[[Manager], bool]: ...

class ManagerProxy(
    Gio.DBusProxy, Manager, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        ManagerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.ManagerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.ManagerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ManagerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ManagerProxy

    Object GClueManagerProxy

    Signals from GClueManager:
      handle-get-client (GDBusMethodInvocation) -> gboolean
      handle-create-client (GDBusMethodInvocation) -> gboolean
      handle-delete-client (GDBusMethodInvocation, gchararray) -> gboolean
      handle-add-agent (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo | None
        g_interface_name: str
        g_name: str | None
        g_name_owner: str | None
        g_object_path: str
        available_accuracy_level: int
        in_use: bool
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ManagerProxyPrivate: ...
    def __init__(
        self,
        *,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo | None = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ) -> None: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ManagerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ManagerProxy: ...

class ManagerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Manager, Gio.DBusInterface):
    """
    :Constructors:

    ::

        ManagerSkeleton(**properties)
        new() -> Geoclue.ManagerSkeleton

    Object GClueManagerSkeleton

    Signals from GClueManager:
      handle-get-client (GDBusMethodInvocation) -> gboolean
      handle-create-client (GDBusMethodInvocation) -> gboolean
      handle-delete-client (GDBusMethodInvocation, gchararray) -> gboolean
      handle-add-agent (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        available_accuracy_level: int
        in_use: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ManagerSkeletonPrivate: ...
    def __init__(
        self,
        *,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ManagerSkeletonPrivate(GObject.GPointer): ...

class Simple(GObject.Object, Gio.AsyncInitable):
    """
    :Constructors:

    ::

        Simple(**properties)
        new_finish(result:Gio.AsyncResult) -> Geoclue.Simple
        new_sync(desktop_id:str, accuracy_level:Geoclue.AccuracyLevel, cancellable:Gio.Cancellable=None) -> Geoclue.Simple
        new_with_thresholds_finish(result:Gio.AsyncResult) -> Geoclue.Simple
        new_with_thresholds_sync(desktop_id:str, accuracy_level:Geoclue.AccuracyLevel, time_threshold:int, distance_threshold:int, cancellable:Gio.Cancellable=None) -> Geoclue.Simple

    Object GClueSimple

    Properties from GClueSimple:
      desktop-id -> gchararray: DesktopID
        Desktop ID
      accuracy-level -> GClueAccuracyLevel: AccuracyLevel
        Requested accuracy level
      client -> GClueClientProxy: Client
        Client proxy
      location -> GClueLocationProxy: Location
        Location proxy
      distance-threshold -> guint: DistanceThreshold
        DistanceThreshold
      time-threshold -> guint: TimeThreshold
        TimeThreshold

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        client: ClientProxy | None
        distance_threshold: int
        location: LocationProxy | None
        time_threshold: int
        accuracy_level: AccuracyLevel
        desktop_id: str

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> SimplePrivate: ...
    def __init__(
        self,
        *,
        accuracy_level: AccuracyLevel = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        time_threshold: int = ...,
    ) -> None: ...
    # override
    def get_client(self) -> ClientProxy | None: ...
    def get_location(self) -> Location | None: ...
    @staticmethod
    def new(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, result: Gio.AsyncResult) -> Simple: ...
    @classmethod
    def new_sync(
        cls,
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
    ) -> Simple: ...
    @staticmethod
    def new_with_thresholds(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        time_threshold: int,
        distance_threshold: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_with_thresholds_finish(cls, result: Gio.AsyncResult) -> Simple: ...
    @classmethod
    def new_with_thresholds_sync(
        cls,
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        time_threshold: int,
        distance_threshold: int,
        cancellable: Gio.Cancellable | None = None,
    ) -> Simple: ...

class SimpleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SimpleClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class SimplePrivate(GObject.GPointer): ...

class ClientProxyCreateFlags(GObject.GFlags):
    AUTO_DELETE = 1
    NONE = 0

class AccuracyLevel(GObject.GEnum):
    CITY = 4
    COUNTRY = 1
    EXACT = 8
    NEIGHBORHOOD = 5
    NONE = 0
    STREET = 6
