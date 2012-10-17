import ConfigParser, os

class Conf:
    def __init__(self, do_read=False):
        self.conf = ConfigParser.ConfigParser()    
        self.section = None

        if do_read:
            self.read()

    def read(self, section=None):
        '''Reads the config file and optionally sets the section'''
        self.conf.read(self.__path())
        self.set_section(section)

    def save(self):
        self.conf.write(open(self.__path(), 'wb'))

    def set_section(self, section):
        if section is not None and self.has_section(section):
            self.section = section
        else:
             self.section = None

    def getint(self, option, default=None):
        return self.__get(option, self.conf.getint, default)

    def getboolean(self, option, default=None):
        return self.__get(option, self.conf.getboolean, default)

    def getfloat(self, option, default=None):
        return self.__get(option, self.conf.getfloat, default)

    def __get(self, option, func, default=None):
        '''Returns a value from the current section.'''
        if self.section is not None and self.has_option(option):
            return func(self.section, option)
        else:
            return default

    def items(self):
        return self.conf.items(self.section)

    def sites(self):
        '''Returns a list of websites in the config file.'''
        site_list = self.conf.sections()
        site_list.remove("main")

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

    def __path(self):
        return os.path.join(os.path.dirname(__file__), "..", "config", "config.cfg")
