def date(day, month, year):
    if day * month == year%100:
        return True
    else:
        return False
day = int(input('введите день: '))
month = int(input('введите месяц: '))
year = int(input('введите год: '))

print(date(day, month, year))
