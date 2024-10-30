import matplotlib.pyplot as plt

from pandas import DataFrame


class ScatterPlot:
    def __init__(self, dataframe: DataFrame, save_plot: bool = True) -> None:
        self.dataframe = dataframe
        self.save_plot = save_plot

    def scatter_plot(self, x_column, y_column) -> None:
        ...