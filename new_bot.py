import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

state = 1

updater = Updater(token="5689428489:AAHZCYxzZe1cvcRMoxhIdPjsfx0VSN8lGVQ", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global state
    if state == 1:
        text = """
Ви прокидаєтесь в темній кімнаті, що ви будете робити?
1: Спати далі
2: Йти гуляти
"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        state += 1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    global state
    if state == 2:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Хороший вибір")
            state = 1
            text = "Гра закінчилась. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            text = """"
Треба знайти ключі. Де будемо шукати?
1: Шухляда
2: На кухні
            """
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
    elif state == 3:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Нічо не знайшов")
            state += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Послизнувся і вмер. Бадум тсс...")
            state += 1
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()