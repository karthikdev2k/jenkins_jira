#from jira import JIRA
#from collections import Counter

#options = {'server': 'http://localhost:8089'}
#jira = JIRA(options)
#jira = JIRA(basic_auth=('admin', 'admin'))
#issue = jira.issue('AIT-1')

import jira.client
from jira.client import JIRA

print ['Going to fetch the issues for issue AIT-1'] 
options = {'server': 'http://localhost:8089'}
jira = JIRA(options, basic_auth=('admin', 'admin'))
issue = jira.issue('AIT-1')

print ['/n################################################'] 
print ['Going to fetch the COMMENTS for issue AIT-1'] 
comment = jira.add_comment('AIT-1', 'new comment another one>?!')    # no Issue object required
comment = jira.add_comment(issue, 'new comment for now!!', visibility={'type': 'role', 'value': 'Administrators'})  # for admins only

comment.update(body = 'updated comment body')
comment.delete()

print ['/n################################################'] 
print ['Going to fetch the TRANSITIONS for issue AIT-1'] 
issue = jira.issue('AIT-1')
transitions = jira.transitions(issue)
print[(t['id'], t['name']) for t in transitions]