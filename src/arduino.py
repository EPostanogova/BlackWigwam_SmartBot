import serial
import time
import logging

class ArduinoConnector:
    def __init__(self,com_port,baudrate):

        self.logger = logging.getLogger('Arduino')
        self.com_port=com_port
        self.baudrate=baudrate
        self.ser = serial.Serial(com_port,baudrate)
        time.sleep(5)
    def echo(self,msg):

        self.ser.write(msg)
        time.sleep(1)
        msg_echo=self.ser.readline()
        self.ser.close()

