import math

def f(x):
    return 4 / (x * x + 1) 

x0 = 0.
x1 = 1.
n = 100000

res = 0.
h = (x1 - x0) / n
for i in range(n + 1):
    if i == 0 or i == n:
        coeff = 1.
    elif i % 2 == 1:
        coeff = 4.
    else:
        coeff = 2.
    res += coeff * f(x0 + i * h)

res *= h / 3


ans = math.pi
diff = abs(ans - res)
print("result: %f" % res)
print("ans: %f" % ans)
print("diff: %f" % diff)