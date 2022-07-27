import sys
sys.path.append('..')
from utils import *
from eigenvalue_test import eigenvalue_test

A = [[1., 3., 3., 1.], [3., 2., 0., 2], [3., 0., 3., 1.], [1., 2., 1., 1.]]
n = len(A)
x = init_rand_vec(n)
x = normalize_vec(x)


MAX_ITER = 20
eps = 1e-10

pre_val = 1e18

# x_k: y_{k - 1} / || y_{k - 1} ||
# y_k: A x_k
for iter in range(MAX_ITER):
    y = matvec_mul(A, x)
    x = normalize_vec(y)
    # The actual representation is (x_k, y_k) / (x_k, x_k), but it can be replaced with (x_k, y_k) as long as
    # x is normalized. 
    cur_val = inner_prod(x, y) 
    if (abs(pre_val - cur_val) <= eps): # stop condition
        break
    pre_val = cur_val 


λ = inner_prod(x, y)
print("Eigenvalue with max absolute value: {:.3e}".format(λ))

if (eigenvalue_test(A, x, λ)):
    print("Test passed!")



