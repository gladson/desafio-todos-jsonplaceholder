import logging


class Logger:
    def __init__(self, msg):
        self.logger = logging.getLogger(__name__)
        self.msg = msg

    def info(self):
        self.logger.info(msg=self.msg)

    def debug(self):
        self.logger.debug(msg=self.msg)

    def warning(self):
        self.logger.warning(msg=self.msg)

    def error(self):
        self.logger.error(msg=self.msg)
