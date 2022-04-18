import sys
import pandas as pd

#Emails
emailsInput1 = pd.read_csv('./combinationScripts/insiderOnly/emailsInput1.csv', low_memory=False)
emailsInput2 = pd.read_csv('./combinationScripts/insiderOnly/emailsInput2.csv', low_memory=False)
emailsInput3 = pd.read_csv('./combinationScripts/insiderOnly/emailsInput3.csv', low_memory=False)

combinedEmails= pd.merge(emailsInput1,emailsInput2, how='outer', on=["id","date","to","from","size","attachments","content"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsInput3.astype(str), how='outer',on=["id","date","user","pc","to","cc","bcc","from","size","attachments","content"
]).fillna("")

combinedEmails.to_csv("./data/combined/insiderOnly/email.csv", index = False)