class Website:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = config

    def check(self):
        print "Checking " + self.domain
