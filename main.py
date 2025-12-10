from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 Your bot is working!")

app = ApplicationBuilder().token("8560085341:AAGQNfPsZF13dXy6ETQ2WLndYrobgwWb_34").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
