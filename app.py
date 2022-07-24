
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import warnings

from datetime import datetime

from views.designDetails import *
from views.page2 import index
from views.page3 import byanimal
from views.page4 import searchandadd

from libs.helpy import *
from libs.sql_conn import *

warnings.filterwarnings('ignore')


BUTTONS = {}
BUTTONS['search'] = BUTTON(0)
BUTTONS['add'] = BUTTON(0)




##############################################
##################  App  #####################
##############################################

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME])
app.config.suppress_callback_exceptions = True
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div(
    [dcc.Location(id="url"), sidebar, content])




##############################################
################## Page - 1 ##################
##############################################

@app.callback([Output("all-numbers", "children"),
               Output("cat-numbers", "children"),
               Output("dog-numbers", "children"),
               Output("bird-numbers", "children"),
               Output("livestock-numbers", "children"),
               Output("other-numbers", "children"),
               Output("animals-counts-pie", 'figure')],
              [Input("count-radio", "value"),
              Input('timestamp-datepicker', 'start_date'),
              Input('timestamp-datepicker', 'end_date')])
def card_values(radio_value, startdate, enddate):
    counts = read_animals(query=f"""
        SELECT
            animal_type,
            COUNT({radio_value} animal_id)
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
        GROUP BY 1
        ORDER BY 2 DESC
        """)

    cat = animal_counts(counts, 'Cat')
    dog = animal_counts(counts, 'Dog')
    bird = animal_counts(counts, 'Bird')
    livestock = animal_counts(counts, 'Livestock')
    other = animal_counts(counts, 'Other')

    pie_chart = px.pie(counts, values='count', names='animal_type',
                             hover_data=['animal_type'],
                             title='Percentages of the Animal Counts by Types')
    pie_chart.update_traces(textposition='inside', textinfo='percent+label')

    return counts['count'].sum(), cat, dog, bird, livestock, other, pie_chart


@app.callback([Output("outcome-counts-pie", "figure"),
               Output('yearly_counts', 'figure'),
               Output('outcome-counts', 'figure'),
               Output('weekly-outcome-counts', 'figure')],
              [Input("count-radio", "value"),
              Input('timestamp-datepicker', 'start_date'),
              Input('timestamp-datepicker', 'end_date')])
def outcome_values(radio_value, startdate, enddate):
    counts = read_animals(query=f"""
        SELECT
            outcome_type,
            COUNT({radio_value} animal_id) as count_of_animals
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
        GROUP BY 1
        ORDER BY 2 DESC
        """)

    bar_chart = px.bar(counts, x='outcome_type', y='count_of_animals',
                       color='outcome_type',
                       text='count_of_animals',
                       title='Numbers of the Animal Counts by Outcomes')

    yearly = read_animals(query=f"""
        SELECT
            animal_type,
            CAST(EXTRACT(year from date_of_birth) as integer) as birth_year,
            COUNT({radio_value} animal_id)
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
        GROUP BY 1,2
        ORDER BY 2 DESC, 3 DESC
        """)

    yearly_bar = px.bar(yearly, x='birth_year', y='count',
                        color='animal_type',
                        text='count',
                        title='Animals Counts by Birth Year')


    outcomes = read_animals(f"""
        SELECT
            animal_type,
            outcome_type,
            COUNT({radio_value} animal_id) as count_
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
        GROUP BY 1,2
        ORDER BY 3 DESC
        """)


    outcome_bar = px.bar(outcomes, x= 'outcome_type', y='count_',
                        color = 'animal_type',
                        barmode='group',
                        text='count_',
                        title='Animals Counts by Animal Types and Outcome Types')



    query = f"""
    SELECT
        DATE_TRUNC('WEEK', datetime_),
        outcome_type,
        COUNT({radio_value} animal_id)
    FROM animals
    WHERE DATE(datetime_) >= '{startdate}'
        AND DATE(datetime_) <= '{enddate}'
    GROUP BY 1,2
    ORDER BY 1
    """

    DF = read_animals(query)


    line_chart = px.line(DF, x = 'date_trunc', y="count", color='outcome_type')



    return bar_chart, yearly_bar, outcome_bar, line_chart


##############################################
################## Page - 2 ##################
##############################################

@app.callback([Output('animaltype-dropdown', 'options'),
               Output('animaltype-dropdown', 'value')],
              [Input('birthdate-datepicker', 'start_date'),
              Input('birthdate-datepicker', 'end_date')])
def assign_dropdown(startdate, enddate):
    df = read_animals(f"""SELECT
        DISTINCT animal_type
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'""")

    options = [{'label': animal, 'value': animal}
               for animal in df['animal_type']]
    if len(options) > 0:
        return options, options[0]['label']
    else:
        return [{'label': 'Veri Yok', 'value': 'Veri Yok'}]


@app.callback([Output("plot1", "figure"),
               Output('plot2', 'figure'),
               Output('plot3', 'figure'),
               Output('selected-animal-card', 'src'),
               Output('number-selected-animal-card', 'children')],
              [Input('birthdate-datepicker', 'start_date'),
              Input('birthdate-datepicker', 'end_date'),
              Input('animaltype-dropdown', 'value'),
              Input('select-pieces-plot2', 'value'),
              Input('slider_x', 'value')])
def outcome_values(startdate, enddate, animal_type, type_dropdown, slider_value):
    query = f"""
    SELECT
                DATE_TRUNC('MONTH', date_of_birth) month_,
                COUNT(DISTINCT animal_id) as count_of_animals
            FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
            AND animal_type = '{animal_type}'
            GROUP BY 1
            ORDER BY 1 DESC
    """

    dfs = read_animals(query)

    query = f"""
    SELECT
                DATE_TRUNC('MONTH', datetime_) month_,
                COUNT(DISTINCT animal_id) as count_of_animals
            FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
            AND animal_type = '{animal_type}'
            GROUP BY 1
            ORDER BY 1 DESC
    """

    dfz = read_animals(query)

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=dfs['month_'], y=dfs['count_of_animals'],
                             mode='lines+markers',
                             name='birth_date'))
    fig.add_trace(go.Scatter(x=dfz['month_'], y=dfz['count_of_animals'],
                             mode='lines+markers',
                             name='datetime_'))
    fig.update_layout(title=f"Counts of the {animal_type}s by Birth Date and Outcome Date (as Month)")

    dfx = read_animals(f"""
        SELECT
            outcome_type,
            outcome_subtype,
            COUNT(DISTINCT animal_id)
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
            AND animal_type = '{animal_type}'
        GROUP BY 1, 2
        """)

    sun_burst = px.sunburst(dfx, path=['outcome_type', 'outcome_subtype'],
                                values='count',
                                title = f"Outcome Types and Subtypes of {animal_type}s")





    dfg = read_animals(f"""
        SELECT
            {type_dropdown},
            COUNT(DISTINCT animal_id) count_
        FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
            AND animal_type = '{animal_type}'
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT {slider_value}
        """)

    plot2 = px.bar(dfg, x = type_dropdown, y = 'count_',
                                color = type_dropdown,
                                text='count_',
                                title = f"Counts of {animal_type}s by Top {len(dfg)} {type_dropdown} Types")





    dfa = read_animals(f"""    
        SELECT
                COUNT(DISTINCT animal_id)
            FROM animals
        WHERE DATE(datetime_) >= '{startdate}'
            AND DATE(datetime_) <= '{enddate}'
            AND animal_type = '{animal_type}'
            """)

    return fig, plot2, sun_burst, animal_photos[animal_type], dfa['count'].sum()



##############################################
################## Page - 3 ##################
##############################################



@app.callback(Output('search-result', 'children'),
              [Input('search-field', 'value'),
              Input('search-key', 'value'),
              Input('search-button', 'n_clicks')])
def search_results(search_by, keyword, click_):

    isTrue = BUTTONS['search'].isNew(click_)

    if (isTrue and keyword != None):
        df = read_animals(f"""
            SELECT
            *
            FROM animals
            WHERE LOWER({search_by}) = '{keyword.lower()}'
            ORDER BY datetime_ DESC
        """)
        if len(df) == 0:
            result = html.H1("There is no animal with this informations!")
        else:
            result = dash_table.DataTable(
                                    columns=[{"name": i, "id": i} for i in list(df.columns)],
                                    page_size=8,
                                    style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold'
                                    },
                                    style_cell={
                                        'backgroundColor': 'rgb(50,50,50)',
                                        'color': 'white',
                                        'whiteSpace': 'normal',
                                        'overflow': 'hidden',
                                        'textOverflow': 'ellipsis',
                                        #'minWidth': '80px', 'width': '130px', 'maxWidth': '130px'
                                    },
                                    data= df.to_dict('rows')
                                    )

        return result

    
    return html.H1("Search the animal You wanna see the informations!!")




@app.callback(Output('add-confirm', 'displayed'),
              [Input('add-name', 'value'),
              Input('add-animaltype', 'value'),
              Input('add-animalid', 'value'),
              Input('add-age', 'value'),
              Input('add-color', 'value'),
              Input('add-breed', 'value'),
              Input('add-outcometype', 'value'),
              Input('add-outcomesubtype', 'value'),
              Input('add-sexuponoutcome', 'value'),
              Input('add-birthdate', 'date'),
              Input('add-button', 'n_clicks')])
def search_results(name, type_, id, age, color, breed, outcome_type, outcome_subtype, outcome_sex, birthdate, click_):
    
    isTrue = BUTTONS['add'].isNew(click_)
    if (isTrue and type_ and id and age and color and breed and outcome_type and outcome_subtype and outcome_sex and birthdate and click_):
        values = [age, id, outcome_type, breed, color, birthdate + ' 00:00:00', str(datetime.now()), birthdate + ' 00:00:00', name, outcome_subtype, outcome_type, outcome_sex]
        insert_animal_one(values)
        return True
    else:
        return False
##############################################
##################  END  #####################
##############################################


@app.callback([Output(f"{i}-link", "active") for i in pageList],
              [Input("url", "pathname")],
              )
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/{i}" for i in pageList]


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/index"]:
        return index
    elif pathname == "/by_animal":
        return byanimal
    elif pathname == "/search_and_add":
        return searchandadd
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"This page is not available..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=9595, host="0.0.0.0")
