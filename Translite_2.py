import telebot

token = ''
bot = telebot.TeleBot(token)

bot_name = '@My_Meow123_bot'


def translite(b):
    a = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',
         ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
         '’': 'э', 'z': 'ф', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'}

    text = str(b).lower()
    translit_text = ''
    for r in text:
        if r == ' ':
            translit_text += ' '

            continue
        elif r not in a:
            translit_text += r

            continue
        elif r in a:
            translit_text += a.get(r)

    return translit_text


@bot.message_handler()
def start(message):
    if message.text == bot_name:
        mess = translite(message.reply_to_message.text)
        mess += ' мяу'
        bot.send_message(message.chat.id, mess, reply_to_message_id =  message.reply_to_message.id)
    else:
        pass


bot.polling(none_stop=True)
