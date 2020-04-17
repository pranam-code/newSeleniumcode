import logging
logging.basicConfig(filename="C:/test/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.DEBUG
                    )

logging.debug("this is debug message") # not critical thats why not printed
logging.info("This is info message") # not critical thats why not printed
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")