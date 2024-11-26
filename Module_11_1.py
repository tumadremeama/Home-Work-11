import requests

# Выполнение HTTP-запросов
# Обработка ответов от сервера

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print(f'Данные успешно получены:')
    print(response.json())
else:
    print(f'Ошибка при получении данных:', response.status_code)