#!/usr/bin/env python

import time
import struct
import sys

import pigpio # official ) http://abyz.co.uk/rpi/pigpio/python.html

if sys.version > '3':
   buffer = memoryview

class ADXL345:
    ADXL345_I2C_ADDR=0x1d
    RUNTIME=60.0
    BUS=1

    def __init__(self):
        self.pi = pigpio.pi() # open local Pi
        self.h = self.pi.i2c_open(self.BUS, self.ADXL345_I2C_ADDR)

        if self.h >= 0 : # Connected OK?
            # Initialise ADXL345.
            self.pi.i2c_write_byte_data(self.h, 0x2d, 0)  # POWER_CTL reset.
            self.pi.i2c_write_byte_data(self.h, 0x2d, 8)  # POWER_CTL measure.
            self.pi.i2c_write_byte_data(self.h, 0x31, 0)  # DATA_FORMAT reset.
            self.pi.i2c_write_byte_data(self.h, 0x31, 11) # DATA_FORMAT full res +/- 16g.

            self.read = 0
            self.start_time = time.time()
        else :
            self.pi.stop()


def main():
    adxl345 = ADXL345()

    while (time.time()-adxl345.start_time) < adxl345.RUNTIME:
        (s, b) = adxl345.pi.i2c_read_i2c_block_data(adxl345.h, 0x32, 6)

        if s >= 0:
            (x, y, z) = struct.unpack('<3h', buffer(b))

            if x<60 and x>-60 and y<60 and y>-60 :
                print("・") 

            elif (abs(x) - abs(y)) > 0 :
                if x < 0:
                    print("=>")
                else :
                    print("<=")
            else :
                if y<0:
                    print("↓")
                else :
                    print("↑")

            # print("{} {} {}".format(x, y, z))
            adxl345.read += 1

    adxl345.pi.i2c_close(adxl345.h)
    adxl345.pi.stop()

if __name__=='__main__':
    main()