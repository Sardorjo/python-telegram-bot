import logging
import wikipedia # pip install wikipedia

from aiogram import Bot, Dispatcher, executor, types # pip install aiogram==2.4

API_TOKEN = "6359393844:AAEKdHK9WDgrT2SSgc_32sp1BF3hN3Llp7Q"

# Languages you can enter your language hear
language_mapping = {
    "uzbek": "uz",
    "english": "en",
    "russian": "ru",
}

start_command = """
🚀 Welcome back to Wikibot!

You're all set to explore the world of knowledge. 🌍✨

Just type any keyword, like "book" 📚, and I'll provide you with information about it.

Need to change the language? Use the /set_lang command.

If you want more details or assistance, type /help.

Happy learning with Wikibot! 🤖📖
"""

help_command = """
📚 Welcome to the Wikipedia Bot!

🤖 What is Wikibot?
Wikibot is your mini Wikipedia on Telegram! 🌐

🔍 How to Use:
To get information about any topic, simply send the keyword in your message, and I'll provide you with relevant information. For example, if you want to learn about "books," just type "book."

🌍 Change Language:
You can change the language of the bot with the following commands:
/set_lang "russian" - Switch to Russian
/set_lang "english" - Switch to English
/set_lang "uzbek" - Switch to Uzbek

🔄 Start Over:
To start a new search or refresh, use the /start command.

❓ Need Help?
If you want to learn more about me or need assistance, just type /help.

Enjoy exploring knowledge with Wikibot! 📖🌟

"""

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """This command will be called when type /start"""
    await message.reply(start_command)

@dp.message_handler(commands=["help"])
async def send_discription(message: types.Message):
    """This command will be called when type /start"""
    await message.reply(help_command)

@dp.message_handler(commands=["set_lang"])
async def send_language(message: types.Message):
    """This command will be called when type /set_lang 'language'"""
    try:
        lang = message.text.replace("/set_lang", "").strip().lower()

        if lang  in language_mapping:
            # Upgrade the Wikipedia Language
            wikipedia.set_lang(language_mapping[lang])
            await message.answer(f"Language: {language_mapping[lang]}")
        else:
            await message.answer("Incorrect language name. Enter one of the following language. Uzbek, English, Russian")
    except Exception as e:
        print(e)
        await message.answer("There was an error. Try again.")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("No article on this topic has bin found")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)