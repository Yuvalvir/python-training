if "__main__"==__name__:

    return_str = raw_input("enter the string")
    if 'a' in return_str:
        return_str = return_str.replace("a", "aba")
    if 'e' in return_str:
        return_str = return_str.replace("e", "ebe")
    if 'i' in return_str:
        return_str = return_str.replace("i", "ibi")
    if 'o' in return_str:
        return_str = return_str.replace("o", "obo")
    if 'u' in return_str:
        return_str = return_str.replace("u", "ubu")
    print(return_str)

