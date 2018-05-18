#/usr/bin/python
import re
import os
import sys
import json
import urllib
import subprocess
from jira import JIRA

options_server = {'server': 'https://devopscoeinstcs.atlassian.net'}

jira = JIRA(options=options_server, basic_auth=('username_for jira', 'password_for_jira'))

#Get all the issues
issues = jira.search_issues('project="PCAB"')
#parent_issue = sys.argv[4]
flag=0
print("Flag initiated to 0")
if "Recovery" in sys.argv[2]:
        print("1")
        extractedSubject=sys.argv[2][10:]
        for issue in issues:
                print("2")
                print(issue.fields.summary)
                print(extractedSubject)
                if issue.fields.summary==extractedSubject:
                        if "To Do" == str(issue.fields.status):
                                jira.transition_issue(issue, '61')
                                jira.add_comment(issue, sys.argv[3])
else:
        print('3')
        for issue in issues:
                if issue.fields.summary==sys.argv[2]:
                        print("4")
                        if "Resolved For Now" == str(issue.fields.status):
                                print("5")
                                jira.transition_issue(issue, '81')
                        if "Closed" != str(issue.fields.status):
                                print("6")
                                flag=1
                                jira.add_comment(issue, sys.argv[3])

        if(flag==0):
                print("Inside flag=0")
                new_issue = jira.create_issue(project='PCAB', summary=sys.argv[2],description=sys.argv[3], issuetype={'name': 'Bug'})
                #jira.create_issue_link('Duplicate',new_issue,parent_issue,None)
