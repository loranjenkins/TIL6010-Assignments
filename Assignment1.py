# import libraries
import os
import pandas as pd

#bulletpoint 1.
# path to the downloaded data folder, e.g. 'Downloads/Region_Mobility_Report_CSVs/'

data_dir = '\\Users\\loran\\Desktop\\Mechanical engineering - Delft\Master\\2nd - Q1\\Programming\\Region_Mobility_Report_CSVs'
country_code = 'AG_Region_Mobility_Report.csv'

#bulletpoint 2.
all_files = os.listdir(data_dir)
print(all_files)
# initilisation
target_file_name = ''
year = '2020'

for file_name in all_files:
    # check if this file is for 2020
    is_year = '2020_' #hier geedit
    # if yes, we check if the file name is for the country that you select
    if is_year:
        # check if the country_code is in the file_name
        is_country = country_code #hier geedit
        if is_country:
            # found the file, save it to 'target_file_name'
            target_file_name = is_year + country_code
            # we stop looking by breaking out of the for loop
            break
if not target_file_name:
    print('File not found. Check your country code (or select a different one)!')

else:
    print('Found file name is: ' + target_file_name)
    # get the path to the file
    file_path = data_dir
    print('Path to the file is: ' + file_path)

#bulletpoint 3.

data_dir = pd.read_csv(r'C:\Users\loran\Desktop\Mechanical engineering - Delft\Master\2nd - Q1\Programming\2020_NE_Region_Mobility_Report.csv')