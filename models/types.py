from typing import TypedDict, NotRequired

class EntryRaw(TypedDict):

    #頭尾時間
    StartTime: str
    EndTime: str

    #溫度
    Temperature: NotRequired[str]

    #降雨機率
    ProbabilityOfPrecipitation: NotRequired[str]

    #風向
    WindDirection: NotRequired[str]

    #風速
    WindSpeed: NotRequired[str]

    #紫外線
    UVIndex: NotRequired[str]
    UVExposureLevel: NotRequired[str]

    #天氣現象
    Weather: NotRequired[str]

    #綜合描述
    WeatherDescription: NotRequired[str]

    #日出日落
    Date: NotRequired[str]
    BeginCivilTwilightTime: NotRequired[str]
    SunRiseTime: NotRequired[str]
    SunRiseAZ: NotRequired[str]
    SunTransitTime: NotRequired[str]
    SunTransitAlt: NotRequired[str]
    SunSetTime: NotRequired[str]
    SunSetAZ: NotRequired[str]
    EndCivilTwilightTime: NotRequired[str]


TimeRaw =  list[EntryRaw]

class ElementRaw(TypedDict):
    ElementName: str
    Time: TimeRaw

class LocationRaw(TypedDict):
    LocationName: str
    
    #溫度
    Temperature: ElementRaw

    #降雨機率
    ProbabilityOfPrecipitation: ElementRaw

    #風向
    WindDirection: ElementRaw

    #風速
    WindSpeed: ElementRaw

    #紫外線
    UVIndex: ElementRaw

    #天氣現象
    Weather: ElementRaw

    #綜合描述
    WeatherDescription: ElementRaw