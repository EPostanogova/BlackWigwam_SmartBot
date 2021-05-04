from arduino import ArduinoConnector

AC=ArduinoConnector(com_port='COM6',baudrate=115200)
print(AC.echo(msg='Hello'))