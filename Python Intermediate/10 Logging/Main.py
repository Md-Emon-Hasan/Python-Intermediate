# using logging method
print("using logging method:")
from asyncio import streams
from cgitb import handler
import logging

# import formatter
# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warning message")
# logging.error("this is a error message")
# logging.critical("this is a critical message")

# logging config
print("using logging config:")
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warning message")
# logging.error("this is a error message")
# logging.critical("this is a critical message")

# using prpagate logger
print("using propagate logger:")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
import Helper

# using lock handler
print("using lock handler:")
# logger = logging.getLogger(__name__)
# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("file.log")
# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.WARNING)
# formatter = logging.Formatter("%(fname)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
# logger.addHandler(stream_h)
# logger.addHandler(file_h)
# logger.warning("this is warning")
# logger.error("this is error")

# import logging
# import logging.config
# logging.config.fileConfig("logging.conf", defaults=None, disable_existing_loggers=True)
# # logging.config.dictConfig("logging.conf", defaults=None, disable_existing_loggers=True)
# logger = logging.getLogger("simpleExample")
# logger.debug("this is a debug message")

# import logging
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)

# import logging
# import traceback
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except:
#     logging.error("the error is %s", traceback.format_exc())

# using RotatingFileHandler
print("using RotatingFileHandler:") 
import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# roll over after 2KB and keep backup logs app.log.1, app.log.2, etc
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)
for _ in range(10000):
    logger.info("hello world!")

# using TimedRotatingFileHandler
print("using TimedRotatingFileHandler:") 
import logging
import time
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# s, m, h, d, midnight, w0
handler = TimedRotatingFileHandler("timed_test.log", when="s", interval=5, backupCount=5)
logger.addHandler(handler)
for _ in range(6):
    logger.info("hello world!")
    time.sleep(5)

