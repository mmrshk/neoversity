from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Returns a list of colleagues to congratulate on their birthday within the next 7 days (including today).
    If a birthday falls on a weekend, the congratulation date is moved to the following Monday.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            name = user["name"]
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, ValueError):
            continue

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            weekday = congratulation_date.weekday()
            if weekday == 5:
                congratulation_date += timedelta(days=2)
            elif weekday == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.8"},
        {"name": "Jane Smith", "birthday": "1990.02.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
