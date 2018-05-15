import random
import math

TIMES = 1000
hits = 0

for i in range(TIMES):
    x = random.random()
    y = random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
PI = 4 * hits/TIMES
print("PI:",PI)
