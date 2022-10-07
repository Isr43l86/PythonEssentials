daysInAMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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
    if isYearLeap(year) and month == 2:
        return 29
    return daysInAMonth[month-1]
 
def dayOfYear(year, month, day):
    reultF2 = daysInMonth(year, month)
    if reultF2 == None:
        return None
    if day < 1 or day > reultF2:
        return None
    if isYearLeap(year):
        daysInAMonth[1] = 29
        return sum(daysInAMonth)
    else:
        return sum(daysInAMonth)
 

print(dayOfYear(2000, 12, 31))