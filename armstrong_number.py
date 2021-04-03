a = int(input('enter a number '))
sum = 0
temp = a
while a>0:
    b = a%10
    sum = sum+b**3
    a //= 10
if temp == sum:
    print("number is armstrong number ")
else:
    print('number is not armstrong ')
