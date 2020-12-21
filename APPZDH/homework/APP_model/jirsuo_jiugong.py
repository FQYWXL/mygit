from appium.webdriver.common.touch_action import TouchAction
from homework.APP_page.app_tenxunxinwen import tenxunxinwen
def unlock(password):
    # driver=tenxunxinwen()
    action = TouchAction(tenxunxinwen())
    p=[
            [230,960],[450,960],[660,960],
           [230,1180],[450,1180],[660,1180],
           [230,1390],[450,1390],[660,1390]
        ]
    # password=[1,2,3,5,7,8,9]
    #按住第一个键
    action.press(x=p[password[0]-1][0],y=p[password[0]-1][1])
    #移动
    for i in password[1:]:
        action.move_to(x=p[i-1][0],y=p[i-1][1])
        action.wait(500)
    action.release()
    # 提交
    action.perform()