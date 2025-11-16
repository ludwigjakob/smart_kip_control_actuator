import RPi.GPIO as GPIO
import time
from actuator_control.actuator_manager import ActuatorManager
from data_connector.connector_manager import ConnectorManager
from actuator_control.fan.fan_factory import load_fans

connector_manager = ConnectorManager()

fans = load_fans("config.json")
manager = ActuatorManager(fans, connector_manager)

try:
    while True:
        manager.run()
        time.sleep(2)
except KeyboardInterrupt:
    print("Beende...")
finally:
    for fan in fans:
        fan.stop()
    GPIO.cleanup()
