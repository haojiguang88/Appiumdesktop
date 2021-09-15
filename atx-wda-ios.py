import atx
import time
import allure
import pytest
import os

# 简单说一下:这个atx是网易开源用pytho写的,也需要wda,跟appium没有一毛钱关系
# 做ios自动化直接用wda也行,用这个atx也行,appium太重了!
# 需要执行8100端口转发与wda启动两个命令

def test_steps_demo(test_data1):
    assert True


# 连接
d = atx.connect('http://localhost:8100', platform='ios')
# 打开车旺大卡
d.start_app('cn.com.trafficguide.hyggpt')
time.sleep(3)

# 关闭车旺大卡
d.stop_app('cn.com.trafficguide.hyggpt')
if __name__ == '__main__':
    pytest.main(['--alluredir', '../reports/result'])
    os.system('allure generate ../reports/result -o ../reports/report --clean')