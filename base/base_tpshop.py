from tools.untils import DriverUntil
from selenium.webdriver.support.wait import WebDriverWait


class BaseTPShop(object):
    # 初始化
    def __init__(self):
        self.driver = DriverUntil().get_driver()

    # 查找元素
    def base_find_element(self, location, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*location))

    # 输入内容
    def base_input_text(self, location, value):
        element = self.base_find_element(location)
        element.clear()
        element.send_keys(value)

    # 点击元素方法
    def base_click_element(self, location):
        self.base_find_element(location).click()

    # 获取异常文本信息
    def base_get_element_text(self, loc):
        return self.base_find_element(loc).text


