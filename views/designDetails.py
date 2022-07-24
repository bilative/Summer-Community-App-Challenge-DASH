import dash_html_components as html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#111111",
    "color": "#C8C8C8"
}


CONTENT_STYLE = {
    "margin-left": "16.5rem",
    "margin-right": "0.5rem",
    "padding": "1rem 0.5rem",
    "bacground-color": "black"
}


pageList = ['index', 'by_animal', 'search_and_add']


sidebar = html.Div(
    [
        html.H3("Bilal Latif Ozdemir", className="display-4"),
        html.Hr(),
        html.P(
            "This Dashboard built for Plotly/Dash Community Challange by Bilal Latif Ozdemir!!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("General Counts",
                            href="/index", id="index-link"),
                dbc.NavLink("By Animals",
                            href="/by_animal", id="by_animal-link"),
                dbc.NavLink("Search Animal",
                            href="/search_and_add", id="search_and_add-link")
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE,
)