

import sqlite3
#INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (1, 'Paul', 32, 'California', 20000.00 );
conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE FILE
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       TORRENT            TEXT     NOT NULL,
       UPLOADER        CHAR(50),
       UPLOAD_TIME DATE,
       SEEDING INT,
       DOWNLOADED INT,
       DOWNLOADING INT,
       SIZE         DOUBLE);''')
print("File table created successfully")
c.execute('''CREATE TABLE SEEDING
       (UID INT PRIMARY KEY     NOT NULL,
       NAME           CHAR(50)    NOT NULL,
       FID            INT     NOT NULL,
       UPLOADED        CHAR(50),
       DOWNLOADED CHAR(50),
       CLIENT CHAR(50));''')
print("SEEDING table created successfully")
c.execute('''CREATE TABLE USER
       (UID INT PRIMARY KEY     NOT NULL,
       NAME           CHAR(50)    NOT NULL,
       CREATE_TIME DATE,
       LAST_ACTIVE            DATE,
       SHARE_RATE       DOUBLE,
       DOWNLOADED CHAR(50),
       UPLOADED CHAR(50),
       RATE DOUBLE);''')
print("USER table created successfully")
c.execute('''CREATE TABLE DOWNLOAD
       (ID INT PRIMARY KEY     NOT NULL,
       UID    INT    NOT NULL,
       USER_NAME CHAR(50),
             FILE_NAME CHAR(50),
        FID    INT    NOT NULL,
       DOWNLOAD_TIME DATE);''')
print("DOWNLOAD table created successfully")

conn.commit()
conn.close()