import plotly.express as px


def generate_chart(columns, rows):

    if len(columns) != 2 or len(rows) == 0:
        return None

    x = [row[0] for row in rows]
    y = [row[1] for row in rows]

    fig = px.bar(
        x=x,
        y=y,
        labels={
            "x": columns[0],
            "y": columns[1]
        }
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        margin=dict(l=30, r=30, t=30, b=30),
        height=420
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )