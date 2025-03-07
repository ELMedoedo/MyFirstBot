import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem


logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, Боба! Зачем вызвал?")

def name_planet(update, context):  
    print('Вызван /planet')
    update.message.reply_text('Введите название планеты на английском - Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto')

    planets = {"Mercury": ephem.Mercury("2025/03/07"), 
            "Venus": ephem.Venus("2025/03/07"), 
            "Mars" : ephem.Mars("2025/03/07"), 
            "Saturn": ephem.Saturn("2025/03/07"), 
            "Uranus": ephem.Uranus("2025/03/07"), 
            "Neptune": ephem.Neptune("2025/03/07"),
            "Pluto": ephem.Pluto("2025/03/07")
            }
    if user_text in planets:


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

def talk_to_me(update, context):
    user_text=update.message.text
    print(user_text)
    update.message.reply_text(user_text)





if __name__ == "__main__":
    main()