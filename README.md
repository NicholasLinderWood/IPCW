# IPCW
Within this repository contains all the code required to calculate bias corrected without-transplant survival using inverse probability censoring weights (IPCW). To run this analysis I assume the user of this code has access to the following standard analysis files from the Scientific Registry of Transplant Recipients:

cand_liin.dta, stathist_liin.dta

DESCRIPTION OF FILES:

Generate Data Set.py - Script that creates three data sets. A "MasterFile" from which are created an "A" file and a "B" file. These files are formatted in such a way to be used for Kaplan-Meier/IPCW survival analysis. See the file for additional details.

Generate_Master_File.py - Generate Data Set.py

Convert_Master_File_to_A_and_B_Files.py - Used by Generate Data Set.py

IPCW.py - Contains the class definition for the IPCW survival estimator. Used by RunIPCW.py

KaplanMeier.py - Contains the class definition for KaplanMeier survival estimator. Used by RunIPCW.py and IPCW.py

RunIPCW.py - Contains the code that will run the IPCW analysis. You will need to create the A and B files (using Generate Data Set.py) prior to running this script.

If you have any questions regarding the code, analysis, etc. please feel free to contact me at nwood@usna.edu.
