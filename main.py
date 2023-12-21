import telebot
import os
from fuzzywuzzy import fuzz
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
mas=[]
if os.path.exists('data/Fraza.txt'):
    f=open('data/Fraza.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/Fraza.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'
@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Чтобы начать работу напиши мне привет:))')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    f=open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s=answer(message.text)
    f.write('u: ' + message.text + '\n' + s +'\n')
    f.close()
    bot.send_message(message.chat.id, s)
bot.polling(none_stop=True, interval=0)