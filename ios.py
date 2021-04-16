# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep
caps = {}
caps["platformName"] = "ios"
caps["platformVersion"] = "14.0.1"
caps["deviceName"] = "hjg"
caps["udid"] = "8287a0aa673816364493bf1f853f4e6658276398"
caps["app"] = "com.sinoiov.driver"
caps["automationName"] = "XCUITest"
caps["xcodeOrgId"] = "3LMYQAV6FL"
caps["xcodeSigningId"] = "iPhone Developer"
caps["wdaLocalPort"] = "8100"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(5)


driver.quit()
