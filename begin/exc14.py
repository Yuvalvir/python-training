import sys
print ("this is the name of this file:" + sys.argv[0])
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    for line in f:
        print(line)
