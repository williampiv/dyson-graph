import configparser as c
import dysonsensors as ds
import dysoninfluxdb as di

def main() -> None:
    dyson_devices = c.ConfigParser()
    dyson_devices.read('devices.ini')
    influxdb_config = c.ConfigParser()
    influxdb_config.read('influxdb.ini')
    print(dyson_devices.sections())
    for section in dyson_devices.sections():
        readings = ds.get_dyson_readings(dyson_devices[section]['ip_address'], dyson_devices[section]['username'], dyson_devices[section]['password'])
        influxdb_readings = di.dyson_readings_to_influxdb_points(readings['humidity'], readings['temperature'], section)
        print(influxdb_readings)
        di.post_points_to_influxdb(influxdb_readings, influxdb_config['influxdb']['address'], influxdb_config['influxdb']['username'], influxdb_config['influxdb']['password'], influxdb_config['influxdb']['database'])


if __name__ == "__main__":
    main()
