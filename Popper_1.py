#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def servo_map(before_value, before_range_min, before_range_max, after_range_min, after_range_max):
    percent = (before_value - before_range_min) / (before_range_max - before_range_min)
    after_value = after_range_min + percent * (after_range_max - after_range_min)
    return after_value

# Setup for the GPIO
GPIO.setmode(GPIO.BOARD)
hip_servo_pin = 32
knee_servo_pin = 33
GPIO.setup(hip_servo_pin, GPIO.OUT)
GPIO.setup(knee_servo_pin, GPIO.OUT)

hip_servo = GPIO.PWM(hip_servo_pin, 50)  # 50 [Hz] frequency
knee_servo = GPIO.PWM(knee_servo_pin, 50)  # 50 [Hz] frequency

servo_time = 0.01
servo_width_min = 2.5
servo_width_max = 12.5

# Start
hip_servo.start(0)
knee_servo.start(0)

try:
    while True:
        # Lift
        for angle in range(0, 31, 1):
            hip_angle = servo_map(angle, 0, 30, servo_width_min, servo_width_max)
            knee_angle = servo_map(angle, 0, 30, servo_width_min, servo_width_max)
            hip_servo.ChangeDutyCycle(hip_angle)
            knee_servo.ChangeDutyCycle(knee_angle)
            time.sleep(servo_time)

        # Lower
        for angle in range(30, -1, -1):
            hip_angle = servo_map(angle, 0, 30, servo_width_min, servo_width_max)
            knee_angle = servo_map(angle, 0, 30, servo_width_min, servo_width_max)
            hip_servo.ChangeDutyCycle(hip_angle)
            knee_servo.ChangeDutyCycle(knee_angle)
            time.sleep(servo_time)

except KeyboardInterrupt:
    pass

# Cleanup on exit
hip_servo.stop()
knee_servo.stop()
GPIO.cleanup()
