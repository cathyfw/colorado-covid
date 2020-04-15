from matplotlib import pyplot as plt
import pandas as pd

def make_figure():
    covid_cases = pd.read_pickle("/Users/catherinewalsh/covid_cases_df")

    yesterday_cumulative = covid_cases["Cumulative"].iloc[-1]
    today_cumulative = 7303
    today_date = "2020-04-12"
    today_df = pd.DataFrame([[today_date, today_cumulative,
                              today_cumulative-yesterday_cumulative]], columns=covid_cases.columns)

    covid_cases = covid_cases.append(today_df, ignore_index=True)
    covid_cases.to_pickle("covid_cases_df")

    x = covid_cases["Cumulative"]
    y = covid_cases["New"]
    avg_new = [sum(y)/len(y)]*len(y)

    fig = plt.figure()
    plt.plot(x, y)
    plt.plot(x, avg_new)

    plt.xlabel("Cumulaive Cases")
    plt.ylabel("New Cases")
    plt.title("New Cases vs Cumulative Cases -- log scale")
    plt.xscale("log")
    plt.yscale("log")

    return fig
