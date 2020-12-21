from time import sleep
from homework.APP_model import unlock
from homework.APP_page.app_tenxunxinwen import tenxunxinwen

driver = tenxunxinwen()
# 手机锁屏
driver.press_keycode(26)
sleep(2)
# 按下返回键
driver.press_keycode(4)
sleep(2)
aa = driver.get_window_size(windowHandle='current')
x = aa["width"]
y = aa["height"]
driver.swipe(0.5 * x, 0.8 * y, 0.5 * x, 0.1 * y, 500)
sleep(3)
unlock([1, 2, 3, 5, 7, 8, 9])
