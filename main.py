import os
import telegram
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def codewars(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends codewars account link."""
    await update.message.reply_text(f'PyNinjaAlex codewars account: {"https://www.codewars.com/users/PYninjaAlex"}')


async def github(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends github account link."""
    await update.message.reply_text(f'PyNinjaAlex github account: {"https://github.com/PYninjaAlex/"}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with two inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("github", url="https://github.com/PYninjaAlex/"),
            InlineKeyboardButton("codewars", url="https://www.codewars.com/users/PYninjaAlex")
        ]
    ]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Links:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")    


def main() -> None:
    """Run the bot."""
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(CommandHandler("github", github))
    application.add_handler(CommandHandler("codewars", codewars))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()


if __name__ == '__main__':
    main()
