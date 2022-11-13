# coding=utf8
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
from urllib.parse import quote
# ^ for problem solve with Percent encoding

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

url = "https://www.partycity.com/girls-costumes"
r = requests.get(url=url, headers=headers)

def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--safebrowsing-disable-download-protection")
    options.add_argument("safebrowsing-disable-extension-blacklist")
    driver = webdriver.Chrome(options=options, executable_path=f"C:\\Users\\Admin\\Desctop\\project_1\\chromedriver\\chromedriver.exe")

    try:
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Admin\\Desctop\\project_1\\chromedriver\\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(10)

        with open("girls_costumes_sel.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_data_with_selenium("https://www.partycity.com/girls-costumes")

if __name__ == "__main__":
    main()

with open("girls_costumes_sel.html", encoding="utf-8") as file:
    src = file.read()

# soup = BeautifulSoup(src, "lxml")
data_page_number = driver.find_element_by_xpath("data-page-number")
print(data_page_number)