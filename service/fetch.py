import requests
from dotenv import load_dotenv
import os
from models.types import LocationRaw
load_dotenv()

# Query

url = "https://opendata.cwa.gov.tw/linked/graphql"

query = """
query forecast($city: String!, $today: String!) {
    forecast(LocationName: $city) {
        Locations {
            LocationName,
            
            Temperature {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    Temperature
                }
            },

            ProbabilityOfPrecipitation {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    ProbabilityOfPrecipitation
                }
            },

            WindDirection {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    WindDirection
                }
            },

            WindSpeed {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    WindSpeed
                }
            },

            UVIndex {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    UVIndex,
                    UVExposureLevel
                }
            },

            Weather {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    Weather
                }
            },

            WeatherDescription {
                ElementName,
                Time (first: 2) {
                    StartTime,
                    EndTime,
                    WeatherDescription
                }
            },

            sunRise (timeTo: $today) {
                Date,
                BeginCivilTwilightTime
                SunRiseTime,
                SunRiseAZ,
                SunTransitTime,
                SunTransitAlt,
                SunSetTime,
                SunSetAZ,
                EndCivilTwilightTime
            }
        }
    }
}
"""

params = {
    "Authorization": os.environ["WEATHER"]
}

# Main Function

def fetch(city:str) -> LocationRaw:

    json_data = {
        "query": query,
        "variables": {
            "city": city
        }
    }

    resp = requests.post(
        url,
        params=params,
        json=json_data,
        verify=False
    )

    return resp.json()["data"]["forecast"]["Locations"][0]