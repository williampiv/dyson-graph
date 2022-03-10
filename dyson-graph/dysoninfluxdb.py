from influxdb import InfluxDBClient


def dyson_readings_to_influxdb_points(
    humidity: int, temperature: float, location: str
) -> list:
    formatted_list = [
        {
            "measurement": "humidity",
            "tags": {"location": location},
            "fields": {"value": humidity},
        },
        {
            "measurement": "temperature",
            "tags": {"location": location},
            "fields": {"value": temperature},
        },
    ]
    return formatted_list


def post_points_to_influxdb(
    points_to_post: list,
    influxdb_address: str,
    influxdb_user: str,
    influxdb_pass: str,
    influxdb_db: str,
    influxdb_port: int = 8086,
    influxdb_ssl: bool = True,
) -> bool:
    influx_client = InfluxDBClient(
        influxdb_address,
        influxdb_port,
        influxdb_user,
        influxdb_pass,
        influxdb_db,
        influxdb_ssl,
    )
    try:
        influx_client.write_points(points_to_post)
    except Exception:
        return False
    return True
