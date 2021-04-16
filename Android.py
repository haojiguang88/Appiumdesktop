# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10.0.0"
caps["deviceName"] = "RF8N613SNHB"
caps["appPackage"] = "com.sinoiov.driver"
caps["appActivity"] = ".InitActivity"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

sleep(5)

driver.quit()
