#!/usr/bin/env python2
#-*-coding:utf-8-*-

import serial
import serial.tools.list_ports
import parser

# sentence = "$GHFPD,1234,12234.123,90.123,45.55,33.2,23.66,127.1111,78.23,1.1,2.3,6.6,1.5,16,23,2,4*68"
# sentence = "$GNGGA,124216.00,2812.21694085,N,11301.30710367,E,2,00,9999.0,57.0184,M,-16.1671,M,1.0,3330*72"
# sentence = "$GINS,1451,368123.310,34.1966,108.85,80.3,12.3,34.3,1.4,0.32,-22,90.32,11,1,2,3,4,5,1.1,7,*58"
# sentence = "$GPZDA,124216.00,24,03,2024,,*65"
# sentence = "$GNRMC,124216.00,A,2812.21694085,N,11301.30710367,E,0.226,276.4,240324,4.0,W,D,C*5E"
# sentence = "$GNGGA,022527.00,3039.60789882,N,10414.13208340,E,4,26,1.1,573.7596,M,-42.6563,M,1.0,3998*72"
# sentence = "$GPVTG,,,,,,,,,A*3F"

class Test:

    def __init__(self):
        self.serial = None

        ports = list(serial.tools.list_ports.comports())
        # 输出串口名
        for port, desc, hwid in sorted(ports):
            print(f'Port: {port}, Description: {desc}, Hardware ID: {hwid}')

    def test_com(self, port, baud):
        
        try:
            self.serial = serial.Serial(port=port, baudrate=baud, timeout=0.2)
        except Exception as e:
            print(f"无法打开串口: {e}")
            exit()
        while True:
            data = self.serial.readline().strip()
            if data:
                nmea_str = data.decode('ascii')
                print(nmea_str)
                res = parser.parse_nmea_sentence(nmea_str)
                print(res)

if __name__ == '__main__':
    app = Test()
    serial_port = "/dev/cu.usbserial-14330"
    serial_baud = "115200"
    app.test_com(port=serial_port, baud=serial_baud)