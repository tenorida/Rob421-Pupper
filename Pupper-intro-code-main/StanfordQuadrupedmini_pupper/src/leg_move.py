#!/usr/bin/env python3

import os
import sys
import time

# This is a script that will allow you to move each indidual servo!
# With this you will be able to make custom movements.
# below is an example of how might you use this, build on it if you think it is helpful
# What you need to change is the pwm# value which matches each servo
# pwm1 = J15 connection on the board
# pwm 2 = J14...... pwm16 = J1
# ranges:  0 degree(echo 500000), 90 degree(echo 1500000), 180 degree(echo 2500000)

# The following test was done plugging in an extra servo to J15

zero = 500000
ninety = 1500000
one_eight = 2500000 
total_degrees = 180
mid_degrees = 90

total_pwm_change_first_half = ninety - zero
total_pwm_change_second_half = one_eight - zero


pwm_per_degree_first_half = total_pwm_change_first_half/mid_degrees
pwm_per_degree_second_half = total_pwm_change_second_half/total_degrees
class MoveServos:

    def move_servo13():
        global zero
        what_degree = 30
        if what_degree <= 90:
            degree_finder = zero + (pwm_per_degree_first_half * what_degree)
        else:
            degree_finder = zero + (pwm_per_degree_second_half * what_degree)

        os.system("echo " + str(degree_finder) + " > /sys/class/pwm/pwmchip0/pwm13/duty_cycle")
        time.sleep(1)
        os.system("echo 2500000 > /sys/class/pwm/pwmchip0/pwm13/duty_cycle")
        time.sleep(1)
        os.system("echo 500000 > /sys/class/pwm/pwmchip0/pwm13/duty_cycle")


    def move_servo12():
        global zero
        what_degree = 30
        if what_degree <= 90:
            degree_finder = zero + (pwm_per_degree_first_half * what_degree)
        else:
            degree_finder = zero + (pwm_per_degree_second_half * what_degree)
    
        os.system("echo " + str(degree_finder) + " > /sys/class/pwm/pwmchip0/pwm12/duty_cycle")
        time.sleep(1)
        os.system("echo 2500000 > /sys/class/pwm/pwmchip0/pwm12/duty_cycle")
        time.sleep(1)
        os.system("echo 500000 > /sys/class/pwm/pwmchip0/pwm12/duty_cycle")
        print("done")

def main():
    # os.system("sudo systemctl stop robot")
    move_servo13()

if __name__ == "__main__":
    main()
