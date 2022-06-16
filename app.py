from dash import Dash, dcc, html, Input, Output, callback
from pages import Dashboard, inicio


app = Dash(__name__, suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])

server = app.server

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),

    html.Div(children=[

        html.Header(children=[

            html.Img(src=app.get_asset_url('Logo.svg')),

            html.Nav(className = "nav_links", children=[

                html.Ul(children=[
                    html.Li(children=[html.A('Inicio', href='/inicio')]),
                    html.Li(children=[html.A('Dashboard', href='/Dashboard')]),
                    html.Li(children=[html.A('Score Model', href='/Score Model')]),
                    html.Li(children=[html.A('¿Como lo Hacemos?', href='/¿Como lo hacemos?')]),
                    html.Li(children=[html.A('Nuestro Equipo', href='/Nuestro Equipo')])
                ])

            ])

        ]),

        html.Div(id='page-content'),
    
    ]),

]) 


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/inicio':
        return inicio.layout
    elif pathname == '/Dashboard':
        return Dashboard.layout
    else:
        return inicio.layout

if __name__ == '__main__':
    app.run_server(debug=True)