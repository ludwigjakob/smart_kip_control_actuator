import asyncio
from kasa import Discover

async def main():
    dev = await Discover.discover_single(
        "192.168.1.100",
        username="ludwig.jakob91@googlemail.com",
        password="K1Pwohnwagen"
    )
    await dev.update()
    print("Status vor Aktion:", dev.is_on)

    # Einschalten
    await dev.turn_on()
    await dev.update()
    print("Status nach Einschalten:", dev.is_on)

    # Ausschalten
    await dev.turn_off()
    await dev.update()
    print("Status nach Ausschalten:", dev.is_on)

    await dev.close()   # Session schließen


if __name__ == "__main__":
    asyncio.run(main())