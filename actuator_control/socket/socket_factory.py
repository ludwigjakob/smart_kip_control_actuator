import json
from common.utils.debug import Debugger
from actuator_control.socket.actuator_socket_tapop100 import SocketTAPOp100

debug = Debugger()

def load_sockets(config_path="config.json", connector_manager=None):
    with open(config_path) as f:
        config = json.load(f)

    sockets = []
    for sock_cfg in config.get("actors", {}).get("sockets", []):
        if sock_cfg["type"] == "tapo_p100":
            socket = SocketTAPOp100(
                id=sock_cfg["id"],
                host=sock_cfg["host"],
                connector_manager=connector_manager
            )
            sockets.append(socket)
        else:
            debug.log(f"Unbekannter Socket Typ: {sock_cfg['type']}", label="Socket Factory")

    return sockets
