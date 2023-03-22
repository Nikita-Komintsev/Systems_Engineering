import numpy as np
import matplotlib.pyplot as plt
from tkinter.ttk import Notebook
from tkinter import ttk, Tk, Label
import tkinter as tk


class Window:
    def __init__(self, width, height, title="MyWindow"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+300+200")
        self.root.geometry("+300+100")
        Label(self.root, text="Оптимальные стратегии игры: ", font=("Helvetica", 18)).pack()
        Label(self.root, text="p*=[7/9; 2/9]", font=("Helvetica", 18)).pack()
        Label(self.root, text="q*=[1/3; 0; 2/3; 0]", font=("Helvetica", 18)).pack()
        Label(self.root, text="Цена игры: V = 10/3", font=("Helvetica", 18)).pack()

    def run(self):
        self.root.mainloop()



# оси
x = np.arange(0, 1.1, 0.000001)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(1.1, 0, 'k', marker='>')

y = np.arange(0, 11)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0, 10, 'k', marker='^')


def intersect(b1_cords, b3_cords):
    x1 = b1_cords[0][0]
    y1 = b1_cords[1][0]
    x2 = b1_cords[0][1]
    y2 = b1_cords[1][1]
    x3 = b3_cords[0][0]
    y3 = b3_cords[1][0]
    x4 = b3_cords[0][1]
    y4 = b3_cords[1][1]
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return (x, y)


matrix_A = [[2, 4, 4, 7], [8, 2, 1, 1]]

b1_cords = [(0, 1), (8, 2)]
b2_cords = [(0, 1), (2, 4)]
b3_cords = [(0, 1), (1, 4)]
b4_cords = [(0, 1), (1, 7)]

plt.plot((1, 1), (0, 10), linestyle='--', color='k')

plt.plot(b1_cords[0], b1_cords[1], color='k')
plt.text(0.01, 8, 'B1')
plt.text(1.01, 2, 'B1')

plt.plot(b2_cords[0], b2_cords[1], color='k')
plt.text(0.01, 2.2, 'B2')
plt.text(1.01, 4.2, 'B2')

plt.plot(b3_cords[0], b3_cords[1], color='k')
plt.text(0.01, 1.3, 'B3')
plt.text(1.01, 3.8, 'B3')

plt.plot(b4_cords[0], b4_cords[1], color='k')
plt.text(0.01, 0.7, 'B4')
plt.text(1.01, 7, 'B4')

# пересечение прямых b1 b3 в точке N
intersection = intersect(b1_cords, b3_cords)
plt.plot(intersection[0], intersection[1], 'ro')
plt.text(intersection[0] + 0.01, intersection[1] - 0.5, "N")
print(intersection)

# выделение красным нижней огибающей
# от b4 до  intersection
dot1 = b4_cords[0][0], intersection[0]
dot2 = b4_cords[1][0], intersection[1]
plt.plot(dot1, dot2, color='red')

# от intersection до b1
dot1 = intersection[0], b1_cords[0][1]
dot2 = intersection[1], b1_cords[1][1]
plt.plot(dot1, dot2, color='red')

# перпендикуляр на ось X
dot1 = intersection[0], intersection[0]
dot2 = 0, intersection[1]
plt.plot(dot1, dot2, linestyle='--', color='red')
plt.text(intersection[0], -0.4, 'p1*')

# в консоль ответ
print("Оптимальные стратегии игры:")
print("p*=[7/9; 2/9]")
print("q*=[1/3; 0; 2/3; 0]")
print("Цена игры: V = 10/3")

window = Window(800, 500, "KDZ 2")

plt.grid()
plt.show()

window.run()
