import ConfigParser, os

class Conf:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()    
        self.section = None

    def read(self, section=None):
        '''Reads the config file and optionally sets the section'''
        path = os.path.join(os.path.dirname(__file__), "..", "config", "config.cfg")
        self.conf.read(path)
        self.set_section(section)

    def set_section(self, section):
        if section is not None and self.has_section(section):
            self.section = section
        else:
             self.section = None

    def get(self, option, default=None):
        if self.section is not None and self.has_option(option):
            return self.conf.getint(self.section, option)
        else:
            return default

    def sites(self):
        pass

    def add_site(self, details):
        pass

    def remove_site(self, section):
        pass

    def has_option(self, option):
        return self.conf.has_option(self.section, option)

    def has_section(self, section):
        return self.conf.has_section(section)
