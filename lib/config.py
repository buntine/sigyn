import ConfigParser, os

class Conf:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()    
        self.section = None

    def read(self, section):
        path = os.path.join(os.path.dirname(__file__), "..", "config", "config.cfg")
        self.conf.read(path)

        if self.conf.has_section(section):
            self.section = section

    def get(self, option, default=None):
        if self.section is not None and self.has_option(option):
            return self.conf.getint(self.section, option)
        else:
            return default

    def add(self, details):
        pass

    def remove(self, section):
        pass

    def has_option(self, option):
        return self.conf.has_option(self.section, option)
