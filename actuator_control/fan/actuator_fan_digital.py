import RPi.GPIO as GPIO
from actuator_control.base_actuator import Actuator
from common.utils.debug import Debugger

debug = Debugger()

class FanDigital(Actuator):
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)  # Initialzustand: aus


    def activate(self, value: int | None = None):
        if value is not None and value >= 100:
            GPIO.output(self.pin, GPIO.HIGH)
            debug.log(f"Fan activated (digital HIGH, value={value})", label="FanDigital")
        else:
            GPIO.output(self.pin, GPIO.LOW)
            debug.log(f"Fan not activated (value={value})", label="FanDigital")


    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)
        debug.log("Fan stopped", label="FanDigital")

