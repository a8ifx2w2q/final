import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("--window-size=1920x1480")
gChromeOptions.add_argument("--disable-dev-shm-usage")
gChromeOptions.add_argument("--incognito")
gChromeOptions.add_argument("--headless")
gChromeOptions.add_argument("--no-sandbox")
gDriver1 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
gDriver2 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
gDriver3 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
gDriver4 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
gDriver5 = webdriver.Chrome(options=gChromeOptions, executable_path=ChromeDriverManager().install())
check=1
while(check>0):
    try:
        gDriver1.get(weburl)
        gDriver2.get(weburl)
        gDriver3.get(weburl)
        gDriver4.get(weburl)
        gDriver5.get(weburl)
        time.sleep(30)
        gDriver1.close()
        gDriver2.close()
        gDriver3.close()
        gDriver4.close()
        gDriver5.close()
        print("Times Run = ", check)
        check=check+1
    except:
        print("failed :/")
