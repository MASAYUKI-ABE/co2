# -*- coding:utf-8 -*-

import time
import sqlite3
from mh_z19 import get_co2


if __name__ == '__main__':
    #sql = u"""
    #create table co2 (
    #id INTEGER PRIMARY KEY AUTOINCREMENT,
    #created_at TIMESTAMP DEFAULT (DATETIME('now','localtime')),
    #conceco2 INTEGER
    #);
    #"""
    #cur.execute(sql)

    while True:
        con = sqlite3.connect("data.db", isolation_level='DEFERRED')
        cur = con.cursor()
        value = get_co2()
        t = (int(value["co2"]),)
        cur.execute(u"insert into co2 (conceco2) values (?)",t)
        con.commit()
        con.close()
        time.sleep(10.0)
