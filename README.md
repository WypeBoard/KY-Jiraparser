# Jira-parser KY

Parse data from Kommunernes ydelsessystem (KY) Jira.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following software is required for this project to compile locally

```
Python3 (Verified on Python 3.8.2)
```

For running the program locally a user on ``KY-jira`` is required!

### Installing

As a general rule with python. Create a virtual environment for the project, this can be googled.

Run the following lines to download the required dependencies.

```
$Venv/bin/pip install jira pandas
```

Update [config.ini](https://github.com/WypeBoard/KY-Jiraparser/blob/master/config.ini) in the following lines
```
1: username
2: password
6: bug_filters # can be jira search statements or saved filters
7: test_execution # KY-xxxx
```

## Deployment

To run the program with the following command
```
$Venv/bin/python Main.py
```

Program output can be seen in the console.

## Authors

* **Nikolaj Bové Højholt** - [WypeBoard](https://github.com/WypeBoard)

See also the list of [contributors](https://github.com/WypeBoard/KY-Jiraparser/graphs/contributors) who participated in this project.