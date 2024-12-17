
import pytest
from datetime_tools.get_duration import (
    get_duration_minutes,
    get_months_difference
    ) # type: ignore


def test_get_year_and_week():

    assert get_duration_minutes("14:45", "15:10") == 25


def test_same_month():
    """Test when the start and end date are in the same month."""
    past_date = "2024-12-01"
    months_passed = get_months_difference(past_date)
    assert months_passed == 0, f"Expected 0 months, but got {months_passed}"


def test_one_month_difference():
    """Test when the start and end date are exactly one month apart."""
    past_date = "2024-11-01"
    months_passed = get_months_difference(past_date)
    assert months_passed == 1, f"Expected 1 month, but got {months_passed}"


def test_multiple_months_difference():
    """Test when the start and end date are several months apart."""
    past_date = "2024-06-01"
    months_passed = get_months_difference(past_date)
    assert months_passed == 6, f"Expected 6 months, but got {months_passed}"


def test_cross_year():
    """Test when the start and end date span across different years."""
    past_date = "2023-12-15"
    months_passed = get_months_difference(past_date)
    assert months_passed == 12, f"Expected 12 months, but got {months_passed}"


def test_edge_case_end_of_month():
    """Test when the start date is at the end of the month and the end date is in the next month."""
    past_date = "2023-12-31"
    months_passed = get_months_difference(past_date)
    assert months_passed == 12, f"Expected 12 months, but got {months_passed}"


def test_invalid_date_format():
    """Test when an invalid date format is provided."""
    with pytest.raises(ValueError):
        get_months_difference("12-31-2023", date_format="%d-%m-%Y")
