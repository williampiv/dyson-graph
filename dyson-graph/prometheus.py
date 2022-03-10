from prometheus_client import CollectorRegistry, Counter, push_to_gateway
from typing import Dict


def generate_push_metrics(pushgateway_ip: str, job: str, metrics: Dict, location: str) -> bool:
    reg = CollectorRegistry()
    for key in metrics.keys():
        c = Counter(key, "", registry=reg, labelnames=["location", "collection"])
        c.labels(location, "dyson-graph").inc(metrics[key])
    try:
        push_to_gateway(pushgateway_ip, job, reg)
    except Exception as e:
        print(e)
        return False
    return True
