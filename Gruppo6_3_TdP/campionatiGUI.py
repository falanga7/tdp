import tkinter as tk
from tkinter import *
from tkinter import ttk
from Gruppo6_3_TdP import xlrd
from Gruppo6_3_TdP.xlrd.sheet import ctype_text
from math import sqrt
from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap
from Gruppo6_3_TdP.TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from Gruppo6_3_TdP.campionato import Campionato
from Gruppo6_3_TdP.partita  import Partita

def dispatcher_partite(file, campionato):
    x_workbook = xlrd.open_workbook(file)
    x_sheet = x_workbook.sheet_by_name(campionato)
    nrows = x_sheet.nrows
    partite = ProbeHashMap(cap=int(nrows/ 0.5 + 1))
    n = 1
    try:
        while not n == nrows:
            date = xlrd.xldate_as_tuple(x_sheet.cell(n, 1).value, x_workbook.datemode)
            home_team = x_sheet.cell(n, 2).value
            away_team = x_sheet.cell(n, 3).value
            FTHG = int(x_sheet.cell(n, 4).value)
            if x_sheet.cell(n, 5).value != '':
                FTAG = int(x_sheet.cell(n, 5).value)
            if x_sheet.cell(n, 6).value != '':
                FTR = x_sheet.cell(n, 6).value
            if x_sheet.cell(n,7).value != '':
                HTHG = int(x_sheet.cell(n, 7).value)
            if x_sheet.cell(n, 8).value != '':
                HTAG = int(x_sheet.cell(n, 8).value)
            if x_sheet.cell(n, 9).value != '':
                HTR = x_sheet.cell(n, 9).value
            partita = Partita(date, home_team, away_team, FTHG, FTAG, FTR, HTHG, HTAG, HTR)
            partite[date] = partita
            n += 1
    except IndexError:
        print(n)
    return partite

def dispatcher(file, cl):
    x_workbook = xlrd.open_workbook(file)
    campionati = ProbeHashMap(cap=int(len(cl)/0.5 + 1))
    for campionatoe in cl.keys():
        x_sheet = x_workbook.sheet_by_name(campionatoe)
        nrows = x_sheet.nrows
        ns = int((1 + sqrt(1 + 4 * (nrows - 1))) / 2)
        ng = (ns - 1) * 2
        squadre = ChainHashMap(cap=int(ns / 0.9 + 1))
        n = 1
        try:
            while not squadre._n == ns or not n == x_sheet.nrows:
                home_team = x_sheet.cell(n, 2).value
                away_team = x_sheet.cell(n, 3).value
                squadre[home_team] = home_team
                squadre[away_team] = away_team
                n += 1
        except IndexError:
            print(n)
        campionato = Campionato(campionatoe,cl[campionatoe], squadre)
        campionati[campionatoe] = campionato
    return campionati


def oncschange(index, value, op):
    for squadraR in squadreT.get_children():
        squadreT.delete(squadraR)
    squadreT.heading("#0").clear()
    squadreT.heading("#0", text=campionati[comboC.get()].nome(), anchor='w')
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
oc = {"E0":'Premier League', "SC0":'Scottish Premiership', "D1":'Bundesliga', "SP1":'Liga Spagnola', 'I1':'Serie A', "F1":'Ligue 1', "N1":'Eredivise', "B1":'Pro League', "P1":'Primeira Liga', "T1":'Super Lig', "G1":'Souper Ligka Ellada'}
comboC = ttk.Combobox(root, textvariable=csv, values=list(oc.keys()))
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
partite = {}
for key in campionati.keys():
    partite[key] = dispatcher_partite("all-euro-data-2016-2017.xls", key)

# codice per interfaccia grafica a schermo intero, premere ESC per uscire
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()
