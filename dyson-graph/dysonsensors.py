import libdyson as ld


def kelvin_to_fahrenheit(kelvin_temp: float) -> float:
    return round((kelvin_temp - 273.15) * (9 / 5) + 32, 2)


def get_dyson_readings(dyson_ip: str, dyson_username: str, dyson_password: str) -> dict:
    device = ld.get_device(
        dyson_username, dyson_password, ld.DEVICE_TYPE_PURE_COOL_LINK
    )
    device.connect(dyson_ip)
    readings = {}
    readings["temperature"] = kelvin_to_fahrenheit(device.temperature)
    readings["humidity"] = device.humidity
    device.disconnect()
    return readings
