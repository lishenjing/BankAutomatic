from selenium.webdriver.common.by import By
from bank.utils.base import Page
from time import sleep


class Login(Page):
    url = '/'

    # bbs_login_user_loc=(By.XPATH,"//div[@id='mzCust']/div/img")
    # bbs_login_button_loc =(By.ID,"mzLogin")
    #
    # def bbs_login(self):
    #     self.find_element(*self.bbs_login_user_loc).click()
    #     sleep(1)
    #     self.find_element(*self.bbs_login_button_loc).click()

    # login_username_loc = (By.XPATH, '//input[@placeholder="请输入您的姓名"]')
    # login_phone_loc = (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]')
    # login_sms_loc = (By.XPATH, '//div[@id="smscode"]')
    login_org_loc = (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]')

    # login_button_loc = (By.XPATH, '//div[@class="reviseBtn"]/p')

    # 登陆用户名
    def login_username(self, username, login_username_loc):
        self.find_element(*login_username_loc).send_keys(username)

    # 登陆手机号码
    def login_phone(self, phone, login_phone_loc):
        self.find_element(*login_phone_loc).send_keys(phone)

    # 点击验证码
    def login_sms(self, login_sms_loc):
        self.find_element(*login_sms_loc).click()

    # 填写验证码
    def fill_login_sms(self, send_sms_loc, code):
        self.find_element(*send_sms_loc).send_keys(code)

    # 输入机构代码
    def login_org(self, org, login_org_loc):
        self.find_element(*login_org_loc).send_keys(org)

    # 输入身份证
    def login_identity(self, identity, login_identity_loc):
        self.find_element(*login_identity_loc).send_keys(identity)

    # 登陆按钮
    def login_button(self, login_button_loc):
        self.find_element(*login_button_loc).click()


    # 立即申请按钮
    def apply_button(self, apply_button_loc):
        self.find_element(*apply_button_loc).click()

    # 同意按钮
    def agree_button(self, agree_button_loc):
        self.find_element(*agree_button_loc).click()



    # 输入单位名称
    def login_company(self, company, login_company_loc):
        self.find_element(*login_company_loc).send_keys(company)



    # 输入区号
    def area_code(self, area, area_code_loc):
        self.find_element(*area_code_loc).send_keys(area)


    # 输入区号后面的单位号码
    def fixed_phone(self, line, fixed_phone_loc):
        self.find_element(*fixed_phone_loc).send_keys(line)




    # 输入电子邮箱
    def e_mail(self, email, login_email_loc):
        self.find_element(*login_email_loc).send_keys(email)



    #部门名称
    def department_name(self, departname, department_name_loc):
        self.find_element(*department_name_loc).send_keys(departname)








    #单位地址
    def department_addr(self, departaddr, department_addr_loc):
        self.find_element(*department_addr_loc).send_keys(departaddr)




    #家庭地址
    def home_addr(self, homeaddr, home_addr_loc):
        self.find_element(*home_addr_loc).send_keys(homeaddr)



    #年收入
    def annual_salary(self, salary, annual_salary_loc):
        self.find_element(*annual_salary_loc).send_keys(salary)



    #贷款金额
    def bank_loan(self, loan, bank_loan_loc):
        self.find_element(*bank_loan_loc).send_keys(loan)




    #婚姻状况
    def marry_status(self,marry_status_loc ):
        self.find_element(*marry_status_loc).click()

    #学历状况
    def educational_status(self,educational_loc):
        self.find_element(*educational_loc).click()



    # 定义统一登陆接口
    def user_login(self, username, phone, url, number):
        # self.open()
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入您的姓名"]'))
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]'))
        self.login_org(number, (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]'))
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        sleep(3)
        self.login_button((By.XPATH, '//div[@class="reviseBtn"]/p'))
        sleep(3)

    def login_recommendation(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        self.login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/div'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]')
        print('code: ' + code.text)

        self.fill_login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'), code.text)
        self.login_button((By.XPATH, '//button[@class="confirm"]'))
        sleep(3)

    def mgm_recommendation(self, phone, username, url, org):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入手机号码"]'))
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        self.login_org(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(3)
        self.login_button((By.XPATH, '//p[@class="com"]'))
        sleep(3)
        sleep(3)

    def t_recommendation(self, phone, url, org):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.login_org(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(2)
        self.login_button((By.XPATH, '//p[@class="com"]'))
        sleep(2)

    def gift_distribute(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        # self.bbs_login()
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.login_button((By.XPATH, '//p[@class="com"]'))
        sleep(2)


    def fast_progress(self, identity, url):

        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.login_identity(identity, (By.XPATH, '//input[@placeholder="请输入您的身份证号码"]'))
        sleep(1)
        self.login_button((By.XPATH, '//p[@class="com"]'))

    def customer_progress(self, identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.login_identity(identity, (By.XPATH, '//input[@placeholder="请输入您的身份证号码"]'))
        sleep(1)
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入办卡所用手机号"]'))
        sleep(1)
        self.login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[3]/div/div[3]/button'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/div')
        print('code: ' + code.text)

        self.fill_login_sms((By.XPATH, '//input[@placeholder="请输入获取的验证码"]'), code.text)
        sleep(2)
        self.login_button((By.XPATH, '//p[@class="com"]'))


    def t_code(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.login_phone(phone, (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))
        sleep(1)
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.login_button((By.XPATH, '//p[@class="com"]'))


    def apply_card(self, username,identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入身份证上的姓名"]'))
        sleep(1)
        self.login_identity(identity, (By.XPATH, '//input[@placeholder="请输入您的18位身份证号码"]'))
        sleep(1)
        self.login_phone(phone, (By.XPATH, '//*[@id="tel"]'))
        sleep(1)
        self.login_sms((By.XPATH, '//button[@id="yz"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smsCodeShow"]')
        print('code: ' + code.text)

        sleep(1)
        self.fill_login_sms((By.XPATH, '//*[@id="identifyCode"]'), code.text)
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="next"]'))


    sms_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[5]/div/p[2]')
    # pawd_error_hint_loc=(By.XPATH,"//ng-tip/div")
    user_login_success_loc = (By.XPATH, '//*[@id="app"]/div/img')

    # 用户名错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 验证码错误提示
    def pwd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 等了成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
