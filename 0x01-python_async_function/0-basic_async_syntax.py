#!/usr/bin/env python3
"""Function that waits for a random delay between 0 and max_delay"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """function that waits for a random delay between 0 and max_delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
