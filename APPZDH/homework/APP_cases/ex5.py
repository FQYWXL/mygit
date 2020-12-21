from time import sleep

from homework.APP_page.app_tenxunxinwen import tenxunxinwen
driver=tenxunxinwen()
#获取窗口大小





aa=driver.get_window_size(windowHandle='current')
x=aa["width"]
y=aa["height"]
print(aa)
# driver.tap([(740,1550)],500)
# driver.tap([()])

# 点击我的
driver.find_element_by_xpath('//android.widget.RelativeLayout[@resource-id=\"com.tencent.news:id/user_tab_button\"]/android.widget.RelativeLayout[1]').click()
sleep(1)
# 点击设置
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.tencent.news:id/title_right\"]').click()
sleep(2)
#点击推送设置
driver.find_element_by_xpath('//android.widget.TextView[@text=\"推送设置\"]').click()
sleep(3)
#点击取消
driver.find_element_by_id('android:id/button2').click()
sleep(2)
#点击返回
# driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.tencent.news:id/title_bar_btn_back\"]').click()
driver.tap([(42,108)],500)
sleep(2)
#点击新闻
driver.find_element_by_xpath('//android.widget.RelativeLayout[@resource-id=\"com.tencent.news:id/news_tab_button\"]/android.widget.RelativeLayout[1]').click()
sleep(2)
#点击其中一条新闻
# driver.find_element_by_xpath('//android.widget.TextView[@text=\"上海“穷人”为何不卖掉房子，换几百万，去周边城市过富人生活？\"]').click()
driver.tap([(340,940)],500)
sleep(2)
#点击分享按钮
driver.find_element_by_xpath('//android.widget.ImageButton[@resource-id=\"com.tencent.news:id/title_btn_share\"]').click()
sleep(2)
#点击新浪微博
driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.tencent.news:id/id_gallery_container_1\"]/android.widget.RelativeLayout[1]/android.widget.ImageButton[1]').click()
sleep(2)
#点击关闭按钮
driver.find_element_by_xpath('//android.widget.TextView[@text=\"关闭\"]').click()
sleep(2)
#点击返回按钮
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.tencent.news:id/title_bar_btn_back\"]').click()
sleep(2)