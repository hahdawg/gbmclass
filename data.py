import pandas as pd


def load_raw_data():
    res = pd.read_csv("train.csv")
    res.columns = res.columns.str.lower()
    res["date"] = pd.to_datetime(res["date"], format="%Y-%m-%d")
    return res


def process_data(raw):
    by_store = raw.groupby("store", as_index=False)["sales"].sum()
    by_store = by_store.sort_values(by="sales")
    by_store = by_store.iloc[-100:]

    res = raw.copy()
    res = res.merge(by_store[["store"]], on="store")

    res.loc[res["stateholiday"] != 0] = 1
    res = res.drop("customers", axis=1)
    res.to_csv("rossmann.csv")
    return res
