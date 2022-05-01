# TextMining
Dataset:
The CERT  Insider Threat Test Dataset is a collection of synthetic insider threat test datasets that provide both background and malicious actor synthetic data. The dataset is maintained by Carnegie Melon University and serves as the industry standard for insider screening testing. The data contains 9 different releases each adding new functionality to that of earlier releases.

Preprocessing:
The dataset is 87.23 GB of insider test data. All of the data across 9 releases were downloaded and pre-processed to meet our needs. 
The goal of this project is to find insight into insider threats within this dataset. To do so we only needed to look at the following categories of data: emails, files, decoy files, and psychometric data. From this subset, we further narrowed our scope by removing data that was not associated with insider incidents. We separated this data by making scripts to isolate insider data for each release. Additional scripts were used to then merge the data for each release into a Masterfile. Each release introduced different functionality upon prior data, this was addressed by adding empty fields for missing data.
All of the scripts created to process the data can be found in the Git Repo under “combinationScripts”. To run code an additional download is necessary. The data used in this repo is larger than GitHub's file upload size limit. 

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

Mining:
    Our mining focused on two major tasks: identification of trends and a insider threats within emails

    Identification of Trends:
        Decoy files, emails, files, and psychometric data
        The most common phrases and file extensions through Ngrams

    Develop a model for identifying insider threats:
        Utilizing a corpus of insider attacks to identify potential insider threats
        Creating a custom stoplist to identify potential insider threats

Results:
    The reports directory has the results of our text mining

**Note
The data directory is hidden in the .gitignore by default.