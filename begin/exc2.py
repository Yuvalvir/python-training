if "__main__"==__name__:
    num1=0
    num2=1
    sum=num1+num2
    print(num1)
    while True:
        print (sum)
        num2=num1
        num1=sum
        sum=num1+num2
        if sum>10000:
            break

