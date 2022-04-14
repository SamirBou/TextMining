import sys
import pandas as pd

#Psychometrics
psychometricsR2 = pd.read_csv('./data/r2/psychometric.csv', low_memory=False)
psychometricsR31 = pd.read_csv('./data/r3.1/psychometric.csv', low_memory=False)
psychometricsR32 = pd.read_csv('./data/r3.2/psychometric.csv', low_memory=False)
psychometricsR41 = pd.read_csv('./data/r4.1/psychometric.csv', low_memory=False)
psychometricsR42 = pd.read_csv('./data/r4.2/psychometric.csv', low_memory=False)
psychometricsR51 = pd.read_csv('./data/r5.1/psychometric.csv', low_memory=False)
psychometricsR52 = pd.read_csv('./data/r5.2/psychometric.csv', low_memory=False)
psychometricsR61 = pd.read_csv('./data/r6.1/psychometric.csv', low_memory=False)
psychometricsR62 = pd.read_csv('./data/r6.2/psychometric.csv', low_memory=False)

combinedPsychometrics= pd.merge(psychometricsR2,psychometricsR31, how='outer', on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR32.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR41.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR42.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR51.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR52.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR61.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")
combinedPsychometrics= pd.merge(combinedPsychometrics.astype(str),psychometricsR62.astype(str), how='outer',on=["employee_name","user_id","O","C","E","A","N"]).fillna("")

combinedPsychometrics.to_csv("./data/combined/psychometric.csv", index = False)