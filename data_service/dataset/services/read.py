import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader


def read_csv_file(file_path: str) -> DataFrame:
    dataframe = pd.read_csv(filepath_or_buffer=file_path)
    return dataframe


def read_big_csv_file(file_path: str, chunk_size: int = 5000) -> TextFileReader:
    chunk_dataframe = pd.read_csv(
        filepath_or_buffer=file_path,
        engine='python',
        chunksize=chunk_size,
        encoding='utf-8',
        on_bad_lines='skip'
    )
    return chunk_dataframe
