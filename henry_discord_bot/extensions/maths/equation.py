import lightbulb
import hikari
import requests

plugin = lightbulb.Plugin("Equation")

@plugin.command()
@lightbulb.command("equation", "Gives a math equation for you to solve")
@lightbulb.implements(lightbulb.PrefixCommand)
async def equation(ctx: lightbulb.Context):
    pass


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)