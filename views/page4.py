import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from datetime import date


REFRESH_INTERVAL = dcc.Interval(
    id='interval-component', interval=4*150005, n_intervals=0)
searchandadd = html.Div([
    dbc.Card([
        html.Hr(),

        dbc.CardBody([


            dbc.CardBody([
                dbc.Row(
                    dbc.Col([
                        html.H5('Searchin Criteria: '),
                        dcc.Dropdown(
                            id='search-field',
                            options=[
                                {'label': 'animal_id', 'value': 'animal_id'},
                                {'label': 'name', 'value': 'name'}
                            ],
                            value='animal_id'),
                        html.H5('Keyword: '),
                        dbc.Input(id='search-key',
                                  type='text',
                                  placeholder='Write your keyword', style={'margin-top': '10px'}),
                        dbc.Button("Search", id='search-button',
                                   color="primary", style={'margin-top': '10px'})
                    ], width=3)
                ),
                dbc.Row(
                    dbc.Col(
                        html.Div(id='search-result'), width=9
                    ), style={'margin-top': '20px'}
                )
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'}),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.H5('Animal Name'),
                        dbc.Input(id='add-name',
                                  type='text',
                                  placeholder='name'),
                        html.H5("Animal Type:"),
                        dcc.Dropdown(
                            id='add-animaltype',
                            options=[
                                {'label': 'Dog', 'value': 'Dog'},
                                {'label': 'Cat', 'value': 'Cat'},
                                {'label': 'Bird', 'value': 'Bird'},
                                {'label': 'Livestock', 'value': 'Livestock'},
                                {'label': 'Other', 'value': 'Other'}
                            ],
                            placeholder='animal_type'),
                        html.H5('Animal Id:'),
                        dbc.Input(id='add-animalid',
                                  type='text',
                                  placeholder='animal_id')
                    ], width=3),
                    dbc.Col([
                        html.H5("Age upon Outcome"),
                        dbc.Input(id='add-age',
                                  type='text',
                                  placeholder='age_upon_outcome'),
                        html.H5('Color'),
                        dbc.Input(id='add-color',
                                  type='text',
                                  placeholder='color'),
                        html.H5('Breed:'),
                        dbc.Input(id='add-breed',
                                  type='text',
                                  placeholder='breed')
                    ], width=3),
                    dbc.Col([
                        html.H5('Outcome Type:'),
                        dcc.Dropdown(
                            id='add-outcometype',
                            options=[{"label": i, "value": i} for i in ['Return to Owner', 'Transfer', 'Adoption', 'Euthanasia', 'Died',
                                                                        'Disposal', 'Relocate', 'Missing', 'Rto-Adopt', 'NaN', 'dfhfdh']],
                            placeholder='outcome_type'),
                        html.H5('Outcome Subtype'),
                        dcc.Dropdown(
                            id='add-outcomesubtype',
                            options=[{"label": i, "value": i} for i in ['NaN', 'Partner', 'Rabies Risk', 'Aggressive', 'Foster',
                                                                        'Suffering', 'SCRP', 'Offsite', 'Enroute', 'Medical', 'In Foster',
                                                                        'In Kennel', 'Behavior', 'Court/Investigation', 'Barn', 'At Vet',
                                                                        'Possible Theft', 'Snr', 'Underage', 'In Surgery', 'fghhgfjsdf']],
                            placeholder='outcome_type'),
                        html.H5('Outcome Sex'),
                        dbc.Input(id='add-sexuponoutcome',
                                  type='text',
                                  placeholder='sex_upon_outcome')
                    ], width=3),
                    dbc.Col([
                        html.H5('Birthdate:'),
                        dcc.DatePickerSingle(
                            id='add-birthdate',
                            min_date_allowed=date(1990, 1, 1),
                            max_date_allowed=date.today(),
                            initial_visible_month=date.today(),
                            date=date.today(), style={'margin-bottom': '10px'}),
                        html.Br(),
                        dbc.Button("Add", id='add-button',
                                   color="primary"),
                        dcc.ConfirmDialog(
                            id='add-confirm',
                            message="New record added!",
                        )])
                ]),
                dbc.Row(
                    dbc.Col(
                        html.Div(id='search-result2'), width=9
                    ), style={'margin-top': '20px'}
                )
            ], style={'backgroundColor': '#B8D9F4', 'margin-bottom': '15px'})
        ], style={'backgroundColor': '#AAAAAA'})

    ]),
    html.Hr(),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
