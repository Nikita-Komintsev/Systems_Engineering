
from pulp import *
from sympy import Point, Polygon, Line
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.patches import Rectangle

n = 11

gamma1 = 5*n
gamma3 = -6*n

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem = pulp.LpProblem('0',LpMaximize)
problem += (-3)*x1 + x2, "Функция цели"
problem += x1 + x2 >= 2*n, "1"
problem += x1 - 2*x2 <= n, "2"
problem += (-3)*x1 + 2*x2 <= 2*n, "3"
problem += x1 + 0*x2 <= 4*n, "4"
problem += 0*x1+x2 <= 3*n, "5"
problem += x1 + (-3)*x2 >= gamma3, "6"
problem += x1 + x2 >= gamma1, "7"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
# print("Значение функции :")
# print(abs(value(problem.objective)))

def cal_intersection(k1, b1, k2, b2):
    x = (b2 - b1) / (k1 - k2)
    y = k1 * (b2 - b1) / (k1 - k2) + b1
    return (x, y)


plt.figure(figsize=(6, 6))
plt.axis([-5, 60, -5, 60])

# оси
x = np.arange(0.0, 60)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(60, 0.0, 'k', marker='>')

y = np.arange(0.0, 60)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 60, 'k', marker='^')

d = np.linspace(-0,120,1000)
x,y = np.meshgrid(d,d)
plt.imshow( ((y<=3*n) & (y>=0) & (x<=4*n) & (x>=0) & (y>=2*n-x) & (2*y>=x-n) & (2*y<=2*n+3*x) & (y>=gamma1-x) & (3*y<=-gamma3+x)).astype(int) ,
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

# l1: x2 >= 55 - x1
x = [0, 55]
y = [55, 0]
plt.plot(x, y, "green",)# label="l1: x2 >= 55 - x1")
plt.text(1,55,"l1")

# l2: x2 <= 22 + (x1/3)
x = [0, 51]
y = [22, 39]
plt.plot(x, y, "green",)# label="l2: x2 <= 22 + (x1/3)")
plt.text(1,24,"l2")

# точки
# y = 33 и -3*x1 + 2*x2  <= 22
x_cross_A, y_cross_A = cal_intersection(0, 33, 3 / 2, 11)
x_cross_A = round(x_cross_A, 2)
y_cross_A = round(y_cross_A, 2)
plt.plot(x_cross_A, y_cross_A, 'bo', markersize=2.)
plt.text(x_cross_A + 0.1, y_cross_A, "A")
#
# y = 33 и x = 44
x_cross_B = 44
y_cross_B = 33
plt.plot(x_cross_B, y_cross_B, 'bo', markersize=2.)
plt.text(x_cross_B + 0.1, y_cross_B, "B")
#
# x = 44 и x1 - 2*x2  <= 11
x_cross_C = 44
y_cross_C = 16.5
plt.plot(x_cross_C, y_cross_C, 'bo', markersize=2.)
plt.text(x_cross_C + 0.1, y_cross_C, "C")

# x1 + x2  >= 22 и  x1 - 2*x2  <= 11
x_cross_D, y_cross_D = cal_intersection(-1, 22, 0.5, -5.5)
x_cross_D = round(x_cross_D, 2)
y_cross_D = round(y_cross_D, 2)
plt.plot(x_cross_D, y_cross_D, 'bo', markersize=2.)
plt.text(x_cross_D + 0.1, y_cross_D, "D")

# # x1 + x2  >= 22 и  -3*x1 + 2*x2  <= 22
x_cross_E, y_cross_E = cal_intersection(-1, 22, 3 / 2, 11)
x_cross_E = round(x_cross_E, 2)
y_cross_E = round(y_cross_E, 2)
plt.plot(x_cross_E, y_cross_E, 'bo', markersize=2.)
plt.text(x_cross_E + 0.1, y_cross_E, "E")

# прямые по точкам
# A-B
x = [x_cross_A, x_cross_B]
y = [y_cross_A, y_cross_B]
plt.plot(x, y, 'k', label="y = 33")
# B-C
x = [x_cross_B, x_cross_C]
y = [y_cross_B, y_cross_C]
plt.plot(x, y, 'blue', label="x = 44")
# C-D
x = [x_cross_C, x_cross_D]
y = [y_cross_C, y_cross_D]
plt.plot(x, y, 'cyan', label="x - 2y = 11")
# D-E
x = [x_cross_D, x_cross_E]
y = [y_cross_D, y_cross_E]
plt.plot(x, y, 'magenta', label="x + y = 22")
# E-A
x = [x_cross_E, x_cross_A]
y = [y_cross_E, y_cross_A]
plt.plot(x, y, 'yellow', label=" -3x + 2y = 22")

# пересечения фигуры с l1 l2
# l1 и y = 33
x_cross_F, y_cross_F = cal_intersection(0, 33, -1, 55)
x_cross_F = round(x_cross_F, 2)
y_cross_F = round(y_cross_F, 2)
plt.plot(x_cross_F, y_cross_F, 'bo', markersize=2.)
plt.text(x_cross_F, y_cross_F - 1, "F")

# l1 и  x1 - 2*x2  <= 11
x_cross_G, y_cross_G = cal_intersection(-1, 55, 0.5, -5.5)
x_cross_G = round(x_cross_G, 2)
y_cross_G = round(y_cross_G, 2)
plt.plot(x_cross_G, y_cross_G, 'bo', markersize=2.)
plt.text(x_cross_G + 0.1, y_cross_G, "G")

# l2 и  -3*x1 + 2*x2  <= 22
x_cross_H, y_cross_H = cal_intersection(1 / 3, 22, 3 / 2, 11)
x_cross_H = round(x_cross_H, 2)
y_cross_H = round(y_cross_H, 2)
plt.plot(x_cross_H, y_cross_H, 'bo', markersize=2.)
plt.text(x_cross_H + 0.1, y_cross_H, "H")

# l2 и y = 33
x_cross_K, y_cross_K = cal_intersection(0, 33, 1 / 3, 22)
x_cross_K = round(x_cross_K, 2)
y_cross_K = round(y_cross_K, 2)
plt.plot(x_cross_K, y_cross_K, 'bo', markersize=2.)
plt.text(x_cross_K + 0.1, y_cross_K, "K")

# l1 и l2
x_cross_Q, y_cross_Q = cal_intersection(-1, 55, 1 / 3, 22)
x_cross_Q = round(x_cross_Q, 2)
y_cross_Q = round(y_cross_Q, 2)
plt.plot(x_cross_Q, y_cross_Q, 'bo', markersize=2.)
plt.text(x_cross_Q + 0.1, y_cross_Q, "Q")

# Вектор
plt.arrow(0, 0, -3, 1, width = 0.3)
point_a = Point(-3, 1)
point_zero = Point(0.0, 0.0)
vector = Line(point_a, point_zero)
perpendicular = vector.perpendicular_line(point_zero)

x_perp = [0, 1]
y_perp = [0, 3]
slope, intercept = np.polyfit(x_perp, y_perp, 1)
x = np.linspace(0, 20)
plt.plot(x, slope * x + intercept, 'red')
print("∇=[-3;1]\n")


# Оптимальные
array = [["Q", x_cross_Q, y_cross_Q], ["K", x_cross_K, y_cross_K],
         ["B", x_cross_B, y_cross_B], ["C", x_cross_C, y_cross_C],["G", x_cross_G, y_cross_G]]
opt = ''
int_opt = -1000
# for dot in array:
#     x_opt = dot[1]
#     y_opt = dot[2]
#     f2 = -3 * x_opt + y_opt
#     print("f2(" + dot[0] + ")=" + str(f2))
#     if f2 >= int_opt:
#         opt = dot[0]
#         int_opt = f2

axes = plt.gca()
for dot in array:
    if dot[0] == opt:
        x_opt = dot[1]
        y_opt = dot[2]
        x_val = np.array(axes.get_xlim())
        y_val = np.array(slope * (x_val - x_opt) + y_opt)
        plt.plot(x_val, y_val, '--')
        f1 = round(x_opt + y_opt, 2)
        f2 = round(-3*x_opt + y_opt, 2)
        f3 = round(x_opt - 3*y_opt, 2)
        print("\nт."+dot[0]+"("+str(x_opt)+";"+str(y_opt)+")"+"-оптимальное решение")
        print("\nf1("+dot[0]+")=", f1)
        print("f2("+dot[0]+")=", f2)
        print("f3("+dot[0]+")=", f3)

# legend
plt.legend(loc="upper right")
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')

plt.grid()
plt.show()