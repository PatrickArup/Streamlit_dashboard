import streamlit as st
import pandas as pd
from openpyxl import load_workbook


#Title within page
st.title("New tender announcements")


## Load file
Filename = 'Temporary test file.xlsx'
book = load_workbook(Filename)
#Read data
xls = pd.ExcelFile(Filename, engine='openpyxl')
dataset = pd.read_excel(xls,sheet_name='Sheet name 1')

##Set query
#filter for Tender interest = "Undecided" and date = Today() + 15 days
dataset_filter=dataset.query(
    '(`Column 1` > 50) and (`Column 2` < 50)'
)

Accepted_interest = ['Interest', 'No interest', 'Undecided']


## Display table
#Editable data table with locked columns with names indicated
newdata = st.data_editor(dataset_filter, 
               key="Data_editor",
               disabled=("Column 2","Column 3","Column 5"))

dataset.update(newdata)
#if calculate: 





## Save data
# use `with` to avoid other exceptions
with pd.ExcelWriter(Filename, engine="openpyxl") as writer:
    writer.book = book
    writer.sheets.update(dict((ws.title, ws) for ws in book.worksheets))

    dataset.to_excel(writer, sheet_name='Sheet name 1', index=False)


