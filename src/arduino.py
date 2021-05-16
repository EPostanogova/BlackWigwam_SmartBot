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


    def echo(self,msg,timeout=3):
        msg_echo = ""
        start_time = datetime.datetime.now()
        while len(msg_echo) == 0:
            self.ser.write(str.encode(msg))
            msg_echo = self.ser.readline()
            cur_time = datetime.datetime.now()
            if (cur_time - start_time).total_seconds() >= timeout * 60:
                break
        self.ser.close()
        return msg_echo.decode()

    def get_humidity(self,msg,timeout=3):
        msg_echo = ""
        start_time = datetime.datetime.now()
        while len(msg_echo) == 0:
            self.ser.write(str.encode(msg))
            msg_echo = self.ser.readline()
            cur_time = datetime.datetime.now()
            if (cur_time - start_time).total_seconds() >= timeout * 60:
                break

        return msg_echo.decode()

    def get_temperature(self,msg,timeout=3):

        msg_echo = ""
        start_time = datetime.datetime.now()
        while len(msg_echo) == 0:
            self.ser.write(str.encode(msg))
            msg_echo = self.ser.readline()
            cur_time = datetime.datetime.now()
            if (cur_time - start_time).total_seconds() >= timeout * 60:
                break

        return  msg_echo.decode()
