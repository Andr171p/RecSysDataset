import pandas as pd
from pandas import DataFrame


def save_csv_file(dataframe: DataFrame, file_path: str) -> None:
    dataframe.to_csv(path_or_buf=file_path)
