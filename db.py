from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram Bot Token
BOT_TOKEN = "7749918794:AAFlgbWy2k9BTzJMPjFB1eJe7G4WUBniMrQ"

# Predefined responses for legal tech queries
LEGAL_TECH_RESPONSES = {
    "what is a contract management system?": (
        "A contract management system helps organize, track, and automate the lifecycle of contracts. "
        "It ensures compliance, reduces risks, and improves efficiency."
    ),
    "how do i integrate ai into legal practice?": (
        "Integrating AI into legal practice involves using tools like legal research platforms, contract review software, "
        "and predictive analytics to automate tasks, save time, and enhance decision-making."
    ),
    "what is e-discovery?": (
        "E-discovery refers to identifying, collecting, and reviewing electronic data for legal cases. "
        "Tools like Relativity or Everlaw help streamline this process."
    ),
}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to iLegal AI! 🤖\n"
        "Ask me anything about legal technology, compliance, or automation.\n"
        "Type your question to get started!"
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "You can also type questions like:\n"
        "- What is a contract management system?\n"
        "- How do I integrate AI into legal practice?"
    )

# Message handler for predefined responses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()  # Convert message to lowercase for matching
    response = LEGAL_TECH_RESPONSES.get(user_message, "Sorry, I don't have an answer for that question yet.")
    await update.message.reply_text(response)

# Main function to set up the bot
def main():
    # Create the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
