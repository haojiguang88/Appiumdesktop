# coding: utf-8
import uiautomator2 as u2

#进行设备链接
d = u2.connect_usb('RF8N613SNHB')
d.sleep(5)

#启动app
d.app_start('com.sinoiov.driver')
d.sleep(5)
#退出
d.app_stop('com.sinoiov.driver')


