import serial
import time
import logging
import datetime

class ArduinoConnector:
    def __init__(self,com_port,baudrate):

        self.logger = logging.getLogger('Arduino')
        self.com_port=com_port
        self.baudrate=baudrate
        self.ser = serial.Serial(com_port,baudrate,timeout=1)


    def echo(self,msg):
        self.ser.write(str.encode(msg))
        msg_echo = ""
        start_time = datetime.datetime.now()
        timeout=3
        while len(msg_echo) == 0:
            msg_echo = self.ser.read(self.ser.inWaiting())
            cur_time = datetime.datetime.now()
            if (cur_time - start_time).total_seconds() >= timeout * 60:
                break
        self.ser.close()
        return msg_echo.decode("utf-8")

