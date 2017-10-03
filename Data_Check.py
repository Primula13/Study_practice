"""Написать функцию check_my_date, принимающую число месяц и год.
Вернуть True, если такая дата существует и False иначе."""
import calendar


def check_my_date(day, month, year):

    if day <= 0 or month <= 0 or year <= 0:
        return False
    else:
        if month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
            return True
        elif month in (4, 6, 9, 11) and day <= 30:
            return True
        elif month == 2:
            if calendar.isleap(year) is True and day <= 29:
                return True
            elif day <= 28:
                return True
            else:
                return False
        else:
            return False
