import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

async def tarot(update, context):
    prompt = "Сделай виртуальный расклад Таро на сегодня для пользователя"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    await update.message.reply_text(response['choices'][0]['message']['content'])