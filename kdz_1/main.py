import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from matplotlib.ticker import (MultipleLocator)
import sys

# окно таблицы
app = QApplication(sys.argv)
qwidget = QWidget()
qwidget.setWindowTitle("Table")
qwidget.resize(1280, 500)
label_text_title = QLabel()
label_text_title.setText("Алгоритм многокритериального ранжирования")
qwidget.setStyleSheet("QLabel{font-size: 18pt;}")

qwindow = QWidget()
qwindow.setWindowTitle("Info")
qwindow.resize(1280, 500)
qwindow.setStyleSheet("QLabel{font-size: 18pt;}")
label1 = QLabel()
label2 = QLabel()
label3 = QLabel()
label1.setText("Контрольное домашнее задание №1.1")
label2.setText("Множество эффективных проектов:")

n = 17
N = 100
# table = PrettyTable()
p = []
r1 = 1
r2 = 0.85
r3 = 0.75
k_i = []
mas_b_i_new = []
mas_k_i_new = []

# сетка
fig, ax = plt.subplots(figsize=(10, 8))

ax.set_xlim(0, (n * 2) + 2)
ax.set_ylim(0, (n * 2) + 2)

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

# оси
x = np.arange(0.0, (n * 2) + 2, 0.000001)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot((n * 2) + 2, 0.0, 'k', marker='>')

y = np.arange(0.0, (n * 2) + 2, 0.000001)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, (n * 2) + 2, 'k', marker='^')

# круг
circle = plt.Circle((n, n), n, color='r', fill=False,
                    label="(f1-" + str(n) + ")^2 + (f2-" + str(n) + ")^2 ≤ " + str(n ** 2))
ax = plt.gca()
ax.add_patch(circle)
plt.axis('scaled')

# прямая f1+f2
x = [0, n * 2]
y = [n * 2, 0]
plt.plot(x, y, 'blue', label="f1 + f2  ≥" + str(2 * n))

# прямая -f1+f2
x = [0, n]
y = [n, n * 2]
plt.plot(x, y, 'green', label="-f1 + f2 ≤" + str(n))

# legend
plt.legend(loc="upper left")

# массив всех точек
list_of_dots_new = []

# рандомим и проверяем область
for i in range(1, N+1):
    x = round(np.random.uniform(n * 2), 2)
    y = round(np.random.uniform(n * 2), 2)
    while ((x - n) ** 2 + (y - n) ** 2 > n ** 2) or (-x + y > n) or (x + y < n * 2):
        x = round(np.random.uniform(n * 2), 2)
        y = round(np.random.uniform(n * 2), 2)
    list_of_dots_new.append([i, x, y])
    # list_of_dots[i][1] = x
    # list_of_dots[i][2] = y
print(list_of_dots_new)
# считаем Bi
for i in range(0, N):
    count_b_i = 0
    x_current = list_of_dots_new[i][1]
    y_current = list_of_dots_new[i][2]
    #Построение конусов доминирования
    # plt.vlines(x=x_current, ymin=y_current, ymax=y_current+4, colors='k')
    # plt.hlines(y=y_current, xmin=x_current, xmax=x_current+4, colors='k')
    # Построение обратных конусов доминирования
    # plt.vlines(x=x_current, ymin=y_current, ymax=y_current - 4, colors='k')
    # plt.hlines(y=y_current, xmin=x_current, xmax=x_current - 4, colors='k')
    for j in range(1, N):
        if (list_of_dots_new[j][1] >= x_current and list_of_dots_new[j][2] >= y_current and list_of_dots_new[j][1] != x_current
                and list_of_dots_new[j][2] != y_current):
            count_b_i += 1
    mas_b_i_new.append([i+1, count_b_i])
    mas_k_i_new.append([i+1, 0])

# второе задание p = {}
for i in range(len(mas_b_i_new)):
    if mas_b_i_new[i][1] == 0:
        p.append(mas_b_i_new[i])
print("Оптимальные решения")
print(p)
print_p = []
for i in range(len(p)):
    print_p.append(p[i][0])
label3.setText("p = { " + ", ".join(repr(e) for e in print_p) + " }")
print("\nmas_b_i_new")
print(mas_b_i_new)

main_table = []

# консольная таблица
table_field = ["i"]
row_f1 = ["f1"]
row_f2 = ["f2"]
row_b_i = ["b_i"]
row_Fi_i = ["Ф_i"]
row_k_i = ["k_i"]
row_r1 = ["r1 = 1"]
row_r2 = ["r2 = 0.85"]
row_r3 = ["r3 = 0.75"]

for i in range(len(list_of_dots_new)):
    table_field.append(list_of_dots_new[i][0])
    row_f1.append(list_of_dots_new[i][1])
    row_f2.append(list_of_dots_new[i][2])

main_table.append(row_f1)
main_table.append(row_f2)
for i in range(0, N):
    row_b_i.append(mas_b_i_new[i][1])
    Fi_i = round(1 / (1 + (mas_b_i_new[i][1] / (N - 1))), 2)
    r1 = round(abs(1 - Fi_i), 2)
    r2 = round(abs(0.85 - Fi_i), 2)
    r3 = round(abs(0.75 - Fi_i), 2)
    # меньшее по столбцу
    if r2 >= r1 <= r3:
        k_i = 1
    elif r1 >= r2 <= r3:
        k_i = 2
    else:
        k_i = 3
    row_Fi_i.append(Fi_i)
    row_k_i.append(k_i)
    row_r1.append(r1)
    row_r2.append(r2)
    row_r3.append(r3)
    mas_k_i_new[i][1] = k_i

main_table.append(row_b_i)
main_table.append(row_Fi_i)
main_table.append(row_k_i)
main_table.append(row_r1)
main_table.append(row_r2)
main_table.append(row_r3)

print("\nmas_k_i_new")
print(mas_k_i_new)

# отрисовка точек по цветам
for i in range(len(list_of_dots_new)):
    if mas_k_i_new[i][1] == 1:
        plt.plot(list_of_dots_new[i][1], list_of_dots_new[i][2], 'bo')
        plt.text(list_of_dots_new[i][1] + 0.1, list_of_dots_new[i][2], list_of_dots_new[i][0])
    if mas_k_i_new[i][1] == 2:
        plt.plot(list_of_dots_new[i][1], list_of_dots_new[i][2], 'ro')
        plt.text(list_of_dots_new[i][1] + 0.1, list_of_dots_new[i][2], list_of_dots_new[i][0])
    if mas_k_i_new[i][1] == 3:
        plt.plot(list_of_dots_new[i][1], list_of_dots_new[i][2], 'go')
        plt.text(list_of_dots_new[i][1] + 0.1, list_of_dots_new[i][2], list_of_dots_new[i][0])

# вывод таблицы
layout = QVBoxLayout()
layout2 = QVBoxLayout()

tableWidget = QTableWidget()
numrows = 8
numcols = N+1
tableWidget.setColumnCount(numcols)
tableWidget.setRowCount(numrows)

for col in range(numcols):
    tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(str(table_field[col])))
for row in range(numrows):
    for column in range(numcols):
        tableWidget.setItem(row, column, QTableWidgetItem(str(main_table[row][column])))

layout.addWidget(label_text_title)
layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()

layout2.addWidget(label1)
layout2.addWidget(label2)
layout2.addWidget(label3)
qwindow.setLayout(layout2)
qwindow.show()

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.grid()
plt.show()

sys.exit(app.exec_())