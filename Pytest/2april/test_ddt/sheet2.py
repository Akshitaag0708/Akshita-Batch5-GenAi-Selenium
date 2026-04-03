import openpyxl
import pytest
def get_test_data():
    wb=openpyxl.load_workbook("test.xlsx")        # if it is in same directory direct pass file name otherwise full path
    ws=wb["sheet1"]

    data=[]

    for row in ws.iter_rows(min_row=2,values_only=True):
        data.append(row)
    return data

# print(get_test_data())