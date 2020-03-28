import sys
import os


def exc_to_sol(exc):
    return_str1 = exc.split()
    number1 = int(return_str1[0])
    number2 = int(return_str1[2])
    if return_str1[1] == "+":
        sol = number1 + number2
    elif return_str1[1] == "-":
        sol = number1 - number2
    elif return_str1[1] == "*":
        sol = number1 * number2
    elif return_str1[1] == "/":
        sol = number1 / number2
    return_str2 = str(number1) + return_str1[1] + str(number2) + "=" + "" + str(sol)
    return return_str2+""


def main():
    FILE_NAME_H = sys.argv[1]
    FILE_NAME_S = sys.argv[2]
    if not os.path.isfile(FILE_NAME_H) and os.path.isfile(FILE_NAME_S):
        print "dictionary do not found"
        exit(1)
    FILE_NAME_S = open(FILE_NAME_S, 'a')
    with open(FILE_NAME_H, 'r') as f:
        for excr in f:
            return_str = exc_to_sol(excr)
            FILE_NAME_S.write(return_str)
    FILE_NAME_S.close()


if __name__ == '__main__':
    main()
