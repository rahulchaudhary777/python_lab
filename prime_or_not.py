a = int(input('enter a number '))

for i in range(2,a):
    if a%i==0:
        print("number is not prime")
        break
    else:
        print('number is prime')
        break

# without loop

a = int(input('enter a number '))

if a%1==0 and a%2!=0:
    print("number is prime ")
else:
    print('number is not prime ')


