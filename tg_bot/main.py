import os
from dotenv import load_dotenv

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, TypeHandler

from heandlers import send_welcome, send_help, its_bread, its_cat
from filters import YesFilter, NoFilter


load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
updater = Updater(token=os.getenv('BOT_TOKEN'))

handler = ConversationHandler(
    entry_points=[CommandHandler('start', send_welcome)],
    states={
        1: [MessageHandler(YesFilter, its_bread), MessageHandler(YesFilter, its_cat)],
        # 2: [MessageHandler(Filters.regex(r'\d{4}-\d\d-\d\d'), get_birth_date)],
        # 3: [MessageHandler(Filters.regex(r'\d{4}-\d\d-\d\d'), get_best_date), CommandHandler('skip', skip_best_date)],
        # 4: [MessageHandler(Filters.regex(r'\d\d:\d\d'), get_best_time), CommandHandler('skip', skip_best_time)],
        # 5: [MessageHandler(Filters.regex(r'Ok'), get_doctor_list), MessageHandler(Filters.regex(r'Return'), send_welcome)],
        # 6: [MessageHandler(Filters.text, create_emias_appointment)],
    },
    fallbacks=[]
)

updater.dispatcher.add_handler(CommandHandler('help', send_help))
updater.dispatcher.add_handler(handler)


updater.start_polling()
updater.idle()