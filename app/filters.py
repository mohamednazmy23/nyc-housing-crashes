from dash import html, dcc
from app.helpers import BOROUGHS, YEARS, DEFAULT_FILTERS


def filter_bar():
    d = DEFAULT_FILTERS
    return html.Div(className="filter-bar", children=[
        html.Div(className="filter-row", children=[
            dcc.Dropdown(id="borough-dd", className="dd", clearable=False, value=d["borough"],
                         options=[{"label": "All boroughs", "value": "ALL"}] +
                                 [{"label": b.title(), "value": b} for b in BOROUGHS]),
            dcc.Dropdown(id="year-from-dd", className="dd", clearable=False, value=d["year_from"],
                         options=[{"label": f"From {y}", "value": y} for y in YEARS]),
            dcc.Dropdown(id="year-to-dd", className="dd", clearable=False, value=d["year_to"],
                         options=[{"label": f"To {y}", "value": y} for y in YEARS]),
            dcc.Dropdown(id="construction-dd", className="dd", clearable=False,
                         value=d["construction_type"], options=[
                             {"label": "All construction", "value": "ALL"},
                             {"label": "New construction", "value": "New Construction"},
                             {"label": "Preservation", "value": "Preservation"}]),
            dcc.Dropdown(id="road-user-dd", className="dd", clearable=False,
                         value=d["road_user"], options=[
                             {"label": "All road users", "value": "all"},
                             {"label": "Pedestrians", "value": "pedestrian"},
                             {"label": "Cyclists", "value": "cyclist"},
                             {"label": "Motorists", "value": "motorist"}]),
        ]),
        html.Div(className="filter-row", children=[
            dcc.Input(id="search-input", type="text",
                      placeholder='Try "Brooklyn 2022 new buildings"'),
            html.Button("Search", id="search-btn"),
            html.Span(id="search-status"),
            html.Button("Generate Report", id="generate-btn", className="primary", n_clicks=0),
        ]),
    ])


def read_filters(borough, year_from, year_to, construction, road_user):
    """Dropdown values -> one filter dict (task sheet 7.2)."""
    f = dict(DEFAULT_FILTERS)
    if borough:      f["borough"] = borough
    if year_from:    f["year_from"] = int(year_from)
    if year_to:      f["year_to"] = int(year_to)
    if construction: f["construction_type"] = construction
    if road_user:    f["road_user"] = road_user
    if f["year_from"] > f["year_to"]:
        f["year_from"], f["year_to"] = f["year_to"], f["year_from"]
    return f


def register_search_callback(app):
    # STUB: mostafa.2 adds parse_search() and the search callback here
    pass