from typing import TypeVar
from typing_extensions import Final

from discord.ext import commands
from discord.ext.commands import *

ContextT = TypeVar("ContextT", bound=commands.Context)
ConverterT = TypeVar("ConverterT", bound=commands.Converter)
IDConverterT = TypeVar("IDConverterT", bound=commands.IDConverter)

class Bot(commands.Bot[ContextT]): ... # type: ignore[no-redef]
class AutoShardedBot(commands.AutoShardedBot[ContextT]): ... # type: ignore[no-redef]
class Cog(commands.Cog[ContextT]): ... # type: ignore[no-redef]
class Command(commands.Command[ContextT]): ... # type: ignore[no-redef]
class HybridCommand(commands.HybridCommand[ContextT]): ... # type: ignore[no-redef]
class HybridGroup(commands.HybridGroup[ContextT]): ... # type: ignore[no-redef]
class Converter(commands.Converter[ContextT]): ... # type: ignore[no-redef]
class ObjectConverter(commands.ObjectConverter[IDConverterT]): ... # type: ignore[no-redef]
class MemberConverter(commands.MemberConverter[IDConverterT]): ... # type: ignore[no-redef]
class UserConverter(commands.UserConverter[IDConverterT]): ... # type: ignore[no-redef]
class MessageConverter(commands.MessageConverter[IDConverterT]): ... # type: ignore[no-redef]
class TextChannelConverter(commands.TextChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class InviteConverter(commands.InviteConverter[ConverterT]): ... # type: ignore[no-redef]
class GuildConverter(commands.GuildConverter[IDConverterT]): ... # type: ignore[no-redef]
class RoleConverter(commands.RoleConverter[IDConverterT]): ... # type: ignore[no-redef]
class GameConverter(commands.GameConverter[ConverterT]): ... # type: ignore[no-redef]
class ColourConverter(commands.ColourConverter[ConverterT]): ... # type: ignore[no-redef]
ColorConverter = ColourConverter
class VoiceChannelConverter(commands.VoiceChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class StageChannelConverter(commands.StageChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class EmojiConverter(commands.EmojiConverter[IDConverterT]): ... # type: ignore[no-redef]
class PartialEmojiConverter(commands.PartialEmojiConverter[ConverterT]): ... # type: ignore[no-redef]
class PartialMessageConverter(commands.PartialMessageConverter[ConverterT]): ... # type: ignore[no-redef]
class CategoryChannelConverter(commands.CategoryChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class ForumChannelConverter(commands.ForumChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class IDConverter(commands.IDConverter[ConverterT]): ... # type: ignore[no-redef]
class ThreadConverter(commands.ThreadConverter[IDConverterT]): ... # type: ignore[no-redef]
class GuildChannelConverter(commands.GuildChannelConverter[IDConverterT]): ... # type: ignore[no-redef]
class GuildStickerConverter(commands.GuildStickerConverter[IDConverterT]): ... # type: ignore[no-redef]
class ScheduledEventConverter(commands.ScheduledEventConverter[IDConverterT]): ... # type: ignore[no-redef]
class GroupMixin(commands.GroupMixin[ContextT]): ... # type: ignore[no-redef]
class Greedy(commands.Greedy[ConverterT]): ... # type: ignore[no-redef]
class Range(commands.Range[ConverterT]): ... # type: ignore[no-redef]
class HelpCommand(commands.HelpCommand[ContextT]): ... # type: ignore[no-redef]
class DefaultHelpCommand(commands.DefaultHelpCommand[ContextT]): ... # type: ignore[no-redef]
class MinimalHelpCommand(commands.MinimalHelpCommand[ContextT]): ... # type: ignore[no-redef]

__version__: Final[str]
