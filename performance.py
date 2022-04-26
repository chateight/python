import time
import math

start = time.time()
set = list()

flag = False
sqt = 0;
num = 1000000

for i in range(2, num + 1):        # check prime numbers
    flag = False;
    sqt = math.sqrt(i)
    for j in range(2, int(sqt) + 1):
        if i%j == 0:
            flag = True
            break
    if flag != True:
        set.append(i)


end = time.time()
print("elapsed time : ",'{:.0f}'.format((end-start)*1000)+ " ms")
print("number of prime numbers(up to 1M) : ",len(set))
print("")
print("last five prime numbers")
for i in range(5):
    print(set[-5 + i])
