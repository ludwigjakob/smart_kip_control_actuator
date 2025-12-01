import asyncio
import os
from kasa import Discover
from actuator_control.base_actuator import Actuator
from common.utils.debug import Debugger
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
        self.device = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    async def _init_device(self):
        if self.device is None:
            self.device = await Discover.discover_single(
                self.host,
                username=self.username,
                password=self.password
            )
            await self.device.update()

    async def _set_state(self, state: str):
        await self._init_device()
        if state == "on":
            await self.device.turn_on()
            debug.log(f"Tapo Socket {self.id} eingeschaltet", label="SocketTAPOp100")
        else:
            await self.device.turn_off()
            debug.log(f"Tapo Socket {self.id} ausgeschaltet", label="SocketTAPOp100")

    def activate(self, value=None):
        socket_state = self.cm.connectors["socket"].read()["state"]
        self.loop.run_until_complete(self._set_state(socket_state))

    def stop(self, value=None):
        self.cm.connectors["socket"].write("off")
        self.loop.run_until_complete(self._set_state("off"))
        debug.log(f"Socket {self.id} stopped", label="SocketTAPOp100")
