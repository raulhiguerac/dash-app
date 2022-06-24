from enum import auto
from pydoc import classname
from dash import dcc, html, Input, Output, callback
import pandas as pd

df = pd.read_csv('./data/Fundacion Agrupada.csv',sep=';')

layout = html.Div(className='app',children=[
    html.Div(className='menu-toggle',children=[
        html.Div(className='hamburger',children=[
            html.Span()
        ]),
    ]),

    html.Aside(className='sidebar',children=[
        html.H3('Seleccione la caracteristica para filtrar'),
        html.Nav(className='menu',children=[
            html.H3('Año'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()]
                        ,className='menu-item is-active'
                        ,placeholder="Año",
                        ),
            html.H3('Mes'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Mes",),
            html.H3('Regional'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Regional",),
            html.H3('Asignado a'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Asignado a",),
            html.H3('Linea'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Linea'].unique()],
                        className='menu-item',
                        placeholder="Linea",),
            html.H3('Tipo cliente'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Nom tipoCliente'].unique()],
                        className='menu-item',
                        placeholder="Tipo cliente",),
            html.H3('Genero'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Genero",),
            html.H3('Nivel de estudios'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Nivel de estudios",),
            html.H3('Ciudad de residencia'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Ciudad de residencia",),
            html.H3('Estado civil'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Estado civil",),
            html.H3('Ocupación'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Ocupación",),
            html.H3('Profesión u oficio'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Profesión u oficio",),
            html.H3('Sector'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Sector",),
            html.H3('Tipo de vivienda'),
            dcc.Dropdown(id='demo-dropdown',
                        options=[{'label': k, 'value': k} for k in df['Region'].unique()],
                        className='menu-item',
                        placeholder="Tipo de vivienda",),
        ]),
    ]),

    html.Main(className='content',children=[
        html.H1('Welcome, Human'),
        html.P('Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officia, explicabo!'),
        html.Div(className='contenedor-dashboard',children=[
            dcc.Tabs([

                
                dcc.Tab(label='Dashboard Fundación Amacener', children=[
                    html.Br(),
                    html.Div(className='contenedor_pestaña_1',children=[
                        html.Div(className='mini_container',children=[
                            html.H3('Obligaciones Vigentes'),
                            html.H1('1234'),
                        ]),
                        html.Div(className='mini_container',children=[
                            html.H3('Saldo Obligaciones'),
                            html.H1('1234'),
                        ]),
                        html.Div(className='mini_container',children=[
                            html.H3('Nuevos Creditos'),
                            html.H1('1234'),
                            html.H4(''),
                        ]),
                        html.Div(className='mini_container',children=[
                            html.H3('ICV'),
                            html.H1('1234'),
                            html.H4(''),
                        ]),
                        html.Div(className='gaficas_1',children=[
                            dcc.Graph(
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                                            'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                                        'type': 'bar', 'name': u'Montréal'},
                                    ]
                                },responsive=True
                            ),
                        ]),
                        html.Div(className='gaficas_1',children=[
                            dcc.Graph(
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                                            'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                                        'type': 'bar', 'name': u'Montréal'},
                                    ]
                                },responsive=True
                            ),
                        ]),
                        html.Div(className='gaficas_1',children=[
                            dcc.Graph(
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                                            'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                                        'type': 'bar', 'name': u'Montréal'},
                                    ]
                                },responsive=True
                            ),
                        ]),
                        html.Div(className='gaficas_1',children=[
                            dcc.Graph(
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                                            'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                                        'type': 'bar', 'name': u'Montréal'},
                                    ]
                                },responsive=True
                            ),
                        ]),
                    ]),
                ]),

                dcc.Tab(label='Tab two', children=[
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [1, 4, 1],
                                    'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [1, 2, 3],
                                'type': 'bar', 'name': u'Montréal'},
                            ]
                        }
                    ),
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [1, 4, 1],
                                    'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [1, 2, 3],
                                'type': 'bar', 'name': u'Montréal'},
                            ]
                        }
                    )
                ]),

                dcc.Tab(label='Tab three', children=[
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [2, 4, 3],
                                    'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [5, 4, 3],
                                'type': 'bar', 'name': u'Montréal'},
                            ]
                        }
                    )
                ]),

            ]),
            #html.Div(id='tabs-content-example-graph')
        ])
    ])
])

""" @callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))

def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3, 4],
                        'y': [3, 1, 2, 10],
                        'type': 'bar'
                    }]
                },
                responsive= True,
            )
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ]) """