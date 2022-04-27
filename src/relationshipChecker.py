import os
import sys
import pandas as pd
import numpy as np
from collections import Counter
from nltk import ngrams

def filesRelationship(filesInput):
    #Find amount of time each file extension was used
    filesInput['fileExtension'] = filesInput.filename.str.split('.').str[-1]
    report="++++REPORT++++\nFile Extensions Counts:\n"+str(filesInput['fileExtension'].value_counts())+"\n\n"

    #Find amount of times each activity involving a removable media device occured
    report+=("File Activity Counts:\n"+str(filesInput['activity'].value_counts())+"\n\n")

    #Analyze content of files for most common phrases
    openContent=filesInput[filesInput['activity']=='File Open']['content']
    writeContent=filesInput[filesInput['activity']=='File Write']['content']
    copyContent=filesInput[filesInput['activity']=='File Copy']['content']
    deleteContent=filesInput[filesInput['activity']=='File Delete']['content']

    #Find most common phrases for each activity and report them
    content = [y for x in openContent for y in x.split()]
    n = [4]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=("Most Common File Open Phrases:\n"+str(count)+"\n\n")

    content = [y for x in writeContent for y in x.split()]
    n = [4]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=("Most Common File Write Phrases:\n"+str(count)+"\n\n")

    content = [y for x in copyContent for y in x.split()]
    n = [4]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=("Most Common File Copy Phrases:\n"+str(count)+"\n\n")

    content = [y for x in deleteContent for y in x.split()]
    n = [4]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=("Most Common File Delete Phrases:\n"+str(count)+"\n\n")

    #Write report to report directory
    os.makedirs(os.path.dirname("./reports/File Relationship Report.txt"), exist_ok=True)
    with open("./reports/File Relationship Report.txt", "w") as f:
        f.write(report)

def decoyFilesRelationship(decoyFilesInput):
    #Find amount of time each decoy file extension was used
    decoyFilesInput['fileExtension'] = decoyFilesInput.decoy_filename.str.split('.').str[-1]
    report="++++REPORT++++\nDecoy File Extensions Counts:\n"+str(decoyFilesInput['fileExtension'].value_counts())+"\n\n"

    #Find common phrases in emails sent by insiders
    decoyFilesInput['decoyFilesNames'] = decoyFilesInput.decoy_filename.str.split('.').str[0]
    decoyFilesInput['decoyFilesNames'] = decoyFilesInput.decoyFilesNames.str.split("\\").str[-1]
    content = [y for x in decoyFilesInput['decoyFilesNames'] for y in x.split()]
    n = [1]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=("Most Common Decoy File Names:\n"+str(count)+"\n\n")

    #Write report to report directory
    os.makedirs(os.path.dirname("./reports/Decoy File Relationship Report.txt"), exist_ok=True)
    with open("./reports/Decoy File Relationship Report.txt", "w") as f:
        f.write(report)

def emailsRelationship(emailsInput):
    #Start Report
    report="++++REPORT++++\nCommon Phrases in email sent by insiders:\n"

    #Find common phrases in emails sent by insiders
    emailsSentContent=emailsInput[emailsInput['activity']=='Send']['content'].dropna(how='all')
    content = [y for x in emailsSentContent for y in x.split()]
    n = [3,4]
    count = pd.Series([' '.join(y) for x in n for y in ngrams(content, x)]).value_counts().nlargest(5)
    report+=(str(count)+"\n\n")

    #Find attachments sent by insiders over emails
    attachments=emailsInput[emailsInput['activity']=='Send']['attachments'].dropna(how='all')
    attachmentNames = attachments.str.split(';').str[-1]
    attachmentNames = attachmentNames.str.split('(').str[0]
    mostCommonSentFiles = attachmentNames.str.split('\\').str[-1]
    mostCommonFileExtensions = mostCommonSentFiles.str.split('.').str[-1]
    report+="Most common files extensions in emails sent by insiders:\n"+str(mostCommonFileExtensions.value_counts().nlargest(5))+"\n\n"
    report+="Most common files sent by insiders:\n"+str(mostCommonSentFiles.value_counts().nlargest(5))+"\n\n"

    #Write report to report directory
    os.makedirs(os.path.dirname("./reports/Email Relationship Report.txt"), exist_ok=True)
    with open("./reports/Email Relationship Report.txt", "w") as f:
        f.write(report)

def psychometricsRelationship(psychometricsInput):
    #Start Report
    report="++++REPORT++++\n"

    #Count how many insiders had high scores of each personality trait
    report+="High BFI scores:\n"
    report+=(str(psychometricsInput[psychometricsInput["O"] >= 40].shape[0])+" insiders were found to have high levels of openness\n")
    report+=(str(psychometricsInput[psychometricsInput["C"] >= 40].shape[0])+" insiders were found to have high levels of conscientiousness\n")
    report+=(str(psychometricsInput[psychometricsInput["E"] >= 40].shape[0])+" insiders were found to have high levels of extraversion\n")
    report+=(str(psychometricsInput[psychometricsInput["A"] >= 40].shape[0])+" insiders were found to have high levels of agreeableness\n")
    report+=(str(psychometricsInput[psychometricsInput["N"] >= 40].shape[0])+" insiders were found to have high levels of neuroticism\n\n")

    #Count how many insiders had low scores of each personality trait
    report+="Low BFI scores:\n"
    report+=(str(psychometricsInput[psychometricsInput["O"] <= 20].shape[0])+" insiders were found to have low levels of openness\n")
    report+=(str(psychometricsInput[psychometricsInput["C"] <= 20].shape[0])+" insiders were found to have low levels of conscientiousness\n")
    report+=(str(psychometricsInput[psychometricsInput["E"] <= 20].shape[0])+" insiders were found to have low levels of extraversion\n")
    report+=(str(psychometricsInput[psychometricsInput["A"] <= 20].shape[0])+" insiders were found to have low levels of agreeableness\n")
    report+=(str(psychometricsInput[psychometricsInput["N"] <= 20].shape[0])+" insiders were found to have low levels of neuroticism\n")

    #Write report to report directory
    os.makedirs(os.path.dirname("./reports/Psychometric Relationship Report.txt"), exist_ok=True)
    with open("./reports/Psychometric Relationship Report.txt", "w") as f:
        f.write(report)
        
if __name__ == "__main__":
    emails = pd.read_csv('./data/combined/insiderOnly/email.csv', low_memory=False)
    psychometrics = pd.read_csv('./data/combined/psychometric.csv', low_memory=False)
    files = pd.read_csv('./data/combined/file.csv', low_memory=False)
    decoyFiles = pd.read_csv('./data/combined/decoy_file.csv', low_memory=False)

    filesRelationship(files)
    decoyFilesRelationship(decoyFiles)
    emailsRelationship(emails)
    psychometricsRelationship(psychometrics)