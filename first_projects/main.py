# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
from urllib3.util import Url

url = "https://zno.osvita.ua/ukrainian/tema.html"
domen = 'https://zno.osvita.ua'

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

soup = BeautifulSoup(src, "lxml")
items = soup.find_all('li', class_="tag-item main") #
ans = []

for item in items:
        test_list = [] # Розділ з випадаючими темами
        div_tests = item.find('div', class_='l3-wrapper')  # Випадаючий список тем
        tests = div_tests.find_all('li', class_='tag-item')  # Одиночна випадаюча тема
        for test in tests:
                tasks_list = [] #

                URL_test = domen + test.find('a', title='Почати тест').get('href')
                response_test = requests.get(URL_test, headers=headers)
                source = response_test.text
                soup_test = BeautifulSoup(source, "lxml")

                tasks = soup_test.find('div', id='wrap') # спискоз завд теми  тіло першого завд
                task_card = tasks.find_all('div', class_='task-card') # картка завдання
                for task in task_card:
                        question = task.find('div', class_='question').get_text() # Запитання тесту
                        count_task = soup_test.find('div', class_='test-title').find_all('span', 'row') #пошук діва з описом сторінки
                        if f'Кількість завдань: {count_task[-1].get_text()}' not in tasks_list:
                                tasks_list.append(f'Кількість завдань: {count_task[-1].get_text()}')
                                # додавання кількості завдань у список кожне з нового рядка

                        answers_div = task.find('div', class_='answers') # Блок з варіантами відповідей
                        answers = answers_div.find_all('div', class_='answer') # Знайти всі варіанти відповідей
                        answers_list = []  #

                        for answer in answers:
                                letter = answer.find('span').get_text()  # А
                                answers_list.append(f"{letter} - {answer.get_text().replace(letter, '')}") # тире між буквою та запитанням
                                # print(f"{letter} - {answer.get_text().replace(letter, '')}")
                        tasks_list.append(
                                {str(task_card.index(task) + 1) + ". " + question.replace('\n', ''): answers_list}) #{Умова:список відповідей}

                test_list.append({
                        test.find('span').get_text(): tasks_list, # {тема:кількість завдань}
                })
        button = item.find('button', class_='item-name')

        ans.append({
                button.find('b').get_text().replace('\xa0', ''): test_list, # {Розділ : Список тем}
        })

with open('portfolio.json', 'w', encoding='utf-8') as file:
    json.dump(ans, file, indent=3, ensure_ascii=False)