from selenium.webdriver.chrome.options import Options
from appium import webdriver

import time
from selenium import webdriver
from PIL import Image
#----------------------------------------------------同时运行多台机器要启动多个客户端,改端口号
from selenium.webdriver.chrome.options import Options
# android配置
def appium_desired_android():
    data_android = {"platformName": "Android", "platformVersion": "11.0.0", "deviceName": "192.168.137.3:5555",
                    "appPackage": "com.sinoiov.driver", "appActivity": ".InitActivity", "noReset": True}
    driver = webdriver.Remote("http://localhost:4723/wd/hub", data_android)

    driver.implicitly_wait(5)
# ios配置

def appium_desired_ios():
    data_ios = {"platformName": "ios", "platformVersion": "14.0.1", "deviceName": "hjg",
                "udid": "8287a0aa673816364493bf1f853f4e6658276398", "app": "com.sinoiov.driver",
                "automationName": "XCUITest",
                "xcodeOrgId": "3LMYQAV6FL", "xcodeSigningId": "iPhone Developer", "wdaLocalPort": "8100",
                "noReset": True}
    driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", data_ios)
    driver.implicitly_wait(5)
#web配置
def selenium_desirde_web():

    browser = webdriver.Chrome()
    chrome_options = Options()

    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    # chrome_options.add_experimental_option('--disable-gpu')
    time.sleep(1)
    # 访问登录页面
    url = 'http://wlhyp.utrailertj.com/login.html'
    time.sleep(3)
    # 设置界面最大化
    browser.maximize_window()
    browser.get(url)
    # web配置




if __name__ == '__main__':
    appium_desired_android()
    appium_desired_ios()
    selenium_desirde_web()
