st = input('enter a word ')
st = st[::-1]
print(f'reverse string is {st}')

#with loop
b = input('enter a string ')
for i in range((len(b)-1),-1,-1):
    print(b[i],end='')
