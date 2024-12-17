"""
_summary_
"""

import datetime
from datetime import datetime as dt


def get_duration_minutes(start_time, end_time):
    """calculates the duration in minutes between two times on the same day.

    :param start_time: _description_
    :type start_time: _type_
    :param end_time: _description_
    :type end_time: _type_
    :return: _description_
    :rtype: _type_
    """

    start_time_object = dt.strptime(start_time, "%H:%M")
    end_time_object = dt.strptime(end_time, "%H:%M")

    duration = end_time_object - start_time_object
    duration_minutes = round(duration / datetime.timedelta(minutes=1))

    return duration_minutes


def get_months_difference(past_date_str, date_format="%Y-%m-%d"):
    """
    Calculate the number of whole months between a given date in the past and today's date.

    :param past_date_str: The past date as a string.
    :type past_date_str: str
    :param date_format: The format of the past date string (default is "%Y-%m-%d").
    :type date_format: str
    :return: The number of months passed.
    :rtype: int
    """
    # Parse the input date string
    past_date = dt.strptime(past_date_str, date_format)
    today = dt.today()

    # Calculate the difference in years and months
    year_diff = today.year - past_date.year
    month_diff = today.month - past_date.month

    # Total months difference
    total_months = year_diff * 12 + month_diff

    return total_months


if __name__ == "__main__":
    # Example usage
    past_date = "2020-02-01"
    months_passed = get_months_difference(past_date)
    print(f"Months passed since {past_date}: {months_passed}")
