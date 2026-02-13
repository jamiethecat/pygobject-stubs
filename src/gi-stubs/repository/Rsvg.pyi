import typing

from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

HAVE_CSS: bool = True
HAVE_PIXBUF: int = 1
HAVE_SVGZ: bool = True
MAJOR_VERSION: int = 2
MICRO_VERSION: int = 91
MINOR_VERSION: int = 61
VERSION: str = "2.61.91"

def cleanup() -> None: ...
def error_quark() -> int: ...
def init() -> None: ...
def pixbuf_from_file(filename: str) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_max_size(
    filename: str, max_width: int, max_height: int
) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_size(
    filename: str, width: int, height: int
) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_zoom(
    filename: str, x_zoom: float, y_zoom: float
) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_zoom_with_max(
    filename: str, x_zoom: float, y_zoom: float, max_width: int, max_height: int
) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
def set_default_dpi(dpi: float) -> None: ...
def set_default_dpi_x_y(dpi_x: float, dpi_y: float) -> None: ...
def term() -> None: ...

class DimensionData(GObject.GPointer):
    """
    :Constructors:

    ::

        DimensionData()
    """

    width: int = ...
    height: int = ...
    em: float = ...
    ex: float = ...

class Handle(GObject.Object):
    """
    :Constructors:

    ::

        Handle(**properties)
        new() -> Rsvg.Handle
        new_from_data(data:list) -> Rsvg.Handle
        new_from_file(filename:str) -> Rsvg.Handle
        new_from_gfile_sync(file:Gio.File, flags:Rsvg.HandleFlags, cancellable:Gio.Cancellable=None) -> Rsvg.Handle
        new_from_stream_sync(input_stream:Gio.InputStream, base_file:Gio.File=None, flags:Rsvg.HandleFlags, cancellable:Gio.Cancellable=None) -> Rsvg.Handle
        new_with_flags(flags:Rsvg.HandleFlags) -> Rsvg.Handle

    Object RsvgHandle

    Properties from RsvgHandle:
      dpi-x -> gdouble: dpi-x
      dpi-y -> gdouble: dpi-y
      flags -> RsvgHandleFlags: flags
      base-uri -> gchararray: base-uri
      width -> gint: width
      height -> gint: height
      em -> gdouble: em
      ex -> gdouble: ex
      title -> gchararray: title
      desc -> gchararray: desc
      metadata -> gchararray: metadata

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        base_uri: str
        desc: typing.Optional[str]
        dpi_x: float
        dpi_y: float
        em: float
        ex: float
        flags: HandleFlags
        height: int
        metadata: typing.Optional[str]
        title: typing.Optional[str]
        width: int

    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        base_uri: str = ...,
        dpi_x: float = ...,
        dpi_y: float = ...,
        flags: HandleFlags = ...,
    ) -> None: ...
    def close(self) -> bool: ...
    def free(self) -> None: ...
    def get_base_uri(self) -> str: ...
    def get_desc(self) -> typing.Optional[str]: ...
    def get_dimensions(self) -> DimensionData: ...
    def get_dimensions_sub(
        self, id: typing.Optional[str] = None
    ) -> typing.Tuple[bool, DimensionData]: ...
    def get_geometry_for_element(
        self, id: typing.Optional[str] = None
    ) -> typing.Tuple[bool, Rectangle, Rectangle]: ...
    def get_geometry_for_layer(
        self, id: typing.Optional[str], viewport: Rectangle
    ) -> typing.Tuple[bool, Rectangle, Rectangle]: ...
    def get_intrinsic_dimensions(
        self,
    ) -> typing.Tuple[bool, Length, bool, Length, bool, Rectangle]: ...
    def get_intrinsic_size_in_pixels(self) -> typing.Tuple[bool, float, float]: ...
    def get_metadata(self) -> typing.Optional[str]: ...
    def get_pixbuf(self) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
    def get_pixbuf_and_error(self) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
    def get_pixbuf_sub(
        self, id: typing.Optional[str] = None
    ) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
    def get_position_sub(
        self, id: typing.Optional[str] = None
    ) -> typing.Tuple[bool, PositionData]: ...
    def get_title(self) -> typing.Optional[str]: ...
    def has_sub(self, id: str) -> bool: ...
    def internal_set_testing(self, testing: bool) -> None: ...
    @classmethod
    def new(cls) -> Handle: ...
    @classmethod
    def new_from_data(cls, data: typing.Sequence[int]) -> Handle: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Handle: ...
    @classmethod
    def new_from_gfile_sync(
        cls,
        file: Gio.File,
        flags: HandleFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> Handle: ...
    @classmethod
    def new_from_stream_sync(
        cls,
        input_stream: Gio.InputStream,
        base_file: typing.Optional[Gio.File],
        flags: HandleFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> Handle: ...
    @classmethod
    def new_with_flags(cls, flags: HandleFlags) -> Handle: ...
    def read_stream_sync(
        self,
        stream: Gio.InputStream,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def render_cairo(self, cr: cairo.Context[_SomeSurface]) -> bool: ...
    def render_cairo_sub(
        self, cr: cairo.Context[_SomeSurface], id: typing.Optional[str] = None
    ) -> bool: ...
    def render_document(
        self, cr: cairo.Context[_SomeSurface], viewport: Rectangle
    ) -> bool: ...
    def render_element(
        self,
        cr: cairo.Context[_SomeSurface],
        id: typing.Optional[str],
        element_viewport: Rectangle,
    ) -> bool: ...
    def render_layer(
        self,
        cr: cairo.Context[_SomeSurface],
        id: typing.Optional[str],
        viewport: Rectangle,
    ) -> bool: ...
    def set_base_gfile(self, base_file: Gio.File) -> None: ...
    def set_base_uri(self, base_uri: str) -> None: ...
    def set_cancellable_for_rendering(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> None: ...
    def set_dpi(self, dpi: float) -> None: ...
    def set_dpi_x_y(self, dpi_x: float, dpi_y: float) -> None: ...
    def set_size_callback(
        self,
        size_func: typing.Optional[typing.Callable[..., typing.Tuple[int, int]]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_stylesheet(self, css: typing.Sequence[int]) -> bool: ...
    def write(self, buf: typing.Sequence[int]) -> bool: ...

class HandleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HandleClass()
    """

    parent: GObject.ObjectClass = ...

class Length(GObject.GPointer):
    """
    :Constructors:

    ::

        Length()
    """

    length: float = ...
    unit: Unit = ...

class PositionData(GObject.GPointer):
    """
    :Constructors:

    ::

        PositionData()
    """

    x: int = ...
    y: int = ...

class Rectangle(GObject.GPointer):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: float = ...
    y: float = ...
    width: float = ...
    height: float = ...

class HandleFlags(GObject.GFlags):
    FLAGS_NONE = 0
    FLAG_KEEP_IMAGE_DATA = 2
    FLAG_UNLIMITED = 1

class Error(GObject.GEnum):
    FAILED = 0
    @staticmethod
    def quark() -> int: ...

class Unit(GObject.GEnum):
    CH = 9
    CM = 5
    EM = 2
    EX = 3
    IN = 4
    MM = 6
    PC = 8
    PERCENT = 0
    PT = 7
    PX = 1
