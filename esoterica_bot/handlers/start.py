async def start(update, context):
    await update.message.reply_text(
        "🔮 Привет! Я магический бот. Выбери:"
"
        "/numerology – Нумерология
"
        "/tarot – Таро
"
        "/dream – Сон
"
        "/horoscope – Гороскоп
"
        "Пришли фото ладони – и я изучу его ✋ (в разработке)"
    )
