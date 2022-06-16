from dash import dcc, html, Input, Output, callback

image_Landing = 'assets/Imagen_Landing.svg'
image_Landing_pequeña = 'assets/Imagen_Landing_pequeña.svg'

layout = html.Div([

    html.Section(children=[

        html.Div(className='container1', children=[

            html.Div(className='Izquierda',children=[

                html.Div(
                    
                    html.H1('NOMBRE DEL APLICATIVO'),
                
                ),

                html.Br(),
                html.Br(),

                html.Div(

                    html.P(children=['Esta herramienta de visualización',html.Br(),
                        'gráfica le permitira establecer y evaluar ',html.Br(),
                        'la segmentación dinámica de perfiles ',html.Br(),
                        'comerciales y de clientes'
                    ]),

                ),

                html.Br(),
                html.Br(),
                html.Br(),

                html.Div(

                    html.A('VAMOS', href='/Dashboard',className='Boton'),

                ),

            ]),

            html.Div(className='Derecha',children=[

                html.Img(className='Imagen_grande',src=image_Landing),
                html.Img(className='Imagen_pequeña',src=image_Landing_pequeña),
                
            ]),

        ])

    ]),

    html.Section(className='contenedor2',children=[



        html.Div(className='titulo',children=[
                    
            html.H1('¿QUE HACEMOS?')
                
        ]),
      
        html.Div(className='sub-titulo',children=[

            html.P(children=[html.Br(),'Creamos una herramienta de visualización dinamica que permite segmentar clientes, ademas de crear un Score Model para la fundación',html.Br(),
            html.Br(),html.Br(),
            ]),

        ]),

        html.Div(className='secundario',children=[

            html.Div(className='dashboard',children=[

                html.A(href='/Dashboard',className='card', children=[
                    html.Div(className='thumb',id='img_dashboard',children=[

                    ]),

                    html.Article(children=[
                        html.H1('Dashboard'),
                        html.P('Presentamos metricas, KPI’s por año y mes, para que los usuarios puedan ver el comportamiento de los clientes'),
                    ]),
                ]),
            ]),

            html.Div(className='scorecard',children=[

                html.A(href='/Dashboard',className='card', children=[
                    html.Div(className='thumb',id='img_score',children=[

                    ]),

                    html.Article(children=[
                        html.H1('Score Model'),
                        #html.P('Descripción'),
                    ]),
                ]),
            ]),

            html.Div(className='como',children=[

                html.A(href='/Dashboard',className='card', children=[
                    html.Div(className='thumb',id='img_como',children=[

                    ]),

                    html.Article(children=[
                        html.H1('¿Como Lo Hacemos?'),
                    ]),
                ]),
            ]),

            html.Div(className='equipo',children=[

                html.A(href='/Dashboard',className='card', children=[
                    html.Div(className='thumb',id='img_equipo',children=[

                    ]),

                    html.Article(children=[
                        html.H1('Nuestro Equipo'),
                    ]),
                ]),
            ]),

            html.Div(className='fundacion',children=[

                html.A(href='/Dashboard',className='card', children=[
                    html.Div(className='thumb',id='img_fundacion',children=[

                    ]),

                    html.Article(children=[
                        html.H1('Sobre la fundación'),
                    ]),
                ]),
            ]),
        ]),

    ]),

])


""" @callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}' """