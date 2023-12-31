from datetime import datetime, timedelta, tzinfo

class _UTC(tzinfo):
    def dst(self, dt: datetime | None) -> timedelta: ...
    def utcoffset(self, dt: datetime | None) -> timedelta: ...
    def tzname(self, dt: datetime | None) -> str: ...

UTC: _UTC

def timedelta_to_seconds(td: timedelta) -> int: ...

day: timedelta
week: timedelta
hour: timedelta
minute: timedelta
second: timedelta
month: timedelta
year: timedelta

def parse_date(value: str | bytes) -> datetime | None: ...
def serialize_date(dt) -> str: ...
def parse_date_delta(value: str | bytes) -> datetime | None: ...
def serialize_date_delta(value) -> str: ...
