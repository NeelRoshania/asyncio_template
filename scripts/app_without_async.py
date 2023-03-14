import time
import numpy as np
import logging
import logging.config

from asyncio_template.funcs import single_sort_task, nested_sort_tasks

# setup
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': f'logs/{__name__}.log'})
LOGGER = logging.getLogger(__name__) # python_template

"""

     Run concurrent tasks
     
          -> Nested Tasks 
          -> Task A

     Goal
          - Expect Task A to complete before Nested Tasks


"""

def main():
     LOGGER.info('-- app-started --')
     start_time = time.perf_counter()

     values = np.random.randint(1000, size=int(5e3))
     # nested_sort_tasks(
     #      'nested-task', 
     #      [
     #           ['B', values],
     #           ['C', values],
     #           ['D', values],                                       
     #      ]
     # ) # nested tasks
     
     tasks = [single_sort_task(i[0], np.random.randint(1000, size=int(5e3))) for i in enumerate(range(3))]
     
     elapsed_time = time.perf_counter() - start_time
     LOGGER.info(f'-- app-completed in {elapsed_time:.2f}s --')

if __name__ == "__main__":
     main()
