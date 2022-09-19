from level_select import show_levels_select
from game_manager import GameManager
from game_state import GameState
from telegram import Update 
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext 
 
token = "5403480122:AAED8OVpeusNYxgR4BGb-fRZLnR35e4XRd8" 
updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 
 
def start_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
 
def message_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text) 
 
start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
dispatcher.add_handler(text_handler) 
 
# Start bot 
updater.start_polling()

def intro():
    """Function asks for user name to play game."""
    
    print("Введіть ім'я:")
    name = input()
    print(f"Привіт: {name}")
    
def show_game_info(title, version):
    """Shows game info to the user"""
    print(f"{title} v{version}")

# Show game info
game_manager = GameManager("My game", 1)
game_manager.start()

if game_manager.game_state == GameState.START:
    print(game_manager.game_state)
    
    # Show user intro
    intro()

    # Ask user to select game level
    level = show_levels_select()
    print(f'Ви вибрали рівень: {level}')
else:
    print("Game already started.")