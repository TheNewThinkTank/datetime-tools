
import calendar
from datetime import datetime as dt
from datetime_tools.generate_days import (
    generate_dates,
    generate_adjacent_dates,
    generate_random_dates,
    date_range
    )  # type: ignore


def test_generate_dates():
    start = dt(2020, 1, 1)
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


def test_generate_adjacent_dates():
    """Test for generating adjacent dates."""
    date1 = '2024-12-01'
    date2 = '2024-12-05'
 
    dates = generate_adjacent_dates(date1, date2)
 
    # Check that the number of dates is correct
    assert len(dates) == 5, f"Expected 5 dates, but got {len(dates)}"
 
    # Check that the dates are consecutive (1-day interval)
    for i in range(1, len(dates)):
        prev_date = dates[i-1]
        curr_date = dates[i]
        assert (curr_date - prev_date).days == 1, f"Dates {dates[i-1]} and {dates[i]} are not adjacent"
 
    # Check that the start date and end date are included
    assert dates[0] == dt.strptime(date1, "%Y-%m-%d"), f"First date should be {date1}, but got {dates[0]}"
    assert dates[-1] == dt.strptime(date2, "%Y-%m-%d"), f"Last date should be {date2}, but got {dates[-1]}"


def test_generate_random_dates():
    """Test for generating random dates."""
    start_year = 2024
    end_year = 2025

    # Call the function to generate random dates
    random_dates = generate_random_dates(start_year=start_year, end_year=end_year)

    # Calculate the expected number of dates
    expected_len = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Get the number of days in the current month
            num_days = calendar.monthrange(year, month)[1]
            expected_len += num_days * 2  # Two formats (YYYY-MM-DD, YYYY/MM/DD)

    # Check that the number of dates is correct
    assert len(random_dates) == expected_len, f"Expected {expected_len} dates, but got {len(random_dates)}"

    # Check that all generated dates are in the correct format
    for date in random_dates:
        assert len(date.split('-')) == 3 or len(date.split('/')) == 3, f"Invalid date format: {date}"

    # Check that the dates are in the expected year range
    for date in random_dates:
        year = int(date.split('-')[0] if '-' in date else date.split('/')[0])
        assert start_year <= year <= end_year, f"Date {date} is outside the expected year range"


def test_date_range():
    """Test for the date_range function."""
    start_date = "12-01-2024"
    end_date = "12-31-2024"
    step = 7
    
    # Generate the dates using the function
    generated_dates = list(date_range(start_date, end_date, step=step))
    
    # Check that the dates generated match the expected format
    for date in generated_dates:
        dt.strptime(date, "%m-%d-%Y")
    
    # Calculate the number of expected dates
    start = dt.strptime(start_date, "%m-%d-%Y")
    end = dt.strptime(end_date, "%m-%d-%Y")
    
    # Calculate the expected number of dates based on the step
    total_days = (end - start).days + 1  # Including the start date
    expected_dates = (total_days + step - 1) // step  # This handles partial steps
    
    msg = f"Expected {expected_dates} dates, but got {len(generated_dates)}"
    assert len(generated_dates) == expected_dates, msg
    
    # Check that the dates are spaced by the correct number of days
    for i in range(1, len(generated_dates)):
        prev_date = dt.strptime(generated_dates[i-1], "%m-%d-%Y")
        curr_date = dt.strptime(generated_dates[i], "%m-%d-%Y")
        msg = f"Dates {generated_dates[i-1]} and {generated_dates[i]} are not {step} days apart"
        assert (curr_date - prev_date).days == step, msg
    
    # Check that the first date is the start date and the last date is the end date or before it
    first_date = dt.strptime(generated_dates[0], "%m-%d-%Y")
    last_date = dt.strptime(generated_dates[-1], "%m-%d-%Y")
    assert first_date == start, f"First date is not {start_date}"
    assert last_date <= end, f"Last date is after {end_date}"
