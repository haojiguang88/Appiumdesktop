import atx
import time

#简单说一下:这个atx是网易开源用pytho写的,也需要wda,跟appium没有一毛钱关系
#做ios自动化直接用wda也行,用这个atx也行,appium太重了!
#需要执行8100端口转发与wda启动两个命令


#连接
d = atx.connect('http://localhost:8100', platform='ios')
#打开车旺大卡
d.start_app('cn.com.trafficguide.hyggpt')
time.sleep(3)

#关闭车旺大卡
d.stop_app('cn.com.trafficguide.hyggpt')
