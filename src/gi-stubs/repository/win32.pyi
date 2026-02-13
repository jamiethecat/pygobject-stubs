import typing

from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

class MSG(GObject.GPointer): ...
