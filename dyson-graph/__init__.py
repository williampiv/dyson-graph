import configparser as c
import dysonsensors as ds

def main() -> None:
    dyson_devices = c.ConfigParser()
    dyson_devices.read('devices.ini')
    print(dyson_devices.sections())
    for section in dyson_devices.sections():
        readings = ds.get_dyson_readings(dyson_devices[section]['ip_address'], dyson_devices[section]['username'], dyson_devices[section]['password'])
        print(readings)


if __name__ == "__main__":
    main()
