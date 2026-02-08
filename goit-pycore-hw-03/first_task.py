from datetime import datetime, date


def get_days_from_today(input_date):
    """
    Calculates the number of days between the given date and today.

    Parameters:
        input_date (str): Date in format 'YYYY-MM-DD' (e.g. '2020-10-09').

    Returns:
        int: Number of days from the given date to today.
             Negative if the given date is later than today.
             None if the input format is invalid.
    """
    try:
        parsed_date = datetime.strptime(input_date, "%Y-%m-%d").date()
        today = date.today()

        return (today - parsed_date).days
    except ValueError:
        return None


if __name__ == "__main__":
    print(get_days_from_today('2021-10-09'))
