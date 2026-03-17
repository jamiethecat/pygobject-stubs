import typing

from gi.repository import Gdk
from gi.repository import Gly
from typing_extensions import Self

T = typing.TypeVar("T")

def frame_get_texture(frame: Gly.Frame) -> Gdk.Texture: ...
