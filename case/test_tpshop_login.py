import os
import sys

sys.path.append(os.getcwd())

import pytest

from page.page_tpshop_login import PageTPShopLogin
from tools.untils import DriverUntil


class TestTPShopLogin(object):
    _driver = None

    def setup_class(self):
        self.driver = DriverUntil().get_driver()
        self.login = PageTPShopLogin()
        #点击登录连接
        self.login.page_click_home_login_btn()

    # 结束方法
    def teardown_class(self):
        DriverUntil().quit_driver()

    # 测试方法
    @pytest.mark.parametrize('username,pwd,code,success,expect',
                             [('13520395681', '123456', '8888','success','呵呵666'),('13520395681', '123457', '8888','fail','密码错误!')])
    def test_login(self, username, pwd, code, success, expect):

        self.login.page_login(username, pwd, code)
        if success == "success":
            """正向用例"""

            try:
                # 添加断言
                assert expect == self.login.page_get_nickname()
            except Exception as e:
                self.driver.get_screenshot_as_file('./img.png')
            finally:
                # 安全退出
                self.driver.refresh()
                self.login.page_click_loginout_link()
                #点击登录连接
                self.login.page_click_home_login_btn()
        else:
            """反向用例"""
            try:

                assert expect == self.login.page_get_err_text()
                # 点击 异常提示信息确定按钮
                self.login.page_click_err_ok_btn()
            except Exception as e:
                self.driver.get_screenshot_as_file('./img.png')
