from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.patches import Rectangle
from sympy import Point, Polygon, Line
from shapely.geometry import Polygon, LineString

import sys

N = 100

### БКГ

u = [[0.3, 0.7],
     [0.3, 0.6]]

T = [[0, 0],
     [0, 1],
     [1, 1],
     [1, 0]]

P = [[0.3, 0.3],
     [0.3, 0.6],
     [0.7, 0.6],
     [0.7, 0.3]]

# print(P)

L = []
for i in range(len(P)):
    L.append([i + 1, P[i][0] + P[i][1] - 1])
print("L :")
print(L)

edges = [
    [1, 2],
    [1, 4],
    [2, 3],
    [3, 4]]

for i in range(4):
    tl = edges[i][0]
    tr = edges[i][1]

    ltl = L[tl - 1][1]
    ltr = L[tr - 1][1]
    r = ltl * ltr

    print("\nL(t^" + str(tl) + ")L(t^" + str(tr) + ") = " + str(round(ltl,2)) + " * " + str(round(ltr,2)) + " = " + str(round(r,2)))

    if (r > 0):
        print(' – не пересекает\n')
        continue
    else:
        print(' - пересекает\n')

square = Polygon([(0.3, 0.3), (0.7, 0.3), (0.7, 0.6), (0.3, 0.6)])
line = LineString([(1, 0), (0, 1)])
B = line.intersection(square)
print("Точки пересечения: ")
print(B)

point_a = Point(0.7, 0.3)
point_b = Point(0.4, 0.6)
point_zero = Point(0.0, 0.0)

vector1 = Line(point_a, point_zero)
perpendicular1 = vector1.perpendicular_line(point_zero)

vector2 = Line(point_b, point_zero)
perpendicular2 = vector2.perpendicular_line(point_zero)

# print(perpendicular1)
# print(perpendicular2)
# isPerpendicular = vector1.is_perpendicular(perpendicular1)
# isPerpendicular2 = vector2.is_perpendicular(perpendicular2)
# print(isPerpendicular)
# print(isPerpendicular2)

# График 1 квадрат и угол
plt.figure()
ax = plt.gca()
ax.grid()
# оси
x = np.arange(0.0, 1.5, 0.000001)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(1.5, 0.0, 'k', marker='>')

y = np.arange(0.0, 1.5, 0.000001)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 1.5, 'k', marker='^')
#Квадрат
ax.add_patch(Rectangle((0.3, 0.3), 0.4, 0.3, linewidth=2, edgecolor='r', facecolor='none'))
#прямая 1
line1_x = [1, 0]
line1_y = [0, 1]

plt.plot(line1_x, line1_y, color="black", linestyle="-")
# вектора от точек пересечения в ноль
# dot_a, dot_b = np.array(B.coords)
dot_a = [0.7, 0.3]
plt.plot(dot_a[0], dot_a[1], 'bo', markersize=2.)

plt.text(dot_a[0] + 0.1, dot_a[1], "A("+str(dot_a[0])+","+str(dot_a[1])+")")
dot_b = [0.4, 0.6]
plt.plot(dot_b[0], dot_b[1], 'bo', markersize=2.)
plt.text(dot_b[0] + 0.1, dot_b[1]+0.1, "B("+str(dot_b[0])+","+str(dot_b[1])+")")
zeros_coords = [0.0, 0.0]
v1_x = [0, 0.7]
x1_y = [0, 0.3]
plt.plot(v1_x, x1_y)
v2_x = [0, 0.4]
x2_y = [0, 0.6]
plt.plot(v2_x, x2_y)

# Угол
x = [0, 0.3]
y = [0, -0.7]
slope1, intercept1 = np.polyfit(x, y, 1)
# print(slope1, intercept1)
x = np.linspace(0, 0.3)
plt.plot(x, slope1 * x + intercept1)

x = [0, (3 / 5)]
y = [0, -(2 / 5)]
slope2, intercept2 = np.polyfit(x, y, 1)
# print(slope2, intercept2)
x = np.linspace(0, -0.3)
plt.plot(x, slope2 * x + intercept2)

### Работа с графиками
# массив точек u1 u2
list_of_u1_u2 = []
for i in range(1, N + 1):
    u1 = round(np.random.uniform(79), 2)
    u2 = round(np.random.uniform(79), 2)
    list_of_u1_u2.append([i, u1, u2])
# print(list_of_u1_u2)

plt.figure()
ax = plt.gca()
ax.grid()
# отрисовка точек u1 u2
for i in range(len(list_of_u1_u2)):
    plt.plot(list_of_u1_u2[i][1], list_of_u1_u2[i][2], 'bo', markersize=2.)
    # Цифры
    # plt.text(list_of_u1_u2[i][1] + 0.1, list_of_u1_u2[i][2], list_of_u1_u2[i][0])

# массив точек J1 J2
list_of_J1_J2 = []
for i in range(0, len(list_of_u1_u2)):
    j1 = (0.2 * (list_of_u1_u2[i][1] - 70) ** 2) + (0.8 * (list_of_u1_u2[i][2] - 20) ** 2)
    j2 = (0.2 * (list_of_u1_u2[i][1] - 10) ** 2) + (0.8 * (list_of_u1_u2[i][2] - 70) ** 2)
    list_of_J1_J2.append([i, j1, j2])

# print(list_of_J1_J2)

# Парето множество
mas_b_i = []
for i in range(0, len(list_of_J1_J2)):
    count_b_i = 0
    x_current = list_of_J1_J2[i][1]
    y_current = list_of_J1_J2[i][2]
    # Построение конусов доминирования
    # plt.vlines(x=x_current, ymin=y_current, ymax=y_current+4, colors='k')
    # plt.hlines(y=y_current, xmin=x_current, xmax=x_current+4, colors='k')
    # Построение обратных конусов доминирования
    # plt.vlines(x=x_current, ymin=y_current, ymax=y_current - 400, colors='k')
    # plt.hlines(y=y_current, xmin=x_current, xmax=x_current - 400, colors='k')
    for j in range(1, len(list_of_J1_J2)):
        if (list_of_J1_J2[j][1] <= x_current and list_of_J1_J2[j][2] <= y_current and list_of_J1_J2[j][1] != x_current
                and list_of_J1_J2[j][2] != y_current):
            count_b_i += 1
    mas_b_i.append([i + 1, count_b_i])

# Массив Парето оптимальных решений
pareto_array = []
plt.figure()
## Строим угол
x = [0, 0.3]
y = [0, -0.7]
slope1, intercept1 = np.polyfit(x, y, 1)
# print(slope1, intercept1)
x = np.linspace(0, 100, 500)
plt.plot(x, slope1 * x + intercept1)

x = [0, (3 / 5)]
y = [0, -(2 / 5)]
slope2, intercept2 = np.polyfit(x, y, 1)
# print(slope2, intercept2)
x = np.linspace(0, -100, 500)
plt.plot(x, slope2 * x + intercept2)
axes = plt.gca()

# отрисовка J1 J2 Парето
list_of_optimal = []
list_of_optimal_for_table = []
for i in range(len(list_of_J1_J2)):
    # Построение обратных конусов доминирования
    # x_current = list_of_J1_J2[i][1]
    # y_current = list_of_J1_J2[i][2]
    if mas_b_i[i][1] == 0:
        plt.plot(list_of_J1_J2[i][1], list_of_J1_J2[i][2], 'bo', markersize=2.)
        pareto_array.append([i+1,list_of_J1_J2[i][1],list_of_J1_J2[i][2]])
        # ax.axline(list_of_J1_J2[i][1], list_of_J1_J2[i][2], slope1)
        # ax.axline(list_of_J1_J2[i][1], list_of_J1_J2[i][2], slope2)
        # plt.vlines(x=x_current, ymin=y_current, ymax=y_current - 400, colors='k')
        # plt.hlines(y=y_current, xmin=x_current, xmax=x_current - 400, colors='k')
        # Цифры
        # plt.text(list_of_J1_J2[i][1] + 0.1, list_of_J1_J2[i][2], list_of_J1_J2[i][0])
    else:
        pareto_array.append([i + 1, 0, 0])
        plt.plot(list_of_J1_J2[i][1], list_of_J1_J2[i][2], 'ro', markersize=2.)
        # Цифры
        # plt.text(list_of_J1_J2[i][1] + 0.1, list_of_J1_J2[i][2], list_of_J1_J2[i][0])
    flag = False
    x_val1 = np.array(axes.get_xlim())
    y_val1 = np.array(slope1 * (x_val1 - list_of_J1_J2[i][1]) + list_of_J1_J2[i][2])
    # plt.plot(x_val1, y_val1, color="black", linestyle="-")
    x_val2 = np.array(axes.get_xlim())
    y_val2 = np.array(slope2 * (x_val2 - list_of_J1_J2[i][1]) + list_of_J1_J2[i][2])
    # plt.plot(x_val2, y_val2, color="black", linestyle="-")
    x_cur = list_of_J1_J2[i][1]
    y_cur = list_of_J1_J2[i][2]
    # print("x_val1 y_val1 ", x_val1, " ", y_val1)
    # print("x_val2 y_val2 ", x_val2, " ", y_val2)
    # print("\nБерем точку ", list_of_J1_J2[i])
    for j in range(len(list_of_J1_J2)):
        if list_of_J1_J2[j][1] != x_cur and list_of_J1_J2[j][2] != y_cur:
            v1 = (x_val1[1] - x_val1[0], y_val1[1] - y_val1[0])  # Vector 1
            v2 = (x_val2[1] - x_val2[0], y_val2[1] - y_val2[0])  # Vector 2
            v_dot1 = (x_val1[1] - list_of_J1_J2[j][1], y_val1[1] - list_of_J1_J2[j][2])  # dot
            v_dot2 = (x_val2[1] - list_of_J1_J2[j][1], y_val2[1] - list_of_J1_J2[j][2])  # dot
            xp_1 = v1[0] * v_dot1[1] - v1[1] * v_dot1[0]  # Cross
            xp_2 = v2[0] * v_dot2[1] - v2[1] * v_dot2[0]  # Cross
            if xp_2 > 0 and xp_1 > 0:
                flag = True
                # print('Попал в угол ', list_of_J1_J2[j])
    if flag == False:
        list_of_optimal.append(list_of_J1_J2[i])
        list_of_optimal_for_table.append(list_of_J1_J2[i])
    else:
        list_of_optimal_for_table.append([i + 1, 0, 0])

axes = plt.gca()
for i in range(len(list_of_optimal)):
    x = np.linspace(list_of_optimal[i][1], list_of_optimal[i][1]+1000)
    y = np.array(slope1 * (x - list_of_optimal[i][1]) + list_of_optimal[i][2])
    #Оптимальный угол
    # plt.plot(x, y,color="black", linestyle="-", linewidth=1)
    x = np.linspace(list_of_optimal[i][1], list_of_optimal[i][1]-1000)
    y = np.array(slope2 * (x - list_of_optimal[i][1]) + list_of_optimal[i][2])
    # Оптимальный угол
    # plt.plot(x, y, color="black", linestyle="-", linewidth=1)
    plt.plot(list_of_optimal[i][1], list_of_optimal[i][2], 'go', markersize=2.)
    # Цифры
    # plt.text(list_of_optimal[i][1] + 0.1, list_of_optimal[i][2], list_of_optimal[i][0])

# legend
red_dots = mlines.Line2D([], [], color='red', marker='.', linestyle='None',
                         markersize=10, label='Область допустимых оценок')
blue_dots = mlines.Line2D([], [], color='blue', marker='.', linestyle='None',
                          markersize=10, label='Парето оптимальные')
green_dots = mlines.Line2D([], [], color='green', marker='.', linestyle='None',
                         markersize=10, label='Оптимальные решения')
plt.legend(handles=[red_dots, blue_dots, green_dots])

# print(pareto_array)
# print(list_of_optimal)

table = PrettyTable()
table.field_names = ["№", "u1", "u2","J1", "J2","Парето","Конус доминирования"]
for i in range(100):
    if pareto_array[i][1] == 0 and pareto_array[i][2] == 0:
        table.add_row([list_of_u1_u2[i][0],list_of_u1_u2[i][1],list_of_u1_u2[i][2],round(list_of_J1_J2[i][1],2),
                   round(list_of_J1_J2[i][2],2), 0,0])
    elif pareto_array[i][1] != 0 and pareto_array[i][2] != 0 and list_of_optimal_for_table[i][1] == 0 and list_of_optimal_for_table[i][2] == 0:
        table.add_row([list_of_u1_u2[i][0], list_of_u1_u2[i][1], list_of_u1_u2[i][2], round(list_of_J1_J2[i][1], 2),
                       round(list_of_J1_J2[i][2], 2), True,0])
    else:
        table.add_row([list_of_u1_u2[i][0], list_of_u1_u2[i][1], list_of_u1_u2[i][2], round(list_of_J1_J2[i][1], 2),
                       round(list_of_J1_J2[i][2], 2), True, True])

print(table)

plt.grid()
# Вывод всех графиков
plt.show()
