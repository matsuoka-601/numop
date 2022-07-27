import math
def f(x):
    return math.exp(-x * x)

x0 = 0.
x1 = 100.
n = 100000

ret = 0.
h = (x1 - x0) / n
for i in range(n):
    ret += f(x0 + (i + 0.5) * h)
ret *= h


ans = math.sqrt(math.pi) * 0.5
diff = abs(ans - ret)
print("result: %f" % ret)
print("ans: %f" % ans)
print("diff: %f" % diff)