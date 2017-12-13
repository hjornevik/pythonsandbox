from jira import JIRA
import pprint
import re
import datetime
 
# auth settings for JIRA call	
# open file "keys.txt" with user name and password separated by newlines
keyFile = open('keys.txt', 'r')
user = keyFile.readline().rstrip()
passw = keyFile.readline().rstrip()
keyFile.close()

# URLs to JIRA
urlT = 'https://jira.itgit.test.oneadr.net' #Test
#urlP = 'https://jira.itgit.oneadr.net'      #Prod

# connect to JIRA	
jira = JIRA(options= {'server': urlT}, basic_auth=(user, passw))


projects = jira.projects()
jra = jira.project('CBTEC')

# Get issues based on filter
issues = jira.search_issues('project=CBTEC', 'Labels=TEC_Data', expand='changelog',startAt=0, maxResults=2000)

#print(jra.name)
#print(jra.lead.displayName)

#components = jira.project_components(jra)
#[print (c.name) for c in components]  

# jira.project_roles(jra)                     # 'Administrators', 'Developers', etc.
# versions = jira.project_versions(jra)
# [v.name for v in reversed(versions)]        # '5.1.1', '5.1', '5.0.7', '5.0.6', etc.
#print(application_properties())

for i in issues:
    print(i.issue_type)