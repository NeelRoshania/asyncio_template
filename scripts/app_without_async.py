import time
import numpy as np

from asyncio_template.funcs import single_sort_task, nested_sort_tasks
from asyncio_template import logger

"""

     Run concurrent tasks
     
          -> Nested Tasks 
          -> Task A

     Goal
          - Expect Task A to complete before Nested Tasks


"""

def main():
     logger.info('-- app-started --')
     start_time = time.perf_counter()

     values = np.random.randint(1000, size=int(5e3))
     nested_sort_tasks(
          'nested-task', 
          [
               ['B', values],
               ['C', values],
               ['D', values],                                       
          ]
     ) # nested tasks
     
     single_sort_task('A', values) # Task A
     
     elapsed_time = time.perf_counter() - start_time
     logger.info(f'-- app-completed in {elapsed_time:.2f}s --')

if __name__ == "__main__":
     main()
