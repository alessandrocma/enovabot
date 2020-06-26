from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = 'Olá '+update.message.from_user.first_name+', seja bem vindo !!!!'
    context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def main():
    token = '1262014792:AAFwVsMIRnRMOwxxtwv2yaP6XhoN5b2yYxg'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start',welcome))

    updater.start_polling()
    updater.idle()


if __name__=="__main__":
    main()