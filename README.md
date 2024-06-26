### Описание
Проект представляет собой приложение для анализа наборов данных. Оно позволяет загружать данные, выполнять различные статистические расчеты и визуализировать данные с использованием графиков.

### Функциональность
1. **Загрузка данных**: Пользователь может загружать данные из файлов различных форматов (например, CSV, Excel) или использовать встроенные наборы данных для демонстрации функциональности.
2. **Статистические расчеты**: Приложение проводит базовые статистические расчеты для выбранных данных, такие как среднее значение, медиана, стандартное отклонение и корреляция между переменными.
3. **Визуализация данных**: Позволяет пользователю визуализировать данные с помощью различных типов графиков, таких как гистограммы, диаграммы рассеяния, линейные графики и т.д. Для визуализации данных используются библиотеки Matplotlib и Seaborn.
4. **Интерактивность**: Дает возможность пользователю взаимодействовать с графиками, например, изменять типы графиков, настраивать оси координат и фильтровать данные.
5. **Сохранение результатов**: Пользователь может сохранять созданные графики и результаты статистических расчетов для последующего использования или публикации.

### Технологии
- Язык программирования: Python
- Библиотеки: Pandas для работы с данными, Matplotlib и Seaborn для визуализации данных
- Интерфейс: Можно использовать консольный интерфейс или GUI (например, с помощью библиотеки Tkinter или PyQt)

## Использование

1. Установите необходимые зависимости: `pip install -r requirements.txt`
2. Запустите приложение: `python main.py`

## Требования к окружению

- Python 3.x
- Установленные зависимости (см. файл `requirements.txt`)

## Примеры использования

```python
# Пример загрузки данных и построения гистограммы
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('data.csv')

# Построение гистограммы
plt.hist(data['column_name'])
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма данных')
plt.show()
```

## Лицензия

Этот проект лицензируется по лицензии [MIT License](LICENSE).
