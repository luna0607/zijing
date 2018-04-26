# 紫荆爬虫 
   紫荆官网：http://zijingbt.njuftp.org
   
   ## 使用：
   zijing.db是sqlite文件，其中FILE表储存了61355条种子信息。
   USER表储存了72265条用户信息。
   
   files/names储存了72265个用户名，以空格分割。
   
   files/register储存了每天注册的用户数量，json格式。
   
   折线图：http://www.magicluna.me/zijing-register
   
   files/uploadAndDownload储存了每个用户的上传量和下载量，json格式。
   
   散点图：http://www.magicluna.me/zijing-rate
   
   ## 待完成
   SEEDING表待爬取。做种者信息统计。
   
   DOWNLOAD表待爬取。下载者信息统计。
   
   ## 已完成
   
   USER表数据，已用getUser.py爬取。
   
   FILE表数据，已用getFile.py爬取。
   
   ## 注意
   
  getUser.py与getFile.py的抓取都是用我本人的cookie，使用者可以替换成自己的cookie.
  
      headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'accept-encoding': " gzip, deflate",
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': my_cookie.my_cookie_string,    #cookie字符串所在处
        'dnt': '1',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36',
    }