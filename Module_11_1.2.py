import pandas as pd

# Чтение и записи данных в различных форматах
# Обработка и анализ данных с помощью DataFrame

data = pd.read_csv('data.csv')

print(f'Первые 5 строк данных:')
print(data.head())

average_value = data['value'].mean
print(f'Cреднее значение по столбицу "value":', average_value)