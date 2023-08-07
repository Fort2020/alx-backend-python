#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay
for total execution time for wait_n(n, max_delay)
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time (total execution time) / n"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
