import time
import numpy as np
import math # because performance definitely matters
from numba import cuda # because performance DEFINITELY matters
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float32

@cuda.jit() # thanks stackoverflow
def mc_kernel(rng_states, samples_per_thread, out):
    thread_id = cuda.grid(1)
    one = np.float32(1.0)
    subtotal = np.float32(0.0)
    c = np.float32(0.0)
    for _ in range(samples_per_thread):
        x = xoroshiro128p_uniform_float32(rng_states, thread_id) # thanks nvidia for throttling float64 on geforce
        # thanks gemini
        y = math.sqrt(one - x * x) - c # optimisation™
        t = subtotal + y
        c = (t - subtotal) - y
        subtotal = t
    out[thread_id] = np.float64(subtotal) - np.float64(c)

def mc_cuda(samples_per_thread, blocks, threads_per_block, rng_states, vram_block):
    mc_kernel[blocks, threads_per_block](rng_states, samples_per_thread, vram_block)
    cuda.synchronize()
    out = vram_block.copy_to_host() 
    return np.sum(out, dtype=np.float64)

if __name__ == "__main__":
    cuda.select_device(0) # Because whether CUDA works today seems to be the best RNG
    threads_per_block = 256 # thanks google
    blocks = 5440-256
    threads = threads_per_block*blocks # thanks jensen

    rng_states = create_xoroshiro128p_states(threads, seed=9008)
    vram_block = cuda.device_array(threads, dtype=np.float64)

    samples_per_thread_test = (10**10)//threads
    samples_test = (10**10)
    print(f"{samples_test} samples. ")

    mc_cuda(1, blocks, threads_per_block, rng_states, vram_block) # compiles it but doesn't run

    est_start_time = time.perf_counter() # very necessary
    mc_cuda(samples_per_thread_test, blocks, threads_per_block, rng_states, vram_block)
    est_end_time = time.perf_counter()
    print(f"ETA in {((est_end_time-est_start_time)*(10**5))/3600} hours")

    samples_per_thread_real = (10**15)//threads
    samples_real = (10**15)
    print(f"{samples_real} samples. ")

    real_start_time = time.perf_counter()
    total_sum = np.float64(0.0)
    chunks = 1000 # was hitting float32 limits
    for i in range(chunks):
        chunk_sum = mc_cuda(10**6, blocks, threads_per_block, rng_states, vram_block)
        total_sum += chunk_sum # 1 quadrillion in less (pronounce as just over) than 1 hour!
    total_samples_run = chunks * (10**6) * threads
    print(f"pi is about {(total_sum / total_samples_run) * 4.0}")
    real_end_time = time.perf_counter()
    print(f"took {(real_end_time-real_start_time)/3600} hours")