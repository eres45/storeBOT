import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Our Channels", callback_data="channels")],
        [InlineKeyboardButton("Store", callback_data="store")],
        [InlineKeyboardButton("Contact", callback_data="contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Welcome! Please choose an option:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    if query.data == "channels":
        text = (
            "Main Channel link 👇\n"
            "https://t.me/+WmR8_AwNaVFjYjk9\n\n"
            "combo daily drops here 👇\n"
            "https://t.me/+XOYKtSnUYOIwMjM1"
        )
    elif query.data == "store":
        text = (
            "buy  steam games\n"
            "buy configs\n"
            "available to work and build telegram bot , scripts , working apps , websites and more\n"
            "buy netflix , prime , hotstar , and more services\n"
            "buy cursor , windsurf , augment code , trae , and more IDE accounts\n"
            "buy API working keys for  unlimited image gen , chatbot and more\n"
            "buy courses"
        )
    elif query.data == "contact":
        text = "Contact: @eres007"
    else:
        text = "Unknown option"

    await query.edit_message_text(text=text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
