
from datetime_tools.bisect_year import bisect_year  # type: ignore


def test_bisect_year():
    assert bisect_year(1) == ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
