import lightbulb
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.environ.get('TOKEN')
    PREFIX = os.environ.get('PREFIX')
    bot = lightbulb.BotApp(token=TOKEN, prefix=PREFIX)
    bot.load_extensions_from('extensions', recursive=True)
    bot.run()