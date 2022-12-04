import logging
import inspect

class LogGen:
    @staticmethod
    def logjen():
        loggername=inspect.stack()[1][3]
        logger=logging.getLogger(loggername)
        fileHandler=logging.FileHandler(r"C:\Users\HP\PycharmProjects\pythonProject10\logs\automation.log")
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(messege)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

