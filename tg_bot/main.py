import os

from dotenv import load_dotenv
from filters import NoFilter, YesFilter
from heandlers import (first_question, its_bread, its_cat, second_question,
                       send_help)
from telegram import Bot
from telegram.ext import (CommandHandler, ConversationHandler, MessageHandler,
                          Updater)

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
updater = Updater(token=os.getenv('BOT_TOKEN'))


handler = ConversationHandler(
    entry_points=[CommandHandler('start', first_question)],
    states={
        1: [
            MessageHandler(YesFilter(), second_question),
            MessageHandler(NoFilter(), its_cat),
            CommandHandler('start', first_question)
        ],
        2: [
            MessageHandler(NoFilter(), its_bread),
            MessageHandler(YesFilter(), its_cat),
            CommandHandler('start', first_question)
        ]
    },
    fallbacks=[]
)

updater.dispatcher.add_handler(CommandHandler('help', send_help))
updater.dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
