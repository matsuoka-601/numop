import math
def f(x):
    return math.exp(-x * x)

x0 = 0.
x1 = 100.
n = 100000

ret = 0.
h = (x1 - x0) / n
for i in range(n + 1):
    if (i == 0 or i == n):
        coeff = 1.
    else:
        coeff = 2.
    ret += coeff * f(x0 + i * h)
ret *= 0.5 * h


ans = math.sqrt(math.pi) * 0.5
diff = abs(ans - ret)
print("result: %f" % ret)
print("ans: %f" % ans)
print("diff: %f" % diff)