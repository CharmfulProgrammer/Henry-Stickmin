from asyncio import wait_for
import lightbulb
import hikari
import requests

plugin = lightbulb.Plugin("Equation")

base_url = "https://x-math.herokuapp.com/api/"

@plugin.command()
@lightbulb.command("equation", "Gives a math equation for you to solve", aliases=["eq"])
@lightbulb.implements(lightbulb.PrefixCommand)
async def equation(ctx: lightbulb.Context):
    res = requests.get(base_url + "random")
    data = res.json()

    expression = data["expression"]
    answer = data["answer"]

    await ctx.respond(expression)
    # bot waiting for answer here
    event: hikari.events.GuildMessageCreateEvent = await ctx.bot.wait_for(
        hikari.events.GuildMessageCreateEvent,
        timeout=20,
        predicate=lambda e: e.author_id == ctx.author.id
    )

    
    if event.content == str(answer):
        await event.message.respond("correct")
    else:
        await event.message.respond(f"wrong, the correct answer is {answer}")
    



def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)