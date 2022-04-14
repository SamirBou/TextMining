import sys
import pandas as pd

#Files
filesR31 = pd.read_csv('./data/r3.1/file.csv', low_memory=False)
filesR32 = pd.read_csv('./data/r3.2/file.csv', low_memory=False)
filesR41 = pd.read_csv('./data/r4.1/file.csv', low_memory=False)
filesR42 = pd.read_csv('./data/r4.2/file.csv', low_memory=False)
filesR51 = pd.read_csv('./data/r5.1/file.csv', low_memory=False)
filesR52 = pd.read_csv('./data/r5.2/file.csv', low_memory=False)
filesR61 = pd.read_csv('./data/r6.1/file.csv', low_memory=False)
filesR62 = pd.read_csv('./data/r6.2/file.csv', low_memory=False)

combinedFiles= pd.merge(filesR31,filesR32, how='outer', on=["id","date","user","pc","filename","content"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR41.astype(str), how='outer',on=["id","date","user","pc","filename","content"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR42.astype(str), how='outer',on=["id","date","user","pc","filename","content"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR51.astype(str), how='outer',on=["id","date","user","pc","filename","content"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR52.astype(str), how='outer',on=["id","date","user","pc","filename","content","activity","to_removable_media","from_removable_media"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR61.astype(str), how='outer',on=["id","date","user","pc","filename","content","activity","to_removable_media","from_removable_media"]).fillna("")
combinedFiles= pd.merge(combinedFiles.astype(str),filesR62.astype(str), how='outer',on=["id","date","user","pc","filename","content","activity","to_removable_media","from_removable_media"]).fillna("")

combinedFiles.to_csv("./data/combined/file.csv", index = False)