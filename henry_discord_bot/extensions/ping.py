import lightbulb

plugin = lightbulb.Plugin("Ping")

@plugin.command()
@lightbulb.command("ping", "Response with pong")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context):
    await ctx.respond("Pong!")


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)