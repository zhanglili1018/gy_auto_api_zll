

import pytest

from tools.api import request_tool
from tools.data import excel_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

data1=excel_tool.get_test_case("D:\\softwareData\\换源后的\\test_case\\user\\充值接口测试数据(1).xls")


@pytest.mark.parametrize("accountname,changemoney,assert1",data1[1],ids=data1[0])
def test_post_recharge(pub_data,accountname,changemoney,assert1):
    pub_data["accountname"] = accountname
    pub_data["changemoney"] = changemoney
    pub_data["assert1"] = assert1
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None


    json_data = '''
    {
  "accountName": "${accountname}",
  "changeMoney":  "${changemoney}"
}
    '''
    status_code = 200  # 响应状态码
    expect =""   # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
