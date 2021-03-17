# find leap year or not
a = int(input('enter a year'))
if a%4 == 0 and a%100 != 0 or  a%400 == 0:
    print('leap year')
else:
    print('not leap year')
