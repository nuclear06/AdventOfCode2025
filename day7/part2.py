import numpy as np
from functools import lru_cache

with open("./input.txt") as f:
    txt = f.readlines()

begin_loc = txt[0].index("S")
spliter = np.array([[c for c in l.strip()] for l in txt[2::2]]) == "^"
total_layers = len(spliter)


@lru_cache(maxsize=None)
def iter(sp_layer, lazer_idx):
    if sp_layer == total_layers:
        return 1
    if spliter[sp_layer][lazer_idx]:
        return iter(sp_layer + 1, lazer_idx - 1) + iter(sp_layer + 1, lazer_idx + 1)
    else:
        return iter(sp_layer + 1, lazer_idx)


print(iter(0, begin_loc))
