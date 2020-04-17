import logging
logging.basicConfig(filename="C:/test/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%Y %I:%M:%S %p"
                    )
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("this is debug message") # not critical thats why not printed
logger.info("This is info message") # not critical thats why not printed
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")