from lib import website, config

class Sigyn:
    def __init__(self):
        self.conf = config.Conf(do_read=True)
        self.sites = self.conf.sites()

    def check(self):
        print "Checking..."

        for site in self.sites:
            self.conf.set_section(site)

            ws = website.Website(site, self.conf.options())
            ws.check()
