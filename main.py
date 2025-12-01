import RPi.GPIO as GPIO
import time
from actuator_control.actuator_manager import ActuatorManager
from common.data_connector.connector_manager import ConnectorManager
from actuator_control.fan.fan_factory import load_fans
from actuator_control.socket.socket_factory import load_sockets

connector_manager = ConnectorManager()

fans = load_fans("config.json")
sockets = load_sockets("config.json", connector_manager)
actuators = fans + sockets
manager = ActuatorManager(actuators, connector_manager)

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
