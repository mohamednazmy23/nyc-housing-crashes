import plotly.graph_objects as go

MIN_CRASHES = 50
BOROUGHS = ["BRONX", "BROOKLYN", "MANHATTAN", "QUEENS", "STATEN ISLAND"]
YEARS = list(range(2014, 2026))
DEFAULT_FILTERS = {
    "borough": "ALL", "year_from": 2014, "year_to": 2025,
    "construction_type": "ALL", "road_user": "pedestrian",
}


def empty_figure(message):
    """Blank chart that shows a message (used for 'no data' and placeholders)."""
    fig = go.Figure()
    fig.add_annotation(text=message, x=0.5, y=0.5, xref="paper", yref="paper",
                       showarrow=False, font=dict(size=14, color="#888"))
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10),
                      plot_bgcolor="white", paper_bgcolor="white")
    return fig


def apply_filters(tables, filters):
    # STUB: mostafa.2 replaces this with the real rules (task sheet 7.2)
    return tables


_INJURY = {"all": "persons_injured", "pedestrian": "pedestrians_injured",
           "cyclist": "cyclists_injured", "motorist": "motorists_injured"}
_INJURY_CRASH = {"all": "injury_crashes", "pedestrian": "ped_injury_crashes",
                 "cyclist": "cyc_injury_crashes", "motorist": "mot_injury_crashes"}
_UNITS = {"ALL": "units_completed", "New Construction": "units_new_construction",
          "Preservation": "units_preservation"}
_LABEL = {"all": "All road users", "pedestrian": "Pedestrians",
          "cyclist": "Cyclists", "motorist": "Motorists"}


def injury_col(filters):       return _INJURY[filters["road_user"]]
def injury_crash_col(filters): return _INJURY_CRASH[filters["road_user"]]
def units_col(filters):        return _UNITS[filters["construction_type"]]
def road_user_label(filters):  return _LABEL[filters["road_user"]]