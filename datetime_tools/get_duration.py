"""
_summary_
"""

import datetime
from datetime import datetime as dt


def get_duration_minutes(start_time, end_time):
    """_summary_

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
