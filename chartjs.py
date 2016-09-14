# -*- coding:utf-8 -*-

from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    con = sqlite3.connect("data.db", isolation_level='DEFERRED')
    cur = con.cursor()
    cur.execute('SELECT * FROM co2 ORDER BY id desc LIMIT 0, 40;')
    data = cur.fetchall()
    con.commit()
    con.close()
    labels_date = []
    data_co2 = []
    for i in data:
        labels_date.append(i[1])
        data_co2.append(i[2])
    data_co2.reverse()
    labels_date.reverse()
    return render_template('index.html', labels_date=labels_date, data_co2=data_co2)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
