from __future__ import print_function
import time
from dual_mc33926_rpi import motors, MAX_SPEED

# setpoint de velocidades
# basado en la libreria dual mc33926 de pololu
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]  

try:
    motors.enable()
    motors.setSpeeds(0, 0)

    print("Motor 1 adelante")
    for s in test_forward_speeds:
        motors.motor1.setSpeed(s)
        time.sleep(0.005)

    print("Motor 1 reversa")
    for s in test_reverse_speeds:
        motors.motor1.setSpeed(s)
        time.sleep(0.005)

    print("Motor 2 adelante")
    for s in test_forward_speeds:
        motors.motor2.setSpeed(s)
        time.sleep(0.005)

    print("Motor 2 reversa")
    for s in test_reverse_speeds:
        motors.motor2.setSpeed(s)
        time.sleep(0.005)

finally:

  motors.setSpeeds(0, 0)
  motors.disable()
