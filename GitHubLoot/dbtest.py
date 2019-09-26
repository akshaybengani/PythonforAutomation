import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Scope refers to the connecting point where the oauthclient will communicate
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Credentials is the access key for the Google Account shared spreadsheet
credetials = ServiceAccountCredentials.from_json_keyfile_name('GithubLootAPI.json',scope)

# gc is the variable which holds the reference of whole spreadsheet containing all workbook
gc = gspread.authorize(credetials)

# wks is the variable containing the reference of the workbook
wks = gc.open('Free Stuff').worksheet('hacktoberfest')

# To Print whole worksheet
'''print(wks.get_all_records())'''

# To Add row at the end of the last row
'''wks.append_row(['akshaybengani456@gmail.com','123456'])'''

# To Delete a row with an index
'''wks.delete_row(2)'''

# To get a position of a value
'''print(wks.find('123456')._col)'''
'''print(wks.find('123456')._row)'''

# To get value of a particular cell with its cell ID
# Example A1 A2 A10 B1 B2 B10
'''print(wks.acell('A1').value)'''

# To get value of a particular cell by spreadsheet matrix
'''print(wks.cell(1,2).value)'''

# To get value of a whole row from sheet
'''print(wks.row_values(2))'''

# To get value of a whole column from sheet
'''print(wks.col_values(1))'''

# To get cell reference in a variable
'''cell = wks.cell(1,3)'''

# Get data from cell reference
'''data = cell.value'''
'''rown = cell.row'''
'''coln = cell.col'''
'''print(rown,coln)'''

# Update data in a cell
'''wks.update_acell('b4','123456')'''
    # row x column
'''wks.update_cell(4,1,'akshaybengani789@gmail.com')'''



