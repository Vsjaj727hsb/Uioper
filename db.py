from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import openai

# Telegram Bot Token
BOT_TOKEN = "7749918794:AAFlgbWy2k9BTzJMPjFB1eJe7G4WUBniMrQ"

# Admin User ID
ADMIN_ID = 1662672529  # Replace with your Telegram user ID

# AI response generator
async def generate_ai_response(user_message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are iLegal AI, an assistant for legal technology queries."},
                {"role": "user", "content": user_message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {e}"

# Message handler for user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Check if the message is from the admin
    if user_id == ADMIN_ID:
        await update.message.reply_text("Hi Admin! How can I assist you today?")
        return

    # Generate AI-based response
    ai_response = await generate_ai_response(user_message)
    await update.message.reply_text(ai_response)

# Main function to set up the bot
def main():
    # Create the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
