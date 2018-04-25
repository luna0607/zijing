"""
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
"""

import urllib.request

import re

import sqlite3
from bs4 import BeautifulSoup
import my_cookie
try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO


def get_zijing(user_id, c):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'accept-encoding': " gzip, deflate",
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': my_cookie.my_cookie_string,
        'dnt': '1',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36',
    }
    req = urllib.request.Request(
        url="http://zijingbt.njuftp.org/login.html?uid=" + str(user_id),
        headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    # print(soup.find_all("p", class_="not_exist"))

    if len(soup.find_all("p", class_="not_exist")) == 0:
        user_name = soup.h3.getText().split("[")[0]
        user_tables = soup.select("td.user_table")

        create_time = user_tables[0].getText()
        last_active = user_tables[1].getText().split("(")[0]
        privilege = user_tables[2].getText()
        share_rate = user_tables[4].getText()
        uploaded = user_tables[5].getText().split(" ")
        if uploaded[1] == "TB":
            uploaded_size = float(uploaded[0]) * 1024
        elif uploaded[1] == "GB":
            uploaded_size = float(uploaded[0])
        else:
            uploaded_size = -1 * float(uploaded[0])
        downloaded = user_tables[6].getText().split(" ")
        if downloaded[1] == "TB":
            downloaded_size = 1024*float(downloaded[0] )
        elif downloaded[1] == "GB":
            downloaded_size = float(downloaded[0])
        else:
            downloaded_size = -1 * float(downloaded[0])
        rate = user_tables[7].getText()
        c.execute('''INSERT INTO USER (UID,NAME,CREATE_TIME,LAST_ACTIVE,PRIVILEGE,SHARE_RATE,DOWNLOADED,UPLOADED,RATE)
         VALUES (?,?,?,?,?,?,?,?,?);''',
                  (user_id, user_name, create_time, last_active, privilege, share_rate, downloaded_size,
                   uploaded_size, rate))
        print("successfully insert to ser")
        conn.commit()

conn = sqlite3.connect('zijing.db')
c = conn.cursor()
count = 7799
while count != 10000:
    # while count != 18365:
    print(count)
    try:
        get_zijing(count, c)
    except:
        print("except")
        get_zijing(count, c)
    count += 1
