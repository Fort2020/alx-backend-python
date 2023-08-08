#!/usr/bin/env python3
"""a measure_runtime coroutine
execute async_comprehension
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure four times in parallel 
    using asyncio.gather
    """
    first_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter()

    return (elapsed - first_time)
