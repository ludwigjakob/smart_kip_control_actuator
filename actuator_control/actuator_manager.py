from actuator_control.strategies import ManualControl, AutoControl
from data_connector.temperature_connector import TemperatureConnector
from data_connector.threshold_connector import ThresholdConnector


class ActuatorManager:
    def __init__(self, aktoren, connector_manager):
        self.aktoren = aktoren
        self.cm = connector_manager
        # Connectoren für AutoControl
        temp_connector = TemperatureConnector()
        threshold_connector = ThresholdConnector()

        self.strategies = {
            'manual': ManualControl(connector_manager),
            'auto': AutoControl(temp_connector, threshold_connector)
        }

    def run(self):
        mode = self.cm.get("mode")  # z. B. 'manual' oder 'auto'
        strategy = self.strategies.get(mode, self.strategies['manual'])

        for aktor in self.aktoren:
            strategy.apply(aktor)