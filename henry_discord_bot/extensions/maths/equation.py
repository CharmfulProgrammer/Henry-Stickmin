import lightbulb
import hikari
import requests

plugin = lightbulb.Plugin("Equation")

base_url = "https://x-math.herokuapp.com/api/"

@plugin.command()
@lightbulb.command("equation", "Gives a math equation for you to solve", aliases=["eq"])
@lightbulb.implements(lightbulb.PrefixCommand)
async def equation(ctx: lightbulb.Context):
    # for now, it'll be updated
    res = requests.get(base_url + "random")
    data = res.json()

    expression = data["expression"]
    answer = data["answer"]

    await ctx.respond(expression)




def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)