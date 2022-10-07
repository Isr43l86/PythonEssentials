def isYearLeap(year):
    bisiesto = False
    if((year % 4 == 0) and not(year % 100 == 0)):
        bisiesto = True
    elif(( year % 100 == 0) and (year % 400 == 0)):
        bisiesto = True
    return bisiesto 


testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")