from jira import JIRA

import KyConfigParser
import jira_bug
import jira_test

if __name__ == '__main__':
    config = KyConfigParser.KyConfigParser()

    jira = JIRA(config.server_options, basic_auth=config.user)
    bugs = jira_bug.jira_bug(jira, config)
    bugs.run()
    tests = jira_test.jira_test(jira, config)
    tests.run()
