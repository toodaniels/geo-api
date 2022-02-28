from fastapi import FastAPI
from geolib import geohash
from pydantic import BaseModel


class UserGeohash(BaseModel): 
    lat: float
    lon: float
    precision: int


class UserLocation(BaseModel):
    geohash: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 18.810750, -98.964284
@app.post("/to/geohash/")
async def convert_geohash(user_geohash: UserGeohash):
    encoded_geohash = geohash.encode(
        user_geohash.lat,
        user_geohash.lon,
        user_geohash.precision)
    return {
        "lat": user_geohash.lat,
        "lon": user_geohash.lon,
        "geohash": encoded_geohash
    }


@app.post("/to/location/")
async def convert_location(user_location: UserLocation):
    decoded_geohash = geohash.decode(user_location.geohash)
    return {
        "geohash": user_location. geohash,
        "lat": decoded_geohash[0],
        "lon": decoded_geohash[1]
    }
