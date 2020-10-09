from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def date_add(dt, **kwargs):
    """Adds period of days to original date.

    Args:
        dt (datetime.date): Original date
        minutes (int): Number of minutes
        hours (int): Number of hours
        days (int): Number of days
        weeks (int): Number of weeks
        months (int): Number of months

    Returns:
        datetime.date: Date with added days.
    """
    dt = dt + relativedelta(**kwargs)
    return dt


def generate_date_range(date_from, date_to):
    """Generates and returns dates list (all in days)
    between date_from and date_to

    Args:
        date_from (datetime.date): Date range start date.
        date_to (datetime.date): Date range end date.

    Returns:
        list: List of dates between date_from and date_to
    """
    date_range = []
    for i in range((date_to - date_from).days + 1):
        date_range.append(date_add(date_from, i))
    return date_range


def generate_date_range_custom(
    date_from, date_to, minutes=0, hours=0, days=0, weeks=0, months=0
):
    """Generates and returns dates list (all in days)
    between date_from and date_to

    Args:
        date_from (datetime): Starting date.
        date_to (datetime): Ending date.
        minutes (int, optional): Minutes of period. Defaults to 0.
        hours (int, optional): Hours of period. Defaults to 0.
        days (int, optional): Days of period. Defaults to 0.
        weeks (int, optional): Weeks of period. Defaults to 0.
        months (int, optional): Months of period. Defaults to 0.

    Returns:
        [type]: [description]
    """
    date_range = []
    dt = date_from
    while dt < date_to:
        dt = date_add(
            dt, minutes=minutes, hours=hours, days=days, weeks=weeks, months=months
        )
        date_range.append(dt)
    return date_range


def date_to_datetime(dt):
    """Converts datetime.date object to datetime.datetime object.

    Args:
        dt (datetime.date): Datetime.date object to use for convertion.

    Returns:
        datetime.datetime: Object converted to datetime.datetime.
    """
    return datetime(dt.year, dt.month, dt.day)


def str_to_datetime(dt, format="%Y-%m-%d"):
    """Convert string to datetime.

    Args:
        dt (str): Date as string
        format (str, optional): Date format inside string. Defaults to "%Y-%m-%d".

    Returns:
        datetime.datetime: Date in datetime format.
    """
    return datetime.strptime(dt, format)


def last_day_of_month(date):
    date = date_add(date, months=1)
    date = date.replace(day=1)
    date = date_add(date, days=-1)
    return date
