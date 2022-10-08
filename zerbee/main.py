# coding=utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import csv

def get_data(url):
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
for item in cath_list:
    name_of_dir = item.find("a", tabindex="-1").text.strip()


