import math
import sys
sys.path.append("..")
import copy
from utils import mat_mul
from eigenvalue_test import eigenvalue_test

def stop_condition(A):
    eps = 1e-10
    n = len(A)

    for i in range(n):
        for j in range(n):
            if (i == j):
                continue
            if (abs(A[i][j]) >= eps): return False

    return True

def max_abs_elem_idx(A):
    n = len(A)
    cur_max = -1.
    cur_idx = [-1, -1]
    for i in range(n):
        for j in range(n):
            if (i == j): continue
            if (abs(A[i][j]) > cur_max):
                cur_max = abs(A[i][j])
                cur_idx = [i, j]
    return cur_idx


def calc_theta(A, p, q):
    a_pq = A[p][q]
    a_pp = A[p][p]
    a_qq = A[q][q]
    eps = 1e-10
    PI = math.pi

    if (abs(a_pp - a_qq) <= eps): return PI / 4.
    else:
        return 1./2. * math.atan(-2. * a_pq / (a_pp - a_qq))        

def sim_trans(A):
    n = len(A)
    R = [[0. for j in range(n)] for i in range(n)]
    for i in range(n):
        R[i][i] = 1.

    p, q = max_abs_elem_idx(A)
    theta = calc_theta(A, p, q)

    R[p][p] = math.cos(theta) 
    R[p][q] = math.sin(theta)
    R[q][p] = -math.sin(theta)
    R[q][q] = math.cos(theta)

    A = mat_mul(R, mat_mul(A, R), True)

    return R, A    


A = [[1., 3., 3., 1.], [3., 2., 0., 2], [3., 0., 3., 1.], [1., 2., 1., 1.]]
A_before = copy.deepcopy(A)
assert(len(A) == len(A[0])) # A should be square matrix
n = len(A) 

U = None

MAX_ITER = 20

for iter in range(MAX_ITER):
    R, A = sim_trans(A)
    if (U != None): U = mat_mul(U, R)
    else: U = R

    if (stop_condition(A)):
        print("stop at %d iteration" % iter)
        break


eigval_list = []

print("Eigenvalue: ")
for i in range(n):
    print("     λ_%d = " % i, end = '')
    print('{:.3e}'.format(A[i][i]))
    eigval_list.append(A[i][i])


print("Eigenvector: ")
for i in range(n):
    print("     v_%d = [" % i, end = '')
    for j in range(n):
        tmp_str = '{:.3e}'.format(U[j][i])
        if (j != n - 1): tmp_str += ', ' 
        print(tmp_str, end = '')
    print("]^T")


for i in range(n):
    v = []
    for j in range(n):
        v.append(U[j][i])
    if (eigenvalue_test(A_before, v, eigval_list[i]) == False):
        print("Test Failed.")

print("Test passed!")