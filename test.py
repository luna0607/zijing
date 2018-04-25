import sqlite3
import time
import json


def registerChart():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute(
        '''SELECT count(*),strftime('%Y-%m-%d',  CREATE_TIME) FROM USER  GROUP BY strftime('%Y-%m-%d',  CREATE_TIME)''')
    with open('./register', 'w') as f:
        count = 0
        tmp = []
        for row in c:
            count += 1
            word = [int(time.mktime(time.strptime(row[1], "%Y-%m-%d")) * 1000), row[0]]
            tmp.append(word)
        js = json.dumps(tmp)
        f.write(js)


def uploadAndDownload():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''SELECT UPLOADED, DOWNLOADED FROM USER''')
    with open('./uploadAndDownload', 'w') as f:
        tmp = []
        for row in c:
            word1 = row[0]
            word2 = row[1]
            if row[0] < 0:
                word1 = int(row[0])*1024*-1
            if row[1] < 0:
                word2 = int(row[1])*-1 * 1024
            word = [word1, word2]
            tmp.append(word)
        js = json.dumps(tmp)
        f.write(js)


uploadAndDownload()
