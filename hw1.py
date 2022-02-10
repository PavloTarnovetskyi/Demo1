import os, sys

path = sys.argv[1]
prefix = sys.argv[2]
counts = int(sys.argv[3])
mode = int("0o"+sys.argv[4], 10)

for i in range(1,counts+1):
    Newfoder = os.path.join(path, prefix + str(i))
    os.mkdir(Newfoder, mode)
print('Folder is created')