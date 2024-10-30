import pandas as pd
from pandas import DataFrame

from data_service.dataset.services.utils import required_columns, replace_education


class CategoricalEncoder:
    def __init__(self, dataframe: DataFrame) -> None:
        # self.dataframe = required_columns(dataframe=dataframe)
        self.dataframe = dataframe

    def binary_encoding(self) -> DataFrame | None:
        self.dataframe['Пол'] = self.dataframe['Пол'].apply(
            lambda x: 1 if x == 'М' else 0
        )
        self.dataframe['Спорт'] = self.dataframe['Спорт'].apply(
            lambda x: 0 if pd.isna(x) else 1
        )
        self.dataframe['Иностранное гражданство'] = self.dataframe['Иностранное гражданство'].apply(
            lambda x: 0 if pd.isna(x) else 1
        )
        self.dataframe['Приказ о зачислении'] = self.dataframe['Приказ о зачислении'].apply(
            lambda x: 0 if pd.isna(x) else 1
        )
        self.dataframe['Полученное образование'] = self.dataframe['Полученное образование'].apply(
            replace_education
        )
        return self.dataframe

    def one_hot_encoding(self) -> DataFrame | None:
        self.dataframe = pd.get_dummies(data=self.dataframe)
        return self.dataframe
