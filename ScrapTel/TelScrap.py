from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_API_TOKEN' with the token obtained from BotFather
TOKEN = '6603156470:AAH-BOCMDZdSItK2SqS1UoNDjrVaT1B-ei4'
bot = Bot(token=TOKEN)

def download_media(update, context):
    # Access media file information
    media = update.message.document  # Change this depending on the type of media you're interested in
    file_id = media.file_id

    # Download the file
    file = bot.get_file(file_id)
    file.download(f"C:\\Users\\naray\\Downloads\\")  # Specify the path to save the downloaded file

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register a handler for document messages (you can customize it based on the type of media you want to download)
    dp.add_handler(MessageHandler(Filters.document, download_media))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
