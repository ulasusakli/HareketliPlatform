import RPi.GPIO as GPIO
import time

from motorModule import RobotController

# Motorların başlangıç açıları 0,0,0 olarak ayarlanmıştır.
# Motoru Saat yönünde sürmek için robot.move_motor_cw(i,a) komutunu kullanın
# Motoru Saat yönünün tersinde sürmek için robot.move_motor_ccw(i,a) komutunu kullanın
# Röleyi aktif etmek için 


testRobot = RobotController()


testRobot.move_motor_cw(1, 360)
testRobot.move_motor_cw(2, 360)
testRobot.move_motor_cw(3, 360)

time.sleep(3)
testRobot.relay_on()
time.sleep(3)

testRobot.move_motor_ccw(1, 360)
testRobot.move_motor_ccw(2, 360)
testRobot.move_motor_ccw(3, 360)

time.sleep(3)
testRobot.relay_off()
time.sleep(3)
       