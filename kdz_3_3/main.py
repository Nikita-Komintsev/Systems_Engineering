from tkinter import *
from tkinter import ttk

root = Tk()
root.title("KDZ 3")
root.geometry("700x400")
columns = ("k", "i", "B1","B2","B3","B4", "a(k)", "j","A1","A2","b(k)","V(k)")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.column("#1",width=50,anchor=CENTER, stretch=NO)
tree.column("#2",width=50,anchor=CENTER, stretch=NO)
tree.column("#3",width=50,anchor=CENTER, stretch=NO)
tree.column("#4",width=50,anchor=CENTER, stretch=NO)
tree.column("#5",width=50,anchor=CENTER, stretch=NO)
tree.column("#6",width=50,anchor=CENTER, stretch=NO)
tree.column("#7",width=50,anchor=CENTER, stretch=NO)
tree.column("#8",width=50,anchor=CENTER, stretch=NO)
tree.column("#9",width=50,anchor=CENTER, stretch=NO)
tree.column("#10",width=50,anchor=CENTER, stretch=NO)
tree.column("#11",width=50,anchor=CENTER, stretch=NO)
tree.column("#12",width=50,anchor=CENTER, stretch=NO)
my_Font = ('URW Gothic L','12','bold')

tree.heading("k", text="k")
tree.heading("i", text="i")
tree.heading("B1", text="B1")
tree.heading("B2", text="B2")
tree.heading("B3", text="B3")
tree.heading("B4", text="B4")
tree.heading("a(k)", text="a(k)")
tree.heading("j", text="j")
tree.heading("A1", text="A1")
tree.heading("A2", text="A2")
tree.heading("b(k)", text="b(k)")
tree.heading("V(k)", text="V(k)")
A = [[2, 4, 4, 7], [8, 2, 1, 1]]
B = [[2, 8], [4, 2], [4, 1], [7, 1]]

i = 0
newA = [0, 0, 0, 0]
newB = [0, 0]
MAX_ITER = 100
dictA = {0: 0, 1: 0}
dictB = {0: 0, 1: 0, 2: 0, 3: 0}
print('k i B1 B2 B3 B4 a j A1 A2 b V')
person = list()
for k in range(1, MAX_ITER + 1):

    for a in range(4):
        newA[a] += A[i][a]
    dictA[i] += 1
    ak = min(newA) / k
    j = newA.index(min(newA))
    dictB[j] += 1
    for b in range(2):
        newB[b] += B[j][b]
    bk = max(newB) / k
    vk = (ak + bk) / 2
    person = [k, i + 1, newA[0], newA[1], newA[2], newA[3], round(ak, 3), j + 1, newB[0], newB[1], round(bk, 3),
              round(vk, 3)]
    tree.insert("", END, values=person)

    i = newB.index(max(newB))



print("k = " + str(k) + ";a(k) = " + str(ak) + ";b(k) = " + str(bk) + ";V(k) = " + str(vk))
p1 = dictA[0] / MAX_ITER
p2 = dictA[1] / MAX_ITER
print(dictA)
q1 = dictB[0] / MAX_ITER
q2 = dictB[1] / MAX_ITER
q3 = dictB[2] / MAX_ITER
q4 = dictB[3] / MAX_ITER
print(dictB)
print("p* = (" + str(p1) + ", " + str(p2) + "); q* = (" + str(q1) + ", " + str(q2) + ", " + str(q3) + ", " + str(
    q4) + "); V = " + str(vk))
ttk.Label(text="k = " + str(k) + ";a(k) = " + str(ak) + ";b(k) = " + str(bk) + ";V(k) = " + str(vk)+"\np* = (" + str(p1) + ", " + str(p2) + "); q* = (" + str(q1) + ", " + str(q2) + ", " + str(q3) + ", " + str(
    q4) + "); V = " + str(vk) ,font=my_Font).pack(fill=BOTH)
root.mainloop()