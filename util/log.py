from loguru import logger


class Log:
    def warning(self, message):
        logger.warning(message)

    def error(self, message):
        logger.error(message)