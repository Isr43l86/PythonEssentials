import re

def isYearLeap(year):
    bisiesto = False
    if((year % 4 == 0) and not(year % 100 == 0)):
        bisiesto = True
    elif(( year % 100 == 0) and (year % 400 == 0)):
        bisiesto = True
    return bisiesto 


def daysInMonth(year, month):
    if month > 12 or month < 1 or not isinstance(year, int) or not isinstance(month, int):
        return None

    daysInAMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return daysInAMonth[month-1]


testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print(result,"OK")
    else:
        print(result,"Failed")
