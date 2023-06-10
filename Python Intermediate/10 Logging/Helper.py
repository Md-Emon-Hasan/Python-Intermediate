from asyncio.log import logger
import logging

# using prpagate logger
print("using propagate logger:")
logger = logging.getLogger(__name__)
logger.propagate = False # if we use False propagate logger hide the message default value it's using True show the message
logger.info("hello from helper")

# using lock handler
print("using lock handler:")
