import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
# Сверху библиотеки Ткинтер (Консоль), НамПай (Калькулятор), МатПлот (Математические графики)

# График + Прогноз
def plot_graph(months, production):
    predicted_production = production + 10  

    # График
    plt.figure(figsize=(10, 6))
    plt.plot(months, production, 'bo-', label='Фактическая добыча')
    plt.plot(months, predicted_production, 'r--', label='Прогнозируемая добыча')

    # Подписи
    for i, prod in enumerate(production):
        plt.text(months[i], prod, f'({months[i]}, {int(prod)})', fontsize=9, ha='left')

    # UI
    plt.title('Прогнозирование добычи по месяцам')
    plt.xlabel('Месяцы')
    plt.ylabel('Добыча (млн. ед.)')
    plt.xticks(np.arange(1, 13, 1))  # Месяцы 1-12
    plt.legend()
    plt.grid(True)
    plt.show()

    # Статистика
    total_production = np.sum(production)  # Общая добыча
    total_production_billion = total_production / 1000  # Млн -> Млрд
    percent_change = ((predicted_production[-1] - production[-1]) / production[-1]) * 100  # Изменение в %

    # Тип месторождения
    if total_production < 10000:
        field_type = "Мелкое"
    elif 10000 <= total_production <= 100000:
        field_type = "Среднее"
    else:
        field_type = "Крупное"

    # Вывод в Ткинтер
    result_message = (
        f"Сумма добычи: {total_production_billion:.2f} млрд\n"
        f"Изменение добычи: {percent_change:.2f}%\n"
        f"Категория месторождения: {field_type}"
    )
    messagebox.showinfo("Результаты прогнозирования", result_message)

# Получение данных от пользователя
def get_data_from_user():
    def submit_data():
        production = np.zeros(12)
        for i in range(12):
            try:
                production[i] = float(entries[i].get())
            except ValueError:
                messagebox.showerror("Ошибка", f"Некорректное значение для месяца {i+1}") # Варнинг на тот случай, если нету числа
                return
        root.destroy()
        plot_graph(np.array(range(1, 13)), production)
    
    root = tk.Tk()
    root.title("Ввод данных о добыче")
    
    entries = []
    for i in range(12):
        tk.Label(root, text=f"Месяц {i+1}:").grid(row=i, column=0)
        entry = tk.Entry(root)
        entry.grid(row=i, column=1)
        entries.append(entry)
    
    tk.Button(root, text="Отправить", command=submit_data).grid(row=12, columnspan=2)
    root.mainloop()

get_data_from_user() # ПУСК
