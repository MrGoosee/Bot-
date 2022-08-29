import telebot
import config
import random
import json
from scan import filteredNews, filteredhref
from scan2 import filteredimg


bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, этот бот создан по приколу)))'.format(message.from_user, bot.get_me()),parse_mode='html')
    bot.send_message(message.chat.id, 'Введите команду /help, чтобы узнать какие команды я могу выполнять.')

# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     bot.send_message(message.chat.id, message.text)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Все команды:\n/start - запуск бота.\n/help - показывает все команды.\n/habr - посты с новостями.\n/img - выводит аниме арты.\n/img2 - выводит все аниме арты")




@bot.message_handler(commands=['habr'])
def news(message):
    c = 0
    for data in filteredNews:
        c+= 1
        bot.send_message(message.chat.id, f"{c}){data}")
    bot.send_message(message.chat.id, "Напишите номер новости которую вы хотите прочесть или 0 если хотите вписать другую команду)")
    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.text == "0":
            pass

        else:
            if message.text.isdigit():
                if 0 < int(message.text)< 20:
                    bot.send_message(message.chat.id, filteredhref[int(message.text) - 1])
                elif int(message.text) > 20:
                    bot.send_message(message.chat.id, "Такого поста нет!Слишком большое число!")
                elif int(message.text) < 0:
                    bot.send_message(message.chat.id, "Такого поста нет!Слишком маленькое число!")
            else:
                bot.send_message(message.chat.id, "Ты меня не обманешь! Это не число!")

@bot.message_handler(commands=['img'])
def news(message):
    i = random.randint(1,len(filteredimg)-1)
    # with open('img.json') as f:
    #     if message.from_user is f:
    #         pass
    #     else:
    #         trunk_template = [f'{filteredimg[i]}'
    #                           ]
    #
    #         to_json = {message.from_user: trunk_template}
    #         with open('img.json', 'w') as f:
    #             json.dump(to_json, f, sort_keys=True, indent=2)
    bot.send_message(message.chat.id, filteredimg[i])


@bot.message_handler(commands=['img2'])
def news(message):
    for i in range(1, len(filteredimg)):
        bot.send_message(message.chat.id, filteredimg[i])
#RUN
bot.polling(none_stop=True)

