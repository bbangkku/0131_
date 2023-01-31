import sys
sys.stdin = open("./nn.txt","r")

n = int(input())
for i in range(n):
    a = 'YES'
    answer = []
    k = list(map(str,input()))
    
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
    
