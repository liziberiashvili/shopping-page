import logging
import logging.config


class LoggerUtils:
    logging.config.fileConfig(fname='../resources/logger_config.conf',
                              disable_existing_loggers=False)

    @staticmethod
    def info(message):
        return logging.getLogger(__name__).info(message)

    @staticmethod
    def debug(message):
        return logging.getLogger(__name__).debug(message)

    @staticmethod
    def error(message):
        return logging.getLogger(__name__).error(message)


