import pulp
from pulp import PULP_CBC_CMD
import tkinter as tk
from tkinter import Label


# Primal
problem = pulp.LpProblem("Primal", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem += x1 + x2

problem += 2 * x1 + 8 * x2 >= 1
problem += 4 * x1 + 2 * x2 >= 1
problem += 4 * x1 + 1 * x2 >= 1
problem += 7 * x1 + 1 * x2 >= 1

problem.solve(PULP_CBC_CMD(msg=0))

x1 = round(pulp.value(x1), 3)
x2 = round(pulp.value(x2), 3)
Fmin1 = round(pulp.value(problem.objective), 3)
V_x = round(1 / (pulp.value(x1) + pulp.value(x2)), 3)

print("Primal Solution:")
print("x1 =", x1)
print("x2 =", x2)
print("Fmin =", Fmin1)

print("V = ", V_x)
p1 = round(pulp.value(x1) * V_x, 3)
p2 = round(pulp.value(x2) * V_x, 3)
print(f'p1 = {p1}; p2 = {p2}')

# Dual
dual_problem = pulp.LpProblem("Dual", pulp.LpMaximize)

y1 = pulp.LpVariable("y1", lowBound=0)
y2 = pulp.LpVariable("y2", lowBound=0)
y3 = pulp.LpVariable("y3", lowBound=0)
y4 = pulp.LpVariable("y4", lowBound=0)

dual_problem += y1 + y2 + y3 + y4

dual_problem += 2 * y1 + 4 * y2 + 4 * y3 + 7 * y4 <= 1
dual_problem += 8 * y1 + 2 * y2 + 1 * y3 + 1 * y4 <= 1

dual_problem.solve(PULP_CBC_CMD(msg=0))

y1 = round(pulp.value(y1), 3)
y2 = round(pulp.value(y2), 3)
y3 = round(pulp.value(y3), 3)
y4 = round(pulp.value(y4), 3)
Fmin2 = round(pulp.value(dual_problem.objective), 3)

print()
print("Dual Solution:")
print("y1 =", y1)
print("y2 =", y2)
print("y3 =", y3)
print("y4 =", y4)
print("Fmin=", Fmin2)
V_y = round(1 / (pulp.value(y1) + pulp.value(y2) + pulp.value(y3)), 3)
print("V = ", V_y)

q1 = round(pulp.value(y1) * V_y, 3)
q2 = round(pulp.value(y2) * V_y, 3)
q3 = round(pulp.value(y3) * V_y, 3)
q4 = round(pulp.value(y4) * V_y, 3)
print(f'q1 = {q1}; q2 = {q2}; q3 = {q3}; q4 = {q4}')

# print final solution
print()
print("Решение игры: ")
print(f'p1* = {p1}; p2 = {p2}')
print(f'q1* = {q1}; q2 = {q2}; q3 = {q3}; q4 = {q4}')
print("V = ", V_x)


class Window:
    def __init__(self, width, height, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+300+200")
        self.root.geometry("+300+100")
        Label(self.root, text="Дана матричная игра: ", font=("Helvetica", 18)).pack()
        Label(self.root, text="      | 2 4 4 7 | ", font=("Helvetica", 18)).pack()
        Label(self.root, text="A = | 8 2 1 1 | ", font=("Helvetica", 18)).pack()

        Label(self.root, text="\nПрямая задача: ", font=("Helvetica", 18)).pack()
        Label(self.root, text=f'x1 = {x1}; x2 = {x2}', font=("Helvetica", 14)).pack()
        # Label(self.root, text=f'x1 = {x1}; x2 = {x2}; x3 = 0; x4 = {x2}; x5 = 0; x6 = 0,7', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'Fmin = {Fmin1}', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'V = {V_x}', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'p1 = {p1}; p2 = {p2}', font=("Helvetica", 14)).pack()

        Label(self.root, text="\nДвойственная задача: ", font=("Helvetica", 18)).pack()
        Label(self.root, text=f'y1 = {y1}; y2 = {y2}; y3 = {y3}; y4 = {y4}', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'q1 = {q1}; q2 = {q2}; q3 = {q3}; q4 = {q4}',
              font=("Helvetica", 14)).pack()
        Label(self.root, text=f'V = {V_y}', font=("Helvetica", 14)).pack()

        Label(self.root, text="\nРешение игры:", font=("Helvetica", 18)).pack()
        Label(self.root, text=f'p* = [{p1}; {p2}]', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'q* = [{q1}; {q2}; {q3}; {q4}]', font=("Helvetica", 14)).pack()
        Label(self.root, text=f'V = {V_y}', font=("Helvetica", 14)).pack()

    def run(self):
        self.root.mainloop()


window = Window(800, 600, "KDZ 4")

window.run()
