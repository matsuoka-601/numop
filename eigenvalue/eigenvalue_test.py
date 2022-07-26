import sys
sys.path.append('..')
from utils import inner_prod

def eigenvalue_test(A, v, eigval):
    eps = 1e-5
    n = len(A)
    
    for j in range(n):
        lhs = inner_prod(A[j], v)
        rhs = eigval * v[j]
        if (abs(lhs - rhs) >= eps):
            return False
    return True