import sys
from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import * # type: ignore

ContextT = TypeVar("ContextT", bound=commands.Context)
ConverterT = TypeVar("ConverterT", bound=commands.Converter)
IDConverterT = TypeVar("IDConverterT", bound=commands.IDConverter)


if TYPE_CHECKING:

    class Bot(commands.Bot[ContextT]):  # type: ignore[no-redef]
        ...

    class AutoShardedBot(commands.AutoShardedBot[ContextT]):  # type: ignore[no-redef]
        ...

    class Cog(commands.Cog[ContextT]):  # type: ignore[no-redef]
        ...

    class Command(commands.Command[ContextT]):  # type: ignore[no-redef]
        ...

    class HybridCommand(commands.HybridCommand[ContextT]):  # type: ignore[no-redef]
        ...

    class HybridGroup(commands.HybridGroup[ContextT]):  # type: ignore[no-redef]
        ...

    class Converter(commands.Converter[ContextT]):  # type: ignore[no-redef]
        ...

    class ObjectConverter(commands.ObjectConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class MemberConverter(commands.MemberConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class UserConverter(commands.UserConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class MessageConverter(commands.MessageConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class TextChannelConverter(commands.TextChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class InviteConverter(commands.InviteConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    class GuildConverter(commands.GuildConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class RoleConverter(commands.RoleConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GameConverter(commands.GameConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    class ColourConverter(commands.ColourConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    ColorConverter = ColourConverter

    class VoiceChannelConverter(commands.VoiceChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class StageChannelConverter(commands.StageChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class EmojiConverter(commands.EmojiConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class PartialEmojiConverter(commands.PartialEmojiConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    class PartialMessageConverter(commands.PartialMessageConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    class CategoryChannelConverter(commands.CategoryChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class ForumChannelConverter(commands.ForumChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class IDConverter(commands.IDConverter[ConverterT]):  # type: ignore[no-redef]
        ...

    class ThreadConverter(commands.ThreadConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GuildChannelConverter(commands.GuildChannelConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GuildStickerConverter(commands.GuildStickerConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class ScheduledEventConverter(commands.ScheduledEventConverter[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GroupMixin(commands.GroupMixin[ContextT]):  # type: ignore[no-redef]
        ...

    class Group(commands.Group[ContextT]):  # type: ignore[no-redef]
        ...

    class HelpCommand(commands.HelpCommand[ContextT]):  # type: ignore[no-redef]
        ...

    class DefaultHelpCommand(commands.DefaultHelpCommand[ContextT]):  # type: ignore[no-redef]
        ...

    class MinimalHelpCommand(commands.MinimalHelpCommand[ContextT]):  # type: ignore[no-redef]
        ...

else:

    class Bot(commands.Bot, Generic[ContextT]):
        ...

    class AutoShardedBot(commands.AutoShardedBot, Generic[ContextT]):
        ...

    if sys.version_info >= (3, 7):

        class Cog(commands.Cog, Generic[ContextT]):
            ...

    else:

        from typing import GenericMeta

        class _GenericCogMeta(commands.CogMeta, GenericMeta):
            ...

        class Cog(commands.Cog, Generic[ContextT], metaclass=_GenericCogMeta):
            ...

    class Command(commands.Command, Generic[ContextT]):
        ...

    class HybridCommand(commands.HybridCommand, Generic[ContextT]):  # type: ignore[no-redef]
        ...

    class HybridGroup(commands.HybridGroup, Generic[ContextT]):  # type: ignore[no-redef]
        ...

    class Converter(commands.Converter, Generic[ContextT]):  # type: ignore[no-redef]
        ...

    class ObjectConverter(commands.ObjectConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class MemberConverter(commands.MemberConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class UserConverter(commands.UserConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class MessageConverter(commands.MessageConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class TextChannelConverter(commands.TextChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class InviteConverter(commands.InviteConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    class GuildConverter(commands.GuildConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class RoleConverter(commands.RoleConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GameConverter(commands.GameConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    class ColourConverter(commands.ColourConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    ColorConverter = ColourConverter

    class VoiceChannelConverter(commands.VoiceChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class StageChannelConverter(commands.StageChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class EmojiConverter(commands.EmojiConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class PartialEmojiConverter(commands.PartialEmojiConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    class PartialMessageConverter(commands.PartialMessageConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    class CategoryChannelConverter(commands.CategoryChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class ForumChannelConverter(commands.ForumChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class IDConverter(commands.IDConverter, Generic[ConverterT]):  # type: ignore[no-redef]
        ...

    class ThreadConverter(commands.ThreadConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GuildChannelConverter(commands.GuildChannelConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GuildStickerConverter(commands.GuildStickerConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class ScheduledEventConverter(commands.ScheduledEventConverter, Generic[IDConverterT]):  # type: ignore[no-redef]
        ...

    class GroupMixin(commands.GroupMixin, Generic[ContextT]):
        ...

    class Group(commands.Group, Generic[ContextT]):
        ...

    class HelpCommand(commands.HelpCommand, Generic[ContextT]):
        ...

    class DefaultHelpCommand(commands.DefaultHelpCommand, Generic[ContextT]):
        ...

    class MinimalHelpCommand(commands.MinimalHelpCommand, Generic[ContextT]):
        ...
        
if sys.version_info >= (3, 8):
    
    from importlib.metadata import version
    from typing import Final
    
    _version = version
    
else:
    
    from typing import Callable
    
    import importlib_metadata
    from typing_extensions import Final
    
    _version: Callable[[str], str] = importlib_metadata.version
    
__version__: Final[str] = _version('discord-ext-commands-types')
