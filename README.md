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

<img width="903" height="403" alt="image" src="https://github.com/user-attachments/assets/0f531b19-4602-4541-ab4d-42086092f479" />

It returns a json like this:

```json
{
  "id": "softliQ.D/BS00000001",
  "series": "softliQ.D",
  "serial_number": "BS40041620",
  "name": "Mein Gerät",
  "type": 18,
  "has_errors": false,
  "last_service": "2025-03-19",
  "errors": [],
  "salt": [
    {
      "value": 282,
      "date": "2025-12-21"
    },
    {
      "value": 0,
      "date": "2025-12-20"
    },
    {
      "value": 117,
      "date": "2025-12-19"
    }
  ],
  "water": [
    {
      "value": 284,
      "date": "2025-12-21"
    },
    {
      "value": 138,
      "date": "2025-12-20"
    },
    {
      "value": 89,
      "date": "2025-12-19"
    }
  ],
  "nominal_flow": 1.8,
  "raw_water": 23,
  "soft_water": 8,
  "_next_regeneration_raw": "2025-12-23T04:53:00",
  "_startup_raw": "2021-12-10",
  "_hardware_version_raw": "00000004",
  "_mode_raw": 2,
  "_software_version_raw": "0003.0040"
}
```
