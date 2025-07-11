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
if not TOKEN:
    raise ValueError("No TELEGRAM_TOKEN found. Please set it in your environment variables.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("📢 Our Channels", callback_data="channels")],
        [InlineKeyboardButton("🛒 Store", callback_data="store")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_message = (
        "👋 Welcome to Eres Bot !\n\n"
        "We're excited to have you here.\n\n"
        "🔽 Use the buttons below to get started"
    )

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()

    # Keyboard with a back button.
    back_keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]]
    reply_markup_back = InlineKeyboardMarkup(back_keyboard)

    if query.data == "channels":
        text = (
            "Join our community channels:\n\n"
            "🔗 Main Channel: https://t.me/+WmR8_AwNaVFjYjk9\n"
            "💧 Daily Combo Drops: https://t.me/+XOYKtSnUYOIwMjM1"
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup_back)

    elif query.data == "store":
        text = (
            "Welcome to our store! We offer a wide range of digital products and services, including:\n\n"
            "🎮 Steam Games\n"
            "⚙️ Custom Configurations\n"
            "💻 Custom Development (Telegram bots, scripts, apps, websites)\n"
            "🎬 Streaming Service Subscriptions (Netflix, Prime, Hotstar, etc.)\n"
            "🚀 Developer Tool Accounts (Cursor, Windsurf, Augment Code, Trae, etc.)\n"
            "🔑 API Keys (Unlimited Image Generation, Chatbots, etc.)\n"
            "📚 Educational Courses\n\n"
            "To buy, contact - @eres007"
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup_back)

    elif query.data == "contact":
        text = "For inquiries and support, please reach out to us at: @eres007"
        await query.edit_message_text(text=text, reply_markup=reply_markup_back)

    elif query.data == "main_menu":
        # This is the same as the start command, but we edit the message instead of sending a new one
        keyboard = [
            [InlineKeyboardButton("📢 Our Channels", callback_data="channels")],
            [InlineKeyboardButton("🛒 Store", callback_data="store")],
            [InlineKeyboardButton("📞 Contact", callback_data="contact")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        welcome_message = (
            "👋 Welcome to Eres Bot !\n\n"
            "We're excited to have you here.\n\n"
            "🔽 Use the buttons below to get started"
        )
        await query.edit_message_text(text=welcome_message, reply_markup=reply_markup)


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
