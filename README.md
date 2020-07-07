# Python-Challenge
General notes:
- Used python to calculate required data for each of the Pybank and Pypoll data files.  
- Files stored as Bankmain and Pollmain in the Python-Challenge main folder to facilitate uploading to the github repo.  Read / write data paths updated in order to read from the Resources folder and write back to the same folder
- Once completed, re-created Pollmain analysis using Jupyter and Pandas to calculate the data.  Did not write results to an output file
- In general, I found working with the data in python easier, likely due to a lack of familiarity with the functions available in Panda.  Panda is useful in initially looking at the data, understanding the file, and summarizing the info.  But, I thought the calculating the individual tallies was easier in Python.


7/6:
Pollpanda:
- Calculated individual candidate votes received by using "groupby" and "get_group" fucntions.  Created new dictionary with vote counts and percentages for each candidate and formatted using pd.DataFrame
Pollmain and Bankmain:
-  Deleted variable references where no initial value was required.  For example, do not need to initial declare the variable "Winval" as "Winval = ()"
 

7/4:
Continued working on using Panda to analyze data and format output
- Able to calculate values using value_count function for "Candidate" but need to work on extracting individual candidate vote counts in order to calulate percentage of vote received


7/3:
Tried using Jupyter notebook and pandas to re-create Pollmain analysis under filename Pollpanda


6/28:
Uploaded first working drafts of PyBank and PyPoll projects labeled Bankmain and Pollmain, respectively.  Moved files from .git folders to the main Python Challenge folders to facilitate uploading.

Potential items to improve in python files include:
- Simplifying code to include function references if relevant
- Eliminating initial variable definitions if initial value not required

