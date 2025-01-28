import asyncio
from bleak import BleakClient

# Replace this with your Mi Band's MAC address
mac_address = "EB:D4:7A:64:96:86"  # Example MAC address

# The authentication key you provided
auth_key = bytes.fromhex("5063012572f7aa75de57cd439abab47a")

async def run():
    async with BleakClient(mac_address) as client:
        print(f"Connected: {client.is_connected}")

        # You can now communicate with the Mi Band.
        # Example: Read the battery level (GATT characteristic UUID: 00002a19-0000-1000-8000-00805f9b34fb)
        battery_level = await client.read_gatt_char("00002a19-0000-1000-8000-00805f9b34fb")
        print(f"Battery Level: {battery_level[0]}%")

        # You can explore other characteristics for sleep, heart rate, etc.
        # Example: Read sleep data (if available)
        sleep_data = await client.read_gatt_char("00000016-0000-3512-2118-0009af100700")
        print(sleep_data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
