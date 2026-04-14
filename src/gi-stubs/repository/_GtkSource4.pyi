from typing import Any
from typing import Protocol
from typing import TypeVar

from collections.abc import Callable
from collections.abc import Sequence

import cairo
from gi.repository import _Gdk3
from gi.repository import _Gtk3
from gi.repository import Atk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Pango

T = TypeVar("T")
_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

def completion_error_quark() -> int: ...
def encoding_get_all() -> list[Encoding]: ...
def encoding_get_current() -> Encoding: ...
def encoding_get_default_candidates() -> list[Encoding]: ...
def encoding_get_from_charset(charset: str) -> Encoding | None: ...
def encoding_get_utf8() -> Encoding: ...
def file_loader_error_quark() -> int: ...
def file_saver_error_quark() -> int: ...
def finalize() -> None: ...
def init() -> None: ...
def utils_escape_search_text(text: str) -> str: ...
def utils_unescape_search_text(text: str) -> str: ...

class Buffer(_Gtk3.TextBuffer):
    """
    :Constructors:

    ::

        Buffer(**properties)
        new(table:Gtk.TextTagTable=None) -> GtkSource.Buffer
        new_with_language(language:GtkSource.Language) -> GtkSource.Buffer

    Object GtkSourceBuffer

    Signals from GtkSourceBuffer:
      highlight-updated (GtkTextIter, GtkTextIter)
      source-mark-updated (GtkTextMark)
      undo ()
      redo ()
      bracket-matched (GtkTextIter, GtkSourceBracketMatchType)

    Properties from GtkSourceBuffer:
      can-undo -> gboolean: Can undo
        Whether Undo operation is possible
      can-redo -> gboolean: Can redo
        Whether Redo operation is possible
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to highlight syntax in the buffer
      highlight-matching-brackets -> gboolean: Highlight Matching Brackets
        Whether to highlight matching brackets
      max-undo-levels -> gint: Maximum Undo Levels
        Number of undo levels for the buffer
      language -> GtkSourceLanguage: Language
        Language object to get highlighting patterns from
      style-scheme -> GtkSourceStyleScheme: Style scheme
        Style scheme
      undo-manager -> GtkSourceUndoManager: Undo manager
        The buffer undo manager
      implicit-trailing-newline -> gboolean: Implicit trailing newline


    Signals from GtkTextBuffer:
      changed ()
      insert-text (GtkTextIter, gchararray, gint)
      insert-pixbuf (GtkTextIter, GdkPixbuf)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GtkClipboard)

    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: Tag Table
        Text Tag Table
      text -> gchararray: Text
        Current text of the buffer
      has-selection -> gboolean: Has selection
        Whether the buffer has some text currently selected
      cursor-position -> gint: Cursor position
        The position of the insert mark (as offset from the beginning of the buffer)
      copy-target-list -> GtkTargetList: Copy target list
        The list of targets this buffer supports for clipboard copying and DND source
      paste-target-list -> GtkTargetList: Paste target list
        The list of targets this buffer supports for clipboard pasting and DND destination

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.TextBuffer.Props):
        can_redo: bool
        can_undo: bool
        highlight_matching_brackets: bool
        highlight_syntax: bool
        implicit_trailing_newline: bool
        language: Language | None
        max_undo_levels: int
        style_scheme: StyleScheme | None
        undo_manager: UndoManager | None
        copy_target_list: _Gtk3.TargetList
        cursor_position: int
        has_selection: bool
        paste_target_list: _Gtk3.TargetList
        tag_table: _Gtk3.TextTagTable
        text: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> _Gtk3.TextBuffer: ...
    @property
    def priv(self) -> BufferPrivate: ...
    def __init__(
        self,
        *,
        highlight_matching_brackets: bool = ...,
        highlight_syntax: bool = ...,
        implicit_trailing_newline: bool = ...,
        language: Language | None = ...,
        max_undo_levels: int = ...,
        style_scheme: StyleScheme | None = ...,
        undo_manager: UndoManager | None = ...,
        tag_table: _Gtk3.TextTagTable = ...,
        text: str = ...,
    ) -> None: ...
    def backward_iter_to_source_mark(
        self, category: str | None = None
    ) -> tuple[bool, _Gtk3.TextIter]: ...
    def begin_not_undoable_action(self) -> None: ...
    def can_redo(self) -> bool: ...
    def can_undo(self) -> bool: ...
    def change_case(
        self, case_type: ChangeCaseType, start: _Gtk3.TextIter, end: _Gtk3.TextIter
    ) -> None: ...
    def create_source_mark(
        self, name: str | None, category: str, where: _Gtk3.TextIter
    ) -> Mark: ...
    def do_bracket_matched(
        self, iter: _Gtk3.TextIter, state: BracketMatchType
    ) -> None: ...
    def do_redo(self) -> None: ...
    def do_undo(self) -> None: ...
    def end_not_undoable_action(self) -> None: ...
    def ensure_highlight(self, start: _Gtk3.TextIter, end: _Gtk3.TextIter) -> None: ...
    def forward_iter_to_source_mark(
        self, category: str | None = None
    ) -> tuple[bool, _Gtk3.TextIter]: ...
    def get_context_classes_at_iter(self, iter: _Gtk3.TextIter) -> list[str]: ...
    def get_highlight_matching_brackets(self) -> bool: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_implicit_trailing_newline(self) -> bool: ...
    def get_language(self) -> Language | None: ...
    def get_max_undo_levels(self) -> int: ...
    def get_source_marks_at_iter(
        self, iter: _Gtk3.TextIter, category: str | None = None
    ) -> list[Mark]: ...
    def get_source_marks_at_line(
        self, line: int, category: str | None = None
    ) -> list[Mark]: ...
    def get_style_scheme(self) -> StyleScheme | None: ...
    def get_undo_manager(self) -> UndoManager | None: ...
    def iter_backward_to_context_class_toggle(
        self, context_class: str
    ) -> tuple[bool, _Gtk3.TextIter]: ...
    def iter_forward_to_context_class_toggle(
        self, context_class: str
    ) -> tuple[bool, _Gtk3.TextIter]: ...
    def iter_has_context_class(
        self, iter: _Gtk3.TextIter, context_class: str
    ) -> bool: ...
    def join_lines(self, start: _Gtk3.TextIter, end: _Gtk3.TextIter) -> None: ...
    @classmethod
    def new(cls, table: _Gtk3.TextTagTable | None = None) -> Buffer: ...
    @classmethod
    def new_with_language(cls, language: Language) -> Buffer: ...
    def redo(self) -> None: ...
    def remove_source_marks(
        self, start: _Gtk3.TextIter, end: _Gtk3.TextIter, category: str | None = None
    ) -> None: ...
    def set_highlight_matching_brackets(self, highlight: bool) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_implicit_trailing_newline(
        self, implicit_trailing_newline: bool
    ) -> None: ...
    def set_language(self, language: Language | None = None) -> None: ...
    def set_max_undo_levels(self, max_undo_levels: int) -> None: ...
    def set_style_scheme(self, scheme: StyleScheme | None = None) -> None: ...
    def set_undo_manager(self, manager: UndoManager | None = None) -> None: ...
    def sort_lines(
        self, start: _Gtk3.TextIter, end: _Gtk3.TextIter, flags: SortFlags, column: int
    ) -> None: ...
    def undo(self) -> None: ...

class BufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferClass()
    """
    @property
    def parent_class(self) -> _Gtk3.TextBufferClass: ...
    @property
    def undo(self) -> Callable[[Buffer], None]: ...
    @property
    def redo(self) -> Callable[[Buffer], None]: ...
    @property
    def bracket_matched(
        self,
    ) -> Callable[[Buffer, _Gtk3.TextIter, BracketMatchType], None]: ...
    @property
    def padding(self) -> list[None]: ...

class BufferPrivate(GObject.GPointer): ...

class Completion(GObject.Object, _Gtk3.Buildable):
    """
    :Constructors:

    ::

        Completion(**properties)

    Object GtkSourceCompletion

    Signals from GtkSourceCompletion:
      show ()
      hide ()
      populate-context (GtkSourceCompletionContext)
      move-cursor (GtkScrollStep, gint)
      move-page (GtkScrollStep, gint)
      activate-proposal ()

    Properties from GtkSourceCompletion:
      view -> GtkSourceView: View
        The GtkSourceView bound to the completion
      remember-info-visibility -> gboolean: Remember Info Visibility
        Remember the last info window visibility state
      select-on-show -> gboolean: Select on Show
        Select first proposal when completion is shown
      show-headers -> gboolean: Show Headers
        Show provider headers when proposals from multiple providers are available
      show-icons -> gboolean: Show Icons
        Show provider and proposal icons in the completion popup
      accelerators -> guint: Accelerators
        Number of proposal accelerators to show
      auto-complete-delay -> guint: Auto Complete Delay
        Completion popup delay for interactive completion
      provider-page-size -> guint: Provider Page Size
        Provider scrolling page size
      proposal-page-size -> guint: Proposal Page Size
        Proposal scrolling page size

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        accelerators: int
        auto_complete_delay: int
        proposal_page_size: int
        provider_page_size: int
        remember_info_visibility: bool
        select_on_show: bool
        show_headers: bool
        show_icons: bool
        view: View | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> CompletionPrivate: ...
    def __init__(
        self,
        *,
        accelerators: int = ...,
        auto_complete_delay: int = ...,
        proposal_page_size: int = ...,
        provider_page_size: int = ...,
        remember_info_visibility: bool = ...,
        select_on_show: bool = ...,
        show_headers: bool = ...,
        show_icons: bool = ...,
        view: View = ...,
    ) -> None: ...
    def add_provider(self, provider: CompletionProvider) -> bool: ...
    def block_interactive(self) -> None: ...
    def create_context(
        self, position: _Gtk3.TextIter | None = None
    ) -> CompletionContext: ...
    def do_activate_proposal(self) -> None: ...
    def do_hide(self) -> None: ...
    def do_move_cursor(self, step: _Gtk3.ScrollStep, num: int) -> None: ...
    def do_move_page(self, step: _Gtk3.ScrollStep, num: int) -> None: ...
    def do_populate_context(self, context: CompletionContext) -> None: ...
    def do_proposal_activated(
        self, provider: CompletionProvider, proposal: CompletionProposal
    ) -> bool: ...
    def do_show(self) -> None: ...
    def get_info_window(self) -> CompletionInfo: ...
    def get_providers(self) -> list[CompletionProvider]: ...
    def get_view(self) -> View | None: ...
    def hide(self) -> None: ...
    def remove_provider(self, provider: CompletionProvider) -> bool: ...
    def start(
        self, providers: list[CompletionProvider] | None, context: CompletionContext
    ) -> bool: ...
    def unblock_interactive(self) -> None: ...

class CompletionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def proposal_activated(
        self,
    ) -> Callable[[Completion, CompletionProvider, CompletionProposal], bool]: ...
    @property
    def show(self) -> Callable[[Completion], None]: ...
    @property
    def hide(self) -> Callable[[Completion], None]: ...
    @property
    def populate_context(self) -> Callable[[Completion, CompletionContext], None]: ...
    @property
    def move_cursor(self) -> Callable[[Completion, _Gtk3.ScrollStep, int], None]: ...
    @property
    def move_page(self) -> Callable[[Completion, _Gtk3.ScrollStep, int], None]: ...
    @property
    def activate_proposal(self) -> Callable[[Completion], None]: ...
    @property
    def padding(self) -> list[None]: ...

class CompletionContext(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        CompletionContext(**properties)

    Object GtkSourceCompletionContext

    Signals from GtkSourceCompletionContext:
      cancelled ()

    Properties from GtkSourceCompletionContext:
      completion -> GtkSourceCompletion: Completion
        The completion object to which the context belongs
      iter -> GtkTextIter: Iterator
        The GtkTextIter at which the completion was invoked
      activation -> GtkSourceCompletionActivation: Activation
        The type of activation

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.InitiallyUnowned.Props):
        activation: CompletionActivation
        completion: Completion
        iter: _Gtk3.TextIter

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.InitiallyUnowned: ...
    @property
    def priv(self) -> CompletionContextPrivate: ...
    def __init__(
        self,
        *,
        activation: CompletionActivation = ...,
        completion: Completion = ...,
        iter: _Gtk3.TextIter = ...,
    ) -> None: ...
    def add_proposals(
        self,
        provider: CompletionProvider,
        proposals: list[CompletionProposal] | None,
        finished: bool,
    ) -> None: ...
    def do_cancelled(self) -> None: ...
    def get_activation(self) -> CompletionActivation: ...
    def get_iter(self) -> tuple[bool, _Gtk3.TextIter]: ...

class CompletionContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionContextClass()
    """
    @property
    def parent_class(self) -> GObject.InitiallyUnownedClass: ...
    @property
    def cancelled(self) -> Callable[[CompletionContext], None]: ...
    @property
    def padding(self) -> list[None]: ...

class CompletionContextPrivate(GObject.GPointer): ...

class CompletionInfo(_Gtk3.Window, Atk.ImplementorIface, _Gtk3.Buildable):
    """
    :Constructors:

    ::

        CompletionInfo(**properties)
        new() -> GtkSource.CompletionInfo

    Object GtkSourceCompletionInfo

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.Window.Props):
        accept_focus: bool
        application: _Gtk3.Application | None
        attached_to: _Gtk3.Widget | None
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: _Gdk3.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: GdkPixbuf.Pixbuf | None
        icon_name: str | None
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: str | None
        screen: _Gdk3.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: str | None
        transient_for: _Gtk3.Window | None
        type: _Gtk3.WindowType
        type_hint: _Gdk3.WindowTypeHint
        urgency_hint: bool
        window_position: _Gtk3.WindowPosition
        border_width: int
        resize_mode: _Gtk3.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: _Gdk3.EventMask
        expand: bool
        focus_on_click: bool
        halign: _Gtk3.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: _Gtk3.Container | None
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: _Gtk3.Style
        tooltip_markup: str | None
        tooltip_text: str | None
        valign: _Gtk3.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: _Gdk3.Window | None
        startup_id: str
        child: _Gtk3.Widget

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> _Gtk3.Window: ...
    @property
    def priv(self) -> CompletionInfoPrivate: ...
    def __init__(
        self,
        *,
        accept_focus: bool = ...,
        application: _Gtk3.Application | None = ...,
        attached_to: _Gtk3.Widget | None = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: _Gdk3.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: GdkPixbuf.Pixbuf | None = ...,
        icon_name: str | None = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: _Gdk3.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: _Gtk3.Window | None = ...,
        type: _Gtk3.WindowType = ...,
        type_hint: _Gdk3.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: _Gtk3.WindowPosition = ...,
        border_width: int = ...,
        child: _Gtk3.Widget = ...,
        resize_mode: _Gtk3.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: _Gdk3.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: _Gtk3.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: _Gtk3.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: _Gtk3.Style | None = ...,
        tooltip_markup: str | None = ...,
        tooltip_text: str | None = ...,
        valign: _Gtk3.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ) -> None: ...
    def move_to_iter(
        self, view: _Gtk3.TextView, iter: _Gtk3.TextIter | None = None
    ) -> None: ...
    @classmethod
    def new(cls) -> CompletionInfo: ...

class CompletionInfoClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionInfoClass()
    """
    @property
    def parent_class(self) -> _Gtk3.WindowClass: ...
    @property
    def padding(self) -> list[None]: ...

class CompletionInfoPrivate(GObject.GPointer): ...

class CompletionItem(GObject.Object, CompletionProposal):
    """
    :Constructors:

    ::

        CompletionItem(**properties)
        new() -> GtkSource.CompletionItem

    Object GtkSourceCompletionItem

    Properties from GtkSourceCompletionItem:
      label -> gchararray: Label

      markup -> gchararray: Markup

      text -> gchararray: Text

      icon -> GdkPixbuf: Icon

      icon-name -> gchararray: Icon Name

      gicon -> GIcon: GIcon

      info -> gchararray: Info


    Signals from GtkSourceCompletionProposal:
      changed ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        gicon: Gio.Icon | None
        icon: GdkPixbuf.Pixbuf | None
        icon_name: str | None
        info: str | None
        label: str | None
        markup: str | None
        text: str | None

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> CompletionItemPrivate: ...
    def __init__(
        self,
        *,
        gicon: Gio.Icon | None = ...,
        icon: GdkPixbuf.Pixbuf | None = ...,
        icon_name: str | None = ...,
        info: str | None = ...,
        label: str | None = ...,
        markup: str | None = ...,
        text: str | None = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> CompletionItem: ...
    def set_gicon(self, gicon: Gio.Icon | None = None) -> None: ...
    def set_icon(self, icon: GdkPixbuf.Pixbuf | None = None) -> None: ...
    def set_icon_name(self, icon_name: str | None = None) -> None: ...
    def set_info(self, info: str | None = None) -> None: ...
    def set_label(self, label: str | None = None) -> None: ...
    def set_markup(self, markup: str | None = None) -> None: ...
    def set_text(self, text: str | None = None) -> None: ...

class CompletionItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionItemClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class CompletionItemPrivate(GObject.GPointer): ...
class CompletionPrivate(GObject.GPointer): ...

class CompletionProposal(GObject.GInterface, Protocol):
    """
    Interface GtkSourceCompletionProposal

    Signals from GObject:
      notify (GParam)
    """
    def changed(self) -> None: ...
    def equal(self, other: CompletionProposal) -> bool: ...
    def get_gicon(self) -> Gio.Icon | None: ...
    def get_icon(self) -> GdkPixbuf.Pixbuf | None: ...
    def get_icon_name(self) -> str | None: ...
    def get_info(self) -> str | None: ...
    def get_label(self) -> str: ...
    def get_markup(self) -> str: ...
    def get_text(self) -> str: ...
    def hash(self) -> int: ...

class CompletionProposalIface(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionProposalIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_label(self) -> Callable[[CompletionProposal], str]: ...
    @property
    def get_markup(self) -> Callable[[CompletionProposal], str]: ...
    @property
    def get_text(self) -> Callable[[CompletionProposal], str]: ...
    @property
    def get_icon(self) -> Callable[[CompletionProposal], GdkPixbuf.Pixbuf | None]: ...
    @property
    def get_icon_name(self) -> Callable[[CompletionProposal], str | None]: ...
    @property
    def get_gicon(self) -> Callable[[CompletionProposal], Gio.Icon | None]: ...
    @property
    def get_info(self) -> Callable[[CompletionProposal], str | None]: ...
    @property
    def hash(self) -> Callable[[CompletionProposal], int]: ...
    @property
    def equal(self) -> Callable[[CompletionProposal, CompletionProposal], bool]: ...
    @property
    def changed(self) -> Callable[[CompletionProposal], None]: ...

class CompletionProvider(GObject.GInterface, Protocol):
    """
    Interface GtkSourceCompletionProvider

    Signals from GObject:
      notify (GParam)
    """
    def activate_proposal(
        self, proposal: CompletionProposal, iter: _Gtk3.TextIter
    ) -> bool: ...
    def get_activation(self) -> CompletionActivation: ...
    def get_gicon(self) -> Gio.Icon | None: ...
    def get_icon(self) -> GdkPixbuf.Pixbuf | None: ...
    def get_icon_name(self) -> str | None: ...
    def get_info_widget(self, proposal: CompletionProposal) -> _Gtk3.Widget | None: ...
    def get_interactive_delay(self) -> int: ...
    def get_name(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_start_iter(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> tuple[bool, _Gtk3.TextIter]: ...
    def match(self, context: CompletionContext) -> bool: ...
    def populate(self, context: CompletionContext) -> None: ...
    def update_info(
        self, proposal: CompletionProposal, info: CompletionInfo
    ) -> None: ...

class CompletionProviderIface(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionProviderIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_name(self) -> Callable[[CompletionProvider], str]: ...
    @property
    def get_icon(self) -> Callable[[CompletionProvider], GdkPixbuf.Pixbuf | None]: ...
    @property
    def get_icon_name(self) -> Callable[[CompletionProvider], str | None]: ...
    @property
    def get_gicon(self) -> Callable[[CompletionProvider], Gio.Icon | None]: ...
    @property
    def populate(self) -> Callable[[CompletionProvider, CompletionContext], None]: ...
    @property
    def match(self) -> Callable[[CompletionProvider, CompletionContext], bool]: ...
    @property
    def get_activation(
        self,
    ) -> Callable[[CompletionProvider], CompletionActivation]: ...
    @property
    def get_info_widget(
        self,
    ) -> Callable[[CompletionProvider, CompletionProposal], _Gtk3.Widget | None]: ...
    @property
    def update_info(
        self,
    ) -> Callable[[CompletionProvider, CompletionProposal, CompletionInfo], None]: ...
    @property
    def get_start_iter(
        self,
    ) -> Callable[
        [CompletionProvider, CompletionContext, CompletionProposal],
        tuple[bool, _Gtk3.TextIter],
    ]: ...
    @property
    def activate_proposal(
        self,
    ) -> Callable[[CompletionProvider, CompletionProposal, _Gtk3.TextIter], bool]: ...
    @property
    def get_interactive_delay(self) -> Callable[[CompletionProvider], int]: ...
    @property
    def get_priority(self) -> Callable[[CompletionProvider], int]: ...

class CompletionWords(GObject.Object, CompletionProvider):
    """
    :Constructors:

    ::

        CompletionWords(**properties)
        new(name:str=None, icon:GdkPixbuf.Pixbuf=None) -> GtkSource.CompletionWords

    Object GtkSourceCompletionWords

    Properties from GtkSourceCompletionWords:
      name -> gchararray: Name
        The provider name
      icon -> GdkPixbuf: Icon
        The provider icon
      proposals-batch-size -> guint: Proposals Batch Size
        Number of proposals added in one batch
      scan-batch-size -> guint: Scan Batch Size
        Number of lines scanned in one batch
      minimum-word-size -> guint: Minimum Word Size
        The minimum word size to complete
      interactive-delay -> gint: Interactive Delay
        The delay before initiating interactive completion
      priority -> gint: Priority
        Provider priority
      activation -> GtkSourceCompletionActivation: Activation
        The type of activation

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        activation: CompletionActivation
        icon: GdkPixbuf.Pixbuf
        interactive_delay: int
        minimum_word_size: int
        name: str
        priority: int
        proposals_batch_size: int
        scan_batch_size: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> CompletionWordsPrivate: ...
    def __init__(
        self,
        *,
        activation: CompletionActivation = ...,
        icon: GdkPixbuf.Pixbuf = ...,
        interactive_delay: int = ...,
        minimum_word_size: int = ...,
        name: str = ...,
        priority: int = ...,
        proposals_batch_size: int = ...,
        scan_batch_size: int = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, name: str | None = None, icon: GdkPixbuf.Pixbuf | None = None
    ) -> CompletionWords: ...
    def register(self, buffer: _Gtk3.TextBuffer) -> None: ...
    def unregister(self, buffer: _Gtk3.TextBuffer) -> None: ...

class CompletionWordsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionWordsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class CompletionWordsPrivate(GObject.GPointer): ...

class Encoding(GObject.GBoxed):
    def copy(self) -> Encoding: ...
    def free(self) -> None: ...
    @staticmethod
    def get_all() -> list[Encoding]: ...
    def get_charset(self) -> str: ...
    @staticmethod
    def get_current() -> Encoding: ...
    @staticmethod
    def get_default_candidates() -> list[Encoding]: ...
    @staticmethod
    def get_from_charset(charset: str) -> Encoding | None: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_utf8() -> Encoding: ...
    def to_string(self) -> str: ...

class File(GObject.Object):
    """
    :Constructors:

    ::

        File(**properties)
        new() -> GtkSource.File

    Object GtkSourceFile

    Properties from GtkSourceFile:
      location -> GFile: Location

      encoding -> GtkSourceEncoding: Encoding

      newline-type -> GtkSourceNewlineType: Newline type

      compression-type -> GtkSourceCompressionType: Compression type

      read-only -> gboolean: Read Only


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        compression_type: CompressionType
        encoding: Encoding
        location: Gio.File
        newline_type: NewlineType
        read_only: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> FilePrivate: ...
    def __init__(self, *, location: Gio.File | None = ...) -> None: ...
    def check_file_on_disk(self) -> None: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    def is_deleted(self) -> bool: ...
    def is_externally_modified(self) -> bool: ...
    def is_local(self) -> bool: ...
    def is_readonly(self) -> bool: ...
    @classmethod
    def new(cls) -> File: ...
    def set_location(self, location: Gio.File | None = None) -> None: ...

class FileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class FileLoader(GObject.Object):
    """
    :Constructors:

    ::

        FileLoader(**properties)
        new(buffer:GtkSource.Buffer, file:GtkSource.File) -> GtkSource.FileLoader
        new_from_stream(buffer:GtkSource.Buffer, file:GtkSource.File, stream:Gio.InputStream) -> GtkSource.FileLoader

    Object GtkSourceFileLoader

    Properties from GtkSourceFileLoader:
      buffer -> GtkSourceBuffer: GtkSourceBuffer

      file -> GtkSourceFile: GtkSourceFile

      location -> GFile: Location

      input-stream -> GInputStream: Input stream


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffer: Buffer
        file: File
        input_stream: Gio.InputStream | None
        location: Gio.File | None

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> FileLoaderPrivate: ...
    def __init__(
        self,
        *,
        buffer: Buffer = ...,
        file: File = ...,
        input_stream: Gio.InputStream = ...,
        location: Gio.File = ...,
    ) -> None: ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_input_stream(self) -> Gio.InputStream | None: ...
    def get_location(self) -> Gio.File | None: ...
    def get_newline_type(self) -> NewlineType: ...
    def load_async(
        self,
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        progress_callback: Callable[..., None] | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def load_finish(self, result: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileLoader: ...
    @classmethod
    def new_from_stream(
        cls, buffer: Buffer, file: File, stream: Gio.InputStream
    ) -> FileLoader: ...
    def set_candidate_encodings(self, candidate_encodings: list[Encoding]) -> None: ...

class FileLoaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileLoaderClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class FileLoaderPrivate(GObject.GPointer): ...
class FilePrivate(GObject.GPointer): ...

class FileSaver(GObject.Object):
    """
    :Constructors:

    ::

        FileSaver(**properties)
        new(buffer:GtkSource.Buffer, file:GtkSource.File) -> GtkSource.FileSaver
        new_with_target(buffer:GtkSource.Buffer, file:GtkSource.File, target_location:Gio.File) -> GtkSource.FileSaver

    Object GtkSourceFileSaver

    Properties from GtkSourceFileSaver:
      buffer -> GtkSourceBuffer: GtkSourceBuffer

      file -> GtkSourceFile: GtkSourceFile

      location -> GFile: Location

      encoding -> GtkSourceEncoding: Encoding

      newline-type -> GtkSourceNewlineType: Newline type

      compression-type -> GtkSourceCompressionType: Compression type

      flags -> GtkSourceFileSaverFlags: Flags


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffer: Buffer
        compression_type: CompressionType
        encoding: Encoding
        file: File
        flags: FileSaverFlags
        location: Gio.File
        newline_type: NewlineType

    @property
    def props(self) -> Props: ...
    @property
    def object(self) -> GObject.Object: ...
    @property
    def priv(self) -> FileSaverPrivate: ...
    def __init__(
        self,
        *,
        buffer: Buffer = ...,
        compression_type: CompressionType = ...,
        encoding: Encoding | None = ...,
        file: File = ...,
        flags: FileSaverFlags = ...,
        location: Gio.File = ...,
        newline_type: NewlineType = ...,
    ) -> None: ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_flags(self) -> FileSaverFlags: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileSaver: ...
    @classmethod
    def new_with_target(
        cls, buffer: Buffer, file: File, target_location: Gio.File
    ) -> FileSaver: ...
    def save_async(
        self,
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        progress_callback: Callable[..., None] | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_compression_type(self, compression_type: CompressionType) -> None: ...
    def set_encoding(self, encoding: Encoding | None = None) -> None: ...
    def set_flags(self, flags: FileSaverFlags) -> None: ...
    def set_newline_type(self, newline_type: NewlineType) -> None: ...

class FileSaverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileSaverClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class FileSaverPrivate(GObject.GPointer): ...

class Gutter(GObject.Object):
    """
    :Constructors:

    ::

        Gutter(**properties)

    Object GtkSourceGutter

    Properties from GtkSourceGutter:
      view -> GtkSourceView: View

      window-type -> GtkTextWindowType: Window Type
        The gutters' text window type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        view: View
        window_type: _Gtk3.TextWindowType

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> GutterPrivate: ...
    def __init__(
        self, *, view: View = ..., window_type: _Gtk3.TextWindowType = ...
    ) -> None: ...
    def get_renderer_at_pos(self, x: int, y: int) -> GutterRenderer | None: ...
    def get_view(self) -> View: ...
    def get_window_type(self) -> _Gtk3.TextWindowType: ...
    def insert(self, renderer: GutterRenderer, position: int) -> bool: ...
    def queue_draw(self) -> None: ...
    def remove(self, renderer: GutterRenderer) -> None: ...
    def reorder(self, renderer: GutterRenderer, position: int) -> None: ...

class GutterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class GutterPrivate(GObject.GPointer): ...

class GutterRenderer(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        GutterRenderer(**properties)

    Object GtkSourceGutterRenderer

    Signals from GtkSourceGutterRenderer:
      query-tooltip (GtkTextIter, GdkRectangle, gint, gint, GtkTooltip) -> gboolean
      activate (GtkTextIter, GdkRectangle, GdkEvent)
      queue-draw ()
      query-data (GtkTextIter, GtkTextIter, GtkSourceGutterRendererState)
      query-activatable (GtkTextIter, GdkRectangle, GdkEvent) -> gboolean

    Properties from GtkSourceGutterRenderer:
      visible -> gboolean: Visible
        Visible
      xpad -> gint: X Padding
        The x-padding
      ypad -> gint: Y Padding
        The y-padding
      xalign -> gfloat: X Alignment
        The x-alignment
      yalign -> gfloat: Y Alignment
        The y-alignment
      view -> GtkTextView: The View
        The view
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      window-type -> GtkTextWindowType: Window Type
        The window type
      size -> gint: Size
        The size
      background-rgba -> GdkRGBA: Background Color
        The background color
      background-set -> gboolean: Background Set
        Whether the background color is set

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.InitiallyUnowned.Props):
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: _Gdk3.RGBA
        background_set: bool
        size: int
        view: _Gtk3.TextView
        visible: bool
        window_type: _Gtk3.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.InitiallyUnowned: ...
    @property
    def priv(self) -> GutterRendererPrivate: ...
    def __init__(
        self,
        *,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: _Gdk3.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ) -> None: ...
    def activate(
        self, iter: _Gtk3.TextIter, area: _Gdk3.Rectangle, event: _Gdk3.Event
    ) -> None: ...
    def begin(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: _Gdk3.Rectangle,
        cell_area: _Gdk3.Rectangle,
        start: _Gtk3.TextIter,
        end: _Gtk3.TextIter,
    ) -> None: ...
    def do_activate(
        self, iter: _Gtk3.TextIter, area: _Gdk3.Rectangle, event: _Gdk3.Event
    ) -> None: ...
    def do_begin(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: _Gdk3.Rectangle,
        cell_area: _Gdk3.Rectangle,
        start: _Gtk3.TextIter,
        end: _Gtk3.TextIter,
    ) -> None: ...
    def do_change_buffer(self, old_buffer: _Gtk3.TextBuffer | None = None) -> None: ...
    def do_change_view(self, old_view: _Gtk3.TextView | None = None) -> None: ...
    def do_draw(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: _Gdk3.Rectangle,
        cell_area: _Gdk3.Rectangle,
        start: _Gtk3.TextIter,
        end: _Gtk3.TextIter,
        state: GutterRendererState,
    ) -> None: ...
    def do_end(self) -> None: ...
    def do_query_activatable(
        self, iter: _Gtk3.TextIter, area: _Gdk3.Rectangle, event: _Gdk3.Event
    ) -> bool: ...
    def do_query_data(
        self, start: _Gtk3.TextIter, end: _Gtk3.TextIter, state: GutterRendererState
    ) -> None: ...
    def do_query_tooltip(
        self,
        iter: _Gtk3.TextIter,
        area: _Gdk3.Rectangle,
        x: int,
        y: int,
        tooltip: _Gtk3.Tooltip,
    ) -> bool: ...
    def do_queue_draw(self) -> None: ...
    def draw(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: _Gdk3.Rectangle,
        cell_area: _Gdk3.Rectangle,
        start: _Gtk3.TextIter,
        end: _Gtk3.TextIter,
        state: GutterRendererState,
    ) -> None: ...
    def end(self) -> None: ...
    def get_alignment(self) -> tuple[float, float]: ...
    def get_alignment_mode(self) -> GutterRendererAlignmentMode: ...
    def get_background(self) -> tuple[bool, _Gdk3.RGBA]: ...
    def get_padding(self) -> tuple[int, int]: ...
    def get_size(self) -> int: ...
    def get_view(self) -> _Gtk3.TextView: ...
    def get_visible(self) -> bool: ...
    def get_window_type(self) -> _Gtk3.TextWindowType: ...
    def query_activatable(
        self, iter: _Gtk3.TextIter, area: _Gdk3.Rectangle, event: _Gdk3.Event
    ) -> bool: ...
    def query_data(
        self, start: _Gtk3.TextIter, end: _Gtk3.TextIter, state: GutterRendererState
    ) -> None: ...
    def query_tooltip(
        self,
        iter: _Gtk3.TextIter,
        area: _Gdk3.Rectangle,
        x: int,
        y: int,
        tooltip: _Gtk3.Tooltip,
    ) -> bool: ...
    def queue_draw(self) -> None: ...
    def set_alignment(self, xalign: float, yalign: float) -> None: ...
    def set_alignment_mode(self, mode: GutterRendererAlignmentMode) -> None: ...
    def set_background(self, color: _Gdk3.RGBA | None = None) -> None: ...
    def set_padding(self, xpad: int, ypad: int) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class GutterRendererClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererClass()
    """
    @property
    def parent_class(self) -> GObject.InitiallyUnownedClass: ...
    @property
    def begin(
        self,
    ) -> Callable[
        [
            GutterRenderer,
            cairo.Context[_SomeSurface],
            _Gdk3.Rectangle,
            _Gdk3.Rectangle,
            _Gtk3.TextIter,
            _Gtk3.TextIter,
        ],
        None,
    ]: ...
    @property
    def draw(
        self,
    ) -> Callable[
        [
            GutterRenderer,
            cairo.Context[_SomeSurface],
            _Gdk3.Rectangle,
            _Gdk3.Rectangle,
            _Gtk3.TextIter,
            _Gtk3.TextIter,
            GutterRendererState,
        ],
        None,
    ]: ...
    @property
    def end(self) -> Callable[[GutterRenderer], None]: ...
    @property
    def change_view(
        self,
    ) -> Callable[[GutterRenderer, _Gtk3.TextView | None], None]: ...
    @property
    def change_buffer(
        self,
    ) -> Callable[[GutterRenderer, _Gtk3.TextBuffer | None], None]: ...
    @property
    def query_activatable(
        self,
    ) -> Callable[
        [GutterRenderer, _Gtk3.TextIter, _Gdk3.Rectangle, _Gdk3.Event], bool
    ]: ...
    @property
    def activate(
        self,
    ) -> Callable[
        [GutterRenderer, _Gtk3.TextIter, _Gdk3.Rectangle, _Gdk3.Event], None
    ]: ...
    @property
    def queue_draw(self) -> Callable[[GutterRenderer], None]: ...
    @property
    def query_tooltip(
        self,
    ) -> Callable[
        [GutterRenderer, _Gtk3.TextIter, _Gdk3.Rectangle, int, int, _Gtk3.Tooltip], bool
    ]: ...
    @property
    def query_data(
        self,
    ) -> Callable[
        [GutterRenderer, _Gtk3.TextIter, _Gtk3.TextIter, GutterRendererState], None
    ]: ...
    @property
    def padding(self) -> list[None]: ...

class GutterRendererPixbuf(GutterRenderer):
    """
    :Constructors:

    ::

        GutterRendererPixbuf(**properties)
        new() -> GtkSource.GutterRenderer

    Object GtkSourceGutterRendererPixbuf

    Properties from GtkSourceGutterRendererPixbuf:
      pixbuf -> GdkPixbuf: Pixbuf
        The pixbuf
      icon-name -> gchararray: Icon Name
        The icon name
      gicon -> GIcon: GIcon
        The gicon

    Signals from GtkSourceGutterRenderer:
      query-tooltip (GtkTextIter, GdkRectangle, gint, gint, GtkTooltip) -> gboolean
      activate (GtkTextIter, GdkRectangle, GdkEvent)
      queue-draw ()
      query-data (GtkTextIter, GtkTextIter, GtkSourceGutterRendererState)
      query-activatable (GtkTextIter, GdkRectangle, GdkEvent) -> gboolean

    Properties from GtkSourceGutterRenderer:
      visible -> gboolean: Visible
        Visible
      xpad -> gint: X Padding
        The x-padding
      ypad -> gint: Y Padding
        The y-padding
      xalign -> gfloat: X Alignment
        The x-alignment
      yalign -> gfloat: Y Alignment
        The y-alignment
      view -> GtkTextView: The View
        The view
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      window-type -> GtkTextWindowType: Window Type
        The window type
      size -> gint: Size
        The size
      background-rgba -> GdkRGBA: Background Color
        The background color
      background-set -> gboolean: Background Set
        Whether the background color is set

    Signals from GObject:
      notify (GParam)
    """
    class Props(GutterRenderer.Props):
        gicon: Gio.Icon
        icon_name: str
        pixbuf: GdkPixbuf.Pixbuf
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: _Gdk3.RGBA
        background_set: bool
        size: int
        view: _Gtk3.TextView
        visible: bool
        window_type: _Gtk3.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GutterRenderer: ...
    @property
    def priv(self) -> GutterRendererPixbufPrivate: ...
    def __init__(
        self,
        *,
        gicon: Gio.Icon | None = ...,
        icon_name: str | None = ...,
        pixbuf: GdkPixbuf.Pixbuf | None = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: _Gdk3.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ) -> None: ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    @classmethod
    def new(cls) -> GutterRendererPixbuf: ...
    def set_gicon(self, icon: Gio.Icon | None = None) -> None: ...
    def set_icon_name(self, icon_name: str | None = None) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf | None = None) -> None: ...

class GutterRendererPixbufClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererPixbufClass()
    """
    @property
    def parent_class(self) -> GutterRendererClass: ...
    @property
    def padding(self) -> list[None]: ...

class GutterRendererPixbufPrivate(GObject.GPointer): ...
class GutterRendererPrivate(GObject.GPointer): ...

class GutterRendererText(GutterRenderer):
    """
    :Constructors:

    ::

        GutterRendererText(**properties)
        new() -> GtkSource.GutterRenderer

    Object GtkSourceGutterRendererText

    Properties from GtkSourceGutterRendererText:
      markup -> gchararray: Markup
        The markup
      text -> gchararray: Text
        The text

    Signals from GtkSourceGutterRenderer:
      query-tooltip (GtkTextIter, GdkRectangle, gint, gint, GtkTooltip) -> gboolean
      activate (GtkTextIter, GdkRectangle, GdkEvent)
      queue-draw ()
      query-data (GtkTextIter, GtkTextIter, GtkSourceGutterRendererState)
      query-activatable (GtkTextIter, GdkRectangle, GdkEvent) -> gboolean

    Properties from GtkSourceGutterRenderer:
      visible -> gboolean: Visible
        Visible
      xpad -> gint: X Padding
        The x-padding
      ypad -> gint: Y Padding
        The y-padding
      xalign -> gfloat: X Alignment
        The x-alignment
      yalign -> gfloat: Y Alignment
        The y-alignment
      view -> GtkTextView: The View
        The view
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      window-type -> GtkTextWindowType: Window Type
        The window type
      size -> gint: Size
        The size
      background-rgba -> GdkRGBA: Background Color
        The background color
      background-set -> gboolean: Background Set
        Whether the background color is set

    Signals from GObject:
      notify (GParam)
    """
    class Props(GutterRenderer.Props):
        markup: str
        text: str
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: _Gdk3.RGBA
        background_set: bool
        size: int
        view: _Gtk3.TextView
        visible: bool
        window_type: _Gtk3.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GutterRenderer: ...
    @property
    def priv(self) -> GutterRendererTextPrivate: ...
    def __init__(
        self,
        *,
        markup: str = ...,
        text: str = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: _Gdk3.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ) -> None: ...
    def measure(self, text: str) -> tuple[int, int]: ...
    def measure_markup(self, markup: str) -> tuple[int, int]: ...
    @classmethod
    def new(cls) -> GutterRendererText: ...
    def set_markup(self, markup: str, length: int) -> None: ...
    def set_text(self, text: str, length: int) -> None: ...

class GutterRendererTextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererTextClass()
    """
    @property
    def parent_class(self) -> GutterRendererClass: ...
    @property
    def padding(self) -> list[None]: ...

class GutterRendererTextPrivate(GObject.GPointer): ...

class Language(GObject.Object):
    """
    :Constructors:

    ::

        Language(**properties)

    Object GtkSourceLanguage

    Properties from GtkSourceLanguage:
      id -> gchararray: Language id
        Language id
      name -> gchararray: Language name
        Language name
      section -> gchararray: Language section
        Language section
      hidden -> gboolean: Hidden
        Whether the language should be hidden from the user

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        hidden: bool
        id: str
        name: str
        section: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> LanguagePrivate: ...
    def get_globs(self) -> list[str] | None: ...
    def get_hidden(self) -> bool: ...
    def get_id(self) -> str: ...
    def get_metadata(self, name: str) -> str | None: ...
    def get_mime_types(self) -> list[str] | None: ...
    def get_name(self) -> str: ...
    def get_section(self) -> str: ...
    def get_style_fallback(self, style_id: str) -> str | None: ...
    def get_style_ids(self) -> list[str] | None: ...
    def get_style_name(self, style_id: str) -> str | None: ...

class LanguageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class LanguageManager(GObject.Object):
    """
    :Constructors:

    ::

        LanguageManager(**properties)
        new() -> GtkSource.LanguageManager

    Object GtkSourceLanguageManager

    Properties from GtkSourceLanguageManager:
      search-path -> GStrv: Language specification directories
        List of directories where the language specification files (.lang) are located
      language-ids -> GStrv: Language ids
        List of the ids of the available languages

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        language_ids: list[str] | None
        search_path: list[str]

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> LanguageManagerPrivate: ...
    def __init__(self, *, search_path: Sequence[str] | None = ...) -> None: ...
    @staticmethod
    def get_default() -> LanguageManager: ...
    def get_language(self, id: str) -> Language | None: ...
    def get_language_ids(self) -> list[str] | None: ...
    def get_search_path(self) -> list[str]: ...
    def guess_language(
        self, filename: str | None = None, content_type: str | None = None
    ) -> Language | None: ...
    @classmethod
    def new(cls) -> LanguageManager: ...
    def set_search_path(self, dirs: Sequence[str] | None = None) -> None: ...

class LanguageManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageManagerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class LanguageManagerPrivate(GObject.GPointer): ...
class LanguagePrivate(GObject.GPointer): ...

class Map(View, Atk.ImplementorIface, _Gtk3.Buildable, _Gtk3.Scrollable):
    """
    :Constructors:

    ::

        Map(**properties)
        new() -> Gtk.Widget

    Object GtkSourceMap

    Properties from GtkSourceMap:
      view -> GtkSourceView: View
        The view this widget is mapping.
      font-desc -> PangoFontDescription: Font Description
        The Pango font description to use.

    Signals from GtkSourceView:
      undo ()
      redo ()
      smart-home-end (GtkTextIter, gint)
      show-completion ()
      line-mark-activated (GtkTextIter, GdkEvent)
      move-lines (gboolean)
      move-words (gint)
      move-to-matching-bracket (gboolean)
      change-number (gint)
      change-case (GtkSourceChangeCaseType)
      join-lines ()

    Properties from GtkSourceView:
      completion -> GtkSourceCompletion: Completion
        The completion object associated with the view
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      background-pattern -> GtkSourceBackgroundPatternType: Background pattern
        Draw a specific background pattern on the view
      smart-backspace -> gboolean: Smart Backspace

      space-drawer -> GtkSourceSpaceDrawer: Space Drawer


    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      populate-popup (GtkWidget)
      select-all (gboolean)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean
      insert-emoji ()

    Properties from GtkTextView:
      pixels-above-lines -> gint: Pixels Above Lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels Below Lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      left-margin -> gint: Left Margin
        Width of the left margin in pixels
      right-margin -> gint: Right Margin
        Width of the right margin in pixels
      top-margin -> gint: Top Margin
        Height of the top margin in pixels
      bottom-margin -> gint: Bottom Margin
        Height of the bottom margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      cursor-visible -> gboolean: Cursor Visible
        If the insertion cursor is shown
      buffer -> GtkTextBuffer: Buffer
        The buffer which is displayed
      overwrite -> gboolean: Overwrite mode
        Whether entered text overwrites existing contents
      accepts-tab -> gboolean: Accepts tab
        Whether Tab will result in a tab character being entered
      im-module -> gchararray: IM module
        Which IM module should be used
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      monospace -> gboolean: Monospace
        Whether to use a monospace font

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props(View.Props):
        font_desc: Pango.FontDescription
        view: View | None
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: _Gtk3.TextBuffer
        cursor_visible: bool
        editable: bool
        im_module: str
        indent: int
        input_hints: _Gtk3.InputHints
        input_purpose: _Gtk3.InputPurpose
        justification: _Gtk3.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        populate_all: bool
        right_margin: int
        tabs: Pango.TabArray | None
        top_margin: int
        wrap_mode: _Gtk3.WrapMode
        border_width: int
        resize_mode: _Gtk3.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: _Gdk3.EventMask
        expand: bool
        focus_on_click: bool
        halign: _Gtk3.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: _Gtk3.Container | None
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: _Gtk3.Style
        tooltip_markup: str | None
        tooltip_text: str | None
        valign: _Gtk3.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: _Gdk3.Window | None
        hadjustment: _Gtk3.Adjustment
        hscroll_policy: _Gtk3.ScrollablePolicy
        vadjustment: _Gtk3.Adjustment
        vscroll_policy: _Gtk3.ScrollablePolicy
        child: _Gtk3.Widget

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> View: ...
    def __init__(
        self,
        *,
        font_desc: Pango.FontDescription = ...,
        view: View = ...,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: _Gtk3.TextBuffer | None = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: _Gtk3.InputHints = ...,
        input_purpose: _Gtk3.InputPurpose = ...,
        justification: _Gtk3.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        populate_all: bool = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: _Gtk3.WrapMode = ...,
        border_width: int = ...,
        child: _Gtk3.Widget = ...,
        resize_mode: _Gtk3.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: _Gdk3.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: _Gtk3.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: _Gtk3.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: _Gtk3.Style | None = ...,
        tooltip_markup: str | None = ...,
        tooltip_text: str | None = ...,
        valign: _Gtk3.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        hadjustment: _Gtk3.Adjustment | None = ...,
        hscroll_policy: _Gtk3.ScrollablePolicy = ...,
        vadjustment: _Gtk3.Adjustment | None = ...,
        vscroll_policy: _Gtk3.ScrollablePolicy = ...,
    ) -> None: ...
    def get_view(self) -> View | None: ...
    @classmethod
    def new(cls) -> Map: ...
    def set_view(self, view: View) -> None: ...

class MapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapClass()
    """
    @property
    def parent_class(self) -> ViewClass: ...
    @property
    def padding(self) -> list[None]: ...

class Mark(_Gtk3.TextMark):
    """
    :Constructors:

    ::

        Mark(**properties)
        new(name:str=None, category:str) -> GtkSource.Mark

    Object GtkSourceMark

    Properties from GtkSourceMark:
      category -> gchararray: Category
        The mark category

    Properties from GtkTextMark:
      name -> gchararray: Name
        Mark name
      left-gravity -> gboolean: Left gravity
        Whether the mark has left gravity

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.TextMark.Props):
        category: str
        left_gravity: bool
        name: str | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> _Gtk3.TextMark: ...
    @property
    def priv(self) -> MarkPrivate: ...
    def __init__(
        self, *, category: str = ..., left_gravity: bool = ..., name: str = ...
    ) -> None: ...
    def get_category(self) -> str: ...
    @classmethod
    def new(cls, name: str | None, category: str) -> Mark: ...
    def next(self, category: str | None = None) -> Mark | None: ...
    def prev(self, category: str | None = None) -> Mark | None: ...

class MarkAttributes(GObject.Object):
    """
    :Constructors:

    ::

        MarkAttributes(**properties)
        new() -> GtkSource.MarkAttributes

    Object GtkSourceMarkAttributes

    Signals from GtkSourceMarkAttributes:
      query-tooltip-text (GtkSourceMark) -> gchararray
      query-tooltip-markup (GtkSourceMark) -> gchararray

    Properties from GtkSourceMarkAttributes:
      background -> GdkRGBA: Background
        The background
      pixbuf -> GdkPixbuf: Pixbuf
        The pixbuf
      icon-name -> gchararray: Icon Name
        The icon name
      gicon -> GIcon: GIcon
        The GIcon

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        background: _Gdk3.RGBA
        gicon: Gio.Icon
        icon_name: str
        pixbuf: GdkPixbuf.Pixbuf

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> MarkAttributesPrivate: ...
    def __init__(
        self,
        *,
        background: _Gdk3.RGBA = ...,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
    ) -> None: ...
    def get_background(self) -> tuple[bool, _Gdk3.RGBA]: ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    def get_tooltip_markup(self, mark: Mark) -> str: ...
    def get_tooltip_text(self, mark: Mark) -> str: ...
    @classmethod
    def new(cls) -> MarkAttributes: ...
    def render_icon(self, widget: _Gtk3.Widget, size: int) -> GdkPixbuf.Pixbuf: ...
    def set_background(self, background: _Gdk3.RGBA) -> None: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...

class MarkAttributesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkAttributesClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class MarkAttributesPrivate(GObject.GPointer): ...

class MarkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkClass()
    """
    @property
    def parent_class(self) -> _Gtk3.TextMarkClass: ...
    @property
    def padding(self) -> list[None]: ...

class MarkPrivate(GObject.GPointer): ...

class PrintCompositor(GObject.Object):
    """
    :Constructors:

    ::

        PrintCompositor(**properties)
        new(buffer:GtkSource.Buffer) -> GtkSource.PrintCompositor
        new_from_view(view:GtkSource.View) -> GtkSource.PrintCompositor

    Object GtkSourcePrintCompositor

    Properties from GtkSourcePrintCompositor:
      buffer -> GtkSourceBuffer: Source Buffer
        The GtkSourceBuffer object to print
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      wrap-mode -> GtkWrapMode: Wrap Mode

      highlight-syntax -> gboolean: Highlight Syntax

      print-line-numbers -> guint: Print Line Numbers

      print-header -> gboolean: Print Header

      print-footer -> gboolean: Print Footer

      body-font-name -> gchararray: Body Font Name

      line-numbers-font-name -> gchararray: Line Numbers Font Name

      header-font-name -> gchararray: Header Font Name

      footer-font-name -> gchararray: Footer Font Name

      n-pages -> gint: Number of pages


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        body_font_name: str
        buffer: Buffer
        footer_font_name: str
        header_font_name: str
        highlight_syntax: bool
        line_numbers_font_name: str
        n_pages: int
        print_footer: bool
        print_header: bool
        print_line_numbers: int
        tab_width: int
        wrap_mode: _Gtk3.WrapMode

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> PrintCompositorPrivate: ...
    def __init__(
        self,
        *,
        body_font_name: str = ...,
        buffer: Buffer = ...,
        footer_font_name: str | None = ...,
        header_font_name: str | None = ...,
        highlight_syntax: bool = ...,
        line_numbers_font_name: str | None = ...,
        print_footer: bool = ...,
        print_header: bool = ...,
        print_line_numbers: int = ...,
        tab_width: int = ...,
        wrap_mode: _Gtk3.WrapMode = ...,
    ) -> None: ...
    def draw_page(self, context: _Gtk3.PrintContext, page_nr: int) -> None: ...
    def get_body_font_name(self) -> str: ...
    def get_bottom_margin(self, unit: _Gtk3.Unit) -> float: ...
    def get_buffer(self) -> Buffer: ...
    def get_footer_font_name(self) -> str: ...
    def get_header_font_name(self) -> str: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_left_margin(self, unit: _Gtk3.Unit) -> float: ...
    def get_line_numbers_font_name(self) -> str: ...
    def get_n_pages(self) -> int: ...
    def get_pagination_progress(self) -> float: ...
    def get_print_footer(self) -> bool: ...
    def get_print_header(self) -> bool: ...
    def get_print_line_numbers(self) -> int: ...
    def get_right_margin(self, unit: _Gtk3.Unit) -> float: ...
    def get_tab_width(self) -> int: ...
    def get_top_margin(self, unit: _Gtk3.Unit) -> float: ...
    def get_wrap_mode(self) -> _Gtk3.WrapMode: ...
    @classmethod
    def new(cls, buffer: Buffer) -> PrintCompositor: ...
    @classmethod
    def new_from_view(cls, view: View) -> PrintCompositor: ...
    def paginate(self, context: _Gtk3.PrintContext) -> bool: ...
    def set_body_font_name(self, font_name: str) -> None: ...
    def set_bottom_margin(self, margin: float, unit: _Gtk3.Unit) -> None: ...
    def set_footer_font_name(self, font_name: str | None = None) -> None: ...
    def set_footer_format(
        self,
        separator: bool,
        left: str | None = None,
        center: str | None = None,
        right: str | None = None,
    ) -> None: ...
    def set_header_font_name(self, font_name: str | None = None) -> None: ...
    def set_header_format(
        self,
        separator: bool,
        left: str | None = None,
        center: str | None = None,
        right: str | None = None,
    ) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_left_margin(self, margin: float, unit: _Gtk3.Unit) -> None: ...
    def set_line_numbers_font_name(self, font_name: str | None = None) -> None: ...
    def set_print_footer(self, print_: bool) -> None: ...
    def set_print_header(self, print_: bool) -> None: ...
    def set_print_line_numbers(self, interval: int) -> None: ...
    def set_right_margin(self, margin: float, unit: _Gtk3.Unit) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def set_top_margin(self, margin: float, unit: _Gtk3.Unit) -> None: ...
    def set_wrap_mode(self, wrap_mode: _Gtk3.WrapMode) -> None: ...

class PrintCompositorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintCompositorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class PrintCompositorPrivate(GObject.GPointer): ...

class Region(GObject.Object):
    """
    :Constructors:

    ::

        Region(**properties)
        new(buffer:Gtk.TextBuffer) -> GtkSource.Region

    Object GtkSourceRegion

    Properties from GtkSourceRegion:
      buffer -> GtkTextBuffer: Buffer


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffer: _Gtk3.TextBuffer | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(self, *, buffer: _Gtk3.TextBuffer = ...) -> None: ...
    def add_region(self, region_to_add: Region | None = None) -> None: ...
    def add_subregion(self, _start: _Gtk3.TextIter, _end: _Gtk3.TextIter) -> None: ...
    def get_bounds(self) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter]: ...
    def get_buffer(self) -> _Gtk3.TextBuffer | None: ...
    def get_start_region_iter(self) -> RegionIter: ...
    def intersect_region(self, region2: Region | None = None) -> Region | None: ...
    def intersect_subregion(
        self, _start: _Gtk3.TextIter, _end: _Gtk3.TextIter
    ) -> Region | None: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls, buffer: _Gtk3.TextBuffer) -> Region: ...
    def subtract_region(self, region_to_subtract: Region | None = None) -> None: ...
    def subtract_subregion(
        self, _start: _Gtk3.TextIter, _end: _Gtk3.TextIter
    ) -> None: ...
    def to_string(self) -> str | None: ...

class RegionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegionClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class RegionIter(GObject.GPointer):
    """
    :Constructors:

    ::

        RegionIter()
    """
    @property
    def dummy1(self) -> None: ...
    @property
    def dummy2(self) -> int: ...
    @property
    def dummy3(self) -> None: ...
    def get_subregion(self) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter]: ...
    def is_end(self) -> bool: ...
    def next(self) -> bool: ...

class SearchContext(GObject.Object):
    """
    :Constructors:

    ::

        SearchContext(**properties)
        new(buffer:GtkSource.Buffer, settings:GtkSource.SearchSettings=None) -> GtkSource.SearchContext

    Object GtkSourceSearchContext

    Properties from GtkSourceSearchContext:
      buffer -> GtkSourceBuffer: Buffer
        The associated GtkSourceBuffer
      settings -> GtkSourceSearchSettings: Settings
        The associated GtkSourceSearchSettings
      highlight -> gboolean: Highlight
        Highlight search occurrences
      match-style -> GtkSourceStyle: Match style
        The text style for matches
      occurrences-count -> gint: Occurrences count
        Total number of search occurrences
      regex-error -> gpointer: Regex error
        Regular expression error

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffer: Buffer
        highlight: bool
        match_style: Style
        occurrences_count: int
        regex_error: None | None
        settings: SearchSettings

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> SearchContextPrivate: ...
    def __init__(
        self,
        *,
        buffer: Buffer = ...,
        highlight: bool = ...,
        match_style: Style | None = ...,
        settings: SearchSettings = ...,
    ) -> None: ...
    def backward(
        self, iter: _Gtk3.TextIter
    ) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter, bool]: ...
    def backward_async(
        self,
        iter: _Gtk3.TextIter,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def backward_finish(
        self, result: Gio.AsyncResult
    ) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter, bool]: ...
    def forward(
        self, iter: _Gtk3.TextIter
    ) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter, bool]: ...
    def forward_async(
        self,
        iter: _Gtk3.TextIter,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def forward_finish(
        self, result: Gio.AsyncResult
    ) -> tuple[bool, _Gtk3.TextIter, _Gtk3.TextIter, bool]: ...
    def get_buffer(self) -> Buffer: ...
    def get_highlight(self) -> bool: ...
    def get_match_style(self) -> Style: ...
    def get_occurrence_position(
        self, match_start: _Gtk3.TextIter, match_end: _Gtk3.TextIter
    ) -> int: ...
    def get_occurrences_count(self) -> int: ...
    def get_regex_error(self) -> GLib.Error | None: ...
    def get_settings(self) -> SearchSettings: ...
    @classmethod
    def new(
        cls, buffer: Buffer, settings: SearchSettings | None = None
    ) -> SearchContext: ...
    def replace(
        self,
        match_start: _Gtk3.TextIter,
        match_end: _Gtk3.TextIter,
        replace: str,
        replace_length: int,
    ) -> bool: ...
    def replace_all(self, replace: str, replace_length: int) -> int: ...
    def set_highlight(self, highlight: bool) -> None: ...
    def set_match_style(self, match_style: Style | None = None) -> None: ...

class SearchContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SearchContextClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class SearchContextPrivate(GObject.GPointer): ...

class SearchSettings(GObject.Object):
    """
    :Constructors:

    ::

        SearchSettings(**properties)
        new() -> GtkSource.SearchSettings

    Object GtkSourceSearchSettings

    Properties from GtkSourceSearchSettings:
      search-text -> gchararray: Search text
        The text to search
      case-sensitive -> gboolean: Case sensitive
        Case sensitive
      at-word-boundaries -> gboolean: At word boundaries
        Search at word boundaries
      wrap-around -> gboolean: Wrap around
        Wrap around
      regex-enabled -> gboolean: Regex enabled
        Whether to search by regular expression

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        at_word_boundaries: bool
        case_sensitive: bool
        regex_enabled: bool
        search_text: str | None
        wrap_around: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> SearchSettingsPrivate: ...
    def __init__(
        self,
        *,
        at_word_boundaries: bool = ...,
        case_sensitive: bool = ...,
        regex_enabled: bool = ...,
        search_text: str | None = ...,
        wrap_around: bool = ...,
    ) -> None: ...
    def get_at_word_boundaries(self) -> bool: ...
    def get_case_sensitive(self) -> bool: ...
    def get_regex_enabled(self) -> bool: ...
    def get_search_text(self) -> str | None: ...
    def get_wrap_around(self) -> bool: ...
    @classmethod
    def new(cls) -> SearchSettings: ...
    def set_at_word_boundaries(self, at_word_boundaries: bool) -> None: ...
    def set_case_sensitive(self, case_sensitive: bool) -> None: ...
    def set_regex_enabled(self, regex_enabled: bool) -> None: ...
    def set_search_text(self, search_text: str | None = None) -> None: ...
    def set_wrap_around(self, wrap_around: bool) -> None: ...

class SearchSettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SearchSettingsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class SearchSettingsPrivate(GObject.GPointer): ...

class SpaceDrawer(GObject.Object):
    """
    :Constructors:

    ::

        SpaceDrawer(**properties)
        new() -> GtkSource.SpaceDrawer

    Object GtkSourceSpaceDrawer

    Properties from GtkSourceSpaceDrawer:
      enable-matrix -> gboolean: Enable Matrix

      matrix -> GVariant: Matrix


    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        enable_matrix: bool
        matrix: GLib.Variant

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> SpaceDrawerPrivate: ...
    def __init__(
        self, *, enable_matrix: bool = ..., matrix: GLib.Variant | None = ...
    ) -> None: ...
    def bind_matrix_setting(
        self, settings: Gio.Settings, key: str, flags: Gio.SettingsBindFlags
    ) -> None: ...
    def get_enable_matrix(self) -> bool: ...
    def get_matrix(self) -> GLib.Variant: ...
    def get_types_for_locations(
        self, locations: SpaceLocationFlags
    ) -> SpaceTypeFlags: ...
    @classmethod
    def new(cls) -> SpaceDrawer: ...
    def set_enable_matrix(self, enable_matrix: bool) -> None: ...
    def set_matrix(self, matrix: GLib.Variant | None = None) -> None: ...
    def set_types_for_locations(
        self, locations: SpaceLocationFlags, types: SpaceTypeFlags
    ) -> None: ...

class SpaceDrawerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpaceDrawerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class SpaceDrawerPrivate(GObject.GPointer): ...

class Style(GObject.Object):
    """
    :Constructors:

    ::

        Style(**properties)

    Object GtkSourceStyle

    Properties from GtkSourceStyle:
      line-background -> gchararray: Line background
        Line background color
      line-background-set -> gboolean: Line background set
        Whether line background color is set
      background -> gchararray: Background
        Background color
      background-set -> gboolean: Background set
        Whether background color is set
      foreground -> gchararray: Foreground
        Foreground color
      foreground-set -> gboolean: Foreground set
        Whether foreground color is set
      bold -> gboolean: Bold
        Bold
      bold-set -> gboolean: Bold set
        Whether bold attribute is set
      italic -> gboolean: Italic
        Italic
      italic-set -> gboolean: Italic set
        Whether italic attribute is set
      pango-underline -> PangoUnderline: Pango Underline
        Pango Underline
      underline-set -> gboolean: Underline set
        Whether underline attribute is set
      strikethrough -> gboolean: Strikethrough
        Strikethrough
      strikethrough-set -> gboolean: Strikethrough set
        Whether strikethrough attribute is set
      scale -> gchararray: Scale
        Text scale factor
      scale-set -> gboolean: Scale set
        Whether scale attribute is set
      underline-color -> gchararray: Underline Color
        Underline color
      underline-color-set -> gboolean: Underline color set
        Whether underline color attribute is set

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        background: str
        background_set: bool
        bold: bool
        bold_set: bool
        foreground: str
        foreground_set: bool
        italic: bool
        italic_set: bool
        line_background: str
        line_background_set: bool
        pango_underline: Pango.Underline
        scale: str
        scale_set: bool
        strikethrough: bool
        strikethrough_set: bool
        underline_color: str
        underline_color_set: bool
        underline_set: bool

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        background: str = ...,
        background_set: bool = ...,
        bold: bool = ...,
        bold_set: bool = ...,
        foreground: str = ...,
        foreground_set: bool = ...,
        italic: bool = ...,
        italic_set: bool = ...,
        line_background: str = ...,
        line_background_set: bool = ...,
        pango_underline: Pango.Underline = ...,
        scale: str = ...,
        scale_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        underline_color: str = ...,
        underline_color_set: bool = ...,
        underline_set: bool = ...,
    ) -> None: ...
    def apply(self, tag: _Gtk3.TextTag) -> None: ...
    def copy(self) -> Style: ...

class StyleClass(GObject.GPointer): ...

class StyleScheme(GObject.Object):
    """
    :Constructors:

    ::

        StyleScheme(**properties)

    Object GtkSourceStyleScheme

    Properties from GtkSourceStyleScheme:
      id -> gchararray: Style scheme id
        Style scheme id
      name -> gchararray: Style scheme name
        Style scheme name
      description -> gchararray: Style scheme description
        Style scheme description
      filename -> gchararray: Style scheme filename
        Style scheme filename

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        description: str | None
        filename: str | None
        id: str
        name: str

    @property
    def props(self) -> Props: ...
    @property
    def base(self) -> GObject.Object: ...
    @property
    def priv(self) -> StyleSchemePrivate: ...
    def __init__(self, *, id: str = ...) -> None: ...
    def get_authors(self) -> list[str] | None: ...
    def get_description(self) -> str | None: ...
    def get_filename(self) -> str | None: ...
    def get_id(self) -> str: ...
    def get_name(self) -> str: ...
    def get_style(self, style_id: str) -> Style | None: ...

class StyleSchemeChooser(GObject.GInterface, Protocol):
    """
    Interface GtkSourceStyleSchemeChooser

    Signals from GObject:
      notify (GParam)
    """
    def get_style_scheme(self) -> StyleScheme: ...
    def set_style_scheme(self, scheme: StyleScheme) -> None: ...

class StyleSchemeChooserButton(
    _Gtk3.Button,
    Atk.ImplementorIface,
    _Gtk3.Actionable,
    _Gtk3.Activatable,
    _Gtk3.Buildable,
    StyleSchemeChooser,
):
    """
    :Constructors:

    ::

        StyleSchemeChooserButton(**properties)
        new() -> Gtk.Widget

    Object GtkSourceStyleSchemeChooserButton

    Signals from GtkButton:
      activate ()
      pressed ()
      released ()
      clicked ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.Button.Props):
        always_show_image: bool
        image: _Gtk3.Widget | None
        image_position: _Gtk3.PositionType
        label: str
        relief: _Gtk3.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: _Gtk3.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: _Gdk3.EventMask
        expand: bool
        focus_on_click: bool
        halign: _Gtk3.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: _Gtk3.Container | None
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: _Gtk3.Style
        tooltip_markup: str | None
        tooltip_text: str | None
        valign: _Gtk3.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: _Gdk3.Window | None
        action_name: str | None
        action_target: GLib.Variant
        related_action: _Gtk3.Action
        use_action_appearance: bool
        style_scheme: StyleScheme
        child: _Gtk3.Widget

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> _Gtk3.Button: ...
    def __init__(
        self,
        *,
        always_show_image: bool = ...,
        image: _Gtk3.Widget | None = ...,
        image_position: _Gtk3.PositionType = ...,
        label: str = ...,
        relief: _Gtk3.ReliefStyle = ...,
        use_stock: bool = ...,
        use_underline: bool = ...,
        xalign: float = ...,
        yalign: float = ...,
        border_width: int = ...,
        child: _Gtk3.Widget = ...,
        resize_mode: _Gtk3.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: _Gdk3.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: _Gtk3.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: _Gtk3.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: _Gtk3.Style | None = ...,
        tooltip_markup: str | None = ...,
        tooltip_text: str | None = ...,
        valign: _Gtk3.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: str | None = ...,
        action_target: GLib.Variant = ...,
        related_action: _Gtk3.Action = ...,
        use_action_appearance: bool = ...,
        style_scheme: StyleScheme = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> StyleSchemeChooserButton: ...

class StyleSchemeChooserButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserButtonClass()
    """
    @property
    def parent(self) -> _Gtk3.ButtonClass: ...
    @property
    def padding(self) -> list[None]: ...

class StyleSchemeChooserInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserInterface()
    """
    @property
    def base_interface(self) -> GObject.TypeInterface: ...
    @property
    def get_style_scheme(self) -> Callable[[StyleSchemeChooser], StyleScheme]: ...
    @property
    def set_style_scheme(self) -> Callable[[StyleSchemeChooser, StyleScheme], None]: ...
    @property
    def padding(self) -> list[None]: ...

class StyleSchemeChooserWidget(
    _Gtk3.Bin, Atk.ImplementorIface, _Gtk3.Buildable, StyleSchemeChooser
):
    """
    :Constructors:

    ::

        StyleSchemeChooserWidget(**properties)
        new() -> Gtk.Widget

    Object GtkSourceStyleSchemeChooserWidget

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.Bin.Props):
        border_width: int
        resize_mode: _Gtk3.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: _Gdk3.EventMask
        expand: bool
        focus_on_click: bool
        halign: _Gtk3.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: _Gtk3.Container | None
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: _Gtk3.Style
        tooltip_markup: str | None
        tooltip_text: str | None
        valign: _Gtk3.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: _Gdk3.Window | None
        style_scheme: StyleScheme
        child: _Gtk3.Widget

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> _Gtk3.Bin: ...
    def __init__(
        self,
        *,
        border_width: int = ...,
        child: _Gtk3.Widget = ...,
        resize_mode: _Gtk3.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: _Gdk3.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: _Gtk3.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: _Gtk3.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: _Gtk3.Style | None = ...,
        tooltip_markup: str | None = ...,
        tooltip_text: str | None = ...,
        valign: _Gtk3.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        style_scheme: StyleScheme = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> StyleSchemeChooserWidget: ...

class StyleSchemeChooserWidgetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserWidgetClass()
    """
    @property
    def parent(self) -> _Gtk3.BinClass: ...
    @property
    def padding(self) -> list[None]: ...

class StyleSchemeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeClass()
    """
    @property
    def base_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class StyleSchemeManager(GObject.Object):
    """
    :Constructors:

    ::

        StyleSchemeManager(**properties)
        new() -> GtkSource.StyleSchemeManager

    Object GtkSourceStyleSchemeManager

    Properties from GtkSourceStyleSchemeManager:
      search-path -> GStrv: Style scheme search path
        List of directories and files where the style schemes are located
      scheme-ids -> GStrv: Scheme ids
        List of the ids of the available style schemes

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        scheme_ids: list[str] | None
        search_path: list[str]

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> StyleSchemeManagerPrivate: ...
    def __init__(self, *, search_path: Sequence[str] | None = ...) -> None: ...
    def append_search_path(self, path: str) -> None: ...
    def force_rescan(self) -> None: ...
    @staticmethod
    def get_default() -> StyleSchemeManager: ...
    def get_scheme(self, scheme_id: str) -> StyleScheme | None: ...
    def get_scheme_ids(self) -> list[str] | None: ...
    def get_search_path(self) -> list[str]: ...
    @classmethod
    def new(cls) -> StyleSchemeManager: ...
    def prepend_search_path(self, path: str) -> None: ...
    def set_search_path(self, path: Sequence[str] | None = None) -> None: ...

class StyleSchemeManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeManagerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[None]: ...

class StyleSchemeManagerPrivate(GObject.GPointer): ...
class StyleSchemePrivate(GObject.GPointer): ...

class Tag(_Gtk3.TextTag):
    """
    :Constructors:

    ::

        Tag(**properties)
        new(name:str=None) -> Gtk.TextTag

    Object GtkSourceTag

    Properties from GtkSourceTag:
      draw-spaces -> gboolean: Draw Spaces

      draw-spaces-set -> gboolean: Draw Spaces Set


    Signals from GtkTextTag:
      event (GObject, GdkEvent, GtkTextIter) -> gboolean

    Properties from GtkTextTag:
      name -> gchararray: Tag name
        Name used to refer to the text tag. NULL for anonymous tags
      background -> gchararray: Background color name
        Background color as a string
      foreground -> gchararray: Foreground color name
        Foreground color as a string
      background-gdk -> GdkColor: Background color
        Background color as a GdkColor
      foreground-gdk -> GdkColor: Foreground color
        Foreground color as a GdkColor
      background-rgba -> GdkRGBA: Background RGBA
        Background color as a GdkRGBA
      foreground-rgba -> GdkRGBA: Foreground RGBA
        Foreground color as a GdkRGBA
      font -> gchararray: Font
        Font description as a string, e.g. "Sans Italic 12"
      font-desc -> PangoFontDescription: Font
        Font description as a PangoFontDescription struct
      family -> gchararray: Font family
        Name of the font family, e.g. Sans, Helvetica, Times, Monospace
      style -> PangoStyle: Font style
        Font style as a PangoStyle, e.g. PANGO_STYLE_ITALIC
      variant -> PangoVariant: Font variant
        Font variant as a PangoVariant, e.g. PANGO_VARIANT_SMALL_CAPS
      weight -> gint: Font weight
        Font weight as an integer, see predefined values in PangoWeight; for example, PANGO_WEIGHT_BOLD
      stretch -> PangoStretch: Font stretch
        Font stretch as a PangoStretch, e.g. PANGO_STRETCH_CONDENSED
      size -> gint: Font size
        Font size in Pango units
      size-points -> gdouble: Font points
        Font size in points
      scale -> gdouble: Font scale
        Font size as a scale factor relative to the default font size. This properly adapts to theme changes etc. so is recommended. Pango predefines some scales such as PANGO_SCALE_X_LARGE
      pixels-above-lines -> gint: Pixels above lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels below lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels inside wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      direction -> GtkTextDirection: Text direction
        Text direction, e.g. right-to-left or left-to-right
      left-margin -> gint: Left margin
        Width of the left margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      strikethrough -> gboolean: Strikethrough
        Whether to strike through the text
      strikethrough-rgba -> GdkRGBA: Strikethrough RGBA
        Color of strikethrough for this text
      right-margin -> gint: Right margin
        Width of the right margin in pixels
      underline -> PangoUnderline: Underline
        Style of underline for this text
      underline-rgba -> GdkRGBA: Underline RGBA
        Color of underline for this text
      rise -> gint: Rise
        Offset of text above the baseline (below the baseline if rise is negative) in Pango units
      background-full-height -> gboolean: Background full height
        Whether the background color fills the entire line height or only the height of the tagged characters
      language -> gchararray: Language
        The language this text is in, as an ISO code. Pango can use this as a hint when rendering the text. If not set, an appropriate default will be used.
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      invisible -> gboolean: Invisible
        Whether this text is hidden.
      paragraph-background -> gchararray: Paragraph background color name
        Paragraph background color as a string
      paragraph-background-gdk -> GdkColor: Paragraph background color
        Paragraph background color as a GdkColor
      paragraph-background-rgba -> GdkRGBA: Paragraph background RGBA
        Paragraph background RGBA as a GdkRGBA
      fallback -> gboolean: Fallback
        Whether font fallback is enabled.
      letter-spacing -> gint: Letter Spacing
        Extra spacing between graphemes
      font-features -> gchararray: Font Features
        OpenType Font Features to use
      accumulative-margin -> gboolean: Margin Accumulates
        Whether left and right margins accumulate.
      background-set -> gboolean: Background set
        Whether this tag affects the background color
      foreground-set -> gboolean: Foreground set
        Whether this tag affects the foreground color
      family-set -> gboolean: Font family set
        Whether this tag affects the font family
      style-set -> gboolean: Font style set
        Whether this tag affects the font style
      variant-set -> gboolean: Font variant set
        Whether this tag affects the font variant
      weight-set -> gboolean: Font weight set
        Whether this tag affects the font weight
      stretch-set -> gboolean: Font stretch set
        Whether this tag affects the font stretch
      size-set -> gboolean: Font size set
        Whether this tag affects the font size
      scale-set -> gboolean: Font scale set
        Whether this tag scales the font size by a factor
      pixels-above-lines-set -> gboolean: Pixels above lines set
        Whether this tag affects the number of pixels above lines
      pixels-below-lines-set -> gboolean: Pixels below lines set
        Whether this tag affects the number of pixels above lines
      pixels-inside-wrap-set -> gboolean: Pixels inside wrap set
        Whether this tag affects the number of pixels between wrapped lines
      editable-set -> gboolean: Editability set
        Whether this tag affects text editability
      wrap-mode-set -> gboolean: Wrap mode set
        Whether this tag affects line wrap mode
      justification-set -> gboolean: Justification set
        Whether this tag affects paragraph justification
      left-margin-set -> gboolean: Left margin set
        Whether this tag affects the left margin
      indent-set -> gboolean: Indent set
        Whether this tag affects indentation
      strikethrough-set -> gboolean: Strikethrough set
        Whether this tag affects strikethrough
      strikethrough-rgba-set -> gboolean: Strikethrough RGBA set
        Whether this tag affects strikethrough color
      right-margin-set -> gboolean: Right margin set
        Whether this tag affects the right margin
      underline-set -> gboolean: Underline set
        Whether this tag affects underlining
      underline-rgba-set -> gboolean: Underline RGBA set
        Whether this tag affects underlining color
      rise-set -> gboolean: Rise set
        Whether this tag affects the rise
      background-full-height-set -> gboolean: Background full height set
        Whether this tag affects background height
      language-set -> gboolean: Language set
        Whether this tag affects the language the text is rendered as
      tabs-set -> gboolean: Tabs set
        Whether this tag affects tabs
      invisible-set -> gboolean: Invisible set
        Whether this tag affects text visibility
      paragraph-background-set -> gboolean: Paragraph background set
        Whether this tag affects the paragraph background color
      fallback-set -> gboolean: Fallback set
        Whether this tag affects font fallback
      letter-spacing-set -> gboolean: Letter spacing set
        Whether this tag affects letter spacing
      font-features-set -> gboolean: Font features set
        Whether this tag affects font features

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.TextTag.Props):
        draw_spaces: bool
        draw_spaces_set: bool
        accumulative_margin: bool
        background_full_height: bool
        background_full_height_set: bool
        background_gdk: _Gdk3.Color
        background_rgba: _Gdk3.RGBA
        background_set: bool
        direction: _Gtk3.TextDirection
        editable: bool
        editable_set: bool
        fallback: bool
        fallback_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        font_features_set: bool
        foreground_gdk: _Gdk3.Color
        foreground_rgba: _Gdk3.RGBA
        foreground_set: bool
        indent: int
        indent_set: bool
        invisible: bool
        invisible_set: bool
        justification: _Gtk3.Justification
        justification_set: bool
        language: str
        language_set: bool
        left_margin: int
        left_margin_set: bool
        letter_spacing: int
        letter_spacing_set: bool
        name: str
        paragraph_background_gdk: _Gdk3.Color
        paragraph_background_rgba: _Gdk3.RGBA
        paragraph_background_set: bool
        pixels_above_lines: int
        pixels_above_lines_set: bool
        pixels_below_lines: int
        pixels_below_lines_set: bool
        pixels_inside_wrap: int
        pixels_inside_wrap_set: bool
        right_margin: int
        right_margin_set: bool
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_rgba: _Gdk3.RGBA
        strikethrough_rgba_set: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        tabs: Pango.TabArray
        tabs_set: bool
        underline: Pango.Underline
        underline_rgba: _Gdk3.RGBA
        underline_rgba_set: bool
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        wrap_mode: _Gtk3.WrapMode
        wrap_mode_set: bool
        background: str
        foreground: str
        paragraph_background: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> _Gtk3.TextTag: ...
    def __init__(
        self,
        *,
        draw_spaces: bool = ...,
        draw_spaces_set: bool = ...,
        accumulative_margin: bool = ...,
        background: str = ...,
        background_full_height: bool = ...,
        background_full_height_set: bool = ...,
        background_gdk: _Gdk3.Color = ...,
        background_rgba: _Gdk3.RGBA = ...,
        background_set: bool = ...,
        direction: _Gtk3.TextDirection = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        fallback: bool = ...,
        fallback_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        font_features: str = ...,
        font_features_set: bool = ...,
        foreground: str = ...,
        foreground_gdk: _Gdk3.Color = ...,
        foreground_rgba: _Gdk3.RGBA = ...,
        foreground_set: bool = ...,
        indent: int = ...,
        indent_set: bool = ...,
        invisible: bool = ...,
        invisible_set: bool = ...,
        justification: _Gtk3.Justification = ...,
        justification_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        left_margin: int = ...,
        left_margin_set: bool = ...,
        letter_spacing: int = ...,
        letter_spacing_set: bool = ...,
        name: str = ...,
        paragraph_background: str = ...,
        paragraph_background_gdk: _Gdk3.Color = ...,
        paragraph_background_rgba: _Gdk3.RGBA = ...,
        paragraph_background_set: bool = ...,
        pixels_above_lines: int = ...,
        pixels_above_lines_set: bool = ...,
        pixels_below_lines: int = ...,
        pixels_below_lines_set: bool = ...,
        pixels_inside_wrap: int = ...,
        pixels_inside_wrap_set: bool = ...,
        right_margin: int = ...,
        right_margin_set: bool = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_rgba: _Gdk3.RGBA = ...,
        strikethrough_rgba_set: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        tabs: Pango.TabArray = ...,
        tabs_set: bool = ...,
        underline: Pango.Underline = ...,
        underline_rgba: _Gdk3.RGBA = ...,
        underline_rgba_set: bool = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        wrap_mode: _Gtk3.WrapMode = ...,
        wrap_mode_set: bool = ...,
    ) -> None: ...
    @classmethod
    def new(cls, name: str | None = None) -> Tag: ...

class TagClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TagClass()
    """
    @property
    def parent_class(self) -> _Gtk3.TextTagClass: ...
    @property
    def padding(self) -> list[None]: ...

class UndoManager(GObject.GInterface, Protocol):
    """
    Interface GtkSourceUndoManager

    Signals from GObject:
      notify (GParam)
    """
    def begin_not_undoable_action(self) -> None: ...
    def can_redo(self) -> bool: ...
    def can_redo_changed(self) -> None: ...
    def can_undo(self) -> bool: ...
    def can_undo_changed(self) -> None: ...
    def end_not_undoable_action(self) -> None: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...

class UndoManagerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        UndoManagerIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def can_undo(self) -> Callable[[UndoManager], bool]: ...
    @property
    def can_redo(self) -> Callable[[UndoManager], bool]: ...
    @property
    def undo(self) -> Callable[[UndoManager], None]: ...
    @property
    def redo(self) -> Callable[[UndoManager], None]: ...
    @property
    def begin_not_undoable_action(self) -> Callable[[UndoManager], None]: ...
    @property
    def end_not_undoable_action(self) -> Callable[[UndoManager], None]: ...
    @property
    def can_undo_changed(self) -> Callable[[UndoManager], None]: ...
    @property
    def can_redo_changed(self) -> Callable[[UndoManager], None]: ...

class View(_Gtk3.TextView, Atk.ImplementorIface, _Gtk3.Buildable, _Gtk3.Scrollable):
    """
    :Constructors:

    ::

        View(**properties)
        new() -> Gtk.Widget
        new_with_buffer(buffer:GtkSource.Buffer) -> Gtk.Widget

    Object GtkSourceView

    Signals from GtkSourceView:
      undo ()
      redo ()
      smart-home-end (GtkTextIter, gint)
      show-completion ()
      line-mark-activated (GtkTextIter, GdkEvent)
      move-lines (gboolean)
      move-words (gint)
      move-to-matching-bracket (gboolean)
      change-number (gint)
      change-case (GtkSourceChangeCaseType)
      join-lines ()

    Properties from GtkSourceView:
      completion -> GtkSourceCompletion: Completion
        The completion object associated with the view
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      background-pattern -> GtkSourceBackgroundPatternType: Background pattern
        Draw a specific background pattern on the view
      smart-backspace -> gboolean: Smart Backspace

      space-drawer -> GtkSourceSpaceDrawer: Space Drawer


    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      populate-popup (GtkWidget)
      select-all (gboolean)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean
      insert-emoji ()

    Properties from GtkTextView:
      pixels-above-lines -> gint: Pixels Above Lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels Below Lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      left-margin -> gint: Left Margin
        Width of the left margin in pixels
      right-margin -> gint: Right Margin
        Width of the right margin in pixels
      top-margin -> gint: Top Margin
        Height of the top margin in pixels
      bottom-margin -> gint: Bottom Margin
        Height of the bottom margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      cursor-visible -> gboolean: Cursor Visible
        If the insertion cursor is shown
      buffer -> GtkTextBuffer: Buffer
        The buffer which is displayed
      overwrite -> gboolean: Overwrite mode
        Whether entered text overwrites existing contents
      accepts-tab -> gboolean: Accepts tab
        Whether Tab will result in a tab character being entered
      im-module -> gchararray: IM module
        Which IM module should be used
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      monospace -> gboolean: Monospace
        Whether to use a monospace font

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gtk3.TextView.Props):
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: _Gtk3.TextBuffer
        cursor_visible: bool
        editable: bool
        im_module: str
        indent: int
        input_hints: _Gtk3.InputHints
        input_purpose: _Gtk3.InputPurpose
        justification: _Gtk3.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        populate_all: bool
        right_margin: int
        tabs: Pango.TabArray | None
        top_margin: int
        wrap_mode: _Gtk3.WrapMode
        border_width: int
        resize_mode: _Gtk3.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: _Gdk3.EventMask
        expand: bool
        focus_on_click: bool
        halign: _Gtk3.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: _Gtk3.Container | None
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: _Gtk3.Style
        tooltip_markup: str | None
        tooltip_text: str | None
        valign: _Gtk3.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: _Gdk3.Window | None
        hadjustment: _Gtk3.Adjustment
        hscroll_policy: _Gtk3.ScrollablePolicy
        vadjustment: _Gtk3.Adjustment
        vscroll_policy: _Gtk3.ScrollablePolicy
        child: _Gtk3.Widget

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> _Gtk3.TextView: ...
    @property
    def priv(self) -> ViewPrivate: ...
    def __init__(
        self,
        *,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: _Gtk3.TextBuffer | None = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: _Gtk3.InputHints = ...,
        input_purpose: _Gtk3.InputPurpose = ...,
        justification: _Gtk3.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        populate_all: bool = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: _Gtk3.WrapMode = ...,
        border_width: int = ...,
        child: _Gtk3.Widget = ...,
        resize_mode: _Gtk3.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: _Gdk3.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: _Gtk3.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: _Gtk3.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: _Gtk3.Style | None = ...,
        tooltip_markup: str | None = ...,
        tooltip_text: str | None = ...,
        valign: _Gtk3.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        hadjustment: _Gtk3.Adjustment | None = ...,
        hscroll_policy: _Gtk3.ScrollablePolicy = ...,
        vadjustment: _Gtk3.Adjustment | None = ...,
        vscroll_policy: _Gtk3.ScrollablePolicy = ...,
    ) -> None: ...
    def do_line_mark_activated(
        self, iter: _Gtk3.TextIter, event: _Gdk3.Event
    ) -> None: ...
    def do_move_lines(self, down: bool) -> None: ...
    def do_move_words(self, step: int) -> None: ...
    def do_redo(self) -> None: ...
    def do_show_completion(self) -> None: ...
    def do_undo(self) -> None: ...
    def get_auto_indent(self) -> bool: ...
    def get_background_pattern(self) -> BackgroundPatternType: ...
    def get_completion(self) -> Completion: ...
    def get_gutter(self, window_type: _Gtk3.TextWindowType) -> Gutter: ...
    def get_highlight_current_line(self) -> bool: ...
    def get_indent_on_tab(self) -> bool: ...
    def get_indent_width(self) -> int: ...
    def get_insert_spaces_instead_of_tabs(self) -> bool: ...
    def get_mark_attributes(self, category: str, priority: int) -> MarkAttributes: ...
    def get_right_margin_position(self) -> int: ...
    def get_show_line_marks(self) -> bool: ...
    def get_show_line_numbers(self) -> bool: ...
    def get_show_right_margin(self) -> bool: ...
    def get_smart_backspace(self) -> bool: ...
    def get_smart_home_end(self) -> SmartHomeEndType: ...
    def get_space_drawer(self) -> SpaceDrawer: ...
    def get_tab_width(self) -> int: ...
    def get_visual_column(self, iter: _Gtk3.TextIter) -> int: ...
    def indent_lines(self, start: _Gtk3.TextIter, end: _Gtk3.TextIter) -> None: ...
    @classmethod
    def new(cls) -> View: ...
    @classmethod
    def new_with_buffer(cls, buffer: Buffer) -> View: ...
    def set_auto_indent(self, enable: bool) -> None: ...
    def set_background_pattern(
        self, background_pattern: BackgroundPatternType
    ) -> None: ...
    def set_highlight_current_line(self, highlight: bool) -> None: ...
    def set_indent_on_tab(self, enable: bool) -> None: ...
    def set_indent_width(self, width: int) -> None: ...
    def set_insert_spaces_instead_of_tabs(self, enable: bool) -> None: ...
    def set_mark_attributes(
        self, category: str, attributes: MarkAttributes, priority: int
    ) -> None: ...
    def set_right_margin_position(self, pos: int) -> None: ...
    def set_show_line_marks(self, show: bool) -> None: ...
    def set_show_line_numbers(self, show: bool) -> None: ...
    def set_show_right_margin(self, show: bool) -> None: ...
    def set_smart_backspace(self, smart_backspace: bool) -> None: ...
    def set_smart_home_end(self, smart_home_end: SmartHomeEndType) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def unindent_lines(self, start: _Gtk3.TextIter, end: _Gtk3.TextIter) -> None: ...

class ViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewClass()
    """
    @property
    def parent_class(self) -> _Gtk3.TextViewClass: ...
    @property
    def undo(self) -> Callable[[View], None]: ...
    @property
    def redo(self) -> Callable[[View], None]: ...
    @property
    def line_mark_activated(
        self,
    ) -> Callable[[View, _Gtk3.TextIter, _Gdk3.Event], None]: ...
    @property
    def show_completion(self) -> Callable[[View], None]: ...
    @property
    def move_lines(self) -> Callable[[View, bool], None]: ...
    @property
    def move_words(self) -> Callable[[View, int], None]: ...
    @property
    def padding(self) -> list[None]: ...

class ViewPrivate(GObject.GPointer): ...

class CompletionActivation(GObject.GFlags):
    INTERACTIVE = 1
    NONE = 0
    USER_REQUESTED = 2

class FileSaverFlags(GObject.GFlags):
    CREATE_BACKUP = 4
    IGNORE_INVALID_CHARS = 1
    IGNORE_MODIFICATION_TIME = 2
    NONE = 0

class GutterRendererState(GObject.GFlags):
    CURSOR = 1
    NORMAL = 0
    PRELIT = 2
    SELECTED = 4

class SortFlags(GObject.GFlags):
    CASE_SENSITIVE = 1
    NONE = 0
    REMOVE_DUPLICATES = 4
    REVERSE_ORDER = 2

class SpaceLocationFlags(GObject.GFlags):
    ALL = 7
    INSIDE_TEXT = 2
    LEADING = 1
    NONE = 0
    TRAILING = 4

class SpaceTypeFlags(GObject.GFlags):
    ALL = 15
    NBSP = 8
    NEWLINE = 4
    NONE = 0
    SPACE = 1
    TAB = 2

class BackgroundPatternType(GObject.GEnum):
    GRID = 1
    NONE = 0

class BracketMatchType(GObject.GEnum):
    FOUND = 3
    NONE = 0
    NOT_FOUND = 2
    OUT_OF_RANGE = 1

class ChangeCaseType(GObject.GEnum):
    LOWER = 0
    TITLE = 3
    TOGGLE = 2
    UPPER = 1

class CompletionError(GObject.GEnum):
    ALREADY_BOUND = 0
    NOT_BOUND = 1
    @staticmethod
    def quark() -> int: ...

class CompressionType(GObject.GEnum):
    GZIP = 1
    NONE = 0

class FileLoaderError(GObject.GEnum):
    CONVERSION_FALLBACK = 2
    ENCODING_AUTO_DETECTION_FAILED = 1
    TOO_BIG = 0
    @staticmethod
    def quark() -> int: ...

class FileSaverError(GObject.GEnum):
    EXTERNALLY_MODIFIED = 1
    INVALID_CHARS = 0
    @staticmethod
    def quark() -> int: ...

class GutterRendererAlignmentMode(GObject.GEnum):
    CELL = 0
    FIRST = 1
    LAST = 2

class NewlineType(GObject.GEnum):
    CR = 1
    CR_LF = 2
    LF = 0

class SmartHomeEndType(GObject.GEnum):
    AFTER = 2
    ALWAYS = 3
    BEFORE = 1
    DISABLED = 0

class ViewGutterPosition(GObject.GEnum):
    LINES = -30
    MARKS = -20
