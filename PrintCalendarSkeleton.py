# A stub for printMonth may look like this 
def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)


# A stub for printMonthTitle may look like this 
def printMonthTitle(year, month):
    print("              ", getMonthName(month), year)
    print("--------------------------------------------")
    print("   Sun  Mon  Tue  Wed  Thu  Fri  Sat")


# DONE - stub for getMonthBody may look like this
def printMonthBody(year, month):
    start = getStartDay(year, month)
    days = getNumberOfDaysInMonth(year, month)
    for i in range(start):
        print("            ", end="")

    for i in range(1, days + 1):
        print(format(i, '5d'), end="")
        if (i + start) % 7 == 0:
            print()



# DONE - stub for getMonthName may look like this
def getMonthName(month):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", \
                   "October", "November", "December"]
    return month_names[month - 1]


# DONE - stub for getStartDay may look like this
def getStartDay(year, month):
    START = 3  # 0.1 JAN 1800 WAS WEDNESDAY
    total_number_of_days = getTotalNumberOfDays(year, month) + START
    return total_number_of_days % 7


# DONE - stub for getTotalNumberOfDays may look like this
def getTotalNumberOfDays(year, month):
    total_days = 0
    for y in range(1800, year):
        if isLeapYear(y):
            total_days += 366
        else:
            total_days += 365
    for m in range(1, month):
        total_days = total_days + getNumberOfDaysInMonth(year, m)

    return total_days


# DONE - stub for getNumberOfDaysInMonth may look like this
def getNumberOfDaysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 0  # just in case entered year is weird


# DONE - A stub for isLeapYear may look like this
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():  # Prompt the user to enter year and month
    year = int(input("Enter full year (e.g., 2001): "))
    month = int(input(("Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    printMonth(year, month)


main()
