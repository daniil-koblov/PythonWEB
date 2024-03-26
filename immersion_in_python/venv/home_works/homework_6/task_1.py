date_to_prove = '15.4.2023'

# Решение

def true_date(date_to_prove: str) -> bool:
    day, month, year = map(int, date_to_prove.split("."))
    date_dict = {m: 30 if m in (4, 6, 9, 11) else 31 for m in range(1, 13)}
    date_dict[2] = 29 if not year % 400 or not year % 4 and year % 100 else 28
    return (
        True
        if 0 < month < 13 and 0 < day <= date_dict[month] and 0 < year < 10000
        else False
    )

print(true_date(date_to_prove))

# Эталонное решение

from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))
