import pandas as pd 
import numpy as np
import shutil
import datetime
import calendar
import glob

ahora = datetime.datetime.now()
current_month = ahora.month
current_year =  ahora.year
month = calendar.month_name[current_month]


chase_files = glob.glob("C:/Users/MasterRace/Downloads/*Chase*")
for chase_file in chase_files:
    new_chase_name = chase_file.replace(chase_file, f"{current_year} {month} Chase.csv")
    new_location = "C:/Users/MasterRace/Desktop/Computer/Finance/"+ new_chase_name
    shutil.move(chase_file, new_location)

discover_files = glob.glob("C:/Users/MasterRace/Downloads/*Discover*")
for discover_file in discover_files:
    new_discover_name = discover_file.replace(discover_file, f"{current_year} {month} Discover.csv")
    new_location = "C:/Users/MasterRace/Desktop/Computer/Finance/"+ new_discover_name
    shutil.move(discover_file, new_location)


# Discover statements excel transformations
discover_statement = pd.read_csv(f'{current_year} {month} Discover.csv')
#deletes first 13 rows
#discover_statement = discover_statement.drop(discover_statement.index[:13]) 
discover_statement = discover_statement.reindex(columns=['Trans. Date', 'Post Date', 'Description', 'Category', 'Amount'])
discover_statement["Amount"] = discover_statement["Amount"].apply(lambda x: x*-1)
#discover_statement = discover_statement.drop(discover_statement.index[0]) 

#discover_statement = discover_statement.sort_values(by='Trans. Date', ascending= False)

discover_statement.to_excel(f"{current_year} {month} Discover.xlsx", index=False)


# Chase statement transformations
chase_statement = pd.read_csv(f'{current_year} {month} Chase.csv')
chase_statement = chase_statement.drop(['Type','Memo'], axis=1)

chase_statement.to_excel(f'{current_year} {month} Chase.xlsx', index=False)

#combining files together
discover_excel = pd.read_excel(f'{current_year} {month} Discover.xlsx')
chase_excel = pd.read_excel(f'{current_year} {month} Chase.xlsx')

combined_files = chase_excel[['Transaction Date', 'Post Date', 'Description', 'Category', 'Amount']].merge(discover_excel[['Trans. Date', 'Post Date', 'Description', 'Category', 'Amount']], on = "Transaction Date", how = 'left')
#combined_files = combined_files.sort_values(by='Transaction Date', ascending= False)
combined_files.to_excel(f'{current_year} {month} Fin Report.xlsx')
