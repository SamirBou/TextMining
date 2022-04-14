import sys
import pandas as pd

#Decoy_files
decoy_filesR52 = pd.read_csv('./data/r5.2/decoy_file.csv', low_memory=False)
decoy_filesR61 = pd.read_csv('./data/r6.1/decoy_file.csv', low_memory=False)
decoy_filesR62 = pd.read_csv('./data/r6.2/decoy_file.csv', low_memory=False)

combinedDecoy_files= pd.merge(decoy_filesR52,decoy_filesR61, how='outer', on=["decoy_filename","pc"]).fillna("")
combinedDecoy_files= pd.merge(combinedDecoy_files.astype(str),decoy_filesR62.astype(str), how='outer', on=["decoy_filename","pc"]).fillna("")

combinedDecoy_files.to_csv("./data/combined/decoy_file.csv", index = False)