# -*- coding: utf-8 -*-
import os
import sys
import json
import hashlib
import telebot
import googleapiclient.discovery
import scrapper as scr



if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Неправильное количество аргументов')

    bot = telebot.TeleBot("1794894660:AAGWJ3zeCKsy6qObr3CW11fOYlgGWcjGSEU")
    API_KEY = "AIzaSyASBeMw6E_uKXocqyBBydhzgrzM6Cq9dbQ"
    api_service_name = 'youtube'
    api_version = 'v3'

    # Create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    key_words = sys.argv[1]
    dir_path = 'C:\\Users\\d.abramov\\PycharmProjects\\bot\\'
    h = hashlib.md5(key_words.encode())
    search_name = 'search_{}.json'.format(h.hexdigest())
    path = dir_path + search_name

    if not os.path.isfile(path):
        IDs = scr.get_ids(youtube, key_words)
        URLs = scr.get_urls(youtube, IDs)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(URLs, file, indent=2, ensure_ascii=False)
    else:
        with open(path, 'r') as file:
            URLs = json.load(file)





