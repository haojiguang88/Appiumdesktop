# coding: utf-8
import uiautomator2 as u2

import time
import allure
import pytest
import os


def test_steps_demo():
    # 进行设备链接
    d = u2.connect_usb('RF8N613SNHB')
    d.sleep(5)

    # 启动app
    d.app_start('com.sinoiov.driver')
    d.sleep(5)
    d.app_stop('com.sinoiov.driver')
    assert True