from typing import Union

import os
import pandas as pd
import plotly.graph_objects as go
from pandas import DataFrame, Series


def today_data(today_file):
    today_df: Union[Series, DataFrame] = pd.read_csv(today_file).dropna(axis=0, how="any")
    today_df["value"] = today_df["value"].map(lambda x: int(x))

    return today_df


def make_figure():
    covid_df = today_data(os.environ["DATAFILE"])

    # State cumulative and new CASES by day -- ONSET DATE
    cumulative_cases_by_day = covid_df.loc[covid_df["description"] == "Cumulative Number of Cases by Onset Date"]  # x
    new_cases_by_day = covid_df.loc[covid_df["description"] == "Case Counts by Onset Date"]  # y

    # State cumulative and new HSPLZ by day -- ONSET DATE
    cumulative_hsplz_by_day = covid_df.loc[covid_df["description"] == "Cumulative Number of Hospitalizations by Onset Date"]  # x
    new_hsplz_by_day = cumulative_hsplz_by_day["value"].diff()  # y

    # State cumulative and new DEATHS by day
    cumulative_deaths_by_day = covid_df.loc[covid_df["description"] == "Cumulative Number of Deaths by Onset Date"]  # x
    new_deaths_by_day = cumulative_deaths_by_day["value"].diff()  # y

    cases_hovertemplate = '<b>Total</b>: %{x}'+'<br><b>New</b>: %{y}</br>'+'<br><b>Date</b>: '+cumulative_cases_by_day["attribute"]
    hsplz_hovertemplate = '<b>Total</b>: %{x}'+'<br><b>New</b>: %{y}</br>'+'<br><b>Date</b>: '+cumulative_hsplz_by_day["attribute"]
    deaths_hovertemplate = '<b>Total</b>: %{x}'+'<br><b>New</b>: %{y}</br>'+'<br><b>Date</b>: '+cumulative_deaths_by_day["attribute"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=cumulative_cases_by_day["value"], y=new_cases_by_day["value"],
                             mode='lines',
                             name='Cases',
                             hovertemplate=cases_hovertemplate,
                             showlegend=True))

    fig.add_trace(go.Scatter(x=cumulative_hsplz_by_day["value"], y=new_hsplz_by_day,
                             mode='lines',
                             name='Hospitalizations',
                             hovertemplate=hsplz_hovertemplate,
                             showlegend=True))

    fig.add_trace(go.Scatter(x=cumulative_deaths_by_day["value"], y=new_deaths_by_day,
                             mode='lines',
                             name='Deaths',
                             hovertemplate=deaths_hovertemplate,
                             showlegend=True))

    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")

    fig.update_layout(title='Cumulative vs New COVID-19 Cases, Hospitalizations, and Deaths in Colorado',
                      xaxis_title='Cumulative Cases',
                      yaxis_title='New Cases by Day')

    return fig.to_dict()
