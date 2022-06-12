def day_of_year(month, day, year):
    """
    returns the day of year given a date
    """

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_num = day + sum(days_in_month[0:month-1])
    if year % 4 == 0 and month>2: #leap year
        day_num +=1

    return day_num

if __name__ == "__main__":
    print(day_of_year(4, 1, 2022))