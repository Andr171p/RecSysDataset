import matplotlib.pyplot as plt

from pandas import DataFrame

from data_service.dataset.services.utils import get_root_path


class CurvePlot:
    def __init__(self, dataframe: DataFrame, save_plot: bool = True) -> None:
        self.dataframe = dataframe
        self.save_plot = save_plot

    def curve_column_plot(self, column: str, file_name: str = None) -> None:
        self.dataframe[column].plot()
        if self.save_plot:
            plt.savefig(fr"{get_root_path()}/storage/plots/{file_name}.png")
        plt.title(column)
        # plt.xlabel('')
        # plt.ylabel('')
        plt.show()