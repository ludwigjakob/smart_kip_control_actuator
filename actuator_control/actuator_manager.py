from actuator_control.strategies import ManualControl, AutoControl

class ActuatorManager:
    def __init__(self, aktoren, connector_manager, db):
        self.aktoren = aktoren
        self.cm = connector_manager
        self.db = db
        self.strategies = {
            'manual': ManualControl(connector_manager),
            'auto': AutoControl()
        }

    def run(self):
        mode = self.cm.get("mode")  # z. B. 'manual' oder 'auto'
        strategy = self.strategies.get(mode, self.strategies['manual'])

        for aktor in self.aktoren:
            strategy.apply(aktor)