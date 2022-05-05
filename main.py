import Token
from telegram.ext import *
import robot


def start_command(update: Updater, context: CallbackContext):
    update.message.reply_text('some random thing')


def help_command(update: Updater, context: CallbackContext):
    update.message.reply_text('help')


def handle_message(update: Updater, context: CallbackContext):
    text = str(update.message.text).lower()
    response = robot.sample_responses(text)

    update.message.reply_text(response)


def error(update: Updater,context1, context: CallbackContext):
    print(f"Update {update} caused error {context1.error}")


def main():
    updater = Updater(Token.API_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
