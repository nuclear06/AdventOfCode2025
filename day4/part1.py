import numpy as np

with open("./input.txt") as f:
    papers = f.readlines()

_matrix = [[c for c in papers[i].strip()] for i in range(len(papers))]
matrix: np.ndarray = np.array(_matrix) == "@"

height, width = matrix.shape


def sub_matrix(x, y, r):
    return matrix[
        max(0, y - r) : min(height, y + r + 1), max(0, x - r) : min(width, x + r + 1)
    ]


def check(x, y):
    submatrix = sub_matrix(x, y, 1)
    if np.sum(submatrix) <= 4:  # include self
        return True
    return False


ys, xs = np.where(matrix)
print(sum([check(x, y) for x, y in zip(xs, ys)]))
