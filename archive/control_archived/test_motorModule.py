import time

from motorModule import RobotController

testRobot = RobotController()

testRobot.move_motor_cw(1, 45)
testRobot.move_motor_cw(2, 45)
testRobot.move_motor_cw(3, 45)

time.sleep(1)

testRobot.relay_on(3)


testRobot.move_motor_ccw(1, 45)
testRobot.move_motor_ccw(2, 45)
testRobot.move_motor_ccw(3, 45)

time.sleep(1)

testRobot.relay_off(3)

       