import random

import allure
import requests


from config.conf import API_URL


@allure.feature("用户管理")#一级分类
@allure.story("充值接口")  #二级分类
@allure.title("充值接口-全字段正常流")  #用例名称
def test_kds_recharge(db):
    with allure.step("第一步执行sql语句"):

        res = db.select_execute("SELECT `account_name` FROM `t_cst_account` WHERE `status` = 0 AND `account_name` IS NOT NULL;")
        allure.attach("SELECT `account_name` FROM `t_cst_account` WHERE `status` = 0 AND `account_name` IS NOT NULL;","执行的sql语句", allure.attachment_type.TEXT)

    with allure.step("第二步随机数据取第一个"):
        account_name = random.choice(res)[0]
    with allure.step("第三步准备请求数据"):
        data = {
        "accountName": account_name,
        "changeMoney": 1000000
    }
    with allure.step("第四步发送请求"):
        r = requests.post(f"{API_URL}/acc/recharge", json=data)
    with allure.step("第五步获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)

    with allure.step("第五步获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(str(r.text),"响应正文",allure.attachment_type.TEXT)

    with allure.step("第七步响应断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("充值成功","预期结果",allure.attachment_type.TEXT)
        assert"充值成功" in r.text