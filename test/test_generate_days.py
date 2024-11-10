
from datetime import datetime
from datetime_tools.generate_days import generate_dates


def test_generate_dates():
    start = datetime(2020, 1, 1)
    periods = 5
    expected_dates = [
        "2020-01-01",
        "2020-01-02",
        "2020-01-03",
        "2020-01-04",
        "2020-01-05",
        ]

    generated_dates = list(generate_dates(start, periods))

    assert generated_dates == expected_dates, "The dates generated do not match the expected dates."
