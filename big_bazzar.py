a = int(input('enter amount '))
if a>25000:
    print('you are in gold catogery\nyou got 20% discount \ndiscount amount is ',a*20/100 )
    print('payable amount is ',a-(a*0.2))
elif a>10000 and a<=25000:
    print('you are in silver catogery\nyou got 10% discount \ndiscount amount is ', a * 10 / 100)
    print('payable amount is ', a - (a * 0.1))
elif a<=10000:
    print('you are in bronze catogery\nyou got 5% discount \ndiscount amount is ', a * 5 / 100)
    print('payable amount is ', a - (a * 0.05))
