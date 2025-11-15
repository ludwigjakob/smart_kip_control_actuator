import RPi.GPIO as GPIO
import time
from actuator_control.actuator_fan import Fan
from actuator_control.actuator_manager import ActuatorManager
from data_connector.connector_manager import ConnectorManager

GPIO.setmode(GPIO.BCM)

connector_manager = ConnectorManager()

fan1 = Fan(ena=18, in1=23, in2=24)
fan2 = Fan(ena=13, in1=5, in2=6)

manager = ActuatorManager([fan1, fan2], connector_manager)

try:
    while True:
        manager.run()
        time.sleep(2)
except KeyboardInterrupt:
    print("Beende...")
finally:
    fan1.stop()
    fan2.stop()
    GPIO.cleanup()
