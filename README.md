# Dyson Graph

This project aims to pull data via mqtt from local Dyson Pure Cool Link devices and push that data to InfluxDB for graphic purposes.

Could definitely be extended for other Dyson devices (since we're using LibDyson)


## Examples
Examples contains Kubernetes (k8s) examples of how to deploy the related container as a CronJob, and read from secrets to fill in the ini files containing sensitive info.

## Grafana
Here is an example of this data graphed from InfluxDB into Grafana:

![Grafana screenshot](pics/grafana.png)
