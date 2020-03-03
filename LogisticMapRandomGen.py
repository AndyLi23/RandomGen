from matplotlib import pyplot
import time



def genRandom0To9(x, r, timeMS):
    startTime = time.time()

    while time.time() - startTime < timeMS:
        x = x * r * (1 - x)

    return int(10 * (x - 0.21206445593529658) * (1 / (0.9398583951345673 - 0.21206445593529658)))


def gen(n):
    ans = []

    for i in range(n):
        x = 0.4
        r = 3.757

        ans.append(genRandom0To9(x, r, 0.01))

    return ans

print(gen(100))
