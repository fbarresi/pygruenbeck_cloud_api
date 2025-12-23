# pygruenbeck_cloud_api
simple api for gruenbeck cloud devices (softliQ.D)

[![Docker Image CI](https://github.com/fbarresi/pygruenbeck_cloud_api/actions/workflows/docker-image.yml/badge.svg)](https://github.com/fbarresi/pygruenbeck_cloud_api/actions/workflows/docker-image.yml) [![Docker Pulls](https://img.shields.io/docker/pulls/fbarresi/pygruenbeck-cloud-api.svg)](https://hub.docker.com/r/fbarresi/pygruenbeck-cloud-api/)

This project offers a very simple API based on [pygruenbeck_cloud](https://github.com/p0l0/pygruenbeck_cloud).

It is very easy and don't have the same wide range of feature of pygruenbeck_cloud, but it is useful to integrate other system over a REST-Api.

**Disclaimer**: this API is stateless and dispose the client after each call. <br/>
If you need real-time data or reuse of the inner client please go for [pygruenbeck_cloud](https://github.com/p0l0/pygruenbeck_cloud) or its wonderful Home Assistant integration instead.

## Usage

### Use it from source

requires python `3.12+`

```
pip install -r requirements.txt
fastapi run main.py --port 8000
```
then visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Use it from Docker

```
docker run -p 80:80 --name pygruenbeck_cloud_api fbarresi/pygruenbeck-cloud-api:1.8
```

## Documentation

Once started the documentation is available under `/docs`:

Use your device SN as device id and your GruenbeckCloud credentials to authenticate.

<img width="869" height="543" alt="image" src="https://github.com/user-attachments/assets/f36ceb67-2dc1-4f52-802d-e68565be231d" />


It returns a json like this:

```json
{
  "id": "softliQ.D/BS0000001",
  "series": "softliQ.D",
  "serial_number": "BS0000001",
  "name": "Mein Gerät",
  "type": 18,
  "has_errors": false,
  "last_service": "2025-03-19",
  "errors": [],
  "salt": [
    {
      "value": 0,
      "date": "2025-12-22"
    },
    {
      "value": 282,
      "date": "2025-12-21"
    },
    {
      "value": 0,
      "date": "2025-12-20"
    }
  ],
  "water": [
    {
      "value": 182,
      "date": "2025-12-22"
    },
    {
      "value": 284,
      "date": "2025-12-21"
    },
    {
      "value": 138,
      "date": "2025-12-20"
    }
  ],
  "nominal_flow": 1.8,
  "raw_water": 23,
  "soft_water": 8,
  "next_regeneration": "2025-12-24T04:23:00",
  "_startup_raw": "2021-12-10",
  "hardware_version": "00000004",
  "mode": 2,
  "software_version": "0003.0040",
  "time_zone_offset": 3600
}
```
