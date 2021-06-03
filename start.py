import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("--no-sandbox")
gChromeOptions.add_argument("--window-size=1920x1480")
gChromeOptions.add_argument("--disable-dev-shm-usage")
gChromeOptions.add_argument("--incognito")
gChromeOptions.add_argument("--headless")
try:
    gDriver1 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
    gDriver2 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
    gDriver3 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
    gDriver4 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
    gDriver1.get(weburl)
    print("Website 1 loaded")
    gDriver2.get(weburl)
    print("Website 2 loaded")
    gDriver3.get(weburl)
    print("Website 3 loaded")
    gDriver4.get(weburl)
    print("Website 4 loaded")
    time.sleep(1200)
    gDriver1.quit()
    gDriver2.quit()
    gDriver3.quit()
    gDriver4.quit()
    print("Sucessful")
except:
    print("failed :/")
