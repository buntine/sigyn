import logging

class Website:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = config

    def check(self):
        self.__create_logger()
        self.logger.info("Checking " + self.domain)

    def __create_logger(self):
        handler = logging.FileHandler('logs/' + self.domain + ".log")
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(self.domain)
        self.logger.addHandler(handler)
