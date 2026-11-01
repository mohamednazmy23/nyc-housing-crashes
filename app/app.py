from dash import Dash, html, dcc

app = Dash(__name__, title="NYC Housing × Crashes")
server = app.server  # Render's gunicorn uses this

def card(qid, question, wide=False):
    """One chart card: the question as a heading + an empty graph slot."""
    return html.Div(
        className="card wide" if wide else "card",
        children=[html.H4(question), dcc.Graph(id=qid)],
    )


def section(title, cards):
    return html.Section([
        html.H2(title),
        dcc.Loading(html.Div(className="grid", children=cards)),
    ])

app.layout = html.Div(className="page", children=[
    html.Header([
        html.H1("Are new affordable homes being built on NYC's most dangerous streets?"),
        html.P("Affordable Housing Production (HPD) × Motor Vehicle Crashes (NYPD), 2014–2025"),
    ]),

    # Placeholder until mostafa.2's filter_bar() exists
    html.Div(className="filter-bar", children="Filters + search + Generate Report go here"),

    html.Div(id="story-intro", className="story", children="Story intro goes here (mostafa.3)"),

    section("1. Where", [
        card("q11", "Q11. Where do housing and injury hotspots overlap?", wide=True),
        card("q12", "Q12. Which ZIPs should be safety priorities?"),
        card("q4",  "Q4. More affordable units, more pedestrian-injury crashes?"),
    ]),
    section("2. Who gets housed where", [
        card("q1", "Q1. Are lower-income homes in more dangerous areas?"),
        card("q2", "Q2. New construction vs. preservation: safer or riskier areas?"),
    ]),
    section("3. Over time", [
        card("q3", "Q3. Did completions and injuries move together?"),
        card("q7", "Q7. Do high-growth ZIPs have different crash trends?"),
        card("q5", "Q5. Do crashes change after a building opens?", wide=True),
    ]),
    section("4. Near the buildings", [
        card("q6",  "Q6. Family-sized buildings near more dangerous streets?"),
        card("q8",  "Q8. How far is each building from a crash hotspot?"),
        card("q9",  "Q9. Do crashes near housing peak at school and commute hours?"),
        card("q10", "Q10. Which crash causes are more common near housing?"),
    ]),

    html.Div(id="story-end", className="story", children="Findings, limitations, impact (mostafa.3)"),
])

if __name__ == "__main__":
    app.run(debug=True)