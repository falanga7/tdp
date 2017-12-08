from tkinter import *
from tkinter import ttk
from Gruppo6_3_TdP import xlrd
from math import sqrt
from Gruppo6_3_TdP.TdP_collections.hash_table.chain_hash_map import ChainHashMap
from Gruppo6_3_TdP.TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from Gruppo6_3_TdP.campionato import Campionato
from Gruppo6_3_TdP.partita import Partita
from Gruppo6_3_TdP.giornata import Giornata
from Gruppo6_3_TdP.classifica import Classifica
from Gruppo6_3_TdP.record_classifica import RecordClassifica
from Gruppo6_3_TdP.squadra import Squadra


def dispatcher(cl, file):
    x_workbook = xlrd.open_workbook(file)
    campionati = ProbeHashMap(cap=int(len(cl)/0.5 + 1))
    for codice_campionato in cl.keys():
        if codice_campionato != 'SC0' and codice_campionato != 'P1' and codice_campionato != 'G1':
            x_sheet = x_workbook.sheet_by_name(codice_campionato)
            nrows = x_sheet.nrows
            partite = ChainHashMap(cap=int(nrows / 0.9 + 1))
            ns = int((1 + sqrt(1 + 4 * (nrows - 1))) / 2)
            ng = (ns - 1) * 2
            squadre = ChainHashMap(cap=int(ns / 0.9 + 1))
            n = 1
            g = 0
            try:
                while not squadre._n == ns or not n == x_sheet.nrows:
                    home_team = x_sheet.cell(n, 2).value
                    away_team = x_sheet.cell(n, 3).value
                    squadre[home_team] = Squadra(home_team)
                    squadre[away_team] = Squadra(away_team)
                    n += 1
            except IndexError:
                print("Il campionato considerato non supporta il nostro algoritmo.")

            campionato = Campionato(codice_campionato, cl[codice_campionato], squadre)
            # creo le giornate del campionato: una lista di liste di date. Per convenzione la lista all'indice 0 indica
            # la giornata numero 1, 1 la giornata 2 etc.
            giornate_campionato = [Giornata] * ng
            #inizializzazione classifica per la prima giornata
            lista_squadre = list(squadre)
            giornate_campionato[g] = Giornata(Classifica(lista_squadre),list())
            # ricomincio a leggere il foglio di calcolo dalla prima riga
            n = 1
            lista_partite = list()
            prev_date = None
            date = None
            rinviata = False
            aggiungi_al_calendario = True
            while not n == nrows:
                prev_data = date
                date = xlrd.xldate_as_datetime(x_sheet.cell(n, 1).value, x_workbook.datemode)
                date = str(format(date.date(), "%d/%m/%Y"))
                home_team = x_sheet.cell(n, 2).value
                away_team = x_sheet.cell(n, 3).value
                FTHG = int(x_sheet.cell(n, 4).value)
                FTAG = int(x_sheet.cell(n, 5).value)

                FTR = x_sheet.cell(n, 6).value
                #calcolo punti,vittorie,pareggi e sconfitte
                punti_squadra_casa = 0
                punti_squadra_ospite = 0
                vittoria_squadra_casa = 0
                vittoria_squadra_ospite = 0
                pareggio_squadra_casa = 0
                pareggio_squadra_ospite = 0
                sconfitta_squadra_casa = 0
                sconfitta_squadra_ospite = 0

                if FTR == "H":
                    punti_squadra_casa = 3
                    vittoria_squadra_casa = 1
                    sconfitta_squadra_ospite = 1
                elif FTR == "D":
                    punti_squadra_casa = 1
                    punti_squadra_ospite = 1
                    pareggio_squadra_casa = 1
                    pareggio_squadra_ospite = 1
                elif FTR == "A":
                    punti_squadra_ospite = 3
                    vittoria_squadra_ospite = 1
                    sconfitta_squadra_casa = 1

                # verifico la presenza dei dati nelle celle successive
                # ( se la partita è vinta a tavolino le celle risultano essere vuote)
                if x_sheet.cell(n, 7).value != '':
                    HTHG = int(x_sheet.cell(n, 7).value)
                if x_sheet.cell(n, 8).value != '':
                    HTAG = int(x_sheet.cell(n, 8).value)
                if x_sheet.cell(n, 9).value != '':
                    HTR = x_sheet.cell(n, 9).value

                # calcolo punti,vittorie,pareggi e sconfitte
                punti_squadra_casa_ht = 0
                punti_squadra_ospite_ht = 0
                vittoria_squadra_casa_ht = 0
                vittoria_squadra_ospite_ht = 0
                pareggio_squadra_casa_ht = 0
                pareggio_squadra_ospite_ht = 0
                sconfitta_squadra_casa_ht= 0
                sconfitta_squadra_ospite_ht = 0

                if HTR == "H":
                    punti_squadra_casa_ht = 3
                    vittoria_squadra_casa_ht = 1
                    sconfitta_squadra_ospite_ht = 1
                elif HTR == "D":
                    punti_squadra_casa_ht = 1
                    punti_squadra_ospite_ht = 1
                    pareggio_squadra_casa_ht = 1
                    pareggio_squadra_ospite_ht = 1
                elif HTR == "A":
                    punti_squadra_ospite_ht = 3
                    vittoria_squadra_ospite_ht = 1
                    sconfitta_squadra_casa_ht = 1

                partita = Partita(date, home_team, away_team, FTHG, FTAG, FTR, HTHG, HTAG, HTR)

                record_home = squadre[home_team].record()

                record_ospite = squadre[away_team].record()

                andata = None

                """for row_num in range(int(x_sheet.nrows / 2)):
                    row_value = x_sheet.row_values(row_num)
                    if row_value[2] == away_team and row_value[3] == home_team:
                        print("Amdata", home_team, away_team)
                        date_search = xlrd.xldate_as_datetime(x_sheet.cell(row_num, 1).value, x_workbook.datemode)
                        date_search = str(format(date_search.date(), "%d/%m/%Y"))
                        if date_search in partite.keys():
                            print("Andata0KKK")
                            partite_andata = partite[date_search]
                            for partita in partite_andata:
                                if partita.awayteam() == home_team and partita.hometeam() == away_team:
                                    for giornata in giornate_campionato:
                                        if partita.date() in giornata.date_partite():
                                            andata = giornata.date_partite().index(partita.date())
                                            print("andata", andata, home_team, away_team)
                                            break
                            break"""


                if record_home.partite() > g or record_ospite.partite() > g:

                    if not rinviata:
                        giornate_campionato[g+1] = Giornata(Classifica(giornate_campionato[g].classifica()._lista.copy()),list())

                        g += 1

                    else:
                        rinviata = False


                record_home += RecordClassifica(squadra = home_team, partite = 1, vittorie = vittoria_squadra_casa, pareggi = pareggio_squadra_casa,
                                                sconfitte = sconfitta_squadra_casa, goalfatti = FTHG, goalsubiti = FTAG, punti = punti_squadra_casa,
                                                vittorie_ht=vittoria_squadra_casa_ht, pareggi_ht=pareggio_squadra_casa_ht, sconfitte_ht=sconfitta_squadra_casa_ht,
                                                goalfatti_ht=HTHG, goalsubiti_ht=HTAG, punti_ht=punti_squadra_casa_ht,partite_casa=1,
                                                vittorie_casa=vittoria_squadra_casa, pareggi_casa=pareggio_squadra_casa, sconfitte_casa=sconfitta_squadra_casa,
                                                goalfatti_casa=FTHG, goalsubiti_casa=FTAG, punti_casa=punti_squadra_casa)

                record_ospite += RecordClassifica(squadra=away_team, partite=1, vittorie=vittoria_squadra_ospite,
                                                pareggi=pareggio_squadra_ospite,sconfitte=sconfitta_squadra_ospite, goalfatti=FTAG, goalsubiti=FTHG,
                                                punti=punti_squadra_ospite,vittorie_ht=vittoria_squadra_ospite_ht, pareggi_ht=pareggio_squadra_ospite_ht,
                                                sconfitte_ht=sconfitta_squadra_ospite_ht,goalfatti_ht=HTAG, goalsubiti_ht=HTHG, punti_ht=punti_squadra_ospite_ht,
                                                partite_trasferta=1, vittorie_trasferta=vittoria_squadra_ospite,pareggi_trasferta=pareggio_squadra_ospite,
                                                sconfitte_trasferta=sconfitta_squadra_ospite, goalfatti_trasferta=FTAG,goalsubiti_trasferta=FTAG,
                                                punti_trasferta=punti_squadra_ospite)

                """if andata is not None and (g+1) - andata < ng/2:
                    giornate_campionato[g + 1] = Giornata(Classifica(giornate_campionato[g].classifica()._lista.copy()),
                                                          list())
                    g += 1
                    giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                    giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())
                else:
                    giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                    giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())"""
                giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())

                #            record_home = RecordClassifica(home_team, g + 1, )
                if date != prev_data:
                    if aggiungi_al_calendario:
                        giornate_campionato[g].aggiungi_data(date)

                    else:
                        aggiungi_al_calendario = True
                    lista_partite = list()

                lista_partite.append(partita)
                partite[date] = lista_partite
                n += 1
            campionato.set_partite(partite)
            campionato.set_giornate(giornate_campionato)
            campionati[codice_campionato] = campionato

        elif codice_campionato == 'SC0':
            x_sheet = x_workbook.sheet_by_name(codice_campionato)
            nrows = x_sheet.nrows
            nrows_utili = nrows - 30
            partite = ChainHashMap(cap=int(nrows / 0.9 + 1))
            ns = 12
            ng = (ns - 1) * 3
            squadre = ChainHashMap(cap=int(ns / 0.9 + 1))
            n = 1
            g = 0
            try:
                while not squadre._n == ns or not n == x_sheet.nrows:
                    home_team = x_sheet.cell(n, 2).value
                    away_team = x_sheet.cell(n, 3).value
                    squadre[home_team] = Squadra(home_team)
                    squadre[away_team] = Squadra(away_team)
                    n += 1
            except IndexError:
                print("Il campionato considerato non supporta il nostro algoritmo.")

            campionato = Campionato(codice_campionato, cl[codice_campionato], squadre)
            # creo le giornate del campionato: una lista di liste di date. Per convenzione la lista all'indice 0 indica
            # la giornata numero 1, 1 la giornata 2 etc.
            giornate_campionato = [Giornata] * ng
            # inizializzazione classifica per la prima giornata
            lista_squadre = list(squadre)
            giornate_campionato[g] = Giornata(Classifica(lista_squadre), list())
            # ricomincio a leggere il foglio di calcolo dalla prima riga
            n = 1
            lista_partite = list()
            prev_date = None
            date = None
            rinviata = False
            aggiungi_al_calendario = True
            while not n == nrows_utili:
                prev_data = date
                date = xlrd.xldate_as_datetime(x_sheet.cell(n, 1).value, x_workbook.datemode)
                date = str(format(date.date(), "%d/%m/%Y"))
                home_team = x_sheet.cell(n, 2).value
                away_team = x_sheet.cell(n, 3).value
                FTHG = int(x_sheet.cell(n, 4).value)
                FTAG = int(x_sheet.cell(n, 5).value)

                FTR = x_sheet.cell(n, 6).value
                # calcolo punti,vittorie,pareggi e sconfitte
                punti_squadra_casa = 0
                punti_squadra_ospite = 0
                vittoria_squadra_casa = 0
                vittoria_squadra_ospite = 0
                pareggio_squadra_casa = 0
                pareggio_squadra_ospite = 0
                sconfitta_squadra_casa = 0
                sconfitta_squadra_ospite = 0

                if FTR == "H":
                    punti_squadra_casa = 3
                    vittoria_squadra_casa = 1
                    sconfitta_squadra_ospite = 1
                elif FTR == "D":
                    punti_squadra_casa = 1
                    punti_squadra_ospite = 1
                    pareggio_squadra_casa = 1
                    pareggio_squadra_ospite = 1
                elif FTR == "A":
                    punti_squadra_ospite = 3
                    vittoria_squadra_ospite = 1
                    sconfitta_squadra_casa = 1

                # verifico la presenza dei dati nelle celle successive
                # ( se la partita è vinta a tavolino le celle risultano essere vuote)
                if x_sheet.cell(n, 7).value != '':
                    HTHG = int(x_sheet.cell(n, 7).value)
                if x_sheet.cell(n, 8).value != '':
                    HTAG = int(x_sheet.cell(n, 8).value)
                if x_sheet.cell(n, 9).value != '':
                    HTR = x_sheet.cell(n, 9).value

                # calcolo punti,vittorie,pareggi e sconfitte
                punti_squadra_casa_ht = 0
                punti_squadra_ospite_ht = 0
                vittoria_squadra_casa_ht = 0
                vittoria_squadra_ospite_ht = 0
                pareggio_squadra_casa_ht = 0
                pareggio_squadra_ospite_ht = 0
                sconfitta_squadra_casa_ht = 0
                sconfitta_squadra_ospite_ht = 0

                if HTR == "H":
                    punti_squadra_casa_ht = 3
                    vittoria_squadra_casa_ht = 1
                    sconfitta_squadra_ospite_ht = 1
                elif HTR == "D":
                    punti_squadra_casa_ht = 1
                    punti_squadra_ospite_ht = 1
                    pareggio_squadra_casa_ht = 1
                    pareggio_squadra_ospite_ht = 1
                elif HTR == "A":
                    punti_squadra_ospite_ht = 3
                    vittoria_squadra_ospite_ht = 1
                    sconfitta_squadra_casa_ht = 1

                partita = Partita(date, home_team, away_team, FTHG, FTAG, FTR, HTHG, HTAG, HTR)

                record_home = squadre[home_team].record()

                record_ospite = squadre[away_team].record()

                andata = None

                """for row_num in range(int(x_sheet.nrows / 2)):
                    row_value = x_sheet.row_values(row_num)
                    if row_value[2] == away_team and row_value[3] == home_team:
                        print("Amdata", home_team, away_team)
                        date_search = xlrd.xldate_as_datetime(x_sheet.cell(row_num, 1).value, x_workbook.datemode)
                        date_search = str(format(date_search.date(), "%d/%m/%Y"))
                        if date_search in partite.keys():
                            print("Andata0KKK")
                            partite_andata = partite[date_search]
                            for partita in partite_andata:
                                if partita.awayteam() == home_team and partita.hometeam() == away_team:
                                    for giornata in giornate_campionato:
                                        if partita.date() in giornata.date_partite():
                                            andata = giornata.date_partite().index(partita.date())
                                            print("andata", andata, home_team, away_team)
                                            break
                            break"""

                if record_home.partite() > g or record_ospite.partite() > g:

                    if not rinviata:
                        giornate_campionato[g + 1] = Giornata(
                            Classifica(giornate_campionato[g].classifica()._lista.copy()), list())

                        g += 1

                    else:
                        rinviata = False

                record_home += RecordClassifica(squadra=home_team, partite=1, vittorie=vittoria_squadra_casa,
                                                pareggi=pareggio_squadra_casa,
                                                sconfitte=sconfitta_squadra_casa, goalfatti=FTHG, goalsubiti=FTAG,
                                                punti=punti_squadra_casa,
                                                vittorie_ht=vittoria_squadra_casa_ht,
                                                pareggi_ht=pareggio_squadra_casa_ht,
                                                sconfitte_ht=sconfitta_squadra_casa_ht,
                                                goalfatti_ht=HTHG, goalsubiti_ht=HTAG, punti_ht=punti_squadra_casa_ht,
                                                partite_casa=1,
                                                vittorie_casa=vittoria_squadra_casa,
                                                pareggi_casa=pareggio_squadra_casa,
                                                sconfitte_casa=sconfitta_squadra_casa,
                                                goalfatti_casa=FTHG, goalsubiti_casa=FTAG,
                                                punti_casa=punti_squadra_casa)

                record_ospite += RecordClassifica(squadra=away_team, partite=1, vittorie=vittoria_squadra_ospite,
                                                  pareggi=pareggio_squadra_ospite, sconfitte=sconfitta_squadra_ospite,
                                                  goalfatti=FTAG, goalsubiti=FTHG,
                                                  punti=punti_squadra_ospite, vittorie_ht=vittoria_squadra_ospite_ht,
                                                  pareggi_ht=pareggio_squadra_ospite_ht,
                                                  sconfitte_ht=sconfitta_squadra_ospite_ht, goalfatti_ht=HTAG,
                                                  goalsubiti_ht=HTHG, punti_ht=punti_squadra_ospite_ht,
                                                  partite_trasferta=1, vittorie_trasferta=vittoria_squadra_ospite,
                                                  pareggi_trasferta=pareggio_squadra_ospite,
                                                  sconfitte_trasferta=sconfitta_squadra_ospite,
                                                  goalfatti_trasferta=FTAG, goalsubiti_trasferta=FTAG,
                                                  punti_trasferta=punti_squadra_ospite)

                """if andata is not None and (g+1) - andata < ng/2:
                    giornate_campionato[g + 1] = Giornata(Classifica(giornate_campionato[g].classifica()._lista.copy()),
                                                          list())
                    g += 1
                    giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                    giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())
                else:
                    giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                    giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())"""
                giornate_campionato[g].classifica().aggiungi_record(record_home.copy())
                giornate_campionato[g].classifica().aggiungi_record(record_ospite.copy())

                #            record_home = RecordClassifica(home_team, g + 1, )
                if date != prev_data:
                    if aggiungi_al_calendario:
                        giornate_campionato[g].aggiungi_data(date)

                    else:
                        aggiungi_al_calendario = True
                    lista_partite = list()

                lista_partite.append(partita)
                partite[date] = lista_partite
                n += 1
            campionato.set_partite(partite)
            campionato.set_giornate(giornate_campionato)
            campionati[codice_campionato] = campionato
        else:
            x_sheet = x_workbook.sheet_by_name(codice_campionato)
            nrows = x_sheet.nrows
            partite = ChainHashMap(cap=int(nrows / 0.9 + 1))
            ns = int((1 + sqrt(1 + 4 * (nrows - 1))) / 2)
            ng = (ns - 1) * 2
            squadre = ChainHashMap(cap=int(ns / 0.9 + 1))
            n = 1
            g = 0
            try:
                while not squadre._n == ns or not n == x_sheet.nrows:
                    home_team = x_sheet.cell(n, 2).value
                    away_team = x_sheet.cell(n, 3).value
                    squadre[home_team] = Squadra(home_team)
                    squadre[away_team] = Squadra(away_team)
                    n += 1
            except IndexError:
                print("Il campionato considerato non supporta il nostro algoritmo.")
            campionato = Campionato(codice_campionato, cl[codice_campionato], squadre)

            campionati[codice_campionato] = campionato
    return campionati


def onsb_click():
    squadre_t = tree_view
    empty_tree_view(squadre_t)
    squadre_t.heading("#0").clear()
    squadre_t.heading("#0", text=campionati[ocn[comboC.get()]].nome())
    squadre_t.column("#0")
    squadred = campionati[ocn[comboC.get()]].squadre()
    for squadra in squadred:
        squadre_t.insert("", 0, text=squadra)


def onp_click():
    lista_partite = tree_view
    empty_tree_view(tree_view)
    lista_partite["columns"] = ("one", "two","three","four","five")
    lista_partite.column("#0", minwidth=0, width=100, stretch=NO)
    lista_partite.column("one", minwidth=0, width=100, stretch=NO)
    lista_partite.column("two", minwidth=0, width=100, stretch=NO)
    lista_partite.column("three", minwidth=0, width=100, stretch=NO)
    lista_partite.column("four", minwidth=0, width=100, stretch=NO)
    lista_partite.column("five", minwidth=0, width=100, stretch=NO)
    lista_partite.heading("#0", text="Campionato")
    lista_partite.heading("one", text="Squadra casa")
    lista_partite.heading("two", text="Squadra ospite")
    lista_partite.heading("three", text="FTHG")
    lista_partite.heading("four", text="FTAG")
    lista_partite.heading("five", text="FTR")

    data = comboD.get()
    for campionato in campionati.values():
        partite_campionato = campionato.partite()
        try:
            partite_giorno = partite_campionato[data]
            for partita in partite_giorno:
                lista_partite.insert("", 0, text=campionato.nome(),values=[partita.hometeam(),partita.awayteam(),partita.fthg(),partita.ftag(),partita.ftr()])
        except KeyError:
            print("Nel giorno non si sono giocate partite nel campionato",campionato.nome())


def onc_change(index, value, op):
    giornate = list(range(1, len(campionati[ocn[comboC.get()]].giornate())+1))
    comboG["values"] = giornate
    squadre = campionati[ocn[comboC.get()]].squadre()
    squadreL = []
    for squadra in squadre:
        squadreL.append(squadra)
    comboS["values"] = squadreL


def ong_change(index, value, op):
    date_partite = campionati[ocn[comboC.get()]].giornate()[int(comboG.get())-1].date_partite()
    comboD["values"] = date_partite


def empty_tree_view(tree):
    for i in tree.get_children():
        tree.delete(i)


def stampa_classifica():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get())-1].classifica()
    classifica.ordina(0, False)
    classifica = classifica.lista()
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    lista_partite.column("#0", minwidth=0, width=100, stretch=NO)
    lista_partite.column("one", minwidth=0, width=100, stretch=NO)
    lista_partite.column("two", minwidth=0, width=100, stretch=NO)
    lista_partite.column("three", minwidth=0, width=100, stretch=NO)
    lista_partite.column("four", minwidth=0, width=100, stretch=NO)
    lista_partite.column("five", minwidth=0, width=100, stretch=NO)
    lista_partite.column("six", minwidth=0, width=100, stretch=NO)
    lista_partite.column("seven", minwidth=0, width=100, stretch=NO)
    lista_partite.column("eight", minwidth=0, width=100, stretch=NO)
    lista_partite.column("nine", minwidth=0, width=100, stretch=NO)
    lista_partite.heading("#0", text="Posizione")
    lista_partite.heading("one", text="Squadra")
    lista_partite.heading("two", text="Punti")
    lista_partite.heading("three", text="Partite")
    lista_partite.heading("four", text="V")
    lista_partite.heading("five", text="P")
    lista_partite.heading("six", text="S")
    lista_partite.heading("seven", text="GF")
    lista_partite.heading("eight", text="GS")
    lista_partite.heading("nine", text="DR")
    i = len(campionati[ocn[comboC.get()]].squadre())

    for record_classifica in classifica:
        lista_partite.insert("", 0, text=i,
                             values=[record_classifica.squadra(), record_classifica.punti(),
                                     record_classifica.partite(), record_classifica.vittorie(), record_classifica.pareggi(),
                                     record_classifica.sconfitte(), record_classifica.goalfatti(),
                                     record_classifica.goalsubiti(), record_classifica.goalfatti()-record_classifica.goalsubiti()])
        i = i-1
    lista_partite.pack()


def stampa_classifica_ht():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get())-1].classifica()
    classifica.ordina(0, False)
    classifica = classifica.lista()
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    lista_partite.column("#0", minwidth=0, width=100, stretch=NO)
    lista_partite.column("one", minwidth=0, width=100, stretch=NO)
    lista_partite.column("two", minwidth=0, width=100, stretch=NO)
    lista_partite.column("three", minwidth=0, width=100, stretch=NO)
    lista_partite.column("four", minwidth=0, width=100, stretch=NO)
    lista_partite.column("five", minwidth=0, width=100, stretch=NO)
    lista_partite.column("six", minwidth=0, width=100, stretch=NO)
    lista_partite.column("seven", minwidth=0, width=100, stretch=NO)
    lista_partite.column("eight", minwidth=0, width=100, stretch=NO)
    lista_partite.column("nine", minwidth=0, width=100, stretch=NO)
    lista_partite.heading("#0", text="Posizione")
    lista_partite.heading("one", text="Squadra")
    lista_partite.heading("two", text="Punti")
    lista_partite.heading("three", text="Partite")
    lista_partite.heading("four", text="V")
    lista_partite.heading("five", text="P")
    lista_partite.heading("six", text="S")
    lista_partite.heading("seven", text="GF")
    lista_partite.heading("eight", text="GS")
    lista_partite.heading("nine", text="DS")
    i = len(campionati[ocn[comboC.get()]].squadre())

    for record_classifica in classifica:
        lista_partite.insert("", 0, text=i,
                             values=[record_classifica.squadra(), record_classifica.punti_ht(),
                                     record_classifica.partite(), record_classifica.vittorie_ht(), record_classifica.pareggi_ht(),
                                     record_classifica.sconfitte_ht(), record_classifica.goalfatti_ht(),
                                     record_classifica.goalsubiti_ht(), record_classifica.goalfatti_ht()-record_classifica.goalsubiti_ht()])
        i = i-1
    lista_partite.pack()


def ultimi_cinque_risultati():
    giornata = int(comboG.get())
    squadra = comboS.get()
    lista_record = tree_view
    empty_tree_view(lista_record)
    lista_record["columns"] = ("one", "two")
    lista_record.column("#0", minwidth=0, width=100, stretch=NO)
    lista_record.column("one", minwidth=0, width=100, stretch=NO)
    lista_record.column("two", minwidth=0, width=100, stretch=NO)
    lista_record.heading("#0", text="Giornata")
    lista_record.heading("one", text="Squadra")
    lista_record.heading("two", text="Risultato")
    partite_campionato = campionati[ocn[comboC.get()]].partite()
    g = 0
    while g != 5:
        partite_giornata = campionati[ocn[comboC.get()]].giornate()[giornata - 1 - g].date_partite()
        
        for data in partite_giornata:
            partite_giorno = partite_campionato[data]
            for partita in partite_giorno:
                if g == 5 or giornata-1-g < 0:
                    return
                if partita.hometeam() == squadra:
                    lista_record.insert("", 0, text=giornata - g,
                                        values=[squadra, partita.ftr()])
                    g += 1
                elif partita.awayteam() == squadra:
                    if partita.ftr() == "H":
                        lista_record.insert("", 0, text=giornata - g,
                                            values=[squadra, "A"])
                    elif partita.ftr() == "A":
                        lista_record.insert("", 0, text=giornata - g,
                                            values=[squadra, "H"])
                    else:
                        lista_record.insert("", 0, text=giornata - g,
                                            values=[squadra, partita.ftr()])

                    g += 1


def stampa_squadra_vittoriosa():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get()) - 1].classifica()
    classifica.ordina(1, True)
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two", "three", "four", "five")
    lista_partite.column("#0", minwidth=0, width=200, stretch=NO)
    lista_partite.column("one", minwidth=0, width=200, stretch=NO)
    lista_partite.column("two", minwidth=0, width=200, stretch=NO)
    lista_partite.column("three", minwidth=0, width=200, stretch=NO)
    lista_partite.column("four", minwidth=0, width=200, stretch=NO)
    lista_partite.column("five", minwidth=0, width=200, stretch=NO)
    lista_partite.heading("#0", text="Top vittorie")
    lista_partite.heading("one", text="Vittorie")
    lista_partite.heading("two", text="Top vittorie in casa")
    lista_partite.heading("three", text="Vittorie in casa")
    lista_partite.heading("four", text="Top vittorie in trasferta")
    lista_partite.heading("five", text="Vittorie in trasferta")
    vittoriose = classifica.lista()
    vittoriose_lista = []
    vittoriose_lista.append(vittoriose[0])
    k = 1
    while True:
        if vittoriose[0].vittorie() == vittoriose[k].vittorie():
            vittoriose_lista.append(vittoriose[k])
            k += 1
        else:
            break

    classifica.ordina(2, True)
    vittoriose_in_casa = classifica.lista()
    vittoriose_in_casa_lista = []
    vittoriose_in_casa_lista.append(vittoriose_in_casa[0])
    k = 1
    while True:
        if vittoriose_in_casa[0].vittorie_casa() == vittoriose_in_casa[k].vittorie_casa():
            vittoriose_in_casa_lista.append(vittoriose_in_casa[k])
            k += 1
        else:
            break
    classifica.ordina(3, True)
    vittoriose_in_trasferta = classifica.lista()
    vittoriose_in_trasferta_lista = []
    vittoriose_in_trasferta_lista.append(vittoriose_in_trasferta[0])
    k = 1
    while True:
        if vittoriose_in_trasferta[0].vittorie_trasferta() == vittoriose_in_trasferta[k].vittorie_trasferta():
            vittoriose_in_trasferta_lista.append(vittoriose_in_trasferta[k])
            k += 1
        else:
            break
    km = max(len(vittoriose_lista), len(vittoriose_in_casa_lista), len(vittoriose_in_trasferta_lista))
    for k in range(0, km):

        try:
            vittoriose_record = vittoriose_lista[k]
        except IndexError:
            vittoriose_record = ""
        try:
            vittoriose_in_casa_record = vittoriose_in_casa_lista[k]
        except IndexError:
            vittoriose_in_casa_record = ""
        try:
            vittoriose_in_trasferta_record = vittoriose_in_trasferta_lista[k]
        except IndexError:
            vittoriose_in_trasferta_record = ""
        lista_partite.insert("", 0, text=vittoriose_record.squadra() if type(vittoriose_record) is RecordClassifica else "",
                             values=[vittoriose_record.vittorie() if type(vittoriose_record) is RecordClassifica else "",
                                     vittoriose_in_casa_record.squadra() if type(vittoriose_in_casa_record) is RecordClassifica else "",
                                     vittoriose_in_casa_record.vittorie_casa() if type(vittoriose_in_casa_record) is RecordClassifica else "",
                                     vittoriose_in_trasferta_record.squadra() if type(vittoriose_in_trasferta_record) is RecordClassifica else "",
                                     vittoriose_in_trasferta_record.vittorie_trasferta() if type(vittoriose_in_trasferta_record) is RecordClassifica else ""])
    lista_partite.pack()


def stampa_kspg():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get()) - 1].classifica()
    classifica.ordina(4, True)
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two")
    lista_partite.column("#0", minwidth=0, width=200, stretch=NO)
    lista_partite.column("one", minwidth=0, width=200, stretch=NO)
    lista_partite.heading("#0", text="Top più goal")
    lista_partite.heading("one", text="Goal fatti")
    ks = int(k.get())
    squadre = classifica.lista()[0:ks]
    squadre.reverse()
    for record in squadre:
        lista_partite.insert("", 0, text=record.squadra(),
                             values=[record.goalfatti()])
    lista_partite.pack()


def stampa_ksmg():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get()) - 1].classifica()
    classifica.ordina(5, False)
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two")
    lista_partite.column("#0", minwidth=0, width=200, stretch=NO)
    lista_partite.column("one", minwidth=0, width=200, stretch=NO)
    lista_partite.heading("#0", text="Top meno goal subiti")
    lista_partite.heading("one", text="Goal subiti")
    ks = int(k.get())
    squadre = classifica.lista()[0:ks]
    squadre.reverse()
    for record in squadre:
        lista_partite.insert("", 0, text=record.squadra(),
                             values=[record.goalsubiti()])
    lista_partite.pack()


def stampa_ksmdr():
    classifica = campionati[ocn[comboC.get()]].giornate()[int(comboG.get()) - 1].classifica()
    classifica.ordina(6, True)
    lista_partite = tree_view
    empty_tree_view(lista_partite)
    lista_partite["columns"] = ("one", "two")
    lista_partite.column("#0", minwidth=0, width=200, stretch=NO)
    lista_partite.column("one", minwidth=0, width=200, stretch=NO)
    lista_partite.heading("#0", text="Top migliore differenza reti")
    lista_partite.heading("one", text="Differenza reti")
    ks = int(k.get())
    squadre = classifica.lista()[0:ks]
    squadre.reverse()
    for record in squadre.reverse():
        lista_partite.insert("", 0, text=record.squadra(),
                             values=[record.goalfatti() - record.goalsubiti()])
    lista_partite.pack()


# creazione della GUI
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
bps = ttk.Button(root, text="Squadre", command=onsb_click)
bps.grid(row=3, column=5)
root.grid_rowconfigure(4, weight=1)
bpht = ttk.Button(root, text="Classifica primo tempo \nalla giornata indicata", command=stampa_classifica_ht)
bpht.grid(row=4, column=5)
root.grid_rowconfigure(5, weight=1)
bpft = ttk.Button(root, text="Classifica alla giornata indicata", command=stampa_classifica)
bpft.grid(row=5, column=5)
root.grid_rowconfigure(6, weight=1)
bpfr = ttk.Button(root, text="Ultimi 5 risultati per la squadra indicata", command=ultimi_cinque_risultati)
bpfr.grid(row=6, column=5)
root.grid_rowconfigure(7, weight=1)
bppdi = ttk.Button(root, text="Partite alla data indicata", command=onp_click)
bppdi.grid(row=7, column=5)
root.grid_rowconfigure(8, weight=1)
bpksp = ttk.Button(root, text="k squadre che hanno segnato \npiù goal alla giornata indicata", command=stampa_kspg)
bpksp.grid(row=8, column=5)
root.grid_rowconfigure(9, weight=1)
bpksp = ttk.Button(root, text="k squadre che hanno subito \npiù goal alla giornata indicata", command=stampa_ksmg)
bpksp.grid(row=9, column=5)
root.grid_rowconfigure(10, weight=1)
bpksp = ttk.Button(root, text="k squadre con migliore differenza reti \nalla giornata indicata", command=stampa_ksmdr)
bpksp.grid(row=10, column=5)
root.grid_rowconfigure(11, weight=1)
bpksp = ttk.Button(root, text="Squadre rispettivamente con maggior \nnumero di vittorie, in casa e in trasferta",
                   command=stampa_squadra_vittoriosa)
bpksp.grid(row=11, column=5)
main_frame = ttk.Frame(root, width=1300, height=700, relief="groove")
main_frame.pack_propagate(0)
main_frame.grid(row=2, column=1, columnspan=4, rowspan=10)
tree_scroll_v = ttk.Scrollbar(main_frame, orient="vertical")
tree_scroll_v.pack(side='right', fill='y')
tree_scroll_o = ttk.Scrollbar(main_frame, orient="horizontal")
tree_view = ttk.Treeview(main_frame, selectmode="browse", height=33, xscrollcommand=tree_scroll_o,
                             yscrollcommand=tree_scroll_v)
tree_scroll_o.configure(command=tree_view.xview)
tree_scroll_v.configure(command=tree_view.yview)
tree_scroll_v.pack(side='right', fill='y')
tree_scroll_o.pack(side='bottom', fill='x')
tree_view.pack(side=LEFT, expand=True, fill=BOTH)
bps = ttk.Button(root, text="vittorie, vittorie in casa, vittorie in trasferta", command=None)
ocn = {'Inghilterra': "E0", "Scozia": "SC0", "Germania": 'D1', "Spagna": "SP1",
      'Italia': 'I1', "Francia": 'F1', "Olanda": 'N1', "Belgio": 'B1', "Portogallo": 'P1',
      "Turchia": 'T1', "Grecia": 'G1'}
ocl = {"E0": 'Premier League', "SC0": 'Scottish Premiership', "D1": 'Bundesliga', "SP1": 'Liga Spagnola',
      'I1': 'Serie A', "F1": 'Ligue 1', "N1": 'Eredivise', "B1": 'Pro League', "P1": 'Primeira Liga',
      "T1": 'Super Lig', "G1": 'Souper Ligka Ellada'}
csv = StringVar()
comboC = ttk.Combobox(root, textvariable=csv, values=list(ocn))
comboC.grid(row=2, column=0)
csv.trace("w", onc_change)
gsv = StringVar()
comboG = ttk.Combobox(root, textvariable=gsv, value=None)
comboG.grid(row=2, column=1)
gsv.trace("w", ong_change)
ssv = StringVar()
comboS = ttk.Combobox(root, textvariable=ssv, value=None)
comboS.grid(row=2, column=2)
dsv = StringVar()
comboD = ttk.Combobox(root, textvariable=dsv, value=None)
comboD.grid(row=2, column=3)
k = Entry()
k.grid(row=2, column=4)


def punti(qualcosa):
    return qualcosa.punti()
#Apro il file e passo npome del file excel al dispatcher per ottenere le strutture dati

campionati = dispatcher(ocl, "all-euro-data-2016-2017.xls")
giornate  = campionati['I1'].giornate()
#giornate[15].classifica()._lista.sort(key=punti,reverse=True)
#print(giornate[1].classifica())
# codice per interfaccia grafica a schermo intero, premere ESC per uscire
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()

