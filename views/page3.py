import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from datetime import date


REFRESH_INTERVAL = dcc.Interval(
    id='interval-component', interval=4*15000005, n_intervals=0)
byanimal = html.Div([
    dbc.Card(
        dbc.CardBody([

            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.H5('Animal Type'),
                        dcc.Dropdown(
                            id='animaltype-dropdown',
                            options=[
                                {'label': 'Bar', 'value': 'Bar'},
                                {'label': 'Pie', 'value': 'Pie'}
                            ],
                            value='Pie'),
                            
                        html.H5(
                            "Birth Date"),
                        dcc.DatePickerRange(
                            id='birthdate-datepicker',
                            min_date_allowed=date(1991, 12, 11),
                            max_date_allowed=date(2017, 12, 25),
                            initial_visible_month=date(2017, 12, 25),
                            start_date=date(1991, 12, 11),
                            end_date=date(2017, 12, 25)
                        ),
                        dbc.Card(
                        [
                            dbc.CardImg(
                                id='selected-animal-card',
                                top=True, style={'height': '220px'}),
                            dbc.CardBody(
                                html.H4(children=None,
                                        id='number-selected-animal-card')
                            ),
                        ],style={'margin-top': '10px'}
                    )
                    ], width = 4),
                    dbc.Col(dcc.Graph(id='plot1'), width = 8)
                ])
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),

            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(
                            id='select-pieces-plot2',
                            options=[
                                {'label': 'breed', 'value': 'breed'},
                                {'label': 'color', 'value': 'color'},
                                {'label': 'name', 'value': 'name'},
                                {'label': 'sex_upon_outcome', 'value': 'sex_upon_outcome'}
                            ],
                            value='breed'),
                        dcc.Slider(
                            id='slider_x',
                            min=10,
                            max=50,
                            step=5,
                            className = 'app-slider-color',
                            value=20,
                            updatemode='mouseup',
                            marks={'10': '10', '20': '20', '30': '30', '40': '40', '50': '50'}),
                        dcc.Graph(id='plot2')
                    ], width = 8),
                    dbc.Col([
                        html.H4('Types and Subtypes'),
                        dcc.Graph(id='plot3')
                        ], width=4)
                ])
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),

            html.Hr()

        ], style={'backgroundColor': '#AAAAAA'})

    ),
    html.Hr(),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
