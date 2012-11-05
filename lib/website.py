import logging
import httplib
from lib import database

class Website:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = dict(config)
        self.__create_logger()

    def check(self):
        self.logger.info("Checking %s" % self.domain)
        resp = self.__make_request()

        if resp == None:
            self.logger.warning("%s cannot be resolved!" % self.domain)
            self.__send_notifications()
            return

        if self.__should_notify(resp.status):
            self.logger.warning("%s returned %i" % (self.config["url"], resp.status))
            self.__send_notifications(resp.status)
        else:
            self.logger.info("%s returned %i" % (self.config["url"], resp.status))

    def __make_request(self):
        try:
            if self.config["ssl"] == 'true':
                conn = httplib.HTTPSConnection(self.domain, 443)
            else:
                conn = httplib.HTTPConnection(self.domain)

            req = conn.request("GET", self.config["url"], self.config["timeout"])
            return conn.getresponse()
        except:
            return None

    def __create_logger(self):
        handler = logging.FileHandler('logs/' + self.domain + ".log")
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(self.domain)
        self.logger.addHandler(handler)

    def __send_notifications(self, status=0):
        pass

    def __should_notify(self, status):
        whitelist = self.config["notify"].split(" ")

        return status in map(lambda x: int(x), whitelist)
