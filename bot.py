from typing import List

import telebot
import random
import time
from telebot.types import Message

TOKEN = '854120048:AAE_gACdmHXA1PmQSGIvEHV5H0GfRsrDBt4'
bot = telebot.TeleBot(TOKEN)

happy_emojis = ['😀', '😃', '😄', '😁', '😆', '😉', '🙂', '😋', '😛', '😝', '🥳', '😺', '😸', '😂', '😅']
sad_emojis = ['😒', '😞', '😔', '😟', '😕', '🙁', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😿']
heart_emojis = ['😍', '🥰', '😘', '❤️']
tongue_emojis = ['😋', '😛', '😝', '😜', '🤪']
surprise_emojies = ['🤔', '🤨', '🧐']
angry_emojis = ['😤', '😠', '😡', '🤬', '🤯']
brofist_emojis = ['🤲', '👐', '🙌', '👏', '🤝', '👍', '👎', '👊', '✊', '🤛', '🤜', '🤞', '✌️',
                  '🤟', '🤘', '👌', '👈', '👉', '👆', '👇', '☝️', '️✋', '🤚', '🖐', '🖖', '👋', '🤙', '💪', '🖕', '✍️']
confirm_list = ['Пітверджую', 'Зуб даю', 'Точно-точно', 'ага', '+', '__illuminati comfirmed__', 'Чесне слово']
confirm_trigger_list = ['правда', 'точно', 'серйозно', 'підтвер', 'дійсно','справді']
thanks_trigger_list = ['thanks', 'thank you', '10q', 'дякую']
sticker_id_list = ['CAADBAADTAADVVBXDVc7ZpB4kUURFgQ', 'CAADBAADOwADVVBXDbcPBz9Kr9PAFgQ',
                  'CAADBAADPAADVVBXDftcX0r4VAv5FgQ', 'CAADBAADOgADVVBXDQ1a_GyraZj1FgQ', 'CAADBAADOQADVVBXDZXDhZfW21Y2FgQ']


def upper_caser(word):
    word = word[0].upper() + word[1:]
    return word

@bot.message_handler(content_types=['sticker'])
def recognizer(message):
    stiker_random_list = [message.sticker.file_id, random.choice(sticker_id_list)]
    bot.send_sticker(message.chat.id, random.choice(stiker_random_list))
@bot.message_handler(commands=['start'])
def wellcomer(message):
    bot.reply_to(message, 'Це створіння вам ще стане в пригоді')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def confirmer(message):
    if (message.text.find('What will say illuminati') != -1) or (message.text.find('what will say illuminati') != -1):
        bot.reply_to(message, confirm_list[5])
    elif (message.text.find('дай Боже') != -1) or (message.text.find('Дай Боже') != -1):
        bot.reply_to(message, 'Дай Боже')
    elif (message.text.find('Ілон Маск') != -1) or (message.text.find('Elon Musk') != -1):
        photo = open('tmp/elon.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        for current in confirm_trigger_list:
            if (message.text.find(current) != -1) or (message.text.find(upper_caser(current)) != -1):
                bot.reply_to(message, random.choice(confirm_list))
        for current in thanks_trigger_list:
            if (message.text.find(current) != -1) or (message.text.find(upper_caser(current)) != -1):
                strings = time.strftime("%Y,%m,%d,%H,%M,%S")
                t = strings.split(',')
                numbers = [int(x) for x in t]
                bot.reply_to(message, 'Any'+str(numbers[3])+':'+str(numbers[4]))

    msg = ' '
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
    if msg != ' ':
        bot.reply_to(message, msg)


bot.polling()
