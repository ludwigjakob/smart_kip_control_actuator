import RPi.GPIO as GPIO
from actuator_control.base_actuator import Actuator
from common.utils.debug import Debugger

debug = Debugger()

class FanPWM(Actuator):
    def __init__(self, ena, in1, in2, frequency=1000):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)

        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)


        self.pwm = GPIO.PWM(ena, frequency)
        self.pwm.start(0)

    def activate(self, value):
        self.pwm.ChangeDutyCycle(value)
        debug.log(f"Current Fan Dutycycle: {value}", label="Fan Dutycycle")

    def stop(self):
        self.pwm.stop()
        debug.log(f" Fan stop", label="Fan Dutycycle")
