import sys
sys.path.append('..')
import copy
from utils import list_to_str, inner_prod

def find_pivot_row_idx(A, lb):
    EPS = 1e-7
    ret_idx = -1
    cur_max = EPS
    for row_idx in range(lb, len(A)):
        if (abs(A[row_idx][lb]) > cur_max):
            cur_max = abs(A[row_idx][lb])
            ret_idx = row_idx
    if (ret_idx == -1):
        print("A is not regular.")
        exit()
    return ret_idx

def gauss_elimination(A, b):
    assert(len(A) == len(A[0])) # A should be a square matrix

    n = len(A)

    for row_idx in range(n):
        A[row_idx].append(b[row_idx])

    row_num = n
    col_num = n + 1

    for row_idx in range(row_num):
        pivot_row_idx = find_pivot_row_idx(A, row_idx)
        if (pivot_row_idx != row_idx):
            A[row_idx], A[pivot_row_idx] = A[pivot_row_idx], A[row_idx]
        for sub_row_idx in range(row_idx + 1, row_num):
            coeff = -A[sub_row_idx][row_idx] / A[row_idx][row_idx]
            for sub_col_idx in range(row_idx, col_num):
                A[sub_row_idx][sub_col_idx] += A[row_idx][sub_col_idx] * coeff 
    
    # calc answer
    tmp_ans = [0. for _ in range(n)]
    for row_idx in range(row_num - 1, -1, -1):
        sub = 0.
        for col_idx in range(row_idx + 1, n):
            sub += A[row_idx][col_idx] * tmp_ans[col_idx]
        tmp_ans[row_idx] = (A[row_idx][col_num - 1] - sub) / A[row_idx][row_idx]

    return tmp_ans


def validate(A, x, b):
    n = len(A)
    EPS = 1e-7
    for i in range(n):
        if (abs(inner_prod(A[i], x) - b[i]) < EPS): continue
        else: return False
    return True

A = [[0., 1., -2., 3.], [1., -3., 4., -7.], [-3., 9., 2., -5.], [2., 1., 2., 1.]]
b = [7., 2., 1., -3.]

x = gauss_elimination(copy.deepcopy(A), b)
print("ans: " + list_to_str(x))

if (validate(A, x, b)):
    print("Test passed!")
else:
    print("Test failed.")
