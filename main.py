import os
import telegram
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def codewars(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'PyNinjaAlex codewars account: {"https://www.codewars.com/users/PYninjaAlex"}')


async def github(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'PyNinjaAlex github account: {"https://github.com/PYninjaAlex/"}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("...", callback_data="3")],
        [
            InlineKeyboardButton("github", callback_data="https://github.com/PYninjaAlex/"),
            InlineKeyboardButton("codewars", callback_data="https://www.codewars.com/users/PYninjaAlex")
        ]
    ]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Links: ", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

4
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("github", github))
    app.add_handler(CommandHandler("codewars", codewars))
    app.run_polling()


if __name__ == '__main__':
    main()
