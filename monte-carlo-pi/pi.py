import random
import math # because performance definitely matters
from numba import njit, prange # because performance DEFINITELY matters

@njit(parallel=True, fastmath=True, nogil=True) # thanks stackoverflow
def mc_simulate_parallel(samples):
    total = 0.0
    for _ in prange(samples):
        x = random.random()
        total += math.sqrt(1-x*x) # optimisation™
    return 4.0 * (total/samples)

if __name__ == "__main__":
    print(mc_simulate_parallel(1000000000000)) # 1 trillion, ~3mins on 9950X3D