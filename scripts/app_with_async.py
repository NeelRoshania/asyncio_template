import time
import asyncio
import numpy as np

from asyncio_template.async_funcs import single_sort_task, nested_sort_tasks
from asyncio_template import logger

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

async def main_awaitforeach():
     logger.info('-- app-started --')
     start_time = time.perf_counter()

     values = np.random.randint(1000, size=int(5e3))

     # define task
     task1 = asyncio.create_task(
                                   nested_sort_tasks(
                                             'nested-task', 
                                             [
                                                  ['B', values],
                                                  ['C', values],
                                                  ['D', values],                                       
                                             ]
                                        )
     ) # nested tasks
     task2 = asyncio.create_task(single_sort_task('A', values)) # Task A
     
     # wait for both tasks to finish
     await task1
     await task2
     
     elapsed_time = time.perf_counter() - start_time
     logger.info(f'-- app-completed in {elapsed_time:.2f}s --')

async def main_firsttofinish():
     logger.info('-- app-started --')
     start_time = time.perf_counter()

     values = np.random.randint(1000, size=int(5e3))

     # schedule two calls *concurrently*:
     await asyncio.gather(
                              nested_sort_tasks(
                                        'nested-task', 
                                        [
                                             ['B', values],
                                             ['C', values],
                                             ['D', values],                                       
                                        ]),
                              single_sort_task('A', values)
     )
     
     elapsed_time = time.perf_counter() - start_time
     logger.info(f'-- app-completed in {elapsed_time:.2f}s --')

if __name__ == "__main__":

     # asyncio.run(main_awaitforeach())
     asyncio.run(main_firsttofinish())  
