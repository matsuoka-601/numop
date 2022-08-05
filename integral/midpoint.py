import math
def f(x):
    return math.exp(-x * x)

x0 = 0.     
x1 = 100.
n = 100000

res = 0.
h = (x1 - x0) / n
for i in range(n):
    res += f(x0 + (i + 0.5) * h)
res *= h


ans = math.sqrt(math.pi) * 0.5
diff = abs(ans - res)
print("result: %f" % res)
print("ans: %f" % ans)
print("diff: %f" % diff)