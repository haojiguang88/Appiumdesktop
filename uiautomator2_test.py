# coding: utf-8
import uiautomator2 as u2
#进行设备链接
d = u2.connect_usb('RF8N613SNHB')
#启动app
d.app_start('com.sinoiov.driver')
#点击我的
d.sleep(2)
d(resourceId="com.sinoiov.driver:id/rb_three").click()
#点击系统设置
d.sleep(2)
d(resourceId="com.sinoiov.driver:id/rl_setting").click()
d.sleep(2)
#退出
d.app_stop('com.sinoiov.driver')

d.sleep(2)

