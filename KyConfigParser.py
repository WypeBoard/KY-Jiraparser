import configparser
import datetime

class KyConfigParser:

    user = []
    server_options = {}
    bug_filters = []
    test_execution_keys = ''
    enable_history = False
    log_history_from = datetime.datetime.now()

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        """ Default config """
        self.user.append(self.config.get('DEFAULT', 'username'))
        self.user.append(self.config.get('DEFAULT', 'password'))
        self.server_options.update({'server': self.config.get('DEFAULT', 'jiralink')})
        self.bug_filters.extend(self.aslist('DEFAULT', 'bug_filters'))
        self.test_execution_keys = self.config.get('DEFAULT', 'test_executions')

        """ History log config """
        self.enable_history = self.config.get('HISTORY', 'enable') == 'True'
        if self.enable_history:
            self.log_history_from = datetime.datetime.strptime(self.config.get('HISTORY', 'backtrack_to_date'), '%d-%m-%Y')

    def aslist_cronly(self, section, option):
        value = self.config.get(section, option)
        return list(filter(None, (x.strip() for x in value.splitlines())))


    def aslist(self, section, option, flatten=True):
        """ Return a list of Strings, separating the input based on newlines
        and, if flatten=True (default), also split on spaces within 
        each line."""
        values = self.aslist_cronly(section, option)
        if not flatten:
            return values
        result = []
        for value in values:
            subvalue = value.split()
            result.extend(subvalue)
        return result
