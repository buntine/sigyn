import logging
import httplib

class Website:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = dict(config)
        self.__create_logger()

    def check(self):
        self.logger.info("Checking " + self.domain)

        conn = httplib.HTTPConnection(self.domain)
        req = conn.request("GET", self.config["url"])
        resp = conn.getresponse()
        self.logger.info("Returned HTTP status " + str(resp.status))

    def __create_logger(self):
        handler = logging.FileHandler('logs/' + self.domain + ".log")
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(self.domain)
        self.logger.addHandler(handler)
