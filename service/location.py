from dataclasses import dataclass
from models.entries import *
from models.types import LocationRaw

@dataclass
class TimeSlot:
    temperature: Temperature
    rain: Rain
    direction: Direction
    speed: Speed
    uv: UV
    weather: Weather
    desc: Desc
    sun: Sun

@dataclass
class Location:
    name: str
    now: TimeSlot
    future: TimeSlot

    @classmethod
    def from_dict(cls, data: LocationRaw):
        def make_slot(index: int) -> TimeSlot:
            return TimeSlot(
                temperature = Temperature.from_dict(data["Temperature"]["Time"][index]),
                rain        = Rain.from_dict(data["ProbabilityOfPrecipitation"]["Time"][index]),
                direction   = Direction.from_dict(data["WindDirection"]["Time"][index]),
                speed       = Speed.from_dict(data["WindSpeed"]["Time"][index]),
                uv          = UV.from_dict(data["UVIndex"]["Time"][index]),
                weather     = Weather.from_dict(data["Weather"]["Time"][index]),
                desc        = Desc.from_dict(data["WeatherDescription"]["Time"][index]),
                sun         = Sun.from_dict(data["sunRise"][index]),
            )

        return cls(
            name   = data["LocationName"],
            now    = make_slot(0),
            future = make_slot(1),
        )