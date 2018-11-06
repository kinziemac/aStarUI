import threading
import tkinter as tk
from parse_data import *


class Messenger(threading.Thread):
    def run(self):
        root = tk.Tk()
        colors = ['#e6f7ff', '#b3e6ff', '#80d4ff', '#33bbff', '#00aaff', '#0077b3']
        # root.protocol("WM_DELETE_WINDOW", callback)

        for i in range(boundary):
            for j in range(boundary):
                tk.Label(root, text=str(map[i][j]), background=colors[(map[i][j] - 1)], borderwidth=15 ).grid(row=i,column=j)
        root.mainloop()



txtValues = initializeTxtData()
boundary = txtValues["boundary"]
startIndex = txtValues["start"]
goalIndex = txtValues["goal"]
map = txtValues["map"]



x = Messenger(name="thread 1")
# y = Messenger(name="thread 2")
x.start()
# y.start()
