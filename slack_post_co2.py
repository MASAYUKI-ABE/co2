# -*- coding:utf-8 -*-

import sqlite3
import time
import requests
import json


url = 'your_slack_URL'
con = sqlite3.connect("../data.db", isolation_level='DEFERRED')
cur = con.cursor()
cur.execute('SELECT * FROM co2 ORDER BY id desc LIMIT 0, 0;')
data = cur.fetchall()
con.commit()
con.close()
data_time = data[0][1]
data_co2 = data[0][2]

if data_co2 >= 2000:
    text = "{}\nco2:{}ppm!\nOpen the window!".format(data_time, data_co2)
elif data_co2 >= 1000:
    text = "{}\nco2:{}ppm!\nSomeone is there!".format(data_time, data_co2)

payload = {"text": text}
requests.post(url, data=json.dumps(payload))
