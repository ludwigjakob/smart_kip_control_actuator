# SmartKIP Control Actuator

Hardware control service for refrigerator fans and smart sockets.

## Features
- Control digital fans via GPIO pins
- Prepared support for PWM-controlled fans
- Control Wi-Fi smart sockets (e.g., Tapo P100)
- Reads control states from MariaDB

## Start the app with Docker
```bash
./start.sh
```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
This project uses third-party libraries under the following licenses:
- python-dotenv (BSD-3-Clause)
- mysql-connector-python (GPL-2.0 with FOSS Exception)
- RPi.GPIO (MIT)
- influxdb-client (MIT)
- python-kasa (Apache-2.0)
- aiohttp (Apache-2.0)
