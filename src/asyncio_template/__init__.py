import configparser
import logging
import logging.config

cparser = configparser.ConfigParser()

# # __all__ applies to the situation where from foo.bar import *
# __all__ = [
#     'logger'
# ]