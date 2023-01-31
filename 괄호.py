import sys

n = int(input())
a = 'YES'
for i in range(n):
    k = list(map(str,input()))
    answer = []
    for j in range(len(k)):
        if k[j] == '(':
            answer.append('(')
        elif k[j] == ')':
            if not answer:
                a = 'NO'
                break
            answer.pop()
    if a == 'NO':
        print('NO')
    elif answer:
        print('NO')
    else:
        print('YES')


    


# for i in range(len(input())))
# while True:
    
