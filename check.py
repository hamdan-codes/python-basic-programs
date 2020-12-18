
'''
from collections import namedtuple
a=namedtuple('Study','Name, Tech')

s=a('Hamdan','Python')
print(s)
'''
'''
from collections import deque
a='Hamdan'
s=deque(a)
print(s)
s.pop()
print(s)
print(s.index('a',2,6))
print(s)
s.appendleft('Ch')
print(s)
'''




'''
from collections import ChainMap
a={1:'Ham',2: 'Hii','Hell':'Heaven'}
b={5:'Hello','lang':'Java'}
s=ChainMap(a,b)
print(s)
'''



'''
import array as ar
a=ar.array('f',[1,2,3,4])

print((a*2))

print("hello")
'''





'''
import os

file=open("Filee.txt",'r')
print(file.readline(3))
print(file.readlines(20))
x = lambda a: a*a
print(x(5))
print((lambda a: a*a)(9))
'''



'''

import time
s=time.ctime(time.time())
print(s)
time.sleep(2)
s=time.ctime(time.time())
print(s[10:19])
print(time.strftime("%d-%m-%Y"))

'''



'''
import numpy as np
import time
a=np.array([(1,2,3),(7,8,9),(5,6,7),(3,4,5)])
print(a)

s=time.time()
print(s)
a=np.arange(1000)
print(a)
s1=time.time()
print(s1)
print(str(s1-s))

s=time.time()
print(s)
a=range(1000)
print(a)
s1=time.time()
print(s1)
print(str(s1-s))
'''


'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,1],[1,2,1,1])
plt.show()
'''






'''
import calendar
cal = calendar.month(2020,7)
print(cal)
print(calendar.isleap(2100))
print(int(calendar.isleap(2100)))
print(calendar.isleap(2020))
print(int(calendar.isleap(2020)))
'''

'''
a = 20
b = 33
for i in range(a):
    print("<a"+str(i+1)+".2019@kiit.ac.in>", end=", ")
for i in range(b):
    print("<b"+str(i+1)+".2019@kiit.ac.in>", end=", ")
for i in range(a):
    print("<a"+str(i+1)+".2018@kiit.ac.in>", end=", ")
for i in range(b):
    print("<b"+str(i+1)+".2018@kiit.ac.in>", end=", ")

'''

























