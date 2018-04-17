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
Cookie: hide_filter=1; cookiesession1=2C0BC7512V0LLFHP9BZBQPFI80RDAD37; login="%E6%B1%AA%E6%B1%AA%E5%96%B5"; uid="60371"; md5="%05%3B_%DA%C7J%2F%F2%B5%83%EB(e%CF%BB%26"; per_page="50"
"""

import urllib.request

import re

import sqlite3
from bs4 import BeautifulSoup

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO


def get_zijing(file_id, c):
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
    req = urllib.request.Request(
        url="http://zijingbt.njuftp.org/stats.html?id=" + str(file_id) + "&show=active#seeders",
        headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    # print(soup.find_all("p", class_="not_exist"))

    if len(soup.find_all("p", class_="not_exist")) == 0:
        file_name = soup.h3.string
        file_torrent = soup.select("a.download_link")[0]["href"]
        info_tr = soup.select("tr.file_info")[4]
        print(info_tr.select("a"))
        if len(info_tr.select("a"))>1:
            file_uploader = info_tr.select("a")[1]["href"].split("=")[1]
        else:
            file_uploader=""
        file_upload_time = info_tr.select("td")[0].get_text().split("上传于")[1]
        size_text = soup.select("tr.file_info")[3].select("td")[0].get_text()
        file_size = re.match(r'大小: \n(.*?) \| 文件数', size_text).group(1)
        tmp = file_size.split(" ")
        if tmp[1] == "MB":
            file_size = float(tmp[0]) * 1024
        elif tmp[1] == "GB":
            file_size = float(tmp[0]) * 1024 * 1024
        else:
            file_size = float(tmp[0])
        seed_text = soup.select("tr.file_info")[5].select("td")[0].get_text()
        file_seeding = re.findall(r'\d+', seed_text)[0]
        file_downloading = re.findall(r'\d+', seed_text)[1]
        file_downloaded = re.findall(r'\d+', seed_text)[2]

        c.execute('''INSERT INTO FILE (ID,NAME,TORRENT,UPLOADER,UPLOAD_TIME,SEEDING,DOWNLOADED,DOWNLOADING,SIZE)
VALUES (?,?,?,?,?,?,?,?,?);''',
                  (file_id, file_name, file_torrent, file_uploader, file_upload_time, file_seeding, file_downloaded,
                   file_downloading, file_size))
        print("successfully insert to file")
        conn.commit()


conn = sqlite3.connect('test.db')
c = conn.cursor()
count = 58523
while count != 59277:
#while count != 18365:
    print(count)
    try:
        get_zijing(count, c)
    except:
        print("except")
        get_zijing(count, c)
    count += 1
