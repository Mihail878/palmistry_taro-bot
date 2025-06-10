from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler
from config import TELEGRAM_TOKEN
from handlers.start import start
from handlers.numerology import numerology
from handlers.tarot import tarot
from handlers.dream import dream
from handlers.horoscope import horoscope
from handlers.chiromancy import chiromancy_photo

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("numerology", numerology))
app.add_handler(CommandHandler("tarot", tarot))
app.add_handler(CommandHandler("dream", dream))
app.add_handler(CommandHandler("horoscope", horoscope))
app.add_handler(MessageHandler(filters.PHOTO, chiromancy_photo))

app.run_polling()
