if "__main__" == __name__:
    number = input("enter your number please-only number with 5 numbers")
    print(number)
    return_string = ""
    sum_dig = 0

    while number > 0:
        x = number % 10
        number = number / 10
        sum_dig = sum_dig + x
        return_string = return_string + str(x) + ','
    return_string = return_string[-1::-1]
    return_string=return_string[1::]
    print(return_string)
    print "the sum of the digits:", sum_dig
