import sys
import pandas as pd

#Emails
insidersOnly = pd.read_csv('./data/combined/insiderOnly/email.csv', low_memory=False)
otherEmailsInput = pd.read_csv('./data/r6.2/email.csv', low_memory=False)

combinedEmails= pd.merge(insidersOnly,otherEmailsInput, how='outer', on=["id","date","to","from","size","attachments","content"]).fillna("")

combinedEmails.to_csv("./data/combined/insidersWithNormal.csv", index = False)