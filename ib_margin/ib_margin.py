from pathlib import Path

import numpy as np
import pandas as pd
import requests


def check_data_frame(df: pd.DataFrame) -> bool:
    """Ensure required columns are present"""

    required_cols = {
        "Time",
        "Exchange",
        "Underlying",
        "Product description",
        "Trading Class",
        "Intraday Initial",
        "Intraday Maintenance",
        "Overnight Initial",
        "Overnight Maintenance",
        "Currency",
        "Has Options",
        "Short Overnight Initial",
        "Short Overnight Maintenance",
    }

    return required_cols.issubset(df.columns)


def read(file: Path) -> pd.DataFrame:
    """Read margin file"""

    # read and check margin file
    margin = pd.read_csv(file, parse_dates=["Time"])
    assert check_data_frame(margin)

    return margin


def download(
    url: str = "https://www.interactivebrokers.com/en/index.php?f=26662",
) -> pd.DataFrame:
    """Download margin"""

    # download and parse margin file from URL
    page = requests.get(url)
    tables = pd.read_html(page.content)

    time = pd.Timestamp.now(tz="UTC")
    for t in tables:
        # align column names
        t.columns = t.columns.str.replace("Exchange.*", "Exchange")
        t.columns = t.columns.str.replace(" 1", "")
        # insert time of download
        t.insert(loc=0, column="Time", value=time)

    # flatten list of margin tables
    margin = [t for t in tables if check_data_frame(t)]
    margin = pd.concat(margin)

    return margin


def drop_repeated_values(x):
    """Identify consecutive repeated values and drop them"""
    columns = [
        "Intraday Initial",
        "Overnight Initial",
        "Overnight Maintenance",
        "Short Overnight Initial",
        "Short Overnight Maintenance",
    ]
    x = x.sort_values(by="Time")
    changes = x.loc[:, columns].diff().abs()
    changes = changes.round(2).replace(np.nan, 1).sum(axis=1)
    return x.loc[changes > 0, :]


def merge(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Concatenate data frames and drop duplicates"""

    assert check_data_frame(df1)
    assert check_data_frame(df2)

    df = df1.append(df2, ignore_index=True)

    # drop duplicates
    df["id"] = df["Exchange"] + df["Underlying"] + df["Trading Class"] + df["Currency"]
    df = df.groupby(["id"], sort=False).apply(drop_repeated_values)
    df = df.drop(["id"], axis=1).reset_index(drop=True)

    return df


def write(df: pd.DataFrame, file: Path) -> None:
    """Write margin to file"""

    assert check_data_frame(df)
    df.to_csv(
        file,
        index=False,
        encoding="utf-8",
        date_format="%Y-%m-%dT%H:%M:%SZ",
        float_format="%.6f",
    )
