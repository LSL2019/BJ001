import page
from base.base_tpshop import BaseTPShop


class PageTPShopLogin(BaseTPShop):
    # 点击首页登录按钮
    def page_click_home_login_btn(self):
        self.base_click_element(page.login_btn_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input_text(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input_text(page.login_password, pwd)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input_text(page.login_verify_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click_element(page.login_btn)

    # 获取异常文本信息
    def page_get_err_text(self):
        return self.base_get_element_text(page.login_err_text)

    # 点击异常提示的确定按钮
    def page_click_err_confirm_btn(self):
        self.base_click_element(page.login_err_confirm_btn)

    # 获取用户昵称
    def page_get_nickname(self):
        return self.base_get_element_text(page.login_nickname)

    # 点击安全退出按钮
    def page_click_loginout_link(self):
        self.base_click_element(page.login_loginout_link)

    # 组合业务操作
    def page_login(self, username, pwd, code):
        # 组合操作只封装在一个界面操作的步骤
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_click_login_btn()
