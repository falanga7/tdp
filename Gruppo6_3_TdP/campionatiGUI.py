import tkinter as tk
from tkinter import *
from tkinter import ttk
from Gruppo6_3_TdP import xlrd
from Gruppo6_3_TdP.xlrd.sheet import ctype_text
from math import sqrt
from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap
from Gruppo6_3_TdP.TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from Gruppo6_3_TdP.campionato import Campionato
from Gruppo6_3_TdP.partita import Partita


def dispatcher_partite(file, campionato):
    x_workbook = xlrd.open_workbook(file)
    x_sheet = x_workbook.sheet_by_name(campionato)
    nrows = x_sheet.nrows
    partite = ProbeHashMap(cap=int(nrows/0.5 + 1))
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
        campionato = Campionato(campionatoe, cl[campionatoe], squadre)
        campionati[campionatoe] = campionato
    return campionati


def oncschange(index, value, op):
    for squadraR in squadreT.get_children():
        squadreT.delete(squadraR)
    squadreT.heading("#0").clear()
    squadreT.heading("#0", text=campionati[ocn[comboC.get()]].nome())
    squadreT.column("#0")
    squadred = campionati[ocn[comboC.get()]].squadre()
    for squadra in squadred:
        squadreT.insert("", 0, text=squadra)

root = Tk()

root.title("Campionati")
root.resizable(0, 0)
root.grid_columnconfigure(0, weight=1)
c1 = ttk.Label(root, text="Seleziona il campionato:").grid(row=0, column=0)
root.grid_columnconfigure(1, weight=1)
gl = ttk.Label(root, text="Seleziona o inserisci la giornata:").grid(row=0, column=1)
root.grid_columnconfigure(2, weight=1)
s1 = ttk.Label(root, text="Seleziona o inserisci la squadra:").grid(row=0, column=2)
root.grid_columnconfigure(3, weight=1)
d1 = ttk.Label(root, text="Seleziona o inserisci la data").grid(row=0, column=3)
root.grid_columnconfigure(4, weight=1)
ke = ttk.Label(root, text="Inserisci un numero k:").grid(row=0, column=4)
root.grid_columnconfigure(5, weight=1)
root.grid_rowconfigure(3, weight=1)
bps = ttk.Button(root, text="Squadre", command=None)
bps.grid(row=3, column=5)
root.grid_rowconfigure(4, weight=1)
bpht = ttk.Button(root, text="Classifica primo tempo \nalla giornata indicata", command=None)
bpht.grid(row=4, column=5)
root.grid_rowconfigure(5, weight=1)
bpft = ttk.Button(root, text="Classifica alla giornata indicata", command=None)
bpft.grid(row=5, column=5)
root.grid_rowconfigure(6, weight=1)
bpfr = ttk.Button(root, text="Ultimi 5 risultati per la squadra indicata", command=None)
bpfr.grid(row=6, column=5)
root.grid_rowconfigure(7, weight=1)
bppdi = ttk.Button(root, text="Partite alla data indicata", command=None)
bppdi.grid(row=7, column=5)
root.grid_rowconfigure(8, weight=1)
bpksp = ttk.Button(root, text="k squadre che hanno segnato \npiù goal alla giornata indicata", command=None)
bpksp.grid(row=8, column=5)
root.grid_rowconfigure(9, weight=1)
bpksp = ttk.Button(root, text="k squadre che hanno subito \npiù goal alla giornata indicata", command=None)
bpksp.grid(row=9, column=5)
root.grid_rowconfigure(10, weight=1)
bpksp = ttk.Button(root, text="k squadre con migliore differenza reti \nalla giornata indicata", command=None)
bpksp.grid(row=10, column=5)
root.grid_rowconfigure(11, weight=1)
bpksp = ttk.Button(root, text="Squadre rispettivamente con maggior \nnumero di vittorie, in casa e in trasferta", command=None)
bpksp.grid(row=11, column=5)

bps = ttk.Button(root, text="vittorie, vittorie in casa, vittorie in trasferta", command=None)
ocn = {'Inghilterra': "E0", "Scozia": "SC0", "Germania": 'D1', "Spagna": "SP1",
      'Italia': 'I1', "Francia": 'F1', "Olanda": 'N1', "Belgio": 'B1', "Portogallo": 'P1',
      "Turchia": 'T1', "Grecia": 'G1'}
ocl = {"E0": 'Premier League', "SC0": 'Scottish Premiership', "D1": 'Bundesliga', "SP1": 'Liga Spagnola',
      'I1': 'Serie A', "F1": 'Ligue 1', "N1": 'Eredivise', "B1": 'Pro League', "P1": 'Primeira Liga',
      "T1": 'Super Lig', "G1": 'Souper Ligka Ellada'}
csv = StringVar()
comboC = ttk.Combobox(root, textvariable=csv, values=list(ocn))
csv.trace("w", oncschange)
comboC.grid(row=2, column=0)
gsv = StringVar()
comboG = ttk.Combobox(root, textvariable=gsv, value=None)
comboG.grid(row=2, column=1)
ssv = StringVar()
comboS = ttk.Combobox(root, textvariable=ssv, value=None)
comboS.grid(row=2, column=2)
dsv = StringVar()
comboD = ttk.Combobox(root, textvariable=dsv, value=None)
comboD.grid(row=2, column=3)
k = Entry()
k.grid(row=2, column=4)
squadreT = ttk.Treeview(root, selectmode="extended", height=33)
squadreT.grid(row=1, column=1, columnspan=4, rowspan=10)
campionati = dispatcher("all-euro-data-2016-2017.xls", ocl)
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
