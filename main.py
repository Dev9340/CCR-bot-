import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 How can I help you ? ")

TOKEN = os.getenv("8560085341:AAGQNfPsZF13dXy6ETQ2WLndYrobgwWb_34")
APP_URL = os.getenv("RENDER_EXTERNAL_URL")

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

async def main():
    await application.initialize()
    await application.bot.set_webhook(f"{APP_URL}/webhook")
    await application.start()
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_path="/webhook",
    )
    await application.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
