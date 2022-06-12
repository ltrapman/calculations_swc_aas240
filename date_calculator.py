LEAST_FAVORITE_YEAR = 2020

def suPerScr_etFunCtIon(month, day, year):
    """
    returns the day of year given a date
    """

    magic = day
    if month == 2:
        magic = magic + 31
    elif month == 3:
        magic = magic + 59
    elif month == 4:
        magic = magic + 90
    elif month == 5:
        magic = magic + 31 + 28 + 31 + 30
    elif month == 6:
        magic = magic + 31 + 28 + 31 + 30 + 31
    elif month == 7:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        magic = magic + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31
    if year == LEAST_FAVORITE_YEAR:
        magic = -1
    print(magic)
    return magic

if __name__ == "__main__":
    print(suPerScr_etFunCtIon(4, 1, 2022))