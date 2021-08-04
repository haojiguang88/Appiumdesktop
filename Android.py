# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep



def android_automatic():
    caps = {"platformName": "Android", "platformVersion": "11.0.0", "deviceName": "RF8N613SNHB",
            "appPackage": "com.sinoiov.driver", "appActivity": ".InitActivity", "noReset": True}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    sleep(2)
    driver.quit()


if __name__ == '__main__':
    android_automatic()
