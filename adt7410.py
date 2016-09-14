# -*- coding:utf-8 -*-

import smbus


def get_temp():
    word_data = bus.read_word_data(address_adt7410, register_adt7410)
    data = (word_data & 0xff00)>>8 | (word_data & 0xff)<<8
    data = data>>3
    if data & 0x1000 == 0:
        temperature = data*0.0625
    else:
        temperature = ( ( ~data&0x1fff) + 1 ) * -0.0625
    retrun temperature

    while 1:
        result = ser.write("\xff\x01\x86\x00\x00\x00\x00\x00\x79")
        s = ser.read(9)
        if s[0] == "\xff" and s[1] == "\x86":
            return {'co2': ord(s[2])*256 + ord(s[3])}
        break
