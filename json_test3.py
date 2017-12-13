from jira import JIRA
import pprint
import re
import datetime

# Prepare file output
fh = open("testfile.txt","w")
 
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

# Issue IDs for experimenting:
#issueT = jira.issue('CBTEC-1751') #Test
#issueP = jira.issue('CBQA-2313')  #Prod


# Get issues based on filter
issues = jira.search_issues('Labels=TEC_Data', expand='changelog',startAt=0, maxResults=2000)

# Print csv header
print('Issue ID,Created,Changed date,From,To,Duration')


# Loops - would like to understand better what each one does, and if it can be improved performance vise...
for i in issues:
    changelog = i.changelog
    for history in changelog.histories:
        for item in history.items:                
            if item.field == 'status' and item.toString == 'Acceptance': # Define which end-status to calculate
                createdTime = datetime.datetime.strptime(i.fields.created[:19], '%Y-%m-%dT%H:%M:%S')
                resolvedTime = datetime.datetime.strptime(history.created[:19], '%Y-%m-%dT%H:%M:%S')
                duration = resolvedTime - createdTime
               
                print(i, ',' + i.fields.created[:19] + ',' + history.created[:19] + ',' + item.fromString + ',' + item.toString, ',', duration)

                

                
                

### How to print sorted on resolved time?
### How to print 00 when no days?
### How to present result in Confluence or Teams?
### How to write directly to file?
                #lines_of_text = [i, ',' + i.fields.created[:19] + ',' + history.created[:19] + ',' + item.fromString + ',' + item.toString, ',', duration] 
                #fh.writelines(lines_of_text) 
#                    fh.writelines(lines_of_text)
#                    TypeError: write() argument must be str, not Issue
                #fh.close()                 


                
# Some notes
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__
gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__
repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'field', 'fieldtype', 'from', 'fromS
tring', 'to', 'toString']

item.field:
- End date
- Epic Link
- labels
- Link
- Start date
- status
- Workflow


for i in issues:
    print (i.id)#, i.fields = 'Labels', 'Assignee', 'Status')
"""