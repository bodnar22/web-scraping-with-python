# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import re

from urllib3.util import Url

url = "https://zno.osvita.ua/ukrainian/tema.html"

# запис заголовків браузера, що вберігає від можливого бану або обмеження по часу
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# надсилання запиту на сторінку і збереження результату в змінну src
req = requests.get(url, headers=headers)
src = req.text

# запис змінної src у файл index.html
with open("index.html", "w", encoding="utf-8") as file:
        file.write(src)

# читання файлу зі збереженим кодом сторінки
with open("index.html", encoding="utf-8") as file:
        src = file.read()

# створення обєкта біліотеки BeautifulSoup
soup = BeautifulSoup(src, "lxml")
all_task_of_subjects = soup.find_all(class_="tag-item main")

#створення списку, в який буде поміщатися результат кожної ітерації циклу
all_task_list = []
for item in all_task_of_subjects:
        #форматування елемента до текстового вигляду
        item_text = item.text
        # видаляємо \n у строках
        item_text = " ".join(item_text.split())
        # видаляємо символи лишніх тегів
        rep_result = re.sub("0% | 0%|\(..\)|\(...\)|\(.\)", '', item_text)
        # rep = ("  ")
        # for item in rep_result:
        #         if rep in rep_result:
        #                 rep_result = rep_result.replace(rep, ' ')
        part_of_list = re.split(r'  ', rep_result)
        #додавання ітерації циклу у список
        all_task_list.append(part_of_list)
# print(all_task_list)

name_of_section_list = [] # список з назвами розділів
for item in all_task_list: # кожен список у спискові
        name_of_section = item[0] #назва розділу
        name_of_section_list.append(name_of_section)

name_of_topic_list = []
for elem in all_task_list:
        name_of_topic = elem[1:] # список з темами кожного розділу
        name_of_topic_list.append(name_of_topic)
# print(name_of_topic_list)


# for item in all_task_of_subjects:
#         link = soup.find(class_="tag-item freetemp")
#         href_l = "https://zno.osvita.ua" + str(link.get("href"))
#         print(href_l)

# словарь, ключі у якому назви розділів, а значення список з темами
for item in name_of_topic_list:
        part_of_section_dict = dict(zip(name_of_section_list, name_of_topic_list))
# print(name_of_section_list)
# print(part_of_section_dict)



# запис файлу у .json
with open("all_task_list.json", "w") as file:
        json.dump(all_task_list, file, indent=4, ensure_ascii=False)

# завантаження вмісту файлу у змінну all_task_list
with open("all_task_list.json") as file:
        all_task_list = json.load(file)

# print(all_task_list)














