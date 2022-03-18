import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import strftime, sleep
import json
import datetime

# 头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
# 地址
url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/9b7e3f26-552c-4d21-b86e-81237c74c280'
# 发送请求
response = requests.get(url=url, headers=headers, verify=False)
text = response.text
# 解码json数据
jsonbj = json.loads(text)
# 获取产品名称
pname = jsonbj['data']['name']
# 产品折前的价格
before_price = (jsonbj['data']['market_price']/100)
# 产品折后价格
after_price = (jsonbj['data']['price']/100)
# 产品的规格
specifications = jsonbj['data']['spec']
# 产品的详情
details = (jsonbj['data']['sub_title'])

print("------------------------" + pname + "------------------------------")
print("规格：" + specifications)
print("价格" + str(before_price))
print("原价/折扣价：" + str(before_price) + "/" + str(after_price))
print("详细内容：" + details)
print("\n\n--------------------" + pname + "的价格波动-----------------------")

# 获取当前时间
print(datetime.datetime.now())

while (1):
    response = requests.get(url=url, headers=headers, verify=False)
    text = response.text
    # 转换成json格式
    jsonbj = json.loads(text)
    before_price = (jsonbj['data']['market_price']/100)
    # 获取当前时间
    time = datetime.datetime.now()
    print(str(time) + "价格为" + str(before_price))
    # 休眠时间
    sleep(5)