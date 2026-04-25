import datetime as dt
from models.types import EntryRaw


class Entry:
    def __init__(self, data:EntryRaw):
        self.start = dt.datetime.fromisoformat(data["StartTime"])
        self.end = dt.datetime.fromisoformat(data["EndTime"])

        for key, value in data.items():
            if key not in ("StartTime", "EndTime"):
                setattr(self, key, value)