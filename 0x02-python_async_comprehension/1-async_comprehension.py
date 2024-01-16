""" Async Comprehensions"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Attributes:
        no arguments
    Return:
        The coroutine will collect 10 random numbers using an async
        comprehensing over async_generator, then return the 10 random numbers.
    """
    return [number async for number in async_generator()]
