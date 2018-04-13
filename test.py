'''
Host: zijingbt.njuftp.org
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
DNT: 1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: hide_filter=1; cookiesession1=2C0BC7512V0LLFHP9BZBQPFI80RDAD37; login="%E6%B1%AA%E6%B1%AA%E5%96%B5"; uid="60371"; md5="%05%3B_%DA%C7J%2F%F2%B5%83%EB(e%CF%BB%26"; per_page="50"
'''

import urllib.request
from bs4 import BeautifulSoup

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO


def get_zijing():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'accept-encoding': " gzip, deflate",
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'hide_filter=1; cookiesession1=2C0BC7512V0LLFHP9BZBQPFI80RDAD37; '
                  'login="%E6%B1%AA%E6%B1%AA%E5%96%B5"; uid="60371"; md5="%05%3B_%DA%C7J%2F%F2%B5%83%EB(e%CF%BB%26"; '
                  'per_page="50"',
        'dnt': '1',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36',
    }
    req = urllib.request.Request(url="http://zijingbt.njuftp.org/stats.html?id=106991",
                                 headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode("utf-8")
    soup = BeautifulSoup(data,"html.parser")
    print(soup.h3.string)




get_zijing()
