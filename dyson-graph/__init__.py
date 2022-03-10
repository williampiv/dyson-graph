import configparser as c
import sys

import dysonsensors as ds
import dysoninfluxdb as di
import prometheus as prom
import argparse


def main() -> None:
    # read in the parser items
    parser = argparse.ArgumentParser(description="Graph some dysons")
    parser.add_argument("-i", "--influxdb", action="store_true", help="Send metrics to InfluxDB")
    parser.add_argument("-p", "--prom", choices=["push", "export"],
                        help="Provide metrics for Prometheus, either push gateway or exporter")
    parser.add_argument("-pi", help="prometheus pushgateway ip (for use with -p push)")
    args = parser.parse_args()

    # read dyson device readings
    dyson_devices = c.ConfigParser()
    dyson_devices.read("devices.ini")

    for section in dyson_devices.sections():
        readings = ds.get_dyson_readings(
            dyson_devices[section]["ip_address"],
            dyson_devices[section]["username"],
            dyson_devices[section]["password"],
        )

        # send metrics to influx if influx specified
        if args.influxdb:
            influxdb_config = c.ConfigParser()
            influxdb_config.read("influxdb.ini")
            influxdb_readings = di.dyson_readings_to_influxdb_points(
                readings["humidity"], readings["temperature"], section
            )
            print(influxdb_readings)
            di.post_points_to_influxdb(
                influxdb_readings,
                influxdb_config["influxdb"]["address"],
                influxdb_config["influxdb"]["username"],
                influxdb_config["influxdb"]["password"],
                influxdb_config["influxdb"]["database"],
            )
            sys.exit(0)
        # send metrics to prometheus if specified
        # TODO: build out exporter functionality instead of just push gateway
        elif args.prom:
            # TODO: allow taking in arguments via either env or config like influxdb
            if args.prom == "push":
                if not args.pi:
                    print("please provide an IP for push gateway")
                    sys.exit(1)
                else:
                    ret = prom.generate_push_metrics(
                        args.pi, "dyson-graph", readings, section
                    )
                    if not ret:
                        print("failed to push")
                        sys.exit(1)
                    sys.exit(0)


if __name__ == "__main__":
    main()
