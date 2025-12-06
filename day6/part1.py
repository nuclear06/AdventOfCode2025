# tbh, I think it’s unfair to use python or numpy to solve this problem.
with open("./input.txt") as f:
    txt = f.readlines()

nums, operator = txt[:-1], txt[-1]
import numpy as np

nums = np.array([[int(i) for i in line.split()] for line in nums])
operator = np.array(operator.split())
sums, products = nums[:, operator == "+"], nums[:, operator == "*"]
print(np.sum(sums) + np.prod(products, axis=0).sum())
