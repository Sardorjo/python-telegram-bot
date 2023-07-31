import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API_TOKEN'#From here you put the api you got from the bodfather bot
wikipedia.set_lang("en")#you can choose Wikipedia language from here
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm wikibot!\nCreated by Sardor dev")#you can write what happens when the start button is pressed



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("There is no article on this topic")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
