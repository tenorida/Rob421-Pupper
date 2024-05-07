#!/usr/bin/env python3

import os
import time
import sys

def setup_pwm():
    zero = 500000
    ninety_deg = 1500000
    one_eight_deg = 2500000
    mid_degrees = 90
    total_degrees = 180

    total_pwm_change_first_half = ninety_deg - zero
    total_pwm_change_second_half = one_eight_deg - zero

    pwm_per_degree_first_half = total_pwm_change_first_half / mid_degrees
    pwm_per_degree_second_half = total_pwm_change_second_half / total_degrees

    return zero, pwm_per_degree_first_half, pwm_per_degree_second_half

def move_servo(pwm_base, pwm_per_deg, deg, servo_id):
    if deg <= 90:
        pwm_value = pwm_base + (pwm_per_deg * deg)
    else:
        pwm_value = pwm_base + (pwm_per_deg * deg)  # Can change

    os.system(f"echo {pwm_value} > /sys/class/pwm/pwmchip0/pwm{servo_id}/duty_cycle")
    time.sleep(1)

def main():
    os.system("sudo systemctl stop robot")  # Safety command where can stop all other movements

    zero, pwm_per_degree_first_half, pwm_per_degree_second_half = setup_pwm()

    # Example of a simple movement sequence for one leg using multiple servos
    move_servo(zero, pwm_per_degree_first_half, 30, 10)  # Move to 30 degrees
    move_servo(zero, pwm_per_degree_second_half, 60, 10) # Move to 60 degrees
    move_servo(zero, pwm_per_degree_first_half, 0, 10)   # Reset to 0 degrees

    print("Leg movement completed")

if __name__ == "__main__":
    main()




