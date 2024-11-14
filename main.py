import pandas as pd
from pandas import DataFrame

from sklearn.preprocessing import StandardScaler

from data_service.dataset.services.read import read_csv_file
from data_service.dataset.services.save import save_csv_file
from data_service.dataset.plots.curve_plot import CurvePlot
from data_service.dataset.plots.bar_plot import BarPlot
from data_service.dataset.preprocessing import CategoricalEncoder
from data_service.dataset.selection import XYSplit, TrainTestSplit
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


# curve_plotting(dataframe=df)


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


# bar_plotting(dataframe=df)

df['Полученное образование'] = df['Полученное образование'].apply(replace_education)
print(df['Полученное образование'].value_counts())

df = df.fillna(0)

df_nameless = df.drop('ФИО', axis=1)
df_ohe = CategoricalEncoder(dataframe=df_nameless).one_hot_encoding()
print(df_ohe.columns)
print(df_ohe.shape)

df_final = pd.concat([df['ФИО'], df_ohe], sort=False, axis=1)
X_COLUMNS = ['ФИО', 'Пол', 'Дата рождения', 'Спорт', 'Иностранное гражданство',
       'Ср. балл док-та об образовании', 'Сумма баллов',
       'Сумма баллов за индивидуальные достижения', 'Приказ о зачислении',
       'Рисунок', 'Математика', 'Русский язык', 'Обществознание', 'Физика',
       'История', 'Композиция архитектура', 'Композиция дизайн', 'Информатика',
       'Химия', 'Композиция',
       'Полученное образование_Высшее образование бакалавриат',
       'Полученное образование_Среднее общее образование',
       'Полученное образование_Среднее профессиональное образование',
       'Форма обучения_Заочная', 'Форма обучения_Очная',
       'Форма обучения_Очно-заочная']
df_grouped = df_final.groupby(by=X_COLUMNS,  as_index=False).agg('max')
print(df_grouped.shape)

# x, y = XYSplit(dataframe=df_grouped).x_y_split()

x = df_grouped[X_COLUMNS]
y = df_grouped.drop(labels=X_COLUMNS[1::], axis=1)

save_csv_file(
    dataframe=x,
    file_path=fr'{get_root_path()}/storage/x_y_data/inputs.csv'
)
save_csv_file(
    dataframe=y,
    file_path=fr'{get_root_path()}/storage/x_y_data/outputs.csv'
)

# x_ohe = CategoricalEncoder(dataframe=x[list(x.columns)[1::]]).one_hot_encoding()
# y_ohe = CategoricalEncoder(dataframe=y[list(y.columns)[1::]]).one_hot_encoding()

# x_final = pd.concat([x['ФИО'], x_ohe], sort=False, axis=1)
# y_final = pd.concat([y['ФИО'], y_ohe], sort=False, axis=1)

x_final = x
y_final = y

print(x_final.shape)
print(x_final.columns)
print(y_final.shape)
print(y_final.columns)

save_csv_file(
    dataframe=x_final,
    file_path=fr"{get_root_path()}/storage/ohe_data/x_ohe.csv"
)
save_csv_file(
    dataframe=y_final,
    file_path=fr"{get_root_path()}/storage/ohe_data/y_ohe.csv"
)

x_final = x_final.drop('ФИО', axis=1)
y_final = y_final.drop('ФИО', axis=1)

scaler = StandardScaler()
scaler.fit(x_final)
x_scaled = scaler.transform(x_final)

x_train, x_test, y_train, y_test = TrainTestSplit(
    x=x_scaled,
    y=y_final
).train_test_splitting()

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

x_columns = x_final.columns
y_columns = y_final.columns

x_train_df = pd.DataFrame(x_train, columns=x_columns)
x_test_df = pd.DataFrame(x_test, columns=x_columns)
y_train_df = pd.DataFrame(y_train, columns=y_columns)
y_test_df = pd.DataFrame(y_test, columns=y_columns)

save_csv_file(
    dataframe=x_train_df,
    file_path=fr"{get_root_path()}/storage/processed_data/input/x_train.csv"
)
save_csv_file(
    dataframe=x_test_df,
    file_path=fr"{get_root_path()}/storage/processed_data/input/x_test.csv"
)
save_csv_file(
    dataframe=y_train_df,
    file_path=fr"{get_root_path()}/storage/processed_data/output/y_train.csv"
)
save_csv_file(
    dataframe=y_test_df,
    file_path=fr"{get_root_path()}/storage/processed_data/output/y_test.csv"
)
