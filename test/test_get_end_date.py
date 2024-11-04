
from datetime import datetime, timedelta
from datetime_tools.get_end_date import get_end_date


def test_get_end_date():
    start_date = datetime(2023, 11, 4)
    duration = timedelta(days=10)
    end_date = get_end_date(start_date, duration)

    assert end_date == datetime(2023, 11, 14).date()
