from time import sleep

from selenium import webdriver


class DriverUntil(object):
    _driver = None

    @classmethod
    def get_driver(cls):
        """
        获取driver 对象
        :return:
        """
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://www.baidu.com/')
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """
        退出driver对象
        :return:
        """
        if cls._driver:
            sleep(3)
            cls._driver.quit()
            cls._driver = None



if __name__ == '__main__':
    DriverUntil().get_driver()