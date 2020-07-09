from flask import Flask
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import os

# -----------------------------------------------------------------------------
# Importing Google Sheet data to a Pandas DataFrame and displaying it

googleSheetId = '1gL84hsdrVc-V5Dym02caCBUXjQLHd5LoIRMa2uqxD-E'
worksheetName = 'Sheet1'
url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId,worksheetName)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Flask(__name__) #Reference https://dash.plotly.com/deployment
dash = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=app)

# Eading GoogleSheet CSV to Dataframe
df = pd.read_csv(url)

# Dropping null value columns to avoid errors
df.dropna(inplace = True)

# New Datafram with split value columns
splitdf = df["Programming Language"].str.split(",", n = 1, expand = True)
print(splitdf)

# makeing seperate column for first programming language
df["PL1"] = splitdf[0]
# makeing seperate column for second programming language
df["PL2"] = splitdf[1]


df.drop(columns =["Programming Language"], inplace = True) 


print(df)

app.layout = Div([

    H3('Test header'),

])