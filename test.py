import sqlite3
import time
import json


def registerChart():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute(
        '''SELECT count(*),strftime('%Y-%m-%d',  CREATE_TIME) FROM USER  GROUP BY strftime('%Y-%m-%d',  CREATE_TIME)''')
    with open('./test', 'w') as f:
        count = 0
        tmp = []
        for row in c:
            count += 1
            word = [int(time.mktime(time.strptime(row[1], "%Y-%m-%d"))), row[0]]
            tmp.append(word)
        js = json.dumps(tmp)
        f.write(js)


registerChart()
