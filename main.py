import requests
import json
import logging
import requests.packages.urllib3
import time
from urllib import parse


def daka(xuehao, name):
    requests.packages.urllib3.disable_warnings()
    name=parse.quote(name)
    url = 'http://jk.zzmzz.com/App/index.php/Dk/insert'
    header = {'Host': 'jk.zzmzz.com',
              'Connection': 'keep-alive',
              'Content-Length': '163',
              'Accept': '*/*',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Origin': 'http://jk.zzmzz.com',
              'Referer': 'http://jk.zzmzz.com/app/index.php?m=Dk&title=[02]%20%E3%80%8A%E5%B7%AE%E5%88%AB%E3%80%8B%E7%A4%BA%E8%8C%83%E6%9C%97%E8%AF%BB&yyid=440&shijian=1603103368',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6'
              }
    post_data='xh='+xuehao+'&xm='+name+'&title=%5B02%5D+%E3%80%8A%E5%B7%AE%E5%88%AB%E3%80%8B%E7%A4%BA%E8%8C%83%E6%9C%97%E8%AF%BB&yyid=440&shijian=1603103368'
    print(post_data)
    req = requests.post(url, headers=header, data=post_data, verify=False)
    ret_json = req.json()
    print(ret_json)
    logging.info(str(ret_json))
    if ret_json['code'] == 0:
        print(ret_json['msg'])
    else:
        print(ret_json['title'])

logging.basicConfig(filename='Putonghua.log',level=logging.INFO)
while True:
    name='' #填写姓名
    xuehao='' #填写学号
    daka(xuehao,name)
    time.sleep(121)

