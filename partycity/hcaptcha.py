from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# sitekey=33f96e6a-38cd-421b-bb68-7806e1764460&amp
# 0,23 usd

def solvehCaptcha():
    # https://github.com/2captcha/2captcha-python
    import os

    from twocaptcha import TwoCaptcha

    api_key = os.getenv('http://2captcha.com/in.php', '5c41698de06e11096310e7f9c538c1b0')

    solver = TwoCaptcha(api_key)
    options = Options()
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=options)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver.get('')
    try:
        result = solver.hcaptcha(
            sitekey='33f96e6a-38cd-421b-bb68-7806e1764460&amp',
            url='https://www.zerbee.com/Categories/Furniture.aspx',
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result

# driver = webdriver.Chrome(chrome_options=options)
# driver.get('')

# wait for iframe
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '#cf-challenge-hcaptcha-wrapper > div:nth-child(2) > iframe')))

result = solvehCaptcha()

if result:
    code = result['code']

    driver.execute_script(
        "document.querySelector(" + "'" + '[name=h-captcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'"
    )

    driver.find_element(By.CSS_SELECTOR, "#cf-norobot-container > input").click()
    # driver.find_element(By.CSS_SELECTOR, "body > div.challenge-interface > div.button-submit.button").click()








