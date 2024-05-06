import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_file_path():
    """
    Запрашивает у пользователя путь к файлу и возвращает его.

    Returns:
    str: Путь к файлу.
    """
    while True:
        file_path = input("Введите путь к файлу с данными: ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Файл не найден. Пожалуйста, введите корректный путь к файлу.")

def load_data(file_path):
    """
    Загружает данные из файла.

    Parameters:
    file_path (str): Путь к файлу с данными.

    Returns:
    pandas.DataFrame: Загруженные данные.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return None

def display_histogram(data, column_name):
    """
    Отображает гистограмму для указанного столбца данных.

    Parameters:
    data (pandas.DataFrame): Данные для визуализации.
    column_name (str): Имя столбца данных.
    """
    plt.hist(data[column_name])
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.title(f'Гистограмма данных для столбца "{column_name}"')
    plt.show()

def main():
    # Загрузка данных
    file_path = get_file_path()
    data = load_data(file_path)
    if data is None:
        return

    # Отображение гистограммы
    column_name = input("Введите имя столбца для построения гистограммы: ")
    display_histogram(data, column_name)

if __name__ == "__main__":
    main()
