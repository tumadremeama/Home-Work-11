import matplotlib.pyplot as plt

# для настроики внешнего вида гафиков
# визуализация данных с помощью графиков и диаграмм

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

plt.savefig('plot.png')

plt.show()