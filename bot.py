from typing import List

import telebot
import random
from telebot.types import Message

TOKEN = '854120048:AAE_gACdmHXA1PmQSGIvEHV5H0GfRsrDBt4'
bot = telebot.TeleBot(TOKEN)

happy_emojis = ['😀','😃','😄','😁','😆','😉','🙂','😋','😛','😝','🥳','😺','😸']
sad_emojis =['😒','😞','😔','😟','😕','🙁','😣','😖','😫','😩','🥺','😢','😭','😿']
heart_emojis = ['😍','🥰','😘']
tongue_emojis = ['😋','😛','😝','😜','🤪']
surprise_emojies = ['🤔','🤨','🧐']
angry_emojis = ['😤','😠','😡','🤬','🤯']
brofist_emojis = ['🤲','👐','🙌','👏','🤝','👍','👎','👊','✊','🤛','🤜','🤞','✌️',
                  '🤟','🤘','👌','👈','👉','👆','👇','☝️','️✋','🤚','🖐','🖖','👋','🤙','💪','🖕','✍️']
confirm_list  = ['Пітверджую', 'Зуб даю', 'Точно-точно', 'ага', '+', '__illuminati comfirmed__', 'Чесне слово', '']

@bot.message_handler(commands=['start'])
def wellcomer(message):
    bot.reply_to(message, 'Це створіння вам ще стане в пригоді')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def confirmer(message):
    if (message.text.find('правда') != -1) or (message.text.find('Правда') != -1):
        bot.reply_to(message, random.choice(confirm_list))
    elif (message.text.find('точно') != -1) or (message.text.find('Точно') != -1):
        bot.reply_to(message, random.choice(confirm_list))
    elif (message.text.find('серйозно') != -1) or (message.text.find('Серйозно') != -1):
        bot.reply_to(message, random.choice(confirm_list))
    elif (message.text.find('підтвер') != -1) or (message.text.find('Підтвер') != -1):
        bot.reply_to(message, random.choice(confirm_list))
    elif (message.text.find('дійсно') != -1) or (message.text.find('Дійсно') != -1):
        bot.reply_to(message, random.choice(confirm_list))
    elif (message.text.find('What will say illuminati') != -1) or (message.text.find('what will say illuminati') != -1):
        bot.reply_to(message, confirm_list[5])

    msg = ''
    for i in message.text:
        if i in happy_emojis:
            i = random.choice(happy_emojis)
            msg += str(i)
        elif i in sad_emojis:
            i = random.choice(sad_emojis)
            msg += str(i)
        elif i in tongue_emojis:
            i = random.choice(tongue_emojis)
            msg += str(i)
        elif i in surprise_emojies:
            i = random.choice(surprise_emojies)
            msg += str(i)
        elif i in heart_emojis:
            i = random.choice(heart_emojis)
            msg += str(i)
        elif i in angry_emojis:
            i = random.choice(angry_emojis)
            msg += str(i)
        elif i in brofist_emojis:
            i = random.choice(brofist_emojis)
            msg += str(i)
    bot.reply_to(message, msg)


bot.polling()
