import datetime as dt
from models.types import EntryRaw
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Entry(ABC):
    start: dt.datetime
    end: dt.datetime

    @classmethod
    def _base_args(cls, data:EntryRaw):
        return {
            "start": data["StartTime"],
            "end": data["EndTime"]
        }
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data:EntryRaw): ...
    

@dataclass
class Temperature(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["Temperature"]
        )
    
@dataclass
class Rain(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["ProbabilityOfPrecipitation"]
        )
    
@dataclass
class Direction(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["WindDirection"]
        )
    
@dataclass
class Speed(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["WindSpeed"]
        )
    
@dataclass
class UV(Entry):
    index: str
    level: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            index=data["UVIndex"],
            level=data["UVExposureLevel"]
        )
    
@dataclass
class Weather(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["Weather"]
        )
    
@dataclass
class Desc(Entry):
    value: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            **cls._base_args(data),
            value=data["WeatherDescription"]
        )
    
@dataclass
class Sun:
    date: str
    rise: str
    tansit_time: str
    transit_alt: str
    set: str

    @classmethod
    def from_dict(cls, data:EntryRaw):
        return cls(
            date=data["Date"],
            rise=data["SunRiseTime"],
            transit_time=data["SunTransitTime"],
            transit_alt=data["SunTransitAlt"],
            set=data["SunSetTime"]
        )