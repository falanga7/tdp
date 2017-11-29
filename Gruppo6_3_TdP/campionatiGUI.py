import tkinter as tk
from tkinter import *
from tkinter import ttk
from Gruppo6_3_TdP import xlrd
from Gruppo6_3_TdP.xlrd.sheet import ctype_text
from math import sqrt
from Gruppo6_3_TdP.TdP_collections.hash_table.probe_hash_map import ProbeHashMap


def dispatcher(file):
    x_workbook = xlrd.open_workbook(file)
    x_sheet = x_workbook.sheet_by_name("I1")
    nrows = x_sheet.nrows
    ns = int((1 + sqrt(1+4*(nrows-1)))/2)
    ng = (ns -1) * 2
    squadre = ProbeHashMap(cap= ns)
    n = 0
    for row_idx in range(1, x_sheet.nrows):
        if not n == ns:
            home_team = x_sheet.cell(row_idx, 2).value
            away_team = x_sheet.cell(row_idx, 3).value
            squadre[home_team] = home_team
            squadre[away_team] = away_team
            n = squadre._n

    print("test")


root = Tk()
dispatcher("all-euro-data-2016-2017.xls")
root.title("Campionati")
root.resizable(0, 0)
c1 = ttk.Label(root, justify=tk.CENTER, text="Seleziona il campionato:").pack(side="top")
csv = StringVar()
oc = ["option 1", "option 2", "option 3"]
comboC = ttk.Combobox(root, textvariable=csv, values=oc)
comboC.pack()
ac = ttk.Notebook(root)
squadre = ttk.Frame(ac)
f2 = ttk.Frame(ac)
ac.add(squadre, text='Squadre')
ac.add(f2, text='Two')
ac.pack()

squadreT = ttk.Treeview(root)
squadreT.heading("#0", text='Squadre', anchor='w')
squadreT.column("#0", anchor="w")
squadreT.insert("", 0, text="lol")
squadreT.pack()

# codice per interfaccia grafica a schermo intero, premere ESC per uscire
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()
