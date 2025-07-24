"""
Task 02: Create a Data Visualization Tool
Build a tool that takes a dataset and
generates interactive visualizations using
libraries such as Matplotlib, Seaborn, or
Plotly. This task will enhance their
understanding of data visualization principles
and plotting techniques.
"""

import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load MCU movie dataset
df = pd.read_csv("mcu_movies.csv")

# Convert release date to datetime
df["Release Date"] = pd.to_datetime(df["Release Date"])


# Normalize sizes for better bubble scaling
def normalize(series, scale):
    return (series - series.min()) / (series.max() - series.min()) * scale


df["Budget Size"] = normalize(df["Budget"], 40) + 10
df["BoxOffice Size"] = normalize(df["Box Office"], 60) + df["Budget Size"]

# Outer bubble (Box Office)
outer = go.Scatter(
    x=df["Release Date"],
    y=df["Rotten Tomatoes"],
    mode="markers",
    marker=dict(
        size=df["BoxOffice Size"],
        color="rgba(255,255,255,0.15)",  # faint white outer ring
        line=dict(width=1, color="rgba(255,255,255,0.2)"),
    ),
    hoverinfo="skip",
    showlegend=False,
)

# Inner bubble (Budget) with IMDb rating as color
inner = go.Scatter(
    x=df["Release Date"],
    y=df["Rotten Tomatoes"],
    mode="markers",
    marker=dict(
        size=df["Budget Size"],
        color=df["IMDb Rating"],
        colorscale="Viridis",
        colorbar=dict(
            title="IMDb Rating",
            orientation="v",
            x=1.05,
            y=0.5,
            len=0.6,
            thickness=15,
            bgcolor="rgba(0,0,0,0.6)",
            bordercolor="white",
            borderwidth=1,
        ),
        line=dict(width=2, color="white"),
    ),
    text=[
        f"<b>{title}</b><br>"
        f"Release: {date.date()}<br>"
        f"IMDb: {imdb}/10<br>"
        f"Rotten Tomatoes: {rt}%<br>"
        f"Budget: ${budget}M<br>"
        f"Box Office: ${box}M"
        for title, date, imdb, rt, budget, box in zip(
            df["Title"],
            df["Release Date"],
            df["IMDb Rating"],
            df["Rotten Tomatoes"],
            df["Budget"],
            df["Box Office"],
        )
    ],
    hoverinfo="text",
    showlegend=False,
)

# Create the figure
fig = go.Figure(data=[outer, inner])

# Add layout customizations
fig.update_layout(
    title="Marvel Cinematic Universe Movies",
    title_font=dict(size=28, color="white"),
    plot_bgcolor="rgb(20,20,30)",  # Marvel-ish dark background
    paper_bgcolor="rgb(10,10,15)",
    font=dict(color="white"),
    height=700,
    xaxis=dict(
        title="Release Date",
        rangeslider=dict(visible=True),
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
    ),
    yaxis=dict(
        title="Rotten Tomatoes (%)",
        range=[0, 110],
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
        fixedrange=False,
    ),
)

fig.show()
