from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext.filters import Filters


from settings import settings

from handler import start, save_contact, orders, settings_bot, fikr_qoldirish, info

def main():
    updater = Updater(token=settings.TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler(command='start', callback=start))
    dispatcher.add_handler(MessageHandler(Filters.contact, callback=save_contact))
    dispatcher.add_handler(MessageHandler(Filters.text('Buyurtmalarim'), callback=orders))
    dispatcher.add_handler(MessageHandler(Filters.text('Sozlamalar'), callback=settings_bot))
    dispatcher.add_handler(MessageHandler(Filters.text('Biz haqimizda'), callback=info))
    dispatcher.add_handler(MessageHandler(Filters.text('Fikr qoldirish'), callback=fikr_qoldirish))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
