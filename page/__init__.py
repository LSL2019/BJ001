"""以下是登录模块的配置信息"""
from selenium.webdriver.common.by import By

# 首页的登录连接
login_btn_link = By.LINK_TEXT, '登录'
# 用户名
login_username = By.ID, 'username'
# 密码
login_password = By.ID, 'password'
# 验证码
login_verify_code = By.ID, 'verify_code'
# 登录按钮
login_btn = By.CLASS_NAME, 'J-login-submit'
# 异常提示信息
login_err_text = By.CSS_SELECTOR, '.layui-layer-content'
# 异常提示信息的确定按钮
login_err_confirm_btn = By.CSS_SELECTOR, '.layui-layer-btn0'
# 登录成功之后显示的昵称
login_nickname = By.CSS_SELECTOR, '.userinfo'
# 安全退出
login_loginout_link = By.LINK_TEXT, '安全退出'
