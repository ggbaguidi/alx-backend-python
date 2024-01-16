"""Run time for four parallel comprehensions"""

import time
from importlib import import_module as using
import asyncio

async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    Attributes:
        no arguments
    Return:
        measure the total runtime and return it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
