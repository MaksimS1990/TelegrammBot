from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
