import RPi.GPIO as GPIO
from actuator_control.base_actuator import Actuator
from debug import Debugger

debug = Debugger()

class Fan(Actuator):
    def __init__(self, ena, in1, in2):
        GPIO.setup([ena, in1, in2], GPIO.OUT)
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        self.pwm = GPIO.PWM(ena, 1000)
        self.pwm.start(0)

    def set_duty_cycle(self, value):
        self.pwm.ChangeDutyCycle(value)
        debug.log(f"Current Fan Dutycycle: {value}", label="Fan Dutycycle")

    def stop(self):
        self.pwm.stop()
        debug.log(f" Fan stop", label="Fan Dutycycle")
