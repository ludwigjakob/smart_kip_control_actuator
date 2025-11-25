from actuator_control.base_actuator import Actuator
from debug import Debugger

debug = Debugger()

class SocketTAPOp100(Actuator):
    def __init__(self, id: str, host: str, connector_manager):
        self.id = id
        self.host = host
        self.cm = connector_manager

    def activate(self, value: int | None = None):
        # Wert aus DB holen
        socket_state = self.cm.connectors["socket"].read()["state"]
        if socket_state == "on":
            debug.log(f"Socket {self.id} ON (host={self.host})", label="SocketTAPOp100")
            # hier würdest du die echte Tapo-API oder GPIO/Relais ansteuern
        else:
            debug.log(f"Socket {self.id} OFF (host={self.host})", label="SocketTAPOp100")

    def stop(self, value: int | None = None):
        self.cm.connectors["socket"].write("off")
        debug.log(f"Socket {self.id} stopped", label="SocketActuator")
