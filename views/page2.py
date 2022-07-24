import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from datetime import date

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

REFRESH_INTERVAL = dcc.Interval(
    id='interval-component', interval=4*150005, n_intervals=0)
index = html.Div([
    dbc.Card([
        html.Hr(),

        dbc.CardBody([

            dbc.CardBody([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179334919-0d539a05-e3b2-4c9d-a764-052d2c4e0f86.jpg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("All"),
                                        html.H4(children=None,
                                                id='all-numbers')
                                    ]),
                                ],
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179326921-0a70f671-2f7e-4af7-b17a-642c81293940.jpeg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("Cats"),
                                        html.H4(children=None,
                                                id='cat-numbers')
                                    ]),
                                ],
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179327013-973f27b9-b3ce-4310-8f40-ce8cd5b66296.jpg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("Dogs"),
                                        html.H4(id="dog-numbers")
                                    ]),
                                ],
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179327217-905907b0-5355-4db8-bfe1-2ebddea97bf0.jpeg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("Birds"),
                                        html.H4(id="bird-numbers")
                                    ]),
                                ],
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179327277-e941d449-db8d-4a42-804e-da3270372cdc.jpg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("Livestocks"),
                                        html.H4(id='livestock-numbers')
                                    ]),
                                ],
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://user-images.githubusercontent.com/70684994/179327356-ab0eb452-e87a-4218-a5d1-389e0510f024.jpeg", top=True, style={'height': '90px'}),
                                    dbc.CardBody([
                                        html.H2("Others"),
                                        html.H4(id="other-numbers")
                                    ]),
                                ],
                                #                    style={"width": "18rem"},
                            )
                        )
                    ], style={'text-align': 'center', 'margin-left': '15%', 'margin-right': '15%', 'width': 'auto'})])], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),


            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.P(
                            'Count all treatments or count only unique animals. . .  '),

                        dbc.RadioItems(
                            id="count-radio",
                            options=[
                                {"label": "Unique animals",
                                 "value": 'DISTINCT'},
                                {"label": "All treatments",
                                 "value": ''}
                            ],
                            value='DISTINCT',
                            inline=True
                        )
                    ], style={'margin-right': '15%'}),
                    dbc.Col([
                        html.P(
                            "Choose a Birthdate range for the animal you wanna see"),
                        dcc.DatePickerRange(
                            id='timestamp-datepicker',
                            min_date_allowed=date(2013, 10, 1),
                            max_date_allowed=date(2018, 2, 1),
                            initial_visible_month=date(2018, 2, 1),
                            start_date=date(2013, 10, 1),
                            end_date=date(2018, 2, 1)
                        )
                    ])
                ], style={'text-align': 'center', 'margin-left': '22%', 'margin-right': '22%', 'width': 'auto'})
            ], style={'backgroundColor': '#A16A9A', 'margin-bottom': '15px'}),



            dbc.CardBody([
                dbc.Row([
                    dbc.Col(dcc.Graph(id='animals-counts-pie'), width=6),
                    dbc.Col(dcc.Graph(id='outcome-counts-pie'), width=6)
                ])
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),

            dbc.CardBody([
                dbc.Row(
                    dbc.Col(dcc.Graph(id='yearly_counts'))
                )
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),

            dbc.CardBody([
                dbc.Row(
                    dbc.Col(dcc.Graph(id='outcome-counts'))
                )
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),

            dbc.CardBody([
                dbc.Row(
                    dbc.Col(dcc.Graph(id='weekly-outcome-counts'))
                )
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'})
        ], style={'backgroundColor': '#AAAAAA'})

    ]),
    html.Hr(),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
