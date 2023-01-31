from csv import list_dialects
from re import A
from collections import Counter
import sys
sys.stdin = open("./nn.txt","r")

n = int(input())
numli = []
for i in range(n):
    numli.append(list(map(int,input().split())))
# numli.sort()
s = sorted(numli)
for item in s:
    print(item)
 

# import sys
# input=sys.stdin.readline
# n = int(input())
# numli = []
# for i in range(n):
#     numli.append(list(map(int,input().split())))
# # numli.sort()
# s = sorted(numli)
# t=[]
# for item in s:
#     t.append(str(item[0])+' '+str(item[1]))
# print(*t,sep='\n')