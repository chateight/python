from telnetlib import NOP
import time
import math

start = time.time()
set = list()

flag = False
sqt = 0;
for i in range(2, 1000000):        # check prime numbers
    flag = False;
    sqt = math.sqrt(i)
    for j in range(2, int(sqt)):
        if i%j == 0:
            flag = True
            break
    if flag != True:
        set.append(i)


end = time.time()
print('{:.0f}'.format((end-start)*1000)+ " ms")
print("number of prime numbers(up to 1M) : ",len(set))
