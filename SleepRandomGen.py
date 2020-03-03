import time
from datetime import datetime

def gen(n):

    list1 = []

    for x in range(n):
        dt = datetime.now()
        list1.append(dt.microsecond%10)

        if (dt.microsecond%10 == 0):
            time.sleep(dt.microsecond%10 *0.001 + 0.001)
        else:
            time.sleep(dt.microsecond%10*0.001)

    return list1


print(gen(100))

