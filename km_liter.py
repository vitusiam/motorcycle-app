from tkinter import *

win = Tk()
win.geometry("600x300")
win.config(bg="grey")
win.title("Distance Calculator")

record_distance = [
    [8643, 6.97],
    [8422, 6.53],
    [8220, 7.34]
]


def cal():
    k = int(km.get())
    lt = float(liter.get())
    refuel_at = round(((k - record_distance[0][0]) / lt) * 8.5 + k)
    average = round(((k - record_distance[0][0]) / lt), 2)
    next_refuel.config(text="Vitus, your next refuel is at " + str(refuel_at) + " km.")
    av.config(text="Average " + str(average) + " km/liter")

    new = []
    rk = int(km.get())
    rl = float(liter.get())
    new.append(rk)
    new.append(rl)
    record_distance.insert(0, new)
    print(record_distance)
    file = open("/users/vituswu/desktop/motorcycle app/history.txt", "w")
    file.write(str(record_distance))
    file.close()
    return new


lb = Label(text="Enter current km", bg="grey", fg="white")
lb.pack()

km = Entry()
km.pack()

lb2 = Label(text="How much liter fuel added ?", bg="grey", fg="white")
lb2.pack()

liter = Entry()
liter.pack()

btn = Button(text="Calculate", command=cal)
btn.pack()

next_refuel = Label(text="", bg="grey", fg="white")
next_refuel.pack()

av = Label(text="", bg="grey", fg="white")
av.pack()

win.mainloop()
