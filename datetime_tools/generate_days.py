
import calendar
from datetime import datetime, timedelta
from random import choice
from dateutil import rrule, parser
import pandas as pd  # type: ignore
from typing import Generator


def generate_dates(start: datetime, periods: int) -> Generator:
    """Generate dates lazily."""
    for date in pd.date_range(start, periods=periods):
        yield date.strftime("%Y-%m-%d")


def generate_adjacent_dates(date1='1940-05-03', date2='2011-05-10'):
    """Create dates with dateutil."""
    dates = list(rrule.rrule(rrule.DAILY,
                             dtstart=parser.parse(date1),
                             until=parser.parse(date2)))
    return dates


def generate_random_dates(start_year=1940, end_year=2010):
    """Generate all dates for every month,
    considering the actual number of days in each month."""
    dates = []

    # Loop through each year and month
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):  # 1 to 12 for each month
            # Get the number of days in the current month
            num_days = calendar.monthrange(year, month)[1]

            # Generate all dates in the current month
            for day in range(1, num_days + 1):
                # Format the date as "YYYY-MM-DD" or "YYYY/MM/DD"
                date = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
                dates.append(date)
                # Optionally, add the '/' delimiter version as well
                date_slash = f"{year}/{str(month).zfill(2)}/{str(day).zfill(2)}"
                dates.append(date_slash)

    return dates


def date_range(start, end, step=7, date_format="%m-%d-%Y"):
    """
    Creates generator with a range of dates.
    The dates occur every 7th day (default).

    :param start: the start date of the date range
    :param end: the end date of the date range
    :param step: the step size of the dates
    :param date_format: the string format of the dates inputted and returned
    """
    start = datetime.strptime(str(start), date_format)
    end = datetime.strptime(str(end), date_format)
    num_days = (end - start).days

    for d in range(0, num_days + step, step):
        date_i = start + timedelta(days=d)
        if date_i > end:  # Ensure we don't generate a date beyond the end date
            break
        yield date_i.strftime(date_format)


def main():
    # print(generate_adjacent_dates())

    # dates = generate_random_dates()
    # print(dates)

    # Example usage
    for date in date_range("12-01-2024", "12-31-2024", step=7):
        print(date)


if __name__ == "__main__":
    main()
