n = eval(input('enter he no. of lines '))

for i in range(1,n+1):
    ch = 65
    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch +=1
    print()
