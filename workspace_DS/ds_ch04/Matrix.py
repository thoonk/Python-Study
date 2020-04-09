from typing import List
# 2차원으로 구성된 숫자의 집합으로 list of list로 구현
from datascience.ch04.Vector import Vector

Matrix = List[List[float]]

A = [[1,2,3],
     [4,5,6]]
B = [[1,2],
     [3,4],
     [5,6]]



from typing import Tuple
# 행렬의 구조: n x m 행렬의 경우, (n,m)
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

# i번째 행 얻기
def get_row(A: Matrix, i: int) -> Vector:
    return A[i]
# j번째 행 얻기
def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

# 행렬 만들기
from typing import Callable, List

from matplotlib import collections

Matrix = List[List[float]]

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i,j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def f1(i, j):
    return i*j;

A1 = make_matrix(3,2, f1)
print(A1)

#단위 행렬 만들기
def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i==j else 0) # n x n identity matrix

assert identity_matrix(5) == [[1,0,0,0,0],
                              [0,1,0,0,0],
                              [0,0,1,0,0],
                              [0,0,0,1,0],
                              [0,0,0,0,1]]




