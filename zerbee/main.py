# coding=utf8
import json

from lxml.doctestcompare import strip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import csv
import os

# def get_data(url):
from first_projects.main import letter

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

url = " https://www.partycity.com/"
r = requests.get(url=url, headers=headers)
    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)

    # get cath urls
    # r = requests.get("https://www.partycity.com/", headers=headers)
    # print(r.text)

    # soup = BeautifulSoup(r, "lxml")
    # cath = soup.find_all("div", class_="homecontentwrap innercontentwrap")
    # print(cath)

def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--safebrowsing-disable-download-protection")
    options.add_argument("safebrowsing-disable-extension-blacklist")
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\Users\\Admin\\Desctop\\project_1\\chromedriver\\chromedriver.exe')

#     try:
#         driver = webdriver.Chrome(
#             executable_path="C:\\Users\\Admin\\Desctop\\project_1\\chromedriver\\chromedriver.exe",
#             options=options
#         )
#         driver.get(url=url)
#         time.sleep(10)
#
#         with open("index_selenium.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
# def main():
#     # get_data("https://www.zerbee.com/Categories/Furniture.aspx")
#     get_data_with_selenium(" https://www.partycity.com/")
#
# if __name__ == "__main__":
#     main()
with open("index_selenium.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

cath_list = soup.find_all("div", class_="pc-type pc-type--title-3 pc-navigation__column__header")[:-1]
cath_page_links_list = []
all_cath_dict = {}
for cath in cath_list:
    name_of_dir = cath.find("a", tabindex="-1").text.strip()
    link = cath.find("a", tabindex="-1").get('href')
    cath_page_links_list.append(link)
    all_cath_dict[name_of_dir] = link
    # print(link)
# with open("all_cath_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_cath_dict, file, indent=4, ensure_ascii=False)
#     if not os.path.exists(f"{name_of_dir}"):
#         os.mkdir(f"{name_of_dir}")


    responce_of_cathegorie = requests.get(link, headers=headers)
    cathegorie = responce_of_cathegorie.text
    soup_cath = BeautifulSoup(cathegorie, "lxml")
    cath_page_links_list = []
    subcath_list = soup.find("ul", class_="pc-navigation__menu pc-navigation__menu--secondary").find_all("li", class_="pc-navigation__menu__item")
    for subcath in subcath_list:
        fullname = subcath.find("a", class_="pc-navigation__menu__link").get_text().__str__()
        unn_name = subcath.find("ul", class_="pc-navigation__menu pc-navigation__menu--secondary").find_all("li", class_="pc-navigation__menu__link")
        name_of_subdir = fullname.replace('unn_name', ' ').__str__().replace('', '')
        print(str(f"INFO: Обработано {subcath} страниц из {subcath_list}"))
    print(name_of_subdir)
    # for item in subcath_list:
    #     name_of_subcath = item.find("a", class_="pc-navigation__menu__link").text.strip()
    #     if not os.path.exists(f"{name_of_subcath}"):
    #         os.mkdir(f"{name_of_subcath}")




