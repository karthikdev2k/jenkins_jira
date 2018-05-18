Install the required modules using,

`$ pip install -r requirements.txt`




If you do not have pip installed, install it using:
        > $ easy_install pip


#In case Build is Successful
if (currentBuild.result == 'SUCCESS')
    {
    sh "python /home/ec2-user/JIRA-ticket-creationg-using-zabbix-alerts/jenkins_success.py $env.python_jira_authentication $parent_issue"
    }

#In case Build is Failure
sh "python /home/ec2-user/JIRA-ticket-creationg-using-zabbix-alerts/jenkins.py $env.python_jira_authentication Code_Merge_Has_Failed '$codemergeissue$parent_issue'"