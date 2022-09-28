# coding=utf8
from bs4 import BeautifulSoup
import requests
import csv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

url = "https://rozetka.com.ua/seller/cool-couple/goods/?section_id=4634769"

req = requests.get(url, headers=headers)
src = req.text

with open("rozetka.html", "w", encoding="utf-8") as file:
    file.write(src)

with open("rozetka.html", encoding="utf-8") as file:
    file.read()

soup = BeautifulSoup(src, 'lxml')
page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all(
    "li", class_="pagination__item ng-star-inserted")[-1].text.strip())
print(f"[INFO] Всего страниц: {page_count}...")

with open("rozetka_complete.csv", "w", encoding="utf-8", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        (
            "Имя",
            "Ссылка",
            "Цена",
            "Наличие")
    )

products = []
for page in range(1, page_count + 1):
    print(f"[INFO] Обработка {page} страницы...")
    url = f"https://rozetka.com.ua/seller/cool-couple/goods/?page={page}"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(src, 'lxml')
    items = soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for item in items:
        title = item.find(
            'a', class_="goods-tile__heading ng-star-inserted").text.strip()
        link = item.find(
            'a', class_="goods-tile__heading ng-star-inserted").get('href').strip()
        price = item.find(
                'div', class_="goods-tile__prices").find('p', class_="ng-star-inserted").text.strip().replace('₴', '')
        status = item.find(
            'div', class_="goods-tile__availability").text.strip()
        result = ({
            "title": title,
            "link": link,
            "price": price,
            "status": status
        })

        with open("rozetka_complete.csv", "a", encoding="utf-8", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow((
                    title,
                    link,
                    price,
                    status
                ))
