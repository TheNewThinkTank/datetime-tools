
from datetime import datetime
import pandas as pd  # type: ignore
from typing import Generator


def generate_dates(start: datetime, periods: int) -> Generator:
    """Generate dates lazily."""
    for date in pd.date_range(start, periods=periods):
        yield date.strftime("%Y-%m-%d")
