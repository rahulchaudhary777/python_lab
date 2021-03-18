n = eval(input('enter he no. of lines '))
ch = 97
for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch +=1
    print()
