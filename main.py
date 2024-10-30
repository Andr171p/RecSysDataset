import pandas as pd
from pandas import DataFrame

from data_service.dataset.services.read import read_csv_file
from data_service.dataset.services.save import save_csv_file
from data_service.dataset.plots.curve_plot import CurvePlot
from data_service.dataset.plots.bar_plot import BarPlot
from data_service.dataset.preprocessing import CategoricalEncoder
from data_service.dataset.selection import XYSplit
from data_service.dataset.services.utils import (
    get_root_path,
    save_labels_to_txt_file,
    replace_education
)


df = read_csv_file(
    file_path=rf"{get_root_path()}\storage\preprocessed_data\all_years\applicants 2019-2024.csv"
)
df = df.drop(
    labels=['Unnamed: 0.3', 'Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'Результаты вступ. испытаний'],
    axis=1
)
CurvePlot(dataframe=df, save_plot=False).curve_column_plot(column='Сумма баллов')


def drop_anomaly_value(dataframe: DataFrame) -> DataFrame:
    max_value = dataframe['Сумма баллов'].max()
    dataframe = dataframe.drop(dataframe[dataframe['Сумма баллов'] == max_value].index)
    return dataframe


df = drop_anomaly_value(dataframe=df)


def curve_plotting(dataframe: DataFrame) -> None:
    curve_plot = CurvePlot(dataframe=dataframe)
    curve_plot.curve_column_plot(column='Сумма баллов', file_name='students_scores')


curve_plotting(dataframe=df)


save_labels_to_txt_file(
    file_name=fr"{get_root_path()}/storage/preprocessed_data/all_years/labels.txt",
    labels=list(df.columns)
)

df = CategoricalEncoder(dataframe=df).binary_encoding()


def bar_plotting(dataframe: DataFrame) -> None:
    bar_plot = BarPlot(dataframe=dataframe)
    bar_plot.popular_speciality()
    bar_plot.popular_foreign_students_speciality_plot()
    bar_plot.popular_top_exams_rate_students_speciality_plot(exams_rate=270)
    bar_plot.popular_low_exams_rate_students_speciality_plot(exams_rate=170)


bar_plotting(dataframe=df)

df['Полученное образование'] = df['Полученное образование'].apply(replace_education)
print(df['Полученное образование'].value_counts())

x, y = XYSplit(dataframe=df).x_y_split()

save_csv_file(
    dataframe=x,
    file_path=fr'{get_root_path()}/storage/x_y_data/inputs.csv'
)
save_csv_file(
    dataframe=y,
    file_path=fr'{get_root_path()}/storage/x_y_data/outputs.csv'
)

x_ohe = CategoricalEncoder(dataframe=x[list(x.columns)[1::]]).one_hot_encoding()
y_ohe = CategoricalEncoder(dataframe=y[list(y.columns)[1::]]).one_hot_encoding()

x_final = pd.concat([x['ФИО'], x_ohe], sort=False, axis=1)
y_final = pd.concat([y['ФИО'], y_ohe], sort=False, axis=1)

print(x_final.shape)
print(x_final.columns)
print(y_final.shape)
print(y_final.columns)