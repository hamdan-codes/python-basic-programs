
def seive():
    global a
    for i in range(3,1000000+1,2):
        a[i] = True
    for i in range(3,1000000+1,2):
        if a[i]:
            for j in range(i**2,1000000+1,i):
                a[j] = False

seive()
print(a[1:10])    


### Output : (False True True False True False True False False)
