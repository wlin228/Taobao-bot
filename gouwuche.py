import datetime
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

times = input("Enter the drop time: Year-Month-Day Hour:Min:Seconds :")
# excutable_path = input('Enter the path of your chrome:')
driver = webdriver.Chrome(r'chromedriver.exe')
while True:
    try:
        print("Please scan the QR code and login your taobao account")
        driver.get(
            'https://cart.taobao.com/cart.htm')
        for i in range(30):
            seconds = 30 - i
            time.sleep(1)
            print("\r%02ss till the task begin........" % seconds, end="")
        if driver.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label'):
            break
    except NoSuchElementException:
        print("\rPlease try again and be fast!")
        time.sleep(5)
        driver.refresh()
i = 0
while True:

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if date >= times:
        driver.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label').click()
        print("\rEverything selected and going to checkout page...")
        break
    else:
        time.sleep(0.5)
    print("\rwaiting for products going live... refreshing", i, "times")
    i = i + 1
    driver.refresh()

time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="J_Go"]').click()
driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div[1]/a[2]').click()
print("Check your order")
