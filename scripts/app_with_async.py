import time
import asyncio
import numpy as np
import logging
import logging.config

from asyncio_template.async_funcs import non_compute_bound
from asyncio_template.funcs import single_sort_task as sst
from multiprocessing.dummy import Pool

# setup
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': f'logs/{__name__}.log'})
LOGGER = logging.getLogger(__name__) # python_template

"""

     Run concurrent tasks
     
     -> Nested Tasks 
     -> Task A

     Goal
          - Task A finished before starts

     Patterns
          - Definition: async def function()
          - Application: await function()
     
     Notes
          - The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
               - Simply calling a coroutine will not schedule it to be executed:
          - Blocking code is code that runs synchronously and thus blocks the event loop from being able to run multiple tasks in parallel. 
               - This has the effect of stopping the execution of all functions that are not the synchronous function, until the synchronous function has finished executing.
               - any other blocking call is incompatible with asynchronous Python code, because it will stop everything in its tracks for the duration of the sleep time.
          - async functions return coroutine objects

     Limitations
          - Restricted to non-blocking function calls (those that return nothing untill they're complete)
               - The OS will switch to another thread when it encounters an blocking function

     References
       - https://docs.python.org/3.9/library/asyncio-task.html#coroutines
       - https://tutorial.vcokltfre.dev/tips/blocking/
       - https://realpython.com/async-io-python/
       - https://superfastpython.com/thread-blocking-call-in-python/#:~:text=Blocking%20calls%20are%20calls%20to,context%20switch%20to%20another%20thread.

"""

async def main_noncomputebound():
     LOGGER.info('-- app-started --')
     start_time = time.perf_counter()

     values = np.random.randint(1000, size=int(5e3))

     # schedule non-blocking calls *concurrently*
     tasks = [asyncio.create_task(non_compute_bound(i[0], np.random.randint(1000, size=int(5e3)))) for i in enumerate(range(3))]
     results = await asyncio.gather(*tasks)

     elapsed_time = time.perf_counter() - start_time
     LOGGER.info(f'-- app-completed in {elapsed_time:.2f}s --')

def main_computebound():
     LOGGER.info('-- app-started --')
     start_time = time.perf_counter()

     arrs = [[i[0], np.random.randint(1000, size=int(5e3))] for i in enumerate(range(3))]
     task_ref = [i[0] for i in arrs]
     arr = [i[1] for i in arrs]

     # use multiprocessing for compute bound tasks
     with Pool() as pool:
          results = pool.starmap(sst, zip(task_ref, arr))

     elapsed_time = time.perf_counter() - start_time
     LOGGER.info(f'-- app-completed in {elapsed_time:.2f}s --')

if __name__ == "__main__":

     # asyncio.run(main_awaitforeach())
     # asyncio.run(main_noncomputebound()) 
     main_computebound()
