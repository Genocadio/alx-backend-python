#!/usr/bin/env python3
"""function that returns the list of all the delays (float values)."""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that returns the list of all the delays (float values)."""
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        delays.append(delay)
    return sorted(delays)
