#/usr/bin/python
import re
import os
import sys
import json
import urllib
import subprocess
from jira import JIRA
options_server = {'server': 'https://devopscoeinstcs.atlassian.net'}

jira = JIRA(options=options_server, basic_auth=('username_for_jira', 'password_for_jira'))

#Get all the issues
issues = jira.search_issues('project="PCAB"')
parent_issue = sys.argv[2]
parent_issue = jira.issue(parent_issue)
flag=0
print("Flag initiated to 0")
jira.transition_issue(parent_issue,'5')
