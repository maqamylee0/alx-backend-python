#!/usr/bin/env python3
'''
    an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''function wait_randdom'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
