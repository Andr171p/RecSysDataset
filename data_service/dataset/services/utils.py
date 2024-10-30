import os
from pathlib import Path
from typing import List

import pandas as pd
from pandas import DataFrame

from data_service.configuration.columns import COLUMNS


def get_root_path() -> Path:
    root_path = Path(__file__).resolve().parents[3]
    return root_path


def get_absolute_file_path(file_name: str) -> str:
    path = fr"{get_root_path()}/storage/raw_data"
    absolute_path = fr"{path}/{file_name}"
    return absolute_path


def get_raw_data_files() -> List[str]:
    raw_data_files: List[str] = []
    path = fr"{get_root_path()}/storage/raw_data"
    files = os.listdir(path=path)
    for file in files:
        raw_data_files.append(get_absolute_file_path(file_name=file))
    return raw_data_files


def check_excel_files(files: List[str]) -> List[str]:
    checked = []
    for file in files:
        if file.split('.')[-1] == 'xlsx':
            checked.append(file)
    return checked


def get_age(birth_date: str, current_date: str = '25.08.2019') -> int:
    birth_day, birth_month, birth_year = map(int, birth_date.split('.'))
    current_day, current_month, current_year = map(int, current_date.split('.'))
    age = current_year - birth_year
    if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        age -= 1
    return age


def required_columns(dataframe: DataFrame) -> DataFrame:
    dataframe = dataframe[COLUMNS]
    return dataframe


def replace_education(value):
    if pd.isna(value):
        return 'Не указано'
    elif 'Среднее общее образование' in value:
        return 'Среднее общее образование'
    elif 'Среднее профессиональное образование' in value:
        return 'Среднее профессиональное образование'
    elif 'Высшее образование - специалитет' in value:
        return 'Высшее образование специалитет'
    elif 'Высшее образование' in value:
        return 'Высшее образование бакалавриат'
    else:
        return value


def concat_dataframes(dataframes: List[DataFrame]) -> DataFrame:
    dataframe = pd.concat(dataframes, axis=1)
    return dataframe


def del_nan(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    for column in columns:
        dataframe[column] = dataframe[column].apply(
            lambda x: 0 if pd.isna(x) else x
        )
    return dataframe


def save_labels_to_txt_file(file_name: str, labels: List[str]) -> None:
    with open(file=file_name, mode='w', encoding='utf-8') as file:
        for label in labels:
            file.write(f"{label}\n")
