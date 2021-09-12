# import libraries
import os
import pandas as pd
import requests
import matplotlib.pyplot as plt


#bulletpoint 1.
# path to the downloaded data folder, e.g. 'Downloads/Region_Mobility_Report_CSVs/'

data_dir = '\\Users\\loran\\Desktop\\Mechanical engineering - Delft\Master\\2nd - Q1\\Programming\\Region_Mobility_Report_CSVs'
country_code = 'NL'

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

df_2020 = pd.read_csv(r'C:\Users\loran\Desktop\Mechanical engineering - Delft\Master\2nd - Q1\Programming\2020_NL_Region_Mobility_Report.csv')
a = print(df_2020.iloc[0:10, :])


#bulletpoint 4.

df_2021 = requests.get("http://mirrors-dev.citg.tudelft.nl:8083/google-mobility-data/2021/NE")
if df_2021.status_code == 200:
    print('Success!')
elif df_2021.status_code == 404:
    print('Not Found.')

with open("df_2021.txt", "w") as f:
    f.write(df_2021.text)

file = open("df_2021.txt")
lines_to_print = [0,1,2,3,4,5,7,8,9,10,11]
for index, line in enumerate(file):
  if ( index in lines_to_print):
    print(line)

# #bulletpoint 5. merge 2 dataframes how is this possible?
# df1 = pd.DataFrame(df_2020)
# df2 = pd.DataFrame(df_2021)
# Merged = df1.merge(df2)

#bulletpoint 6 just with standard df 2020
df_nation = df_2020[['country_region_code','country_region']]
df_nation = df_nation.iloc[0:10,:]
df_province = df_2020[["sub_region_1"]]
print(df_province)
df_province = df_province.iloc[0:10,:]
df_city= df_2020[["sub_region_2"]]
df_city = df_city.iloc[0:10,:]
print(df_nation.isna())
print(df_province.isna())
print(df_city.isna())


#bulletpoint 7
df_nation.to_csv (r'C:\Users\loran\PycharmProjects\TIL6010-Assignments\data_dir\processed_data\df_nation.to_csv', index = False, header=True)
df_province.to_csv (r'C:\Users\loran\PycharmProjects\TIL6010-Assignments\data_dir\processed_data\df_province.to_csv', index = False, header=True)
df_city.to_csv (r'C:\Users\loran\PycharmProjects\TIL6010-Assignments\data_dir\processed_data\df_city.to_csv', index = False, header=True)

##PART 2 - Simple Data processing
#1
df_nation_workplace = df_2020[['workplaces_percent_change_from_baseline']].mean()
df_nation_parks = df_2020[['parks_percent_change_from_baseline']].mean()
df_nation_transit_stations = df_2020[['transit_stations_percent_change_from_baseline']].mean()
print(df_nation_workplace)
print(df_nation_parks)
print(df_nation_transit_stations)

#2
df_province = df_2020[["sub_region_1"]]
Amount_provinces_total = df_province.count()
print(Amount_provinces_total)

#3 __> idk yet
df_province1 = df_2020[["sub_region_1", "workplaces_percent_change_from_baseline"]]
Amount_provinces = df_province1.value_counts()
print(Amount_provinces)
province_highest_value = Amount_provinces.iloc[-1:]
print('Province with highest workplace is: ' + str(province_highest_value))

#4
df_workplace_high = df_2020.loc[df_2020.sub_region_1.str.contains("Zeeland", na=False)]
print(df_workplace_high)

#5
df_date = df_workplace_high['date']
print(df_date)
dt_date = pd.to_datetime(df_date)
print(dt_date)
df_workplace_high.loc[:,('date2')] = dt_date
print(df_workplace_high)

#6
df_province_largest = df_workplace_high.sort_values(by='date2',ascending=True)
print(df_province_largest)


# Execute the cell with the following command to visualize the results
df_province_largest.plot('date', 'workplaces_percent_change_from_baseline')
plt.show()
df_province_largest.resample('7D', on='date2').sum()['workplaces_percent_change_from_baseline'].plot()
plt.show()