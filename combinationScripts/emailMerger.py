import sys
import pandas as pd

#Emails
emailsR2 = pd.read_csv('./data/r2/email.csv', low_memory=False)
emailsR31 = pd.read_csv('./data/r3.1/email.csv', low_memory=False)
emailsR32 = pd.read_csv('./data/r3.2/email.csv', low_memory=False)
emailsR41 = pd.read_csv('./data/r4.1/email.csv', low_memory=False)
emailsR42 = pd.read_csv('./data/r4.2/email.csv', low_memory=False)
emailsR51 = pd.read_csv('./data/r5.1/email.csv', low_memory=False)
emailsR52 = pd.read_csv('./data/r5.2/email.csv', low_memory=False)
emailsR61 = pd.read_csv('./data/r6.1/email.csv', low_memory=False)
emailsR62 = pd.read_csv('./data/r6.2/email.csv', low_memory=False)

combinedEmails= pd.merge(emailsR2,emailsR31, how='outer', on=["id","date","to","from"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR32.astype(str), how='outer',on=["id","date","to","from","size","attachments","content"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR41.astype(str), how='outer',on=["id","date","to","from","size","attachments","content"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR42.astype(str), how='outer', on=["id","date","to","from","size","attachments","content","cc","bcc","pc","user"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR51.astype(str), how='outer', on=["id","date","to","from","size","attachments","content","cc","bcc","pc","user"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR52.astype(str), how='outer', on=["activity","id","date","to","from","size","attachments","content","cc","bcc","pc","user"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR61.astype(str), how='outer', on=["activity","id","date","to","from","size","attachments","content","cc","bcc","pc","user"]).fillna("")
combinedEmails= pd.merge(combinedEmails.astype(str),emailsR62.astype(str), how='outer', on=["activity","id","date","to","from","size","attachments","content","cc","bcc","pc","user"]).fillna("")

combinedEmails.to_csv("./data/combined/email.csv", index = False)