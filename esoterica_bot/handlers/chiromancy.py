import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

async def chiromancy_photo(update, context):
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    photo_path = f"{user.id}_hand.jpg"
    await photo_file.download_to_drive(photo_path)

    # Заготовка промпта, GPT не видит фото, но мы ему даем образный запрос
    prompt = (
        "Представь, что ты древний хиромант. "
        "На фотографии ладонь человека. "
        "Сделай мистический, эзотерический анализ руки. "
        "Опиши характер, судьбу и предсказание, как будто ты видишь линии руки, "
        "линию жизни, ума, сердца и судьбы."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    await update.message.reply_text(response['choices'][0]['message']['content'])
