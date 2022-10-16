import time
import numpy as np

def timeit(func, params, itr = 1, digits = 3):
    for i in range(itr):
        t0 = time.time()
        res = func(**params)
        t1 = time.time()
        tres = t1 - t0
    eres = round(np.mean(tres), digits)
    print(f'Mean Execution Time: {eres} seconds')
    return res