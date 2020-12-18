'''n=int(input())
ar=[]
for i in  range(n):
    c=i+1
    '''


def countSetBits(n):
    n += 1
    powerOf2 = 2
    cnt = n // 2
    while (powerOf2 <= n):
        totalPairs = n // powerOf2;
        cnt += (totalPairs // 2) * powerOf2
        if (totalPairs & 1):
            cnt += (n % powerOf2)
        else:
            cnt += 0
        powerOf2 <<= 1
        print(str(cnt))
    return cnt

n = int(input())
print(countSetBits(n))
