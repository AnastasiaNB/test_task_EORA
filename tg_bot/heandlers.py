from telegram.ext import ConversationHandler

def send_help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Напиши /start, чтобы начать диалог."
    )

def send_welcome(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?"
    )
    return 1

def its_cat(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Это кот, а не хлеб! Не ешь его!"
    )
    return ConversationHandler.END

def its_bread(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Это хлеб, а не кот! Ешь его!"
    )
    return ConversationHandler.END