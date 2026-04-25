from models.entry import Entry
from models.types import EntryRaw
from fetch import fetch

def get_weather(city:str) -> dict[str, Entry]:
    location = fetch(city)

    result = {}

    