import telebot
import requests
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help_(message: telebot.types.Message):
    text = 'To start the bot working, please use following format : \n <Currency name>, \
<The currency, you need convert to>, \
<Amount of converting currency>, \n <All available currency to convert: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Currencies available for exchange: '
    for key in keys.keys():
        text ='\n'.join((text, key))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split()

        if len(values) != 3:
            raise ConvertionException('Sorry, you are insert wrong parameters!')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Probably user mistake, please try again!\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Failed to process command for currency!\n{e}')

    else:
        text = f'Cost of {amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()

