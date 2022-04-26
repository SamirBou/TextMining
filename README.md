# TextMining
To run code an additional download is necessary. The data used in this repo is larger than GitHub's individual file upload size.

Download the zip file from this link: 
https://anonfiles.com/P4f6qda9yf/data_zip

Extract the "data" folder from within the zip to the root of the repo. After extracting the folder running the following scripts in this order.
    1. combinationScripts/decoyMerge.py
    2. combinationScripts/emailMerge.py
    3. combinationScripts/fileMerge.py
    4. combinationScripts/psychometricMerge.py
    5. combinationScripts/insiderOnly/insidersOnlyEmailMerger.py
    6. combinationScripts/insidersWithNormal.py

These scripts perform data processing and export the following files to the /data/combined directory
    /data/combined/decoy_file.csv
    /data/combined/file.csv
    /data/combined/email.csv
    /data/combined/insidersWithNormal.csv
    /data/combined/psychometric.csv
    /data/combined/insiderOnly/email.csv    

**Note
The data directory is hidden in the .gitignore by default.