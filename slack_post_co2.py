# -*- coding:utf-8 -*-

import sqlite3
import time
import requests
import json 


url = 'your_slack_URL'
while True:
    con = sqlite3.connect("../data.db", isolation_level='DEFERRED')
    cur = con.cursor()
    cur.execute('SELECT * FROM co2 ORDER BY id desc LIMIT 0, 60;')
    data = cur.fetchall()
    con.commit()
    con.close()
    data_co2 = []
    for i in data:
        data_co2.append(i[2])
    max_ppm = max(data_co2)
    if max_ppm >= 2000:
        payload = {"text": "co2:{}ppm!\nopen the window!".format(max_ppm)}
        requests.post(url, data=json.dumps(payload))
    time.sleep(600.0)
