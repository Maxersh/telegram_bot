# -*- coding: utf-8 -*-
import telebot
import scrapper


def run(urls):
    bot = telebot.TeleBot("1794894660:AAGWJ3zeCKsy6qObr3CW11fOYlgGWcjGSEU")

    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        if message.text == '/start':
            bot.send_message(message.from_user.id, 'started')
        if message.text == '/help':
            bot.send_message(message.from_user.id, 'helped')

    @bot.message_handler(urls, content_types=["text"])
    def handle_text(urls, message):
        bot.send_message(message.from_user.id, urls)
        bot.send_message(message.from_user.id, message)
        if urls and message.text == 'Следующий':
            bot.send_message(message.from_user.id, urls.pop(0))
        elif message.text != 'Следующий':
            urls = scrapper.get_urls(message.text)
            bot.send_message(message.from_user.id, urls.pop(0))
        else:
            bot.send_message(message.from_user.id, 'Кончились видосы :(')


    bot.polling()

if __name__ == '__main__':
    run(['aaa', 'ccc'])