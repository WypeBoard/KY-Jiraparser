from collections import defaultdict


class jira_bug:
    def __init__(self, jira, config):
        self.jira = jira
        self.bug_queries = config.bug_filters
        if config.enable_history:
            self.expand_tag = 'changelog'
            self.log_history = config.log_history_from
        else:
            self.expand_tag = None
        self.issue = defaultdict(dict)

    def pretty_print(self):
        for issuePriority in self.issue.keys():
            key_to_value_lengths = {k: len(v) for k, v in self.issue[issuePriority].items()}
            print(issuePriority, key_to_value_lengths)

    def create_issue_dictionary(self, bug_progression):
        for issue in bug_progression:
            priority = issue.fields.priority.name
            status = issue.fields.status.name
            if status in self.issue[priority]:
                self.issue[priority][status].append(issue.key)
            else:
                self.issue[priority][status] = [issue.key]

    def run(self):
        for bug_list in self.bug_queries:
            result_list = self.jira.search_issues(bug_list, maxResults=False, expand=self.expand_tag)
            self.create_issue_dictionary(result_list)
            self.pretty_print()
