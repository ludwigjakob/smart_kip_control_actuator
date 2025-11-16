import json
from actuator_control.fan.actuator_fan_pwm import FanPWM
from actuator_control.fan.actuator_fan_digital import FanDigital

def load_fans(config_path="config.json"):
    with open(config_path) as f:
        config = json.load(f)

    fans = []
    for fan_cfg in config.get("actors", {}).get("fans", []):
        if fan_cfg["type"] == "pwm":
            fan = FanPWM(
                ena=fan_cfg["ena"],
                in1=fan_cfg["in1"],
                in2=fan_cfg["in2"],
                frequency=fan_cfg.get("frequency", 1000)
            )
            fans.append(fan)
    return fans

