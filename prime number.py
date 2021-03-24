# prime number or not

a  = int(input('enter a number '))

while a:
    if a%2!=0 and a%1==0:
        print('prime number ')
        break
    else:
        print('not prime number ')
        break
