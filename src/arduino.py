import serial
import time

class ArduinoConnector:
    def __init__(self,com_port,baudrate):

        self.logger = logging.getLogger('Arduino')
        self.com_port="COM6"
        self.baudrate=115200
        self.ser = serial.Serial(com_port,baudrate)
    def echo(self,msg=input("Введите что-нибудь: ")):

        ser.write(msg)
        time.sleep(1)
        print (ser.readline())
        ser.close()

