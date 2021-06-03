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
check=1
while(check>0):
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
        time.sleep(30)
        gDriver1.close()
        gDriver2.close()
        gDriver3.close()
        gDriver4.close()
        print("Times Run = ", check)
        check=check+1
    except:
        print("failed :/")
