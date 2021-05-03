from arduino import ArduinoConnector

AC=ArduinoConnector(com_port='COM6',baudrate=115200)
test_string="hello"
rez = bytes(test_string, 'utf-8')
AC.echo(msg=rez)
print(msg_echo)