'''This script runs the IPCW survival estimation by MELD score given
    a set of A and B files.

    Name: Nicholas Wood, PhD
    Institution: USNA
    Email: nwood@usna.edu
'''
import pandas as pd
from IPCW import IPCW


##########################################################################################################
#USER INPUTS
##########################################################################################################
#These can be changed as desired.
##########################################################################################################

#Point to the A and B files
dfA_path = r'C:\Users\Nicholas\Documents\SRTR Survival Files\Survival Data 01-01-2019 to 01-01-2020\MELD-Na A File.csv'
dfB_path = r'C:\Users\Nicholas\Documents\SRTR Survival Files\Survival Data 01-01-2019 to 01-01-2020\MELD-Na B File.csv'

#Define the time up to which you want to calculate survival
t = 90

#Define the column name that identifies candidates
ident_col = 'px_id'

#Define the column name that identifies the MELD score being used
meld_col = 'MELD-Na'

#Define the column name that identifies time
time_col = 'Days'

#Define the column name that identifies death
death_col = 'Death'

#Define the column name that identifies transplant
tx_col = 'Transplant'

#Do want the survival calculation to be fast (but less accurate)? For testing purposes I recommend yes.
#For long study periods (e.g. > 10 years) the calculation can be a little slow (in excess of an hour).
fast = True

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################




#Read in the A and B files
dfA = pd.read_csv(dfA_path)
dfB = pd.read_csv(dfB_path)

#Create the IPCW object
ipcw = IPCW(dfA, dfB, t = t, ident_col = ident_col, time_col = time_col, meld_col = meld_col,
            death_col = death_col, tx_col = tx_col, fast = fast)


#Calculate survival by MELD score
ipcw.CalculateSurvivalByMELD()

#Save the survival data to a file in your local directory
ipcw.SaveSurvivalData(f'IPCW Survival by {meld_col}.csv')

#Plot!
ipcw.PlotSurvivalByMELD(t)


