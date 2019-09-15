import dash_editor_components
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_editor_components.PythonEditor(
        id='input'
    ),
	html.Button('Copy code', id='button'),
	html.P(id='output')
])

@app.callback(
	Output('output', 'children'),
	[Input('button', 'n_clicks')],
	[State('input', 'value')]
)
def copycode(n, code):
	if n:
		return code

if __name__ == '__main__':
    app.run_server(debug=True)
