from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import os

port = int(os.environ.get("PORT", 8050))

df = pd.read_csv("data/dataset.csv")

app = Dash()

app.layout = [
    html.H1(children="Anti-Style", style={"textAlign": "center"}),
]


# Show first 5 rows as HTML table
app.layout = html.Div(
    [
        html.H1("Anti-Style - Preview", style={"textAlign": "center"}),
        html.Table(
            [
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody(
                    [
                        html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
                        for i in range(min(len(df), 5))  # Only first 5 rows
                    ]
                ),
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
