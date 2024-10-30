from pandas import DataFrame

from sklearn.model_selection import train_test_split

from typing import Any

from data_service.configuration.columns import Y_COLUMNS


class XYSplit:
    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def x_y_split(self) -> tuple[DataFrame, DataFrame]:
        y_dataframe = self.dataframe[Y_COLUMNS]
        x_dataframe = self.dataframe.drop(Y_COLUMNS[-1], axis=1)
        return x_dataframe, y_dataframe


class TrainTestSplit:
    def __init__(self, x: Any, y: Any) -> None:
        self._x = x
        self._y = y

    def train_test_splitting(self, test_size: float = 0.2) -> tuple:
        x_train, x_test, y_train, y_test = train_test_split(
            self._x, self._y,
            test_size=test_size,
            shuffle=True,
            random_state=1
        )
        return x_train, x_test, y_train, y_test
