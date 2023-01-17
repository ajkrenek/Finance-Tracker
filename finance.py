import pandas as pd 

# Discover statements excel transformations
discover_statement = pd.read_csv('Discover-Last12Months-20230109.csv')
#deletes first 13 rows
discover_statement = discover_statement.drop(discover_statement.index[:13]) 
discover_statement.columns = discover_statement.columns.tolist()
discover_statement.columns[3], discover_statement.columns[4] = discover_statement.columns[4], discover_statement.columns[3]
discover_statement = discover_statement[discover_statement.columns]
discover_statement = discover_statement.sort_values(by='Trans. Date', ascending= False)

discover_statement.to_excel('discover_file_reordered.xlsx', index=False)

# Chase statement transformations
chase_statement = pd.read_csv('Chase1318_Activity20220101_20221231_20230113.csv')
chase_statement = chase_statement.drop(['Type','Memo'], axis=1)
chase_statement.to_excel('chase_file_reordered.xlsx', index=False)
