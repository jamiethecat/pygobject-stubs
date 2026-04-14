from typing import Any
from typing import Final
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

BUILD_TYPE: Final = "plain"
MAJOR_VERSION: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
VERSION_S: Final = "1.2.1"

def error_quark() -> int: ...
def get_features() -> FeatureFlags: ...
def init() -> None: ...
def message_prettify(message: str, strip_comments: bool, comment_char: int) -> str: ...

class AnnotatedCommit(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_ref(repository:Ggit.Repository, ref:Ggit.Ref) -> Ggit.AnnotatedCommit
    """
    def get_id(self) -> OId | None: ...
    @classmethod
    def new_from_ref(cls, repository: Repository, ref: Ref) -> AnnotatedCommit: ...
    def ref(self) -> AnnotatedCommit | None: ...
    def unref(self) -> None: ...

class Blame(Native):
    """
    :Constructors:

    ::

        Blame(**properties)

    Object GgitBlame

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def from_buffer(self, buffer: Sequence[int]) -> Blame | None: ...
    @staticmethod
    def get_flags(blame_options: BlameOptions) -> BlameFlags: ...
    def get_hunk_by_index(self, idx: int) -> BlameHunk: ...
    def get_hunk_by_line(self, line: int) -> BlameHunk: ...
    def get_hunk_count(self) -> int: ...
    @staticmethod
    def set_flags(blame_options: BlameOptions, flags: BlameFlags) -> None: ...

class BlameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BlameClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class BlameHunk(GObject.GBoxed):
    def get_final_commit_id(self) -> OId | None: ...
    def get_final_signature(self) -> Signature | None: ...
    def get_final_start_line_number(self) -> int: ...
    def get_lines_in_hunk(self) -> int: ...
    def get_orig_commit_id(self) -> OId | None: ...
    def get_orig_path(self) -> str | None: ...
    def get_orig_signature(self) -> Signature | None: ...
    def get_orig_start_line_number(self) -> int: ...
    def is_boundary(self) -> bool: ...
    def ref(self) -> BlameHunk | None: ...
    def unref(self) -> None: ...

class BlameOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Ggit.BlameOptions
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> BlameOptions | None: ...
    def free(self) -> None: ...
    def get_maximum_line(self) -> int: ...
    def get_minimum_line(self) -> int: ...
    def get_minimum_match_characters(self) -> int: ...
    def get_newest_commit(self) -> OId | None: ...
    def get_oldest_commit(self) -> OId | None: ...
    @classmethod
    def new(cls) -> BlameOptions: ...
    def set_maximum_line(self, line: int) -> None: ...
    def set_minimum_line(self, line: int) -> None: ...
    def set_minimum_match_characters(self, characters: int) -> None: ...
    def set_newest_commit(self, oid: OId | None = None) -> None: ...
    def set_oldest_commit(self, oid: OId | None = None) -> None: ...

class Blob(Object):
    """
    :Constructors:

    ::

        Blob(**properties)

    Object GgitBlob

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def get_raw_content(self) -> bytes | None: ...
    def is_binary(self) -> bool: ...

class BlobClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BlobClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class BlobOutputStream(Gio.OutputStream):
    """
    :Constructors:

    ::

        BlobOutputStream(**properties)

    Object GgitBlobOutputStream

    Properties from GgitBlobOutputStream:
      repository -> GgitRepository: Repository
        Repository

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.OutputStream.Props):
        repository: Repository

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.OutputStream: ...
    def __init__(self, *, repository: Repository = ...) -> None: ...
    def get_id(self) -> OId | None: ...

class BlobOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BlobOutputStreamClass()
    """
    @property
    def parent_class(self) -> Gio.OutputStreamClass: ...

class Branch(Ref):
    """
    :Constructors:

    ::

        Branch(**properties)

    Object GgitBranch

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Ref.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Ref: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def delete(self) -> None: ...
    def get_name(self) -> str | None: ...
    def get_upstream(self) -> Ref | None: ...
    def is_head(self) -> bool: ...
    def move(self, new_branch_name: str, flags: CreateFlags) -> Branch | None: ...
    def set_upstream(self, upstream_branch_name: str) -> None: ...

class BranchClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BranchClass()
    """
    @property
    def parent_class(self) -> RefClass: ...

class BranchEnumerator(GObject.GBoxed):
    def get(self) -> Ref | None: ...
    def iterator(self) -> BranchEnumerator | None: ...
    def next(self) -> bool: ...
    def ref(self) -> BranchEnumerator | None: ...
    def unref(self) -> None: ...

class CheckoutOptions(GObject.Object):
    """
    :Constructors:

    ::

        CheckoutOptions(**properties)
        new() -> Ggit.CheckoutOptions or None

    Object GgitCheckoutOptions

    Properties from GgitCheckoutOptions:
      strategy -> GgitCheckoutStrategy: Strategy
        Strategy
      disable-filters -> gboolean: Disable Filters
        Disable filters
      dir-mode -> guint: Dir Mode
        Dir mode
      file-mode -> guint: File Mode
        File mode
      file-open-flags -> gint: File Open Flags
        File open flags
      notify-flags -> GgitCheckoutNotifyFlags: Notify Flags
        Notify flags
      baseline -> GgitTree: Baseline
        Baseline
      target-directory -> gchararray: Target Directory
        Target directory
      ancestor-label -> gchararray: Ancestor Label
        Ancestor label
      our-label -> gchararray: Our Label
        Our label
      their-label -> gchararray: Their Label
        Their label

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        ancestor_label: str | None
        baseline: Tree | None
        dir_mode: int
        disable_filters: bool
        file_mode: int
        file_open_flags: int
        notify_flags: CheckoutNotifyFlags
        our_label: str | None
        strategy: CheckoutStrategy
        target_directory: str | None
        their_label: str | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        ancestor_label: str | None = ...,
        baseline: Tree | None = ...,
        dir_mode: int = ...,
        disable_filters: bool = ...,
        file_mode: int = ...,
        file_open_flags: int = ...,
        notify_flags: CheckoutNotifyFlags = ...,
        our_label: str | None = ...,
        strategy: CheckoutStrategy = ...,
        target_directory: str | None = ...,
        their_label: str | None = ...,
    ) -> None: ...
    def do_notify(
        self,
        why: CheckoutNotifyFlags,
        path: str,
        baseline: DiffFile,
        target: DiffFile,
        workdir: DiffFile,
    ) -> int: ...
    def do_progress(
        self, path: str, completed_steps: int, total_steps: int
    ) -> None: ...
    def get_ancestor_label(self) -> str | None: ...
    def get_baseline(self) -> Tree | None: ...
    def get_dir_mode(self) -> int: ...
    def get_disable_filters(self) -> bool: ...
    def get_file_mode(self) -> int: ...
    def get_file_open_flags(self) -> int: ...
    def get_notify_flags(self) -> CheckoutNotifyFlags: ...
    def get_our_label(self) -> str | None: ...
    def get_paths(self) -> list[str] | None: ...
    def get_strategy(self) -> CheckoutStrategy: ...
    def get_target_directory(self) -> str | None: ...
    def get_their_label(self) -> str | None: ...
    @classmethod
    def new(cls) -> CheckoutOptions | None: ...
    def set_ancestor_label(self, label: str | None = None) -> None: ...
    def set_baseline(self, tree: Tree | None = None) -> None: ...
    def set_dir_mode(self, dir_mode: int) -> None: ...
    def set_disable_filters(self, disable: bool) -> None: ...
    def set_file_mode(self, file_mode: int) -> None: ...
    def set_file_open_flags(self, flags: int) -> None: ...
    def set_notify_flags(self, flags: CheckoutNotifyFlags) -> None: ...
    def set_our_label(self, label: str | None = None) -> None: ...
    def set_paths(self, paths: Sequence[str] | None = None) -> None: ...
    def set_strategy(self, strategy: CheckoutStrategy) -> None: ...
    def set_target_directory(self, directory: str | None = None) -> None: ...
    def set_their_label(self, label: str | None = None) -> None: ...

class CheckoutOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CheckoutOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def notify(
        self,
    ) -> Callable[
        [CheckoutOptions, CheckoutNotifyFlags, str, DiffFile, DiffFile, DiffFile], int
    ]: ...
    @property
    def progress(self) -> Callable[[CheckoutOptions, str, int, int], None]: ...

class CherryPickOptions(GObject.Object):
    """
    :Constructors:

    ::

        CherryPickOptions(**properties)
        new() -> Ggit.CherryPickOptions

    Object GgitCherryPickOptions

    Properties from GgitCherryPickOptions:
      mainline -> guint: Mainline
        Mainline
      checkout-options -> GgitCheckoutOptions: Checkout Options
        Checkout options
      merge-options -> GgitMergeOptions: Merge Options
        Merge options

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        checkout_options: CheckoutOptions
        mainline: int
        merge_options: MergeOptions

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        checkout_options: CheckoutOptions | None = ...,
        mainline: int = ...,
        merge_options: MergeOptions | None = ...,
    ) -> None: ...
    def get_checkout_options(self) -> CheckoutOptions: ...
    def get_mainline(self) -> int: ...
    def get_merge_options(self) -> MergeOptions: ...
    @classmethod
    def new(cls) -> CherryPickOptions: ...
    def set_checkout_options(
        self, checkout_options: CheckoutOptions | None = None
    ) -> None: ...
    def set_mainline(self, mainline: int) -> None: ...
    def set_merge_options(self, merge_options: MergeOptions | None = None) -> None: ...

class CherryPickOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CherryPickOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class CloneOptions(GObject.Object):
    """
    :Constructors:

    ::

        CloneOptions(**properties)
        new() -> Ggit.CloneOptions

    Object GgitCloneOptions

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_create_remote(
        self, repository: Repository, name: str, url: str
    ) -> Remote | None: ...
    def do_create_repository(self, path: str, is_bare: bool) -> Repository | None: ...
    def get_checkout_branch(self) -> str: ...
    def get_fetch_options(self) -> FetchOptions: ...
    def get_is_bare(self) -> bool: ...
    def get_local(self) -> CloneLocal: ...
    @classmethod
    def new(cls) -> CloneOptions: ...
    def set_checkout_branch(self, checkout_branch: str | None = None) -> None: ...
    def set_fetch_options(self, fetch_options: FetchOptions | None = None) -> None: ...
    def set_is_bare(self, bare: bool) -> None: ...
    def set_local(self, local: CloneLocal) -> None: ...

class CloneOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CloneOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def create_repository(
        self,
    ) -> Callable[[CloneOptions, str, bool], Repository | None]: ...
    @property
    def create_remote(
        self,
    ) -> Callable[[CloneOptions, Repository, str, str], Remote | None]: ...

class Commit(Object):
    """
    :Constructors:

    ::

        Commit(**properties)

    Object GgitCommit

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Object: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def amend(
        self,
        update_ref: str | None,
        author: Signature,
        committer: Signature,
        message_encoding: str | None,
        message: str,
        tree: Tree,
    ) -> OId | None: ...
    def get_author(self) -> Signature | None: ...
    def get_committer(self) -> Signature | None: ...
    def get_message(self) -> str | None: ...
    def get_message_encoding(self) -> str | None: ...
    def get_nth_ancestor(self, n: int) -> Commit | None: ...
    def get_parents(self) -> CommitParents | None: ...
    def get_subject(self) -> str | None: ...
    def get_tree(self) -> Tree | None: ...
    def get_tree_id(self) -> OId | None: ...

class CommitClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CommitClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class CommitParents(GObject.Object):
    """
    :Constructors:

    ::

        CommitParents(**properties)
        new(commit:Ggit.Commit) -> Ggit.CommitParents

    Object GgitCommitParents

    Properties from GgitCommitParents:
      commit -> GgitCommit: Commit
        The commit for the parents collection
      size -> guint: Size
        The size of the parents collection

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        commit: Commit
        size: int

    @property
    def props(self) -> Props: ...
    def __init__(self, *, commit: Commit = ...) -> None: ...
    def get(self, idx: int) -> Commit | None: ...
    def get_id(self, idx: int) -> OId | None: ...
    def get_size(self) -> int: ...
    @classmethod
    def new(cls, commit: Commit) -> CommitParents: ...

class CommitParentsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CommitParentsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Config(Native):
    """
    :Constructors:

    ::

        Config(**properties)
        new() -> Ggit.Config
        new_default() -> Ggit.Config
        new_from_file(file:Gio.File) -> Ggit.Config

    Object GgitConfig

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def add_file(self, file: Gio.File, level: ConfigLevel, force: bool) -> None: ...
    def delete_entry(self, name: str) -> bool: ...
    @staticmethod
    def find_global() -> Gio.File: ...
    @staticmethod
    def find_system() -> Gio.File: ...
    def foreach(self, callback: Callable[..., int], *user_data: Any) -> bool: ...
    def get_bool(self, name: str) -> bool: ...
    def get_entry(self, name: str) -> ConfigEntry: ...
    def get_int32(self, name: str) -> int: ...
    def get_int64(self, name: str) -> int: ...
    def get_string(self, name: str) -> str | None: ...
    def match(self, regex: GLib.Regex) -> tuple[str | None, GLib.MatchInfo]: ...
    def match_foreach(
        self, regex: GLib.Regex, callback: Callable[..., int], *user_data: Any
    ) -> bool: ...
    @classmethod
    def new(cls) -> Config: ...
    @classmethod
    def new_default(cls) -> Config: ...
    @classmethod
    def new_from_file(cls, file: Gio.File) -> Config: ...
    def open_level(self, level: ConfigLevel) -> Config: ...
    def set_bool(self, name: str, value: bool) -> bool: ...
    def set_int32(self, name: str, value: int) -> bool: ...
    def set_int64(self, name: str, value: int) -> bool: ...
    def set_string(self, name: str, value: str) -> bool: ...
    def snapshot(self) -> Config: ...

class ConfigClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConfigClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class ConfigEntry(GObject.GBoxed):
    def get_level(self) -> ConfigLevel: ...
    def get_name(self) -> str | None: ...
    def get_value(self) -> str | None: ...
    def ref(self) -> ConfigEntry | None: ...
    def unref(self) -> None: ...

class Cred(Native):
    """
    :Constructors:

    ::

        Cred(**properties)

    Object GgitCred

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, native: None = ...) -> None: ...

class CredClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CredClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class CredPlaintext(Cred, Gio.Initable):
    """
    :Constructors:

    ::

        CredPlaintext(**properties)
        new(username:str, password:str) -> Ggit.CredPlaintext

    Object GgitCredPlaintext

    Properties from GgitCredPlaintext:
      username -> gchararray: user name
        The user name
      password -> gchararray: password
        The password

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Cred.Props):
        password: str
        username: str
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Cred: ...
    def __init__(
        self, *, password: str = ..., username: str = ..., native: None = ...
    ) -> None: ...
    def get_password(self) -> str: ...
    def get_username(self) -> str: ...
    @classmethod
    def new(cls, username: str, password: str) -> CredPlaintext: ...

class CredPlaintextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CredPlaintextClass()
    """
    @property
    def parent_class(self) -> CredClass: ...

class CredSshInteractive(Cred, Gio.Initable):
    """
    :Constructors:

    ::

        CredSshInteractive(**properties)
        new(username:str) -> Ggit.CredSshInteractive

    Object GgitCredSshInteractive

    Properties from GgitCredSshInteractive:
      username -> gchararray: user name
        The user name

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Cred.Props):
        username: str
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Cred: ...
    def __init__(self, *, username: str = ..., native: None = ...) -> None: ...
    def do_prompt(self, prompts: Sequence[CredSshInteractivePrompt]) -> None: ...
    def get_username(self) -> str: ...
    @classmethod
    def new(cls, username: str) -> CredSshInteractive: ...

class CredSshInteractiveClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CredSshInteractiveClass()
    """
    @property
    def parent_class(self) -> CredClass: ...
    @property
    def prompt(
        self,
    ) -> Callable[[CredSshInteractive, Sequence[CredSshInteractivePrompt]], None]: ...

class CredSshInteractivePrompt(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(name:str, instruction:str, text:str, is_masked:bool) -> Ggit.CredSshInteractivePrompt
    """
    @staticmethod
    def __new__(
        cls: type[Self], name: str, instruction: str, text: str, is_masked: bool
    ) -> Self: ...
    def get_instruction(self) -> str: ...
    def get_name(self) -> str: ...
    def get_response(self) -> str: ...
    def get_text(self) -> str: ...
    def is_masked(self) -> bool: ...
    @classmethod
    def new(
        cls, name: str, instruction: str, text: str, is_masked: bool
    ) -> CredSshInteractivePrompt: ...
    def ref(self) -> CredSshInteractivePrompt: ...
    def set_response(self, response: str) -> None: ...
    def unref(self) -> None: ...

class CredSshKeyFromAgent(Cred, Gio.Initable):
    """
    :Constructors:

    ::

        CredSshKeyFromAgent(**properties)
        new(username:str) -> Ggit.CredSshKeyFromAgent or None

    Object GgitCredSshKeyFromAgent

    Properties from GgitCredSshKeyFromAgent:
      username -> gchararray: user name
        The user name

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Cred.Props):
        username: str | None
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, username: str = ..., native: None = ...) -> None: ...
    def get_username(self) -> str | None: ...
    @classmethod
    def new(cls, username: str) -> CredSshKeyFromAgent | None: ...

class CredSshKeyFromAgentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CredSshKeyFromAgentClass()
    """
    @property
    def parent_class(self) -> CredClass: ...

class Diff(Native):
    """
    :Constructors:

    ::

        Diff(**properties)
        new_buffers(buffer1:list=None, buffer1_as_path:str=None, buffer2:list=None, buffer2_as_path:str=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Diff or None
        new_index_to_workdir(repository:Ggit.Repository, index:Ggit.Index=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Diff or None
        new_tree_to_index(repository:Ggit.Repository, old_tree:Ggit.Tree=None, index:Ggit.Index=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Diff or None
        new_tree_to_tree(repository:Ggit.Repository, old_tree:Ggit.Tree=None, new_tree:Ggit.Tree=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Diff or None
        new_tree_to_workdir(repository:Ggit.Repository, old_tree:Ggit.Tree=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Diff or None

    Object GgitDiff

    Properties from GgitDiff:
      repository -> GgitRepository: Repository
        Repository

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        repository: Repository
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, repository: Repository = ..., native: None = ...) -> None: ...
    @staticmethod
    def blob_to_buffer(
        old_blob: Blob | None = None,
        old_as_path: str | None = None,
        buffer: Sequence[int] | None = None,
        buffer_as_path: str | None = None,
        diff_options: DiffOptions | None = None,
        file_cb: Callable[..., int] | None = None,
        binary_cb: Callable[..., int] | None = None,
        hunk_cb: Callable[..., int] | None = None,
        line_cb: Callable[..., int] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def blobs(
        old_blob: Blob | None = None,
        old_as_path: str | None = None,
        new_blob: Blob | None = None,
        new_as_path: str | None = None,
        diff_options: DiffOptions | None = None,
        file_cb: Callable[..., int] | None = None,
        binary_cb: Callable[..., int] | None = None,
        hunk_cb: Callable[..., int] | None = None,
        line_cb: Callable[..., int] | None = None,
        *user_data: Any,
    ) -> None: ...
    def find_similar(self, options: DiffFindOptions | None = None) -> bool: ...
    def foreach(
        self,
        file_cb: Callable[..., int] | None = None,
        binary_cb: Callable[..., int] | None = None,
        hunk_cb: Callable[..., int] | None = None,
        line_cb: Callable[..., int] | None = None,
        *user_data: Any,
    ) -> None: ...
    def format_email(self, options: DiffFormatEmailOptions) -> str | None: ...
    def get_delta(self, index: int) -> DiffDelta | None: ...
    def get_num_deltas(self) -> int: ...
    def merge(self, from_: Diff) -> None: ...
    @classmethod
    def new_buffers(
        cls,
        buffer1: Sequence[int] | None = None,
        buffer1_as_path: str | None = None,
        buffer2: Sequence[int] | None = None,
        buffer2_as_path: str | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Diff | None: ...
    @classmethod
    def new_index_to_workdir(
        cls,
        repository: Repository,
        index: Index | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Diff | None: ...
    @classmethod
    def new_tree_to_index(
        cls,
        repository: Repository,
        old_tree: Tree | None = None,
        index: Index | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Diff | None: ...
    @classmethod
    def new_tree_to_tree(
        cls,
        repository: Repository,
        old_tree: Tree | None = None,
        new_tree: Tree | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Diff | None: ...
    @classmethod
    def new_tree_to_workdir(
        cls,
        repository: Repository,
        old_tree: Tree | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Diff | None: ...
    def print_(
        self, type: DiffFormatType, print_cb: Callable[..., int], *user_data: Any
    ) -> None: ...

class DiffBinary(GObject.GBoxed):
    def get_new_file(self) -> DiffBinaryFile | None: ...
    def get_old_file(self) -> DiffBinaryFile | None: ...
    def ref(self) -> DiffBinary | None: ...
    def unref(self) -> None: ...

class DiffBinaryFile(GObject.GBoxed):
    def get_binary_type(self) -> DiffBinaryType: ...
    def get_data(self, size: int | None = None) -> int: ...
    def get_inflated_size(self) -> int: ...
    def ref(self) -> DiffBinaryFile: ...
    def unref(self) -> None: ...

class DiffClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DiffClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class DiffDelta(GObject.GBoxed):
    def get_flags(self) -> DiffFlag: ...
    def get_new_file(self) -> DiffFile | None: ...
    def get_old_file(self) -> DiffFile | None: ...
    def get_similarity(self) -> int: ...
    def get_status(self) -> DeltaType: ...
    def ref(self) -> DiffDelta | None: ...
    def unref(self) -> None: ...

class DiffFile(GObject.GBoxed):
    def get_flags(self) -> DiffFlag: ...
    def get_mode(self) -> int: ...
    def get_oid(self) -> OId | None: ...
    def get_path(self) -> str | None: ...
    def get_size(self) -> int: ...
    def ref(self) -> DiffFile | None: ...
    def unref(self) -> None: ...

class DiffFindOptions(GObject.Object):
    """
    :Constructors:

    ::

        DiffFindOptions(**properties)
        new() -> Ggit.DiffFindOptions or None

    Object GgitDiffFindOptions

    Properties from GgitDiffFindOptions:
      flags -> GgitDiffFindFlags: Flags
        Flags
      rename-threshold -> guint: Rename Threshold
        Rename threshold
      rename-from-rewrite-threshold -> guint: Rename From Rewrite Threshold
        Rename from rewrite threshold
      copy-threshold -> guint: Copy Threshold
        Copy threshold
      rename-limit -> guint: Rename Limit
        Rename limit
      metric -> GgitDiffSimilarityMetric: Metric
        Metric

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        copy_threshold: int
        flags: DiffFindFlags
        metric: DiffSimilarityMetric | None
        rename_from_rewrite_threshold: int
        rename_limit: int
        rename_threshold: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        copy_threshold: int = ...,
        flags: DiffFindFlags = ...,
        metric: DiffSimilarityMetric = ...,
        rename_from_rewrite_threshold: int = ...,
        rename_limit: int = ...,
        rename_threshold: int = ...,
    ) -> None: ...
    def get_copy_threshold(self) -> int: ...
    def get_flags(self) -> DiffFindFlags: ...
    def get_metric(self) -> DiffSimilarityMetric | None: ...
    def get_rename_from_rewrite_threshold(self) -> int: ...
    def get_rename_limit(self) -> int: ...
    def get_rename_threshold(self) -> int: ...
    @classmethod
    def new(cls) -> DiffFindOptions | None: ...
    def set_copy_threshold(self, threshold: int) -> None: ...
    def set_flags(self, flags: DiffFindFlags) -> None: ...
    def set_metric(self, metric: DiffSimilarityMetric) -> None: ...
    def set_rename_from_rewrite_threshold(self, threshold: int) -> None: ...
    def set_rename_limit(self, limit: int) -> None: ...
    def set_rename_threshold(self, threshold: int) -> None: ...

class DiffFindOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DiffFindOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class DiffFormatEmailOptions(GObject.Object):
    """
    :Constructors:

    ::

        DiffFormatEmailOptions(**properties)
        new() -> Ggit.DiffFormatEmailOptions or None

    Object GgitDiffFormatEmailOptions

    Properties from GgitDiffFormatEmailOptions:
      flags -> GgitDiffFormatEmailFlags: Flags
        Flags
      patch-number -> guint64: Patch Number
        Patch number
      total-patches -> guint64: Total Patches
        Total patches
      id -> GgitOId: Id
        Id
      summary -> gchararray: Summary
        Summary
      body -> gchararray: Body
        Body
      author -> GgitSignature: Author
        Author

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        author: Signature | None
        body: str | None
        flags: DiffFormatEmailFlags
        id: OId | None
        patch_number: int
        summary: str | None
        total_patches: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        author: Signature | None = ...,
        body: str | None = ...,
        flags: DiffFormatEmailFlags = ...,
        id: OId | None = ...,
        patch_number: int = ...,
        summary: str | None = ...,
        total_patches: int = ...,
    ) -> None: ...
    def get_author(self) -> Signature | None: ...
    def get_body(self) -> str | None: ...
    def get_flags(self) -> DiffFormatEmailFlags: ...
    def get_id(self) -> OId | None: ...
    def get_patch_number(self) -> int: ...
    def get_summary(self) -> str | None: ...
    def get_total_patches(self) -> int: ...
    @classmethod
    def new(cls) -> DiffFormatEmailOptions | None: ...
    def set_author(self, author: Signature | None = None) -> None: ...
    def set_body(self, body: str | None = None) -> None: ...
    def set_flags(self, flags: DiffFormatEmailFlags) -> None: ...
    def set_id(self, id: OId | None = None) -> None: ...
    def set_patch_number(self, number: int) -> None: ...
    def set_summary(self, summary: str | None = None) -> None: ...
    def set_total_patches(self, patches: int) -> None: ...

class DiffFormatEmailOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DiffFormatEmailOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class DiffHunk(GObject.GBoxed):
    def get_header(self) -> str: ...
    def get_new_lines(self) -> int: ...
    def get_new_start(self) -> int: ...
    def get_old_lines(self) -> int: ...
    def get_old_start(self) -> int: ...
    def ref(self) -> DiffHunk | None: ...
    def unref(self) -> None: ...

class DiffLine(GObject.GBoxed):
    def get_content(self) -> bytes: ...
    def get_content_offset(self) -> int: ...
    def get_new_lineno(self) -> int: ...
    def get_old_lineno(self) -> int: ...
    def get_origin(self) -> DiffLineType: ...
    def get_text(self) -> str | None: ...
    def ref(self) -> DiffLine | None: ...
    def unref(self) -> None: ...

class DiffOptions(GObject.Object):
    """
    :Constructors:

    ::

        DiffOptions(**properties)
        new() -> Ggit.DiffOptions or None

    Object GgitDiffOptions

    Properties from GgitDiffOptions:
      flags -> GgitDiffOption: Flags
        Flags
      n-context-lines -> gint: N Context Lines
        N context lines
      n-interhunk-lines -> gint: N Interhunk Lines
        N interhunk lines
      old-prefix -> gchararray: Old Prefix
        Old prefix
      new-prefix -> gchararray: New Prefix
        New prefix
      pathspec -> GStrv: Pathspec
        Pathspec

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        flags: DiffOption
        n_context_lines: int
        n_interhunk_lines: int
        new_prefix: str | None
        old_prefix: str | None
        pathspec: list[str] | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        flags: DiffOption = ...,
        n_context_lines: int = ...,
        n_interhunk_lines: int = ...,
        new_prefix: str = ...,
        old_prefix: str = ...,
        pathspec: Sequence[str] | None = ...,
    ) -> None: ...
    def get_flags(self) -> DiffOption: ...
    def get_n_context_lines(self) -> int: ...
    def get_n_interhunk_lines(self) -> int: ...
    def get_new_prefix(self) -> str | None: ...
    def get_old_prefix(self) -> str | None: ...
    def get_pathspec(self) -> list[str] | None: ...
    @classmethod
    def new(cls) -> DiffOptions | None: ...
    def set_flags(self, flags: DiffOption) -> None: ...
    def set_n_context_lines(self, n: int) -> None: ...
    def set_n_interhunk_lines(self, n: int) -> None: ...
    def set_new_prefix(self, prefix: str) -> None: ...
    def set_old_prefix(self, prefix: str) -> None: ...
    def set_pathspec(self, pathspec: Sequence[str] | None = None) -> None: ...

class DiffOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DiffOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class DiffSimilarityMetric(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(file_signature:Ggit.DiffSimilarityMetricFileSignatureCallback, buffer_signature:Ggit.DiffSimilarityMetricBufferSignatureCallback, free_signature:Ggit.DiffSimilarityMetricFreeSignatureCallback, similarity:Ggit.DiffSimilarityMetricSimilarityCallback, user_data=None) -> Ggit.DiffSimilarityMetric
    """
    @staticmethod
    def __new__(
        cls: type[Self],
        file_signature: Callable[..., int],
        buffer_signature: Callable[..., int],
        free_signature: Callable[..., None],
        similarity: Callable[..., int],
        *user_data: Any,
    ) -> Self: ...
    def copy(self) -> DiffSimilarityMetric | None: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls,
        file_signature: Callable[..., int],
        buffer_signature: Callable[..., int],
        free_signature: Callable[..., None],
        similarity: Callable[..., int],
        *user_data: Any,
    ) -> DiffSimilarityMetric: ...

class FetchOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Ggit.FetchOptions
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> FetchOptions | None: ...
    def free(self) -> None: ...
    def get_download_tags(self) -> RemoteDownloadTagsType: ...
    def get_remote_callbacks(self) -> RemoteCallbacks | None: ...
    @classmethod
    def new(cls) -> FetchOptions: ...
    def set_download_tags(self, download_tags: RemoteDownloadTagsType) -> None: ...
    def set_remote_callbacks(
        self, callbacks: RemoteCallbacks | None = None
    ) -> None: ...

class Index(Native, Gio.Initable):
    """
    :Constructors:

    ::

        Index(**properties)

    Object GgitIndex

    Properties from GgitIndex:
      file -> GFile: File
        File

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        file: Gio.File
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, file: Gio.File = ..., native: None = ...) -> None: ...
    def add(self, entry: IndexEntry) -> bool: ...
    def add_file(self, file: Gio.File) -> bool: ...
    def add_path(self, path: str) -> bool: ...
    def get_entries(self) -> IndexEntries | None: ...
    def get_entries_resolve_undo(self) -> IndexEntriesResolveUndo | None: ...
    def get_owner(self) -> Repository | None: ...
    def has_conflicts(self) -> bool: ...
    @staticmethod
    def open(file: Gio.File) -> Index | None: ...
    def read(self, force: bool) -> bool: ...
    def remove(self, file: Gio.File, stage: int) -> bool: ...
    def write(self) -> bool: ...
    def write_tree(self) -> OId | None: ...
    def write_tree_to(self, repository: Repository) -> OId | None: ...

class IndexClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IndexClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class IndexEntries(GObject.GBoxed):
    def get_by_index(self, idx: int) -> IndexEntry | None: ...
    def get_by_path(self, file: Gio.File, stage: int) -> IndexEntry | None: ...
    def ref(self) -> IndexEntries | None: ...
    def size(self) -> int: ...
    def unref(self) -> None: ...

class IndexEntriesResolveUndo(GObject.GBoxed):
    def get(self, idx: int) -> IndexEntryResolveUndo | None: ...
    def get_by_file(self, file: Gio.File) -> IndexEntryResolveUndo | None: ...
    def ref(self) -> IndexEntriesResolveUndo | None: ...
    def size(self) -> int: ...
    def unref(self) -> None: ...

class IndexEntry(GObject.GBoxed):
    def get_dev(self) -> int: ...
    def get_file_size(self) -> int: ...
    def get_flags(self) -> int: ...
    def get_flags_extended(self) -> int: ...
    def get_gid(self) -> int: ...
    def get_id(self) -> OId | None: ...
    def get_ino(self) -> int: ...
    def get_mode(self) -> int: ...
    def get_path(self) -> str: ...
    def get_uid(self) -> int: ...
    def is_conflict(self) -> bool: ...
    def ref(self) -> IndexEntry | None: ...
    def set_commit(self, commit: Commit) -> None: ...
    def set_dev(self, dev: int) -> None: ...
    def set_file_size(self, file_size: int) -> None: ...
    def set_flags(self, flags: int) -> None: ...
    def set_flags_extended(self, flags_extended: int) -> None: ...
    def set_gid(self, gid: int) -> None: ...
    def set_id(self, id: OId | None = None) -> None: ...
    def set_ino(self, ino: int) -> None: ...
    def set_mode(self, mode: int) -> None: ...
    def set_path(self, path: str | None = None) -> None: ...
    def set_uid(self, uid: int) -> None: ...
    def stat(self, file: Gio.File) -> bool: ...
    def unref(self) -> None: ...

class IndexEntryResolveUndo(GObject.GBoxed):
    def get_file(self) -> Gio.File | None: ...
    def get_id(self, stage: int) -> OId | None: ...
    def get_mode(self, stage: int) -> int: ...
    def ref(self) -> IndexEntryResolveUndo | None: ...
    def unref(self) -> None: ...

class Mailmap(Native):
    """
    :Constructors:

    ::

        Mailmap(**properties)
        new() -> Ggit.Mailmap or None
        new_from_repository(repository:Ggit.Repository) -> Ggit.Mailmap or None

    Object GgitMailmap

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def add_entry(
        self,
        real_name: str | None,
        real_email: str | None,
        replace_name: str | None,
        replace_email: str,
    ) -> None: ...
    @classmethod
    def new(cls) -> Mailmap | None: ...
    @classmethod
    def new_from_repository(cls, repository: Repository) -> Mailmap | None: ...
    def resolve(self, replace_name: str, replace_email: str) -> tuple[str, str]: ...
    def resolve_signature(self, signature: Signature) -> Signature | None: ...

class MailmapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MailmapClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class MergeOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Ggit.MergeOptions
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> MergeOptions | None: ...
    def free(self) -> None: ...
    def get_file_favor(self) -> MergeFileFavor: ...
    def get_file_flags(self) -> MergeFileFlags: ...
    def get_flags(self) -> MergeFlags: ...
    def get_rename_threshold(self) -> int: ...
    def get_similarity_metric(self) -> DiffSimilarityMetric | None: ...
    def get_target_limit(self) -> int: ...
    @classmethod
    def new(cls) -> MergeOptions: ...
    def set_file_favor(self, file_favor: MergeFileFavor) -> None: ...
    def set_file_flags(self, file_flags: MergeFileFlags) -> None: ...
    def set_flags(self, flags: MergeFlags) -> None: ...
    def set_rename_threshold(self, rename_threshold: int) -> None: ...
    def set_similarity_metric(self, metric: DiffSimilarityMetric) -> None: ...
    def set_target_limit(self, target_limit: int) -> None: ...

class Native(ObjectFactoryBase):
    """
    :Constructors:

    ::

        Native(**properties)

    Object GgitNative

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(ObjectFactoryBase.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> ObjectFactoryBase: ...
    def __init__(self, *, native: None = ...) -> None: ...

class NativeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NativeClass()
    """
    @property
    def parent_class(self) -> ObjectFactoryBaseClass: ...

class Note(GObject.GBoxed):
    def get_id(self) -> OId | None: ...
    def get_message(self) -> str | None: ...
    def ref(self) -> Note | None: ...
    def unref(self) -> None: ...

class OId(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_raw(raw:list) -> Ggit.OId or None
        new_from_string(str:str) -> Ggit.OId or None
    """
    def compare(self, b: OId) -> int: ...
    def copy(self) -> OId | None: ...
    def equal(self, b: OId) -> bool: ...
    def free(self) -> None: ...
    def has_prefix(self, prefix: str) -> bool: ...
    def hash(self) -> int: ...
    def is_zero(self) -> bool: ...
    @classmethod
    def new_from_raw(cls, raw: Sequence[int]) -> OId | None: ...
    @classmethod
    def new_from_string(cls, str: str) -> OId | None: ...
    def to_string(self) -> str | None: ...

class Object(Native):
    """
    :Constructors:

    ::

        Object(**properties)

    Object GgitObject

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def get_id(self) -> OId | None: ...
    def get_owner(self) -> Repository | None: ...

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class ObjectFactory(GObject.Object):
    """
    :Constructors:

    ::

        ObjectFactory(**properties)

    Object GgitObjectFactory

    Signals from GObject:
      notify (GParam)
    """
    def construct(
        self,
        parent_class: GObject.ObjectClass,
        basetype: type[Any],
        construct_properties: Sequence[GObject.ObjectConstructParam],
    ) -> GObject.Object | None: ...
    @staticmethod
    def get_default() -> ObjectFactory: ...
    def register(self, basetype: type[Any], subtype: type[Any]) -> None: ...
    def unregister(self, basetype: type[Any], subtype: type[Any]) -> None: ...

class ObjectFactoryBase(GObject.Object):
    """
    :Constructors:

    ::

        ObjectFactoryBase(**properties)

    Object GgitObjectFactoryBase

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...

class ObjectFactoryBaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectFactoryBaseClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class ObjectFactoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectFactoryClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Patch(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_blobs(old_blob:Ggit.Blob=None, old_as_path:str=None, new_blob:Ggit.Blob=None, new_as_path:str=None, diff_options:Ggit.DiffOptions=None) -> Ggit.Patch or None
        new_from_diff(diff:Ggit.Diff, idx:int) -> Ggit.Patch or None
    """
    def get_delta(self) -> DiffDelta | None: ...
    def get_hunk(self, idx: int) -> DiffHunk | None: ...
    def get_line_stats(self) -> tuple[bool, int, int, int]: ...
    def get_num_hunks(self) -> int: ...
    def get_num_lines_in_hunk(self, hunk: int) -> int: ...
    @classmethod
    def new_from_blobs(
        cls,
        old_blob: Blob | None = None,
        old_as_path: str | None = None,
        new_blob: Blob | None = None,
        new_as_path: str | None = None,
        diff_options: DiffOptions | None = None,
    ) -> Patch | None: ...
    @classmethod
    def new_from_diff(cls, diff: Diff, idx: int) -> Patch | None: ...
    def ref(self) -> Patch | None: ...
    def to_stream(self, stream: Gio.OutputStream) -> bool: ...
    def to_string(self) -> str | None: ...
    def unref(self) -> None: ...

class ProxyOptions(GObject.Object):
    """
    :Constructors:

    ::

        ProxyOptions(**properties)
        new() -> Ggit.ProxyOptions or None

    Object GgitProxyOptions

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @classmethod
    def new(cls) -> ProxyOptions | None: ...

class ProxyOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class PushOptions(GObject.Object):
    """
    :Constructors:

    ::

        PushOptions(**properties)
        new() -> Ggit.PushOptions or None

    Object GgitPushOptions

    Properties from GgitPushOptions:
      parallelism -> gint: Parallelism
        Parallelism
      callbacks -> GgitRemoteCallbacks: Callbacks
        Callbacks

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        callbacks: RemoteCallbacks
        parallelism: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self, *, callbacks: RemoteCallbacks = ..., parallelism: int = ...
    ) -> None: ...
    def get_parallelism(self) -> int: ...
    def get_remote_callbacks(self) -> RemoteCallbacks | None: ...
    @classmethod
    def new(cls) -> PushOptions | None: ...
    def set_parallelism(self, parallelism: int) -> None: ...
    def set_remote_callbacks(self, callbacks: RemoteCallbacks) -> None: ...

class PushOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PushOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Rebase(Native):
    """
    :Constructors:

    ::

        Rebase(**properties)

    Object GgitRebase

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def abort(self) -> None: ...
    def commit(
        self, author: Signature | None, committer: Signature, message: str | None = None
    ) -> OId | None: ...
    def finish(self, signature: Signature | None = None) -> None: ...
    def get_operation_by_index(self, idx: int) -> RebaseOperation | None: ...
    def get_operation_entry_count(self) -> int: ...
    def get_operation_index(self) -> int: ...
    def next(self) -> RebaseOperation | None: ...

class RebaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RebaseClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class RebaseOperation(GObject.GBoxed):
    def get_exec(self) -> str | None: ...
    def get_id(self) -> OId | None: ...
    def get_operation_type(self) -> RebaseOperationType: ...
    def ref(self) -> RebaseOperation | None: ...
    def unref(self) -> None: ...

class RebaseOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Ggit.RebaseOptions
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> RebaseOptions | None: ...
    def free(self) -> None: ...
    def get_checkout_options(self) -> CheckoutOptions | None: ...
    def get_quiet(self) -> bool: ...
    def get_rewrite_notes_ref(self) -> str | None: ...
    @classmethod
    def new(cls) -> RebaseOptions: ...
    def set_checkout_options(self, checkout_options: CheckoutOptions) -> None: ...
    def set_quiet(self, quiet: bool) -> None: ...
    def set_rewrite_notes_ref(self, rewrite_notes_ref: str) -> None: ...

class Ref(Native):
    """
    :Constructors:

    ::

        Ref(**properties)

    Object GgitRef

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def delete(self) -> None: ...
    def delete_log(self) -> None: ...
    def get_log(self) -> Reflog | None: ...
    def get_name(self) -> str | None: ...
    def get_owner(self) -> Repository | None: ...
    def get_reference_type(self) -> RefType: ...
    def get_shorthand(self) -> str | None: ...
    def get_symbolic_target(self) -> str | None: ...
    def get_target(self) -> OId | None: ...
    def has_log(self) -> bool: ...
    def is_branch(self) -> bool: ...
    def is_note(self) -> bool: ...
    def is_remote(self) -> bool: ...
    def is_tag(self) -> bool: ...
    @staticmethod
    def is_valid_name(name: str) -> bool: ...
    def lookup(self) -> Object | None: ...
    def rename(self, new_name: str, force: bool, log_message: str) -> Ref | None: ...
    def resolve(self) -> Ref | None: ...
    def set_symbolic_target(
        self, target: str, log_message: str | None = None
    ) -> Ref | None: ...
    def set_target(self, oid: OId, log_message: str | None = None) -> Ref | None: ...
    def to_string(self) -> str | None: ...

class RefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RefClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class RefSpec(GObject.GBoxed):
    def get_destination(self) -> str | None: ...
    def get_source(self) -> str | None: ...
    def is_forced(self) -> bool: ...
    def ref(self) -> RefSpec | None: ...
    def unref(self) -> None: ...

class Reflog(GObject.GBoxed):
    def append(self, oid: OId, committer: Signature, message: str) -> bool: ...
    def get_entry_count(self) -> int: ...
    def get_entry_from_index(self, idx: int) -> ReflogEntry | None: ...
    def ref(self) -> Reflog | None: ...
    def rename(self, new_name: str) -> bool: ...
    def unref(self) -> None: ...
    def write(self) -> bool: ...

class ReflogEntry(GObject.GBoxed):
    def get_committer(self) -> Signature | None: ...
    def get_message(self) -> str | None: ...
    def get_new_id(self) -> OId | None: ...
    def get_old_id(self) -> OId | None: ...
    def ref(self) -> ReflogEntry | None: ...
    def unref(self) -> None: ...

class Remote(Native):
    """
    :Constructors:

    ::

        Remote(**properties)
        new(repository:Ggit.Repository, name:str, url:str) -> Ggit.Remote or None
        new_anonymous(repository:Ggit.Repository, url:str) -> Ggit.Remote or None

    Object GgitRemote

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def connect(
        self,
        direction: Direction,
        callbacks: RemoteCallbacks,
        proxy_options: ProxyOptions | None = None,
        custom_headers: str | None = None,
    ) -> None: ...
    def disconnect(self) -> None: ...
    def download(
        self, specs: Sequence[str] | None, fetch_options: FetchOptions
    ) -> bool: ...
    def get_connected(self) -> bool: ...
    def get_fetch_specs(self) -> list[str] | None: ...
    def get_name(self) -> str | None: ...
    def get_owner(self) -> Repository | None: ...
    def get_push_specs(self) -> list[str] | None: ...
    def get_url(self) -> str | None: ...
    def list(self) -> list[RemoteHead] | None: ...
    @classmethod
    def new(cls, repository: Repository, name: str, url: str) -> Remote | None: ...
    @classmethod
    def new_anonymous(cls, repository: Repository, url: str) -> Remote | None: ...
    def prune(self, callbacks: RemoteCallbacks) -> None: ...
    def push(self, specs: Sequence[str] | None, push_options: PushOptions) -> bool: ...
    def update_tips(
        self,
        callbacks: RemoteCallbacks,
        update_fetch_head: bool,
        tags_type: RemoteDownloadTagsType,
        message: str | None = None,
    ) -> bool: ...
    def upload(
        self, specs: Sequence[str] | None, push_options: PushOptions
    ) -> bool: ...

class RemoteCallbacks(GObject.Object):
    """
    :Constructors:

    ::

        RemoteCallbacks(**properties)

    Object GgitRemoteCallbacks

    Signals from GgitRemoteCallbacks:
      update-tips (gchararray, GgitOId, GgitOId)
      progress (gchararray)
      transfer-progress (GgitTransferProgress)
      completion (GgitRemoteCompletionType)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_completion(self, type: RemoteCompletionType) -> None: ...
    def do_credentials(
        self, url: str, username_from_url: str | None, allowed_types: Credtype
    ) -> Cred | None: ...
    def do_progress(self, message: str) -> None: ...
    def do_transfer_progress(self, stats: TransferProgress) -> None: ...
    def do_update_tips(self, refname: str, a: OId, b: OId) -> None: ...

class RemoteCallbacksClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RemoteCallbacksClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def progress(self) -> Callable[[RemoteCallbacks, str], None]: ...
    @property
    def transfer_progress(
        self,
    ) -> Callable[[RemoteCallbacks, TransferProgress], None]: ...
    @property
    def update_tips(self) -> Callable[[RemoteCallbacks, str, OId, OId], None]: ...
    @property
    def completion(self) -> Callable[[RemoteCallbacks, RemoteCompletionType], None]: ...
    @property
    def credentials(
        self,
    ) -> Callable[[RemoteCallbacks, str, str | None, Credtype], Cred | None]: ...

class RemoteClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RemoteClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class RemoteHead(GObject.GBoxed):
    def get_local_oid(self) -> OId | None: ...
    def get_name(self) -> str | None: ...
    def get_oid(self) -> OId | None: ...
    def is_local(self) -> bool: ...
    def ref(self) -> RemoteHead: ...
    def unref(self) -> None: ...

class Repository(Native, Gio.Initable):
    """
    :Constructors:

    ::

        Repository(**properties)

    Object GgitRepository

    Properties from GgitRepository:
      url -> gchararray: URL for cloning a repository
        The URL for cloning a repository
      location -> GFile: Location of repository
        The location of the repository
      is-bare -> gboolean: Is bare
        Is a bare repository
      init -> gboolean: Init
        Whether to initialize a repository
      workdir -> GFile: Path to repository working directory
        The path to the repository working directory
      head -> GgitRef: Head
        Head
      clone-options -> GgitCloneOptions: Clone options
        Clone options

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        clone_options: CloneOptions
        head: Ref | None
        init: bool
        is_bare: bool
        location: Gio.File | None
        url: str
        workdir: Gio.File | None
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> Native: ...
    def __init__(
        self,
        *,
        clone_options: CloneOptions = ...,
        init: bool = ...,
        is_bare: bool = ...,
        location: Gio.File = ...,
        url: str = ...,
        workdir: Gio.File = ...,
        native: None = ...,
    ) -> None: ...
    def add_remote_fetch(self, remote: Remote, refspec: str) -> None: ...
    def add_remote_push(self, remote: Remote, refspec: str) -> None: ...
    def blame_file(
        self, file: Gio.File, blame_options: BlameOptions | None = None
    ) -> Blame | None: ...
    def checkout_head(self, options: CheckoutOptions | None = None) -> bool: ...
    def checkout_index(
        self, index: Index | None = None, options: CheckoutOptions | None = None
    ) -> bool: ...
    def checkout_tree(
        self, tree: Object | None = None, options: CheckoutOptions | None = None
    ) -> bool: ...
    def cherry_pick(self, commit: Commit, options: CherryPickOptions) -> bool: ...
    def cherry_pick_commit(
        self,
        commit: Commit,
        our_commit: Commit,
        mainline: int,
        merge_options: MergeOptions | None = None,
    ) -> Index | None: ...
    @staticmethod
    def clone(
        url: str, location: Gio.File, options: CloneOptions | None = None
    ) -> Repository | None: ...
    def create_blob(self) -> BlobOutputStream | None: ...
    def create_blob_from_buffer(self, buffer: Sequence[int]) -> OId | None: ...
    def create_blob_from_file(self, file: Gio.File) -> OId: ...
    def create_blob_from_path(self, path: str) -> OId | None: ...
    def create_branch(
        self, branch_name: str, target: Object, flags: CreateFlags
    ) -> Branch | None: ...
    def create_commit(
        self,
        update_ref: str | None,
        author: Signature,
        committer: Signature,
        message_encoding: str | None,
        message: str,
        tree: Tree,
        parents: Sequence[Commit],
    ) -> OId | None: ...
    def create_commit_buffer(
        self,
        author: Signature,
        committer: Signature,
        message_encoding: str | None,
        message: str,
        tree: Tree,
        parents: Sequence[Commit],
    ) -> str | None: ...
    def create_commit_from_ids(
        self,
        update_ref: str | None,
        author: Signature,
        committer: Signature,
        message_encoding: str | None,
        message: str,
        tree: OId,
        parents: Sequence[OId],
    ) -> OId | None: ...
    def create_commit_with_signature(
        self,
        commit_content: str,
        signature: str | None = None,
        signature_field: str | None = None,
    ) -> OId | None: ...
    def create_index_entry_for_file(
        self, file: Gio.File | None = None, id: OId | None = None
    ) -> IndexEntry | None: ...
    def create_index_entry_for_path(
        self, path: str | None = None, id: OId | None = None
    ) -> IndexEntry | None: ...
    def create_note(
        self,
        notes_ref: str | None,
        author: Signature,
        committer: Signature,
        id: OId,
        note: str,
        force: bool,
    ) -> OId | None: ...
    def create_reference(self, name: str, oid: OId, log_message: str) -> Ref | None: ...
    def create_remote(self, name: str, url: str) -> Remote | None: ...
    def create_symbolic_reference(
        self, name: str, target: str, log_message: str
    ) -> Ref | None: ...
    def create_tag(
        self,
        tag_name: str,
        target: Object,
        tagger: Signature,
        message: str,
        flags: CreateFlags,
    ) -> OId | None: ...
    def create_tag_annotation(
        self, tag_name: str, target: Object, signature: Signature, message: str
    ) -> OId | None: ...
    def create_tag_from_buffer(self, tag: str, flags: CreateFlags) -> OId | None: ...
    def create_tag_lightweight(
        self, tag_name: str, target: Object, flags: CreateFlags
    ) -> OId | None: ...
    def create_tree_builder(self) -> TreeBuilder | None: ...
    def create_tree_builder_from_tree(self, tree: Tree) -> TreeBuilder | None: ...
    def delete_tag(self, name: str) -> bool: ...
    @staticmethod
    def discover(location: Gio.File) -> Gio.File | None: ...
    @staticmethod
    def discover_full(
        location: Gio.File, across_fs: bool, ceiling_dirs: Sequence[str] | None = None
    ) -> Gio.File | None: ...
    def drop_stash(self, index: int) -> None: ...
    def enumerate_branches(self, list_type: BranchType) -> BranchEnumerator | None: ...
    def file_status(self, location: Gio.File) -> StatusFlags: ...
    def file_status_foreach(
        self,
        options: StatusOptions | None,
        callback: Callable[..., int],
        *user_data: Any,
    ) -> bool: ...
    def get_ahead_behind(self, local: OId, upstream: OId) -> tuple[int, int]: ...
    def get_attribute(
        self, path: str, name: str, flags: AttributeCheckFlags
    ) -> str | None: ...
    def get_config(self) -> Config | None: ...
    def get_default_notes_ref(self) -> str | None: ...
    def get_descendant_of(self, commit: OId, ancestor: OId) -> bool: ...
    def get_head(self) -> Ref | None: ...
    def get_index(self) -> Index | None: ...
    def get_location(self) -> Gio.File | None: ...
    def get_submodule_status(
        self, name: str, ignore: SubmoduleIgnore
    ) -> SubmoduleStatus: ...
    def get_workdir(self) -> Gio.File | None: ...
    @staticmethod
    def init_repository(location: Gio.File, is_bare: bool) -> Repository | None: ...
    def is_bare(self) -> bool: ...
    def is_empty(self) -> bool: ...
    def is_head_detached(self) -> bool: ...
    def is_head_unborn(self) -> bool: ...
    def list_remotes(self) -> list[str] | None: ...
    def list_tags(self) -> list[str] | None: ...
    def list_tags_match(self, pattern: str | None = None) -> list[str] | None: ...
    # override
    def lookup(self, oid: OId, gtype: type[_O]) -> _O | None: ...
    def lookup_blob(self, oid: OId) -> Blob | None: ...
    def lookup_branch(
        self, branch_name: str, branch_type: BranchType
    ) -> Branch | None: ...
    def lookup_commit(self, oid: OId) -> Commit | None: ...
    def lookup_reference(self, name: str) -> Ref | None: ...
    def lookup_reference_dwim(self, short_name: str) -> Ref | None: ...
    def lookup_remote(self, name: str) -> Remote | None: ...
    def lookup_submodule(self, name: str) -> Submodule | None: ...
    def lookup_tag(self, oid: OId) -> Tag | None: ...
    def lookup_tree(self, oid: OId) -> Tree | None: ...
    def merge(
        self,
        their_heads: Sequence[AnnotatedCommit],
        merge_opts: MergeOptions,
        checkout_opts: CheckoutOptions,
    ) -> None: ...
    def merge_base(self, oid_one: OId, oid_two: OId) -> OId | None: ...
    def merge_commits(
        self, our_commit: Commit, their_commit: Commit, merge_options: MergeOptions
    ) -> Index | None: ...
    def merge_trees(
        self,
        ancestor_tree: Tree,
        our_tree: Tree,
        their_tree: Tree,
        merge_options: MergeOptions,
    ) -> Index | None: ...
    def note_foreach(
        self, notes_ref: str | None, callback: Callable[..., int], *user_data: Any
    ) -> bool: ...
    @staticmethod
    def open(location: Gio.File) -> Repository | None: ...
    def path_is_ignored(self, path: str) -> bool: ...
    def read_note(self, notes_ref: str | None, id: OId) -> Note | None: ...
    def rebase_init(
        self,
        branch: AnnotatedCommit | None,
        upstream: AnnotatedCommit | None,
        onto: AnnotatedCommit | None,
        options: RebaseOptions,
    ) -> Rebase | None: ...
    def rebase_open(self, options: RebaseOptions) -> Rebase | None: ...
    def references_foreach(
        self, callback: Callable[..., int], *user_data: Any
    ) -> bool: ...
    def references_foreach_name(
        self, callback: Callable[..., int], *user_data: Any
    ) -> bool: ...
    def remove_note(
        self, notes_ref: str | None, author: Signature, committer: Signature, id: OId
    ) -> bool: ...
    def remove_remote(self, name: str) -> bool: ...
    def rename_remote(self, name: str, new_name: str) -> list[str] | None: ...
    def reset(
        self, target: Object, reset_type: ResetType, checkout_options: CheckoutOptions
    ) -> None: ...
    def reset_default(
        self, target: Object | None, pathspecs: Sequence[str]
    ) -> None: ...
    def revert(self, commit: Commit, options: RevertOptions) -> bool: ...
    def revparse(self, spec: str) -> Object | None: ...
    def save_stash(
        self, stasher: Signature, message: str, flags: StashFlags
    ) -> OId | None: ...
    def set_head(self, ref_name: str) -> bool: ...
    def set_head_detached(self, oid: OId) -> bool: ...
    def set_remote_url(self, remote: str, url: str) -> bool: ...
    def set_submodule_fetch_recurse(
        self, name: str, fetch_recurse_submodules: SubmoduleRecurse
    ) -> None: ...
    def set_submodule_ignore(self, name: str, ignore: SubmoduleIgnore) -> None: ...
    def set_submodule_update(self, name: str, update: SubmoduleUpdate) -> None: ...
    def set_submodule_url(self, name: str, url: str) -> None: ...
    def set_workdir(self, workdir: Gio.File, update_gitlink: bool) -> None: ...
    def stash_foreach(self, callback: Callable[..., int], *user_data: Any) -> bool: ...
    def submodule_foreach(
        self, callback: Callable[..., int], *user_data: Any
    ) -> bool: ...
    def tag_foreach(self, callback: Callable[..., int], *user_data: Any) -> bool: ...

class RepositoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepositoryClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class RevertOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(mainline:int, merge_options:Ggit.MergeOptions=None, checkout_options:Ggit.CheckoutOptions=None) -> Ggit.RevertOptions or None
    """
    @staticmethod
    def __new__(
        cls: type[Self],
        mainline: int,
        merge_options: MergeOptions | None = None,
        checkout_options: CheckoutOptions | None = None,
    ) -> Self: ...
    def copy(self) -> RevertOptions | None: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls,
        mainline: int,
        merge_options: MergeOptions | None = None,
        checkout_options: CheckoutOptions | None = None,
    ) -> RevertOptions | None: ...

class RevisionWalker(Native, Gio.Initable):
    """
    :Constructors:

    ::

        RevisionWalker(**properties)
        new(repository:Ggit.Repository) -> Ggit.RevisionWalker or None

    Object GgitRevisionWalker

    Properties from GgitRevisionWalker:
      repository -> GgitRepository: Repository
        The repository where to make the walking

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        repository: Repository | None
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, repository: Repository = ..., native: None = ...) -> None: ...
    def get_repository(self) -> Repository | None: ...
    def hide(self, oid: OId) -> None: ...
    def hide_glob(self, item: str) -> None: ...
    def hide_head(self) -> None: ...
    def hide_ref(self, item: str) -> None: ...
    @classmethod
    def new(cls, repository: Repository) -> RevisionWalker | None: ...
    def next(self) -> OId | None: ...
    def push(self, oid: OId) -> None: ...
    def push_glob(self, item: str) -> None: ...
    def push_head(self) -> None: ...
    def push_range(self, range: str) -> None: ...
    def push_ref(self, item: str) -> None: ...
    def reset(self) -> None: ...
    def set_sort_mode(self, sort_mode: SortMode) -> None: ...

class RevisionWalkerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RevisionWalkerClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class Signature(Native):
    """
    :Constructors:

    ::

        Signature(**properties)
        new(name:str, email:str, signature_time:GLib.DateTime) -> Ggit.Signature or None
        new_now(name:str, email:str) -> Ggit.Signature or None

    Object GgitSignature

    Properties from GgitSignature:
      encoding -> gchararray: Encoding
        Encoding

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        encoding: str
        native: None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, encoding: str = ..., native: None = ...) -> None: ...
    def copy(self) -> Signature | None: ...
    def get_email(self) -> str | None: ...
    def get_name(self) -> str | None: ...
    def get_time(self) -> GLib.DateTime | None: ...
    def get_time_zone(self) -> GLib.TimeZone | None: ...
    @classmethod
    def new(
        cls, name: str, email: str, signature_time: GLib.DateTime
    ) -> Signature | None: ...
    @classmethod
    def new_now(cls, name: str, email: str) -> Signature | None: ...

class SignatureClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SignatureClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class StatusOptions(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(options:Ggit.StatusOption, show:Ggit.StatusShow, pathspec:list=None) -> Ggit.StatusOptions
    """
    @staticmethod
    def __new__(
        cls: type[Self],
        options: StatusOption,
        show: StatusShow,
        pathspec: Sequence[str] | None = None,
    ) -> Self: ...
    def copy(self) -> StatusOptions | None: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls,
        options: StatusOption,
        show: StatusShow,
        pathspec: Sequence[str] | None = None,
    ) -> StatusOptions: ...

class Submodule(GObject.GBoxed):
    def get_fetch_recurse(self) -> bool: ...
    def get_head_id(self) -> OId: ...
    def get_ignore(self) -> SubmoduleIgnore: ...
    def get_index_id(self) -> OId | None: ...
    def get_name(self) -> str | None: ...
    def get_owner(self) -> Repository | None: ...
    def get_path(self) -> str | None: ...
    def get_update(self) -> SubmoduleUpdate: ...
    def get_url(self) -> str | None: ...
    def get_workdir_id(self) -> OId | None: ...
    def init(self, overwrite: bool) -> None: ...
    def open(self) -> Repository | None: ...
    def ref(self) -> Submodule | None: ...
    def reload(self, force: bool) -> None: ...
    def sync(self) -> None: ...
    def unref(self) -> None: ...
    def update(self, init: bool, options: SubmoduleUpdateOptions) -> None: ...

class SubmoduleUpdateOptions(GObject.Object):
    """
    :Constructors:

    ::

        SubmoduleUpdateOptions(**properties)
        new() -> Ggit.SubmoduleUpdateOptions or None

    Object GgitSubmoduleUpdateOptions

    Properties from GgitSubmoduleUpdateOptions:
      checkout-options -> GgitCheckoutOptions: Checkout Options
        Checkout options
      fetch-options -> GgitFetchOptions: Fetch options
        Fetch options

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        checkout_options: CheckoutOptions | None
        fetch_options: FetchOptions

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        checkout_options: CheckoutOptions | None = ...,
        fetch_options: FetchOptions | None = ...,
    ) -> None: ...
    def get_checkout_options(self) -> CheckoutOptions | None: ...
    def get_fetch_options(self) -> FetchOptions: ...
    @classmethod
    def new(cls) -> SubmoduleUpdateOptions | None: ...
    def set_checkout_options(
        self, checkout_options: CheckoutOptions | None = None
    ) -> None: ...
    def set_fetch_options(self, fetch_options: FetchOptions | None = None) -> None: ...

class SubmoduleUpdateOptionsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SubmoduleUpdateOptionsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Tag(Object):
    """
    :Constructors:

    ::

        Tag(**properties)

    Object GgitTag

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Object: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def get_message(self) -> str | None: ...
    def get_name(self) -> str | None: ...
    def get_tagger(self) -> Signature | None: ...
    def get_target(self) -> Object | None: ...
    def get_target_id(self) -> OId | None: ...
    def get_target_type(self) -> type[Any]: ...
    def peel(self) -> Object | None: ...

class TagClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TagClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class TransferProgress(GObject.GBoxed):
    def copy(self) -> TransferProgress | None: ...
    def free(self) -> None: ...
    def get_indexed_objects(self) -> int: ...
    def get_received_bytes(self) -> int: ...
    def get_received_objects(self) -> int: ...
    def get_total_objects(self) -> int: ...

class Tree(Object):
    """
    :Constructors:

    ::

        Tree(**properties)

    Object GgitTree

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Object: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def get(self, i: int) -> TreeEntry | None: ...
    def get_by_name(self, name: str) -> TreeEntry | None: ...
    def get_by_path(self, path: str) -> TreeEntry | None: ...
    def get_id(self) -> OId | None: ...
    def size(self) -> int: ...
    def walk(
        self, mode: TreeWalkMode, callback: Callable[..., int], *user_data: Any
    ) -> None: ...

class TreeBuilder(Native):
    """
    :Constructors:

    ::

        TreeBuilder(**properties)

    Object GgitTreeBuilder

    Properties from GgitNative:
      native -> gpointer: Native
        Native

    Signals from GObject:
      notify (GParam)
    """
    class Props(Native.Props):
        native: None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Native: ...
    def __init__(self, *, native: None = ...) -> None: ...
    def clear(self) -> None: ...
    def get_entry(self, path: str) -> TreeEntry | None: ...
    def insert(
        self, filename: str, oid: OId, file_mode: FileMode
    ) -> TreeEntry | None: ...
    def remove(self, path: str) -> None: ...
    def write(self) -> OId | None: ...

class TreeBuilderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TreeBuilderClass()
    """
    @property
    def parent_class(self) -> NativeClass: ...

class TreeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TreeClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class TreeEntry(GObject.GBoxed):
    def get_file_mode(self) -> FileMode: ...
    def get_id(self) -> OId | None: ...
    def get_name(self) -> str | None: ...
    def get_object_type(self) -> type[Any]: ...
    def ref(self) -> TreeEntry | None: ...
    def unref(self) -> None: ...

class AttributeCheckFlags(GObject.GFlags):
    FILE_THEN_INDEX = 0
    INDEX_ONLY = 2
    INDEX_THEN_FILE = 1
    NO_SYSTEM = 4

class BlameFlags(GObject.GFlags):
    NORMAL = 0
    TRACK_COPIES_SAME_FILE = 1

class CheckoutNotifyFlags(GObject.GFlags):
    ALL = 65535
    CONFLICT = 1
    DIRTY = 2
    IGNORED = 16
    NONE = 0
    UNTRACKED = 8
    UPDATED = 4

class CheckoutStrategy(GObject.GFlags):
    ALLOW_CONFLICTS = 16
    CONFLICT_STYLE_DIFF3 = 2097152
    CONFLICT_STYLE_MERGE = 1048576
    CONFLICT_STYLE_ZDIFF3 = 33554432
    DISABLE_PATHSPEC_MATCH = 8192
    DONT_OVERWRITE_IGNORED = 524288
    DONT_REMOVE_EXISTING = 4194304
    DONT_UPDATE_INDEX = 256
    DONT_WRITE_INDEX = 8388608
    DRY_RUN = 16777216
    FORCE = 2
    NONE = 1073741824
    NO_REFRESH = 512
    RECREATE_MISSING = 4
    REMOVE_IGNORED = 64
    REMOVE_UNTRACKED = 32
    SAFE = 0
    SKIP_LOCKED_DIRECTORIES = 262144
    SKIP_UNMERGED = 1024
    UPDATE_ONLY = 128
    UPDATE_SUBMODULES = 65536
    UPDATE_SUBMODULES_IF_CHANGED = 131072
    USE_OURS = 2048
    USE_THEIRS = 4096

class CreateFlags(GObject.GFlags):
    FORCE = 1
    NONE = 0

class Credtype(GObject.GFlags):
    DEFAULT = 8
    SSH_CUSTOM = 4
    SSH_INTERACTIVE = 16
    SSH_KEY = 2
    USERPASS_PLAINTEXT = 1

class DiffFindFlags(GObject.GFlags):
    BREAK_REWRITES = 32
    BREAK_REWRITES_FOR_RENAMES_ONLY = 32768
    FIND_ALL = 255
    FIND_AND_BREAK_REWRITES = 48
    FIND_BY_CONFIG = 0
    FIND_COPIES = 4
    FIND_COPIES_FROM_UNMODIFIED = 8
    FIND_DONT_IGNORE_WHITESPACE = 8192
    FIND_EXACT_MATCH_ONLY = 16384
    FIND_FOR_UNTRACKED = 64
    FIND_IGNORE_LEADING_WHITESPACE = 0
    FIND_IGNORE_WHITESPACE = 4096
    FIND_REMOVE_UNMODIFIED = 65536
    FIND_RENAMES = 1
    FIND_RENAMES_FROM_REWRITES = 2
    FIND_REWRITES = 16

class DiffFlag(GObject.GFlags):
    BINARY = 1
    NOT_BINARY = 2
    VALID_ID = 4

class DiffFormatEmailFlags(GObject.GFlags):
    EXCLUDE_SUBJECT_PATCH_MARKER = 1
    NONE = 0

class DiffOption(GObject.GFlags):
    DISABLE_PATHSPEC_MATCH = 4096
    ENABLE_FAST_UNTRACKED_DIRS = 16384
    FORCE_BINARY = 2097152
    FORCE_TEXT = 1048576
    IGNORE_CASE = 1024
    IGNORE_FILE_MODE = 256
    IGNORE_SUBMODULES = 512
    IGNORE_WHITESPACE = 4194304
    IGNORE_WHITESPACE_CHANGE = 8388608
    IGNORE_WHITESPACE_EOL = 16777216
    INCLUDE_IGNORED = 2
    INCLUDE_TYPECHANGE = 64
    INCLUDE_TYPECHANGE_TREES = 128
    INCLUDE_UNMODIFIED = 32
    INCLUDE_UNTRACKED = 8
    MINIMAL = 536870912
    NORMAL = 0
    PATIENCE = 268435456
    RECURSE_IGNORED_DIRS = 4
    RECURSE_UNTRACKED_DIRS = 16
    REVERSE = 1
    SHOW_BINARY = 1073741824
    SHOW_UNMODIFIED = 67108864
    SHOW_UNTRACKED_CONTENT = 33554432
    SKIP_BINARY_CHECK = 8192

class FeatureFlags(GObject.GFlags):
    HTTPS = 2
    SSH = 4
    THREADS = 1

class MergeFileFlags(GObject.GFlags):
    DEFAULT = 0
    DIFF_MINIMAL = 128
    DIFF_PATIENCE = 64
    IGNORE_WHITESPACE = 8
    IGNORE_WHITESPACE_CHANGE = 16
    IGNORE_WHITESPACE_EOL = 32
    SIMPLIFY_ALNUM = 4
    STYLE_DIFF3 = 2
    STYLE_MERGE = 1

class MergeFlags(GObject.GFlags):
    FAIL_ON_CONFLICT = 2
    FIND_RENAMES = 1
    NO_RECURSIVE = 8
    SKIP_REUC = 4

class SortMode(GObject.GFlags):
    NONE = 0
    REVERSE = 4
    TIME = 2
    TOPOLOGICAL = 1

class StashFlags(GObject.GFlags):
    DEFAULT = 0
    INCLUDE_IGNORED = 4
    INCLUDE_UNTRACKED = 2
    KEEP_INDEX = 1

class StatusFlags(GObject.GFlags):
    CONFLICTED = 32768
    CURRENT = 0
    IGNORED = 16384
    INDEX_DELETED = 4
    INDEX_MODIFIED = 2
    INDEX_NEW = 1
    INDEX_RENAMED = 8
    INDEX_TYPECHANGE = 16
    WORKING_TREE_DELETED = 512
    WORKING_TREE_MODIFIED = 256
    WORKING_TREE_NEW = 128
    WORKING_TREE_RENAMED = 2048
    WORKING_TREE_TYPECHANGE = 1024
    WORKING_TREE_UNREADABLE = 4096

class StatusOption(GObject.GFlags):
    DEFAULT = 19
    DISABLE_PATHSPEC_MATCH = 32
    EXCLUDE_SUBMODULES = 8
    INCLUDE_IGNORED = 2
    INCLUDE_UNMODIFIED = 4
    INCLUDE_UNTRACKED = 1
    RECURSE_IGNORED_DIRS = 64
    RECURSE_UNTRACKED_DIRS = 16
    RENAMES_HEAD_TO_INDEX = 128
    RENAMES_INDEX_TO_WORKDIR = 256
    SORT_CASE_INSENSITIVELY = 1024
    SORT_CASE_SENSITIVELY = 512

class SubmoduleStatus(GObject.GFlags):
    INDEX_ADDED = 16
    INDEX_DELETED = 32
    INDEX_MODIFIED = 64
    IN_CONFIG = 4
    IN_HEAD = 1
    IN_INDEX = 2
    IN_WD = 8
    WD_ADDED = 256
    WD_DELETED = 512
    WD_INDEX_MODIFIED = 2048
    WD_MODIFIED = 1024
    WD_UNINITIALIZED = 128
    WD_UNTRACKED = 8192
    WD_WD_MODIFIED = 4096

class BranchType(GObject.GEnum):
    LOCAL = 1
    REMOTE = 2

class CloneLocal(GObject.GEnum):
    AUTO = 0
    LOCAL = 1
    NO_LINKS = 3
    NO_LOCAL = 2

class ConfigLevel(GObject.GEnum):
    APP = 7
    GLOBAL = 4
    HIGHEST = -1
    LOCAL = 5
    PROGRAMDATA = 1
    SYSTEM = 2
    WORKTREE = 6
    XDG = 3

class DeltaType(GObject.GEnum):
    ADDED = 1
    CONFLICTED = 10
    COPIED = 5
    DELETED = 2
    IGNORED = 6
    MODIFIED = 3
    RENAMED = 4
    TYPECHANGE = 8
    UNMODIFIED = 0
    UNREADABLE = 9
    UNTRACKED = 7

class DiffBinaryType(GObject.GEnum):
    DELTA = 2
    LITERAL = 1
    NONE = 0

class DiffFormatType(GObject.GEnum):
    NAME_ONLY = 4
    NAME_STATUS = 5
    PATCH = 1
    PATCH_HEADER = 2
    RAW = 3

class DiffLineType(GObject.GEnum):
    ADDITION = 43
    ADD_EOFNL = 62
    BINARY = 66
    CONTEXT = 32
    CONTEXT_EOFNL = 61
    DELETION = 45
    DEL_EOFNL = 60
    FILE_HDR = 70
    HUNK_HDR = 72

class Direction(GObject.GEnum):
    FETCH = 0
    PUSH = 1

class Error(GObject.GEnum):
    AMBIGUOUS = -5
    BUFS = -6
    EXISTS = -4
    GIT_ERROR = -1
    ITEROVER = -31
    NOTFOUND = -3
    PASSTHROUGH = -30
    @staticmethod
    def quark() -> int: ...

class FileMode(GObject.GEnum):
    BLOB = 33188
    BLOB_EXECUTABLE = 33261
    COMMIT = 57344
    LINK = 40960
    TREE = 16384
    UNREADABLE = 0

class MergeFileFavor(GObject.GEnum):
    NORMAL = 0
    OURS = 1
    THEIRS = 2
    UNION = 3

class PackbuilderStage(GObject.GEnum):
    ADDING_OBJECTS = 0
    DELTAFICATION = 1

class ProxyType(GObject.GEnum):
    AUTO = 1
    NONE = 0
    SPECIFIED = 2

class RebaseOperationType(GObject.GEnum):
    EDIT = 2
    EXEC = 5
    FIXUP = 4
    PICK = 0
    REWORD = 1
    SQUASH = 3

class RefType(GObject.GEnum):
    INVALID = 0
    LISTALL = 3
    OID = 1
    SYMBOLIC = 2

class RemoteCompletionType(GObject.GEnum):
    DOWNLOAD = 0
    ERROR = 2
    INDEXING = 1

class RemoteDownloadTagsType(GObject.GEnum):
    ALL = 3
    AUTO = 1
    NONE = 2
    UNSPECIFIED = 0

class ResetType(GObject.GEnum):
    HARD = 3
    MIXED = 2
    SOFT = 1

class StatusShow(GObject.GEnum):
    INDEX_AND_WORKDIR = 0
    INDEX_ONLY = 1
    WORKDIR_ONLY = 2

class SubmoduleIgnore(GObject.GEnum):
    ALL = 4
    DIRTY = 3
    NONE = 1
    UNSPECIFIED = -1
    UNTRACKED = 2

class SubmoduleRecurse(GObject.GEnum):
    NO = 0
    ONDEMAND = 2
    YES = 1

class SubmoduleUpdate(GObject.GEnum):
    CHECKOUT = 1
    DEFAULT = 0
    MERGE = 3
    NONE = 4
    REBASE = 2

class TreeWalkMode(GObject.GEnum):
    POST = 1
    PRE = 0
