async def start(update, context):
    await update.message.reply_text(
        "👋 Привет! Я магический бот. Выбери:\n\n"
        "/numerology – Нумерология\n"
        "/tarot – Таро\n"
        "/dream – Сон\n"
        "/horoscope – Гороскоп\n\n"
        "Пришли фото ладони — и я изучу его ✋ (в разработке)")
    
