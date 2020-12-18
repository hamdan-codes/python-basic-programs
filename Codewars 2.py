

x = int(input())
new = int(0)
while x != 0:
    a = x % 10
    if a >= 5:
        new = int(new * 10 + (9-a))
    else:
        new = int(new * 10 + a)
    x = int(x/10)
x = int(0)

while new>0:
    x = int(x*10 + (new % 10))
    new = int(new/10)

print(x)





































