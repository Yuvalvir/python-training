# coding=utf-8
FILE_NAME1 = r'C:\Python27\Yuval.txt'
FILE_NAME2 = r'C:\Python27\Virnizki.txt'
FILE_NAME1 = open( r'C:\Python27\Yuval.txt', 'a')
with open(FILE_NAME2, 'r') as file_txt:
    for cop in file_txt:
        FILE_NAME1.write(cop)
FILE_NAME1.close()
