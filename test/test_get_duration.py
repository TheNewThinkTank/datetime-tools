
from datetime_tools.get_duration import get_duration_minutes


def test_get_year_and_week():

    assert (
        get_duration_minutes("14:45", "15:10") == 25
    )
