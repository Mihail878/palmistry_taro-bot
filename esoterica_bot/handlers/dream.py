import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

async def dream(update, context):
    text = " ".join(context.args)
    prompt = f"Расшифруй следующий сон: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    await update.message.reply_text(response['choices'][0]['message']['content'])