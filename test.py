import sqlite3
import time
import json

import matplotlib.pyplot as plt
from wc import WordCloud
import jieba


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
                word1 = int(row[0]) * 1024 * -1
            if row[1] < 0:
                word2 = int(row[1]) * -1 * 1024
            word = [word1, word2]
            tmp.append(word)
        js = json.dumps(tmp)
        f.write(js)


def getNames():
    # conn = sqlite3.connect('test.db')
    # c = conn.cursor()
    # c.execute('''SELECT NAME FROM USER''')
    # with open('./names', 'w',encoding='utf-8') as f:
    #     for row in c:
    #         f.write(str(str(row[0]).encode(encoding='UTF-8', errors='strict'), encoding='utf-8'))
    #         f.write(" ")
    text_from_file_with_apath = open('./names','r',encoding='utf-8').read()

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    my_wordcloud = WordCloud().generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()


getNames()
