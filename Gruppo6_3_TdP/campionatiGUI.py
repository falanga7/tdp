import tkinter as tk
from tkinter import *
from tkinter import ttk
from Gruppo6_3_TdP import xlrd
from Gruppo6_3_TdP.xlrd.sheet import ctype_text
from math import sqrt
from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap
from Gruppo6_3_TdP.TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from Gruppo6_3_TdP.campionato import Campionato
from Gruppo6_3_TdP.squadra import Squadra
from Gruppo6_3_TdP.partita import Partita


def dispatcher(file, cl):
    x_workbook = xlrd.open_workbook(file)
    campionati = ProbeHashMap(cap=int(len(cl)/0.5 + 1))
    for campionatoe in cl:
        x_sheet = x_workbook.sheet_by_name(campionatoe)
        nrows = x_sheet.nrows
        ns = int((1 + sqrt(1 + 4 * (nrows - 1))) / 2)
        ng = (ns - 1) * 2
        squadre = ChainHashMap(cap=int(ns / 0.9 + 1))
        giornate = [None] * (ng + 1)
        n = 1
        try:
            while not squadre._n == ns or not n == x_sheet.nrows:
                home_team = x_sheet.cell(n, 2).value
                away_team = x_sheet.cell(n, 3).value
                squadre[home_team] = Squadra(home_team)
                squadre[away_team] = Squadra(away_team)
                n += 1
        except IndexError:
            print("Il campionato in questione non supporta il nostro algoritmo.")
        n = 0
        for row_idx in range(1, nrows):
            home_team = x_sheet._cell(row_idx, 2)
            away_team = x_sheet._cell(row_idx, 3)
            partita = Partita(x_sheet._cell(row_idx, 1), home_team, away_team, x_sheet._cell(row_idx, 4),
                              x_sheet._cell(row_idx, 5), x_sheet._cell(row_idx, 6), x_sheet._cell(row_idx, 7), x_sheet._cell(row_idx, 8),
                              x_sheet._cell(row_idx, 9))
            sht = squadre[home_team]
            sat = squadre[away_team]
            sht + 1
            sat + 1
            if sht.partite == n +1:
                n += 1





        campionato = Campionato(campionatoe, squadre)
        campionati[campionatoe] = campionato
    return campionati


def oncschange(index, value, op):
    for squadraR in squadreT.get_children():
        squadreT.delete(squadraR)
    squadreT.heading("#0", text='Squadre', anchor='w')
    squadreT.column("#0", anchor="w")
    squadred = campionati[comboC.get()].squadre()
    for squadra in squadred:
        squadreT.insert("", 0, text=squadra)
    squadreT.pack()
    comboC.get()

root = Tk()

root.title("Campionati")
root.resizable(0, 0)
c1 = ttk.Label(root, justify=tk.CENTER, text="Seleziona il campionato:").pack(side="top")
csv = StringVar()
oc = ["E0", "SC0", "D1", "SP1", "I1", "F1", "N1", "B1", "P1", "T1", "G1"]
comboC = ttk.Combobox(root, textvariable=csv, values=oc)
csv.trace("w", oncschange)
comboC.pack()
ac = ttk.Notebook(root)
squadre = ttk.Frame(ac)
f2 = ttk.Frame(ac)
ac.add(squadre, text='Squadre')
ac.add(f2, text='Two')
ac.pack()
squadreT = ttk.Treeview(root, height=33)
campionati = dispatcher("all-euro-data-2016-2017.xls", oc)


# codice per interfaccia grafica a schermo intero, premere ESC per uscire
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()
