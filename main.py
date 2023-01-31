from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import hi_command
from bots_commands import time_command
from bots_commands import *

import time
from datetime import datetime

def calc(usrerexp):
    return eval(usrerexp)

def daysForNewYear():
    now = datetime.today()
    NewYear = datetime(now.year + 1, 1, 1)
    d = NewYear - now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    return ('До конца года осталось : {} дней, {} часа, {} минут, {} секунд.' .format(d.days, hh, mm, ss))

async def days2NewYear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{daysForNewYear()}')

async def calcul(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(calc(update.message.text.split(" ")[1]))


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{time}')

app = ApplicationBuilder().token("5890192989:AAFejDEUaZmVwaXY8X1CcauWytiisoE3paI").build()

app.add_handler(CommandHandler("NY", days2NewYear))

app.add_handler(CommandHandler("hi", hi_command))

app.add_handler(CommandHandler("time", time_command))

app.add_handler(CommandHandler("calcul", calcul))

print('Server Start!')

app.run_polling()