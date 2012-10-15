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

    def save(self):
        path = os.path.join(os.path.dirname(__file__), "..", "config", "config.cfg")
        self.conf.write(open(path, 'wb'))

    def set_section(self, section):
        if section is not None and self.has_section(section):
            self.section = section
        else:
             self.section = None

    def get(self, option, default=None):
        '''Get's a value from the current section.'''
        if self.section is not None and self.has_option(option):
            return self.conf.getint(self.section, option)
        else:
            return default

    def sites(self):
        '''Returns a list of websites in the config file.'''
        site_list = self.conf.sections()
        site_list.remove("Main")

        return site_list

    def add_site(self, name, details):
        if not self.has_section(name):
            self.conf.add_section(name)

            # Set values in details.
            for k in details:
                self.conf.set(name, k, details[k])

            self.save()

            return True
        else:
            return False

    def remove_site(self, section):
        return self.conf.remove_section(section)

    def has_option(self, option):
        return self.conf.has_option(self.section, option)

    def has_section(self, section):
        return self.conf.has_section(section)
