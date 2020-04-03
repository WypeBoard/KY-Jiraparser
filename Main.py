from jira import JIRA
from collections import defaultdict

user = ['test','test']


bug_query = ''
test_query = ''

def create_issue_dictionary(projects):
    _issues = defaultdict(dict)
    for issue in projects:
        priority = issue.fields.priority.name
        status = issue.fields.status.name
        if status in _issues[priority]:
            _issues[priority][status].append(issue.key)
        else:
            _issues[priority][status] = [issue.key]
    return _issues

def pretty_print(issues):
    for issuePriority in issues.keys():
        key_to_value_lengths = {k: len(v) for k, v in issues[issuePriority].items()}
        print(issuePriority, key_to_value_lengths)


def fetch_bug_information(jira):
    _bug_progression = jira.search_issues(bug_query, maxResults=False)
    _issue_dictionary = create_issue_dictionary(_bug_progression)
    pretty_print(_issue_dictionary)


def fetch_test_information(jira):
    _test_progression = jira.search_issues(test_query, maxResults=False)
    for test_execution in _test_progression:
        print(test_execution.fields.summary, end=': ')
        for test_execution_status_collection in test_execution.raw['fields']['customfield_10120']['statuses']:
            print('[',test_execution_status_collection['name'], test_execution_status_collection['statusCount'], end='] ')
        print()

if __name__ == '__main__':
    options = {'server': 'https://kyjira.westeurope.cloudapp.azure.com'}
    jira = JIRA(options, basic_auth=(user))
    fetch_bug_information(jira)
    fetch_test_information(jira)

