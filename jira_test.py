class jira_test:

    def __init__(self, jira, config):
        self.jira = jira
        self.keys_to_query = config.test_execution_keys
        if config.enable_history:
            self.expand_tag = True
        else:
            self.expand_tag = None

        pass

    def fetch_test_information(self):
        for test_execution in self.jira.search_issues('key in (' + self.keys_to_query + ')'):
            print(test_execution.fields.summary, end=': ')
            for test_execution_status_collection in test_execution.raw['fields']['customfield_10120']['statuses']:
                print('[', test_execution_status_collection['name'], test_execution_status_collection['statusCount'],
                      end='] ')
            print()

    def run(self):
        self.fetch_test_information()
