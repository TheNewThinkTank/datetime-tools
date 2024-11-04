
from datetime import datetime, timedelta


def get_end_date(start_date: datetime, duration: timedelta):
    # Ensure start_date is a datetime or date object
    if not isinstance(start_date, datetime):
        raise TypeError("start_date must be a datetime or date object")

    # Ensure duration is a timedelta object
    if not isinstance(duration, timedelta):
        raise TypeError("duration must be a timedelta object")

    # Calculate the end date
    end_date = start_date + duration
    return end_date.date()
