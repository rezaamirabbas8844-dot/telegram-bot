import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8970457681:AAEl3WcFw0sOb1i0EZNNn3HxHvEl2HIk9AM"
OPENROUTER_API_KEY = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.choices[0].message.content
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text(f"خطا: {e}")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("ربات روشن شد ✅")
app.run_polling()
