#-*- coding:utf-8 -*-
from arduino import ArduinoConnector
if __name__ == '__main__':
    AC=ArduinoConnector(com_port='COM6',baudrate=115200)
    #print(AC.echo(msg='Hello'))
    #print(AC.get_humidity(msg='h'))
    print(AC.get_temperature(msg='t'))

