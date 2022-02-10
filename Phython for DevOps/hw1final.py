'''
Task:Create a program that generate folders.
Program name: hw1.py
Input parameters: path, prefix, counts, mode
Example:python hw1.py /home usr 20 551
Result of example run: It creates 20 folders on the path /home with names 
usr1, usr2, etc. and permissions mode 551
'''
import os, sys

pathWhere = sys.argv[1]
prefix = sys.argv[2]
counts = int(sys.argv[3])
mode = int(sys.argv[4])

for i in range(1,counts+1):
    Newfoder = os.path.join(pathWhere, prefix + str(i))
    os.mkdir(Newfoder, mode)

print('Folder is created')
    