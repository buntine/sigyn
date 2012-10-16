import logging

class Website:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = config

        handler = logging.FileHandler('logs/' + domain + ".log")
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(domain)
        self.logger.addHandler(handler)

    def check(self):
        self.logger.info("Checking " + self.domain)
