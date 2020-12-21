def gesture(action,driver,s):
    """
    九宫格解锁
    :param action: TouchAction对象
    :param driver: 当前的driver对象
    :param s: 将解锁过程需要经过的点组合成一个结合传入，e.g."s=[1,2,3,5,7,8,9]"
    :return:
    """
    #取得所有坐标点
    p=[
        [230,960],[450,960],[660,960],
       [230,118],[450,1180],[660,1180],
       [230,1390],[350,1390],[660,1390]
    ]





