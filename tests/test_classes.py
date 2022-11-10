from discord.ext import commands_types

class CustomContext(commands_types.Context):
    ...
    
class CustomConverter(commands_types.Converter):
    ...
    
def test_bot() -> None:
    class CustomBot(commands_types.Bot[CustomContext]):
        ...
        
def test_autosharded_bot() -> None:
    class CustomBot(commands_types.AutoShardedBot[CustomContext]):
        ...
        
def test_cog() -> None:
    class CustomCog(commands_types.Cog[CustomContext]):
        ...
        
def test_command() -> None:
    class CustomCommand(commands_types.Command[CustomContext]):
        ...
        
def test_hybrid_command() -> None:
    class CustomHybridCommand(commands_types.HybridCommand[CustomContext]):
        ...
        
def test_hybrid_group() -> None:
    class CustomHybridGroup(commands_types.HybridGroup[CustomContext]):
        ...
