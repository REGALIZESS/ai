import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog


# Прогноз добычи газа
def plot_graph(months, production):
    predicted_production = production + 10  # Прогнозируемая добыча (на 10 единиц больше)

    # Диаграмма
    plt.figure(figsize=(10, 6))
    plt.plot(months, production, 'bo-', label='Фактическая добыча')
    plt.plot(months, predicted_production, 'r--', label='Прогнозируемая добыча')

    # Подписи на диаграмме
    for i, prod in enumerate(production):
        plt.text(months[i], prod, f'({months[i]}, {int(prod)})', fontsize=9, ha='left')

    # График (UI)
    plt.title('Прогнозирование добычи по месяцам')
    plt.xlabel('Месяцы')
    plt.ylabel('Добыча (тыс. ед.)')
    plt.xticks(np.arange(1, 13, 1))  # Отображение месяцев от 1 до 12
    plt.legend()
    plt.grid(True)
    plt.show()


# Получение данных от пользователя
def get_data_from_user():
    months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    production = np.zeros(12)

    # Окно для ввода данных
    for i in range(12):
        user_input = simpledialog.askstring("Ввод данных", f"Введите добычу для месяца {i + 1} (тыс. ед.):")
        production[i] = float(user_input)

    plot_graph(months, production)


# Интерфейс
root = tk.Tk()
root.withdraw()

# Запуск процесса
get_data_from_user()
