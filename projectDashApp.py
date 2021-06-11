import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px


import pandas as pd 
pd.options.plotting.backend = "plotly" 

app = dash.Dash(__name__)
data = pd.read_excel('kbo2020.xlsx')
#data = data.set_index(['팀명','선수명'])
data = data.set_index(['팀명'])
app.layout = html.Div([
    html.P("팀명:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['두산','롯데','삼성','키움','한화','KIA','KT','LG','NC','SK']
        ],
        value='두산',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_graph(val):
    fig= px.bar(data.loc[val], x='선수명',y='타율', barmode='group', hover_data=['타수','안타','2루타','3루타','홈런'] \
                , color='2020연봉', title='2020년 '+ val +'선수 타율')
    return fig

app.run_server(debug=True)
