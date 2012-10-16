from lib import website, config
import logging
import logging.config

class Sigyn:
    def __init__(self):
        logging.config.fileConfig("config/logging.cfg")

        self.conf = config.Conf(do_read=True)
        self.sites = self.conf.sites()

    def check(self):
        for site in self.sites:
            self.conf.set_section(site)

            ws = website.Website(site, self.conf.items())
            ws.check()
