# Two sets

n = int(input())
x = [x for x in range(1, n+1)]
sumx = sum(x)

set1 = []
set2 = []

if sumx % 2 == 1:
    print('NO')
else:
    print('YES')
    divisor = sumx/2
    for i in range(0, n):
        if (sum(set1) < divisor):
            set1.append(x[-(i+1)])
        if (sum(set1) < divisor):
            set1.append(x[-i])
    print(len(set1))
    for i in set1:
        print(i, end = ' ')
            
    for i in x:
        if i not in set1:
            set2.append(i)
    print()
    print(len(set2))
    for i in set2:
        print(i, end = ' ')
    