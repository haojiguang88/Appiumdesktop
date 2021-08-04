# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep
def ios_automatic():
    caps = {"platformName": "ios", "platformVersion": "14.0.1", "deviceName": "hjg",
            "udid": "8287a0aa673816364493bf1f853f4e6658276398", "app": "com.sinoiov.driver", "automationName": "XCUITest",
            "xcodeOrgId": "3LMYQAV6FL", "xcodeSigningId": "iPhone Developer", "wdaLocalPort": "8100", "noReset": True}

    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    sleep(5)
    driver.quit()
if __name__ == '__main__':

 ios_automatic()

