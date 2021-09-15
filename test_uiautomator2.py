# coding: utf-8
import uiautomator2 as u2

import time
import allure
import pytest
import os


def test_steps_demo(test_data1):
    # 进行设备链接
    d = u2.connect_usb('RF8N613SNHB')
    d.sleep(5)

    # 启动app
    d.app_start('com.sinoiov.driver')
    d.sleep(5)
    d.app_stop('com.sinoiov.driver')
    assert True


if __name__ == '__main__':
    pytest.main(['--alluredir', '../reports/result'])
    os.system('allure generate ../reports/result -o ../reports/report --clean')
