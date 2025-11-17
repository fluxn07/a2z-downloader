import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Load .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# The reply message
REPLY_TEXT = """⚡ *Click the Download Button to Continue!* ⚡

👇 Choose your platform from the menu below:
📸 Instagram  
▶️ YouTube  
📘 Facebook  
🎵 TikTok  
🔞 18+

Enjoy downloading! 🚀
"""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        REPLY_TEXT,
        parse_mode="Markdown"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hey! Send me any link and I’ll help you download it!"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # /start command
    app.add_handler(CommandHandler("start", start))

    # All messages → same reply
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
