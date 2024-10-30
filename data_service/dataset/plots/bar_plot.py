import matplotlib.pyplot as plt

from pandas import DataFrame

from data_service.dataset.services.utils import get_root_path


class BarPlot:
    def __init__(self, dataframe: DataFrame, save_plot: bool = True) -> None:
        self.dataframe = dataframe
        self.save_plot = save_plot

    def popular_speciality(self) -> None:
        self.dataframe['Направление подготовки'].value_counts().plot(kind='bar')
        if self.save_plot:
            plt.savefig(fr"{get_root_path()}/storage/plots/popular_speciality.png")
        plt.title("Популярные направления подготовки")
        plt.xlabel('Направление подготовки')
        plt.ylabel('Количество студентов')
        plt.show()

    def popular_foreign_students_speciality_plot(self) -> None:
        foreign_students_dataframe = self.dataframe[
            self.dataframe['Иностранное гражданство'] == 1
        ]
        foreign_students_dataframe['Направление подготовки'].value_counts().plot(kind='bar')
        if self.save_plot:
            plt.savefig(fr"{get_root_path()}/storage/plots/foreign_students_plot.png")
        plt.title('Популярные направления подготовки у иностранных студентов')
        plt.xlabel('Направление подготовки')
        plt.ylabel('Количество студентов')
        plt.show()

    def popular_top_exams_rate_students_speciality_plot(self, exams_rate: int) -> None:
        exam_students_dataframe = self.dataframe[
            self.dataframe['Сумма баллов'] >= exams_rate
        ]
        exam_students_dataframe['Направление подготовки'].value_counts().plot(kind='bar')
        if self.save_plot:
            plt.savefig(fr"{get_root_path()}/storage/plots/exams_rate_{exams_rate}_plot.png")
        plt.title(f"Популярные направления подготовки среди студентов с суммой баллов больше {exams_rate}")
        plt.xlabel('Направление подготовки')
        plt.ylabel('Количество студентов')
        plt.show()

    def popular_low_exams_rate_students_speciality_plot(self, exams_rate: int) -> None:
        exam_students_dataframe = self.dataframe[
            self.dataframe['Сумма баллов'] <= exams_rate
        ]
        exam_students_dataframe['Направление подготовки'].value_counts().plot(kind='bar')
        if self.save_plot:
            plt.savefig(fr"{get_root_path()}/storage/plots/exams_rate_{exams_rate}_plot.png")
        plt.title(f"Популярные направления подготовки среди студентов с суммой баллов меньше {exams_rate}")
        plt.xlabel('Направление подготовки')
        plt.ylabel('Количество студентов')
        plt.show()

