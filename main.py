from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from pygruenbeck_cloud import PyGruenbeckCloud

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

@app.get("/devices/{device_id}")
async def get(device_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
   api = PyGruenbeckCloud(credentials.username, credentials.password)
   is_logged_in = await api.login()
   if(is_logged_in):
      device_found = await api.set_device_from_id("softliQ.D/"+device_id)
      if(device_found):
         infos = await api.get_device_infos()
         data = get_data_dict(infos)
         api.disconnect()
         return data
      else:
         raise Exception("Device not found")
   else:
      raise Exception("Unable to connect")

@app.get("/devices/{device_id}/water")
async def get(device_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
   api = PyGruenbeckCloud(credentials.username, credentials.password)
   is_logged_in = await api.login()
   if(is_logged_in):
      device_found = await api.set_device_from_id("softliQ.D/"+device_id)
      if(device_found):
         infos = await api.get_device_water_measurements()
         api.disconnect()
         return infos.water
      else:
         raise Exception("Device not found")
   else:
      raise Exception("Unable to connect")

@app.get("/devices/{device_id}/water/last")
async def get(device_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
   api = PyGruenbeckCloud(credentials.username, credentials.password)
   is_logged_in = await api.login()
   if(is_logged_in):
      device_found = await api.set_device_from_id("softliQ.D/"+device_id)
      if(device_found):
         infos = await api.get_device_infos()
         api.disconnect()
         return infos.water[0].value
      else:
         raise Exception("Device not found")
   else:
      raise Exception("Unable to connect")

@app.get("/devices/{device_id}/salt")
async def get(device_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
   api = PyGruenbeckCloud(credentials.username, credentials.password)
   is_logged_in = await api.login()
   if(is_logged_in):
      device_found = await api.set_device_from_id("softliQ.D/"+device_id)
      if(device_found):
         infos = await api.get_device_salt_measurements()
         api.disconnect()
         return infos.salt
      else:
         raise Exception("Device not found")
   else:
      raise Exception("Unable to connect")

@app.get("/devices/{device_id}/salt/last")
async def get(device_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
   api = PyGruenbeckCloud(credentials.username, credentials.password)
   is_logged_in = await api.login()
   if(is_logged_in):
      device_found = await api.set_device_from_id("softliQ.D/"+device_id)
      if(device_found):
         infos = await api.get_device_infos()
         api.disconnect()
         return infos.salt[0].value
      else:
         raise Exception("Device not found")
   else:
      raise Exception("Unable to connect")



def get_data_dict(infos):
   data = {}
   data["id"] = infos.id
   data["series"] = infos.series
   data["serial_number"] = infos.serial_number
   data["name"] = infos.name
   data["type"] = infos.type
   data["has_errors"] = infos.has_error
   data["last_service"] = infos.last_service
   data["errors"] = infos.errors
   data["salt"] = infos.salt
   data["water"] = infos.water
   data["nominal_flow"] = infos.nominal_flow
   data["raw_water"] = infos.raw_water
   data["soft_water"] = infos.soft_water
   data["next_regeneration"] = infos._next_regeneration_raw
   data["startup"] = infos._startup_raw
   data["hardware_version"] = infos._hardware_version_raw
   data["mode"] = infos._mode_raw
   data["software_version"] = infos._software_version_raw
   data["time_zone_offset"] = infos.time_zone.utcoffset(None)
   return data

