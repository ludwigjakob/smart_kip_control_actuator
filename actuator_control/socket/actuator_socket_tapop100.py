import asyncio
import os
from kasa import Discover
from actuator_control.base_actuator import Actuator
from debug import Debugger
from dotenv import load_dotenv

debug = Debugger()
load_dotenv()

class SocketTAPOp100(Actuator):
    def __init__(self, id: str, host: str, connector_manager):
        self.id = id
        self.host = host
        self.cm = connector_manager

        self.username = os.getenv("TAPO_USER")
        self.password = os.getenv("TAPO_PASSWORD")

    async def _set_state(self, state: str):
        """Interne async-Methode zur Steuerung der Tapo-Socket über Kasa."""
        dev = await Discover.discover_single(
            self.host,
            username=self.username,
            password=self.password
        )
        await dev.update()

        if state == "on":
            await dev.turn_on()
            debug.log(f"Tapo Socket {self.id} eingeschaltet", label="SocketTAPOp100")
        else:
            await dev.turn_off()
            debug.log(f"Tapo Socket {self.id} ausgeschaltet", label="SocketTAPOp100")


    def activate(self, value: int | None = None):
        # Wert aus DB holen
        socket_state = self.cm.connectors["socket"].read()["state"]
        
        asyncio.run(self._set_state(socket_state))

    def stop(self, value: int | None = None):
        self.cm.connectors["socket"].write("off")
        asyncio.run(self._set_state("off"))
        debug.log(f"Socket {self.id} stopped", label="SocketActuator")
