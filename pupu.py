import json
import time
import requests

def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/ed60af11-25b0-48b8-bc5b-f9136d9f89ad'
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }

    respnse = requests.get(url, headers=head,verify=False)

    dict = json.loads(respnse.text)  #将字符串转为字典
    name = dict["data"]["name"]  #得到商品名字
    spec = dict["data"]["spec"]  #得到规格
    price = str(int(dict["data"]["price"]) / 100)  #得到折扣价
    market_price = str(int(dict["data"]["market_price"]) / 100)  #得到原价
    share_content = dict["data"]["share_content"]  #得到详细内容
    #将得到内容输出
    print("-------------商品：" + name + "-------------")
    print("规格：" + spec)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + market_price)
    print("详细内容：" + share_content)
    print('\n')

    print("-------------" + name + "-------------")
    try:  # 通过异常抛出，使得结束时不会报错
        while (True):  # 通过循环来不断更新价格
            nowTimeandPrint = time.strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(nowTimeandPrint)
            time.sleep(3)  # time的sleep方法，使每三秒更新一次
    except:
        print("程序结束")

#调用方法
if __name__ == '__main__':
    request_url()
