from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import hi_command
from bots_commands import time_command

def calc(usrerexp):
    return eval(usrerexp)

async def calcul(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(calc(update.message.text.split(" ")[1]))


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{time}')

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("hi", hi_command))

app.add_handler(CommandHandler("time", time_command))

app.add_handler(CommandHandler("calcul", calcul))

print('Server Start!')

app.run_polling()