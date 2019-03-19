
"""
M5Stack + MIDIモジュール + テノリオン(FW v2.1) を光らせるためのサンプル。
UARTでMIDI system exclusive使うものなら流用できると思われます。
uart.writeの後にsleep入れないとハマります。

MIDIモジュールはこちらで購入
https://necobit.com/denshi/m5stack-midi-module/
"""
from m5stack import lcd
import time
from machine import UART

uart = UART(2, tx=17, rx=16)
uart.init(31250, bits=8, parity=None, stop=1)#MIDI

try:
    #remote_on
    _ls=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0xF7])
    uart.write(_ls)
    time.sleep_ms(100) 

    #play
    _ls= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x00, 0xF7])
    uart.write(_ls)
    time.sleep_ms(100)

    layer=0x01
    #current_layer
    _ls=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x10, layer, 0x00, 0x00, 0x00, 0x00, 0xF7])
    uart.write(_ls)
    time.sleep_ms(100)
        
    led_mode=0x00 #on
    x=0x02
    y=0x02
    _ls =bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x06, x, y, layer, led_mode, 0x00, 0xF7])
    uart.write(_ls)
    time.sleep_ms(100)

    #remote off
    _ls=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF7])
    uart.write(_ls)
    time.sleep_ms(100)    

except Exception as e:
    #print(str(e))
    lcd.println(str(e))

