import random
import math
import copy

def normalize_vec(x):
    ret = copy.deepcopy(x)
    norm = math.sqrt(inner_prod(x, x))
    for i in range(len(x)):
        ret[i] /= norm
    return ret

def matvec_mul(A, x):
    ret = []
    n = len(x)
    for i in range(n):
        ret.append(inner_prod(A[i], x))

    return ret

def inner_prod(x, y):
    assert(len(x) == len(y))

    n = len(x)
    ret = 0.

    for i in range(n):
        ret += x[i] * y[i]

    return ret

def init_rand_vec(n):
    ret = []
    for i in range(n):
        ret.append(random.random())
    return ret

def mat_mul(A, B, A_transpose = False):
    n = len(A)
    l = len(A[0])
    m = len(B[0])
    ret = [[0. for j in range(n)] for i in range(n)]

    if (A_transpose == False):
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    ret[i][j] += A[i][k] * B[k][j]
    else:
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    ret[i][j] += A[k][i] * B[k][j]

    return ret