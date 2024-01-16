""" Async Comprehensions"""

from importlib import import_module as using
from typing import List
async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Attributes:
        no arguments
    Return:
        The coroutine will collect 10 random numbers using an async
        comprehensing over async_generator, then return the 10 random numbers.
    """
    return [number async for number in async_generator()]
