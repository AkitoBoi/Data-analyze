import pandas as pd
import matplotlib.pyplot as plt
import os

def get_file_path():
    while True:
        file_path = input("Введите путь к файлу с данными: ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Файл не найден. Пожалуйста, введите корректный путь к файлу.")

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return None

def display_histogram(data, column_name):
    plt.hist(data[column_name])
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.title(f'Гистограмма данных для столбца "{column_name}"')
    plt.show()

def main():
    file_path = get_file_path()
    data = load_data(file_path)
    if data is None:
        return

    column_name = input("Введите имя столбца для построения гистограммы: ")
    display_histogram(data, column_name)

if __name__ == "__main__":
    main()
