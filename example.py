import pyfirmata
from time import sleep
comport = 'COM7'
board = pyfirmata.Arduino(comport)



MotorA = board.get_pin('d:2:o')
MotorB = board.get_pin('d:4:o')
Enable = board.get_pin('d:5:p')
MotorA.write(0)
MotorB.write(1)


iterator = pyfirmata.util.Iterator(board)
iterator.start()
tv = board.get_pin('a:1:i')
sleep(1.0)
def temperature():
    temp = tv.read()+0.1
    tdc = (temp*5000.0-500.0)/10.0
    print(tdc)
    return tdc

pin = 9 # servoPin
def FCount(speed):
    Enable.write(speed)


board.digital[pin].mode = pyfirmata.SERVO

def ServoAngle(Angle):

    board.digital[pin].write(Angle)
    sleep(0.015)



#FCount(1)









