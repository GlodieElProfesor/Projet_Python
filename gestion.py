from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from time import strftime
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
profiles = {
    1:""
}





win = Tk()
win.geometry("1500x700")
win.config(bg = "white")
win.title("GESTION DE PAYEMENT")
#Champ de text dans le frame
Label1 = Label(win, text = "TABLEAU DE PAYEMENT DE FRAIS SCOLAIRE" , font= ("arial", 20 , "bold"), bg = "#A0C7DB", fg="white")
Label1.pack(fill = X)


    


img= PhotoImage(file="images/images_fonds/fond1.png")
Label(win, image=img, bg="white").pack()
 



def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(100, time)

#####################################################################################################################""
def cycle_toplevel():
    global Arbre_cycle

    # Créer une fenêtre Toplevel
    toplevel = Toplevel(win)
    frame_cycle = Frame(toplevel)

    #ajout d'un scroollnarr
    scroll = Scrollbar(frame_cycle)
    scroll.pack(side=RIGHT, fill=Y)

    #la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
    Arbre_cycle = ttk.Treeview(frame_cycle, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
    Arbre_cycle.pack(fill=BOTH, expand=True)

    #configuration de scrollbar dans le treeview
    scroll.config(command=Arbre_cycle.yview)

    #ajoute des entete
    Arbre_cycle.heading(1, text="N°")
    Arbre_cycle.heading(2, text="Noms")
    Arbre_cycle.heading(3, text="Classe")
    Arbre_cycle.heading(4, text="Montants")
    Arbre_cycle.heading(5, text="Date")

    #Redimensionnement de colonne
    Arbre_cycle.column(1, width=20)
    Arbre_cycle.column(2, width=180)
    Arbre_cycle.column(3, width=100)
    Arbre_cycle.column(4, width=100)
    Arbre_cycle.column(5, width=100)

    frame_cycle.pack()
    frame_cycle.pack_propagate(False)
    frame_cycle.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
    frame_cycle.pack()

    # Récupération des données de la base de données et affichage dans Arbre_troisieme
    conn = sqlite3.connect("bases_des_donnees/cycle.db")
    cur = conn.cursor()
    select5 = cur.execute("SELECT * FROM cycle_eleves ORDER BY id DESC")
    select5 = list(select5)
    for i in select5:
        Arbre_cycle.insert("", END, value=i)
    conn.close()

#########################################################################################################################
def quatrieme_toplevel():
    global Arbre_quatrieme

    # Créer une fenêtre Toplevel
    toplevel = Toplevel(win)
    frame_quatrieme = Frame(toplevel)

    #ajout d'un scroollnarr
    scroll = Scrollbar(frame_quatrieme)
    scroll.pack(side=RIGHT, fill=Y)

    #la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
    Arbre_quatrieme = ttk.Treeview(frame_quatrieme, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
    Arbre_quatrieme.pack(fill=BOTH, expand=True)

    #configuration de scrollbar dans le treeview
    scroll.config(command=Arbre_quatrieme.yview)

    #ajoute des entete
    Arbre_quatrieme.heading(1, text="N°")
    Arbre_quatrieme.heading(2, text="Noms")
    Arbre_quatrieme.heading(3, text="Classe")
    Arbre_quatrieme.heading(4, text="Montants")
    Arbre_quatrieme.heading(5, text="Date")

    #Redimensionnement de colonne
    Arbre_quatrieme.column(1, width=20)
    Arbre_quatrieme.column(2, width=180)
    Arbre_quatrieme.column(3, width=100)
    Arbre_quatrieme.column(4, width=100)
    Arbre_quatrieme.column(5, width=100)

    frame_quatrieme.pack()
    frame_quatrieme.pack_propagate(False)
    frame_quatrieme.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
    frame_quatrieme.pack()

    # Récupération des données de la base de données et affichage dans Arbre_troisieme
    conn = sqlite3.connect("bases_des_donnees/quatrieme.db")
    cur = conn.cursor()
    select4 = cur.execute("SELECT * FROM quatrieme_eleves ORDER BY id DESC")
    select4= list(select4)
    for i in select4:
        Arbre_quatrieme.insert("", END, value=i)
    conn.close()

######################################################################################################################
def troisieme_toplevel():
    global Arbre_troisieme

    # Créer une fenêtre Toplevel
    toplevel = Toplevel(win)
    frame_troisieme = Frame(toplevel)

    #ajout d'un scroollnarr
    scroll = Scrollbar(frame_troisieme)
    scroll.pack(side=RIGHT, fill=Y)

    #la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
    Arbre_troisieme = ttk.Treeview(frame_troisieme, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
    Arbre_troisieme.pack(fill=BOTH, expand=True)

    #configuration de scrollbar dans le treeview
    scroll.config(command=Arbre_troisieme.yview)

    #ajoute des entete
    Arbre_troisieme.heading(1, text="N°")
    Arbre_troisieme.heading(2, text="Noms")
    Arbre_troisieme.heading(3, text="Classe")
    Arbre_troisieme.heading(4, text="Montants")
    Arbre_troisieme.heading(5, text="Date")

    #Redimensionnement de colonne
    Arbre_troisieme.column(1, width=20)
    Arbre_troisieme.column(2, width=180)
    Arbre_troisieme.column(3, width=100)
    Arbre_troisieme.column(4, width=100)
    Arbre_troisieme.column(5, width=100)

    frame_troisieme.pack()
    frame_troisieme.pack_propagate(False)
    frame_troisieme.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
    frame_troisieme.pack()

    # Récupération des données de la base de données et affichage dans Arbre_troisieme
    conn = sqlite3.connect("bases_des_donnees/troisieme.db")
    cur = conn.cursor()
    select3 = cur.execute("SELECT * FROM troisieme_eleves ORDER BY id DESC")
    select3 = list(select3)
    for i in select3:
        Arbre_troisieme.insert("", END, value=i)
    conn.close()

######################################################################################################################## 
def deuxieme_toplevel():
    global Arbre_deuxieme

    # Créer une fenêtre Toplevel
    toplevel = Toplevel(win)
    frame_deuxieme = Frame(toplevel)

    #ajout d'un scroollnarr
    scroll = Scrollbar(frame_deuxieme)
    scroll.pack(side=RIGHT, fill=Y)

    #la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
    Arbre_deuxieme = ttk.Treeview(frame_deuxieme, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
    Arbre_deuxieme.pack(fill=BOTH, expand=True)

    #configuration de scrollbar dans le treeview
    scroll.config(command=Arbre_deuxieme.yview)

    #ajoute des entete
    Arbre_deuxieme.heading(1, text="N°")
    Arbre_deuxieme.heading(2, text="Noms")
    Arbre_deuxieme.heading(3, text="Classe")
    Arbre_deuxieme.heading(4, text="Montants")
    Arbre_deuxieme.heading(5, text="Date")

    #Redimensionnement de colonne
    Arbre_deuxieme.column(1, width=20)
    Arbre_deuxieme.column(2, width=180)
    Arbre_deuxieme.column(3, width=100)
    Arbre_deuxieme.column(4, width=100)
    Arbre_deuxieme.column(5, width=100)

    frame_deuxieme.pack()
    frame_deuxieme.pack_propagate(False)
    frame_deuxieme.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
    frame_deuxieme.pack()

    # Récupération des données de la base de données et affichage dans Arbre_troisieme
    conn = sqlite3.connect("bases_des_donnees/deuxieme.db")
    cur = conn.cursor()
    select2 = cur.execute("SELECT * FROM deuxieme_eleves ORDER BY id DESC")
    select2 = list(select2)
    for i in select2:
        Arbre_deuxieme.insert("", END, value=i)
    conn.close()

###########################################################################################################
def ouvrir_toplevel():
    global Arbre_premiere

    # Créer une fenêtre Toplevel
    toplevel = Toplevel(win)
    frame_premiere = Frame(toplevel)

    #ajout d'un scroollnarr
    scroll = Scrollbar(frame_premiere)
    scroll.pack(side=RIGHT, fill=Y)

    #la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
    Arbre_premiere = ttk.Treeview(frame_premiere, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
    Arbre_premiere.pack(fill=BOTH, expand=True)

    #configuration de scrollbar dans le treeview
    scroll.config(command=Arbre_premiere.yview)

    #ajoute des entete
    Arbre_premiere.heading(1, text="N°")
    Arbre_premiere.heading(2, text="Noms")
    Arbre_premiere.heading(3, text="Classe")
    Arbre_premiere.heading(4, text="Montants")
    Arbre_premiere.heading(5, text="Date")

    #Redimensionnement de colonne
    Arbre_premiere.column(1, width=20)
    Arbre_premiere.column(2, width=180)
    Arbre_premiere.column(3, width=100)
    Arbre_premiere.column(4, width=100)
    Arbre_premiere.column(5, width=100)

    frame_premiere.pack()
    frame_premiere.pack_propagate(False)
    frame_premiere.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
    frame_premiere.pack()

    # Récupération des données de la base de données et affichage dans Arbre_troisieme
    conn = sqlite3.connect("bases_des_donnees/premiere.db")
    cur = conn.cursor()
    select1 = cur.execute("SELECT * FROM premiere_eleves ORDER BY id DESC")
    select1 = list(select1)
    for i in select1:
        Arbre_premiere.insert("", END, value=i)
    conn.close()

###############################################################################################################################
def valide():
    global Arbre_troisieme
    global Arbre_deuxieme
    global Arbre_premiere
    Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
    classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
    Montant=entree6.get()
    Date=str(selected_date.get())
    
    if Noms == "" or classe=="" or Montant==""or Date=="":
        messagebox.showerror("erreur","completer tout le champs")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())
        conn= sqlite3.connect("bases_des_donnees/mydatabase.db")
        cur = conn.cursor()

        req = "CREATE TABLE IF NOT EXISTS eleves (id INTEGER primary KEY AUTOINCREMENT,\
        Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"

        cur.execute(req)
        req2= "INSERT INTO eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
        cur.execute(req2,(Noms, classe, Montant, Date))
        conn.commit()
        conn.close()

        conn= sqlite3.connect("bases_des_donnees/mydatabase.db")
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM eleves order by id desc")
        select =list(select)
        Arbre.insert("", END, values = select[0])

        conn.close()

    if Noms == "" or classe == "" or Montant == "" or Date == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())

        # Insertion des données si la classe est égale à "1ère Hp"
        if classe == "1ere HP" or classe == "1ere TCC" or classe=="1ere BC" or classe == "1ere LIT" or classe == "1ere SCIENTIF":
            # Connexion à la base de données
            conn = sqlite3.connect("bases_des_donnees/premiere.db")
            cur = conn.cursor()

            req = "CREATE TABLE IF NOT EXISTS  premiere_eleves (id INTEGER primary KEY AUTOINCREMENT,\
            Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"
            cur.execute(req)
            req2= "INSERT INTO premiere_eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
            cur.execute(req2,(Noms, classe, Montant, Date))
            conn.commit()
            conn.close()


        # Ouverture du toplevel et mise à jour de l'affichage de l'arbre
        if classe == "1ere":
            ouvrir_toplevel()
            conn = sqlite3.connect("bases_des_donnees/premiere.db")
            cur = conn.cursor()
            select_premiere = cur.execute("SELECT * FROM premiere_eleves ORDER BY id DESC")
            select_premiere = list(select_premiere)
            for i in select_premiere:
                Arbre_premiere.insert("", END, value=i)
            conn.close()
    

    if Noms == "" or classe == "" or Montant == "" or Date == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())

        # Insertion des données si la classe est égale à "1ère Hp"
        if classe == "2ème HP" or classe == "2ème TCC" or classe=="2ème BC" or classe == "2ème LIT" or classe == "2ème SCIENTIF":
            # Connexion à la base de données
            conn = sqlite3.connect("bases_des_donnees/deuxieme.db")
            cur = conn.cursor()

            req = "CREATE TABLE IF NOT EXISTS  deuxieme_eleves (id INTEGER primary KEY AUTOINCREMENT,\
            Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"
            cur.execute(req)
            req2= "INSERT INTO deuxieme_eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
            cur.execute(req2,(Noms, classe, Montant, Date))
            conn.commit()
            conn.close()


        # Ouverture du toplevel et mise à jour de l'affichage de l'arbre
        if classe == "2ème":
            deuxieme_toplevel()
            conn = sqlite3.connect("bases_des_donnees/deuxieme.db")
            cur = conn.cursor()
            select_deuxime = cur.execute("SELECT * FROM deuxieme_eleves ORDER BY id DESC")
            select_deuxime = list(select_deuxime)
            for i in select_deuxime:
                Arbre_deuxieme.insert("", END, value=i)
            conn.close()



    if Noms == "" or classe == "" or Montant == "" or Date == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())

        # Insertion des données si la classe est égale à "1ère Hp"
        if classe == "3ème HP" or classe == "3ème TCC" or classe=="3ème BC" or classe == "3ème LIT" or classe == "3ème SCIENTIF":
            # Connexion à la base de données
            conn = sqlite3.connect("bases_des_donnees/troisieme.db")
            cur = conn.cursor()

            req = "CREATE TABLE IF NOT EXISTS  troisieme_eleves (id INTEGER primary KEY AUTOINCREMENT,\
            Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"
            cur.execute(req)
            req2= "INSERT INTO troisieme_eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
            cur.execute(req2,(Noms, classe, Montant, Date))
            conn.commit()
            conn.close()


        # Ouverture du toplevel et mise à jour de l'affichage de l'arbre
        if classe == "3eme":
            troisieme_toplevel()
            conn = sqlite3.connect("bases_des_donnees/troisieme.db")
            cur = conn.cursor()
            select_troisieme = cur.execute("SELECT * FROM troisieme_eleves ORDER BY id DESC")
            select_troisieme = list(select_troisieme)
            for i in select_troisieme:
                Arbre_troisieme.insert("", END, value=i)
            conn.close()




    if Noms == "" or classe == "" or Montant == "" or Date == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())

        # Insertion des données si la classe est égale à "1ère Hp"
        if classe == "4ème HP" or classe == "4ème TCC" or classe=="4ème BC" or classe == "4ème LIT" or classe == "4ème SCIENTIF":
            # Connexion à la base de données
            conn = sqlite3.connect("bases_des_donnees/quatrieme.db")
            cur = conn.cursor()

            req = "CREATE TABLE IF NOT EXISTS  quatrieme_eleves (id INTEGER primary KEY AUTOINCREMENT,\
            Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"
            cur.execute(req)
            req2= "INSERT INTO quatrieme_eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
            cur.execute(req2,(Noms, classe, Montant, Date))
            conn.commit()
            conn.close()

        # Ouverture du toplevel et mise à jour de l'affichage de l'arbre
        if classe == "4ème":
            quatrieme_toplevel()
            conn = sqlite3.connect("bases_des_donnees/quatrieme.db")
            cur = conn.cursor()
            select_quatrieme = cur.execute("SELECT * FROM quatrieme_eleves ORDER BY id DESC")
            select_quatrieme = list(select_quatrieme)
            for i in select_quatrieme:
                select_quatrieme.insert("", END, value=i)
            conn.close()






    if Noms == "" or classe == "" or Montant == "" or Date == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        Noms=str(entree1.get())+" "+str(entree2.get())+" " + str(entree3.get())
        classe=list_der1.get() + list_der2.get() + list_der3.get() + list_der4.get() + list_der5.get()
        Montant=entree6.get()
        Date=str(selected_date.get())

        # Insertion des données si la classe est égale à "1ère Hp"
        if classe == "8ème" or classe == "7ème":
            # Connexion à la base de données
            conn = sqlite3.connect("bases_des_donnees/cycle.db")
            cur = conn.cursor()

            req = "CREATE TABLE IF NOT EXISTS  cycle_eleves (id INTEGER primary KEY AUTOINCREMENT,\
            Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL, Date TEXT NOT NULL)"
            cur.execute(req)
            req2= "INSERT INTO cycle_eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
            cur.execute(req2,(Noms, classe, Montant, Date))
            conn.commit()
            conn.close()

        # Ouverture du toplevel et mise à jour de l'affichage de l'arbre
        if classe == "bases_des_donnees/cycle":
            cycle_toplevel()
            conn = sqlite3.connect("cycle.db")
            cur = conn.cursor()
            select_cycle = cur.execute("SELECT * FROM cycle_eleves ORDER BY id DESC")
            select_cycle = list(select_cycle)
            for i in select_cycle:
                Arbre_cycle.insert("", END, value=i)
            conn.close()


    
##########################################################################################################################""
def delete():
    idSelect = Arbre.item(Arbre.selection())["values"][0]
    conn= sqlite3.connect("bases_des_donnees/mydatabase.db")
    cur = conn.cursor()
    cur.execute("delete from eleves where id ={}".format(idSelect))
    conn.commit()
    if cur.rowcount == 1:
        Arbre.delete(Arbre.selection())

    # Récupération du nom supprimé et enregistrement dans la table "supprimes"
    nom_supprime = Arbre.item(Arbre.selection())["values"][0]
    req = "INSERT INTO corbeil_eleves (nom) values (?)"
    cur.execute(req, (nom_supprime,))
    conn.commit()

    Arbre.delete(Arbre.selection())

########################################################################################################################
def recuperer():
    conn = sqlite3.connect("bases_des_donnees/mydatabase.db")
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM supprimes")
    select = list(select)
    for row in select:
        nom = row[1]
        req = "INSERT INTO eleves (Noms, classe, Montant, Date) values (?, ?, ?, ?)"
        cur.execute(req, (nom, "N/A", "N/A"))
        conn.commit()
        select2 = cur.execute("SELECT * FROM eleves order by id desc")
        select2 = list(select2)
        Arbre.insert("", END, values=select2[0])
    conn.execute("DELETE FROM supprimes")
    conn.commit()
    conn.close()



##################################################################################################################
def Update():
    pass
#################################################################################################################
bouton_recherche_image = PhotoImage(file="images/boutons/recherche.png")


def recherche():
    search_term = search_entry.get()
    conn = sqlite3.connect("bases_des_donnees/mydatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM eleves WHERE Noms LIKE ?", ('%' + search_term + '%',))
    results = cur.fetchall()
    Arbre.delete(*Arbre.get_children())
    for row in results:
        Arbre.insert("", END, value=row)
    conn.close()


search_button = Button(win, image=bouton_recherche_image , font= ("Elephant"), command=recherche)
search_button.place(x=1020,y=40)


search_entry = Entry(win, font= ("Elephant", 14), border=6)
search_entry.place(x = 1150, y =40, width=200, height=40)

##############################################################################################################
def select_treeview(event):
    label_mon_profil.destroy()
    selection_identifiant = Arbre.item(Arbre.selection())["values"][0]
    imgprofil = ("images/photos_eleve/profil_" + str(selection_identifiant) + ".png")
    with open("images/photos_eleve/profil_" + str(selection_identifiant) + ".png", "rb") as f:
        image_profils = Image.open(f)
        new_width = 350
        new_height = 300
        image_profil_resized = image_profils.resize((new_width, new_height))

    # Créer l'objet ImageTk avec l'image redimensionnée
    mon_profils = ImageTk.PhotoImage(image_profil_resized)
    # Créer le label avec l'image redimensionnée
    profiles[1]=mon_profils
    label_mon_profils = Label(win, image=mon_profils)
    label_mon_profils.place(x=0, y=80)

################################################################################################################""

#creation de la barre de menu
barreMenu = Menu(win)





#creation de menus principaux/ on applique ces dofferent menus la barre de menu
menu_principal = Menu(barreMenu)
meu_edition = Menu(barreMenu)
outil_menu = Menu(barreMenu)
corbeil_menu = Menu(barreMenu)





#ajoute des menues principaux a la barre de menu / on ajoute ce different menu a la barre de menu avec leurs noms propreslç
barreMenu.add_cascade(label = "Fichier", menu = menu_principal)
barreMenu.add_cascade(label = "Ediion" , menu = meu_edition)
barreMenu.add_cascade(label = "Outil" , menu = outil_menu)
barreMenu.add_cascade(label = "corbeil" , menu = corbeil_menu)


#ajouter des sous-menus menu
menu_principal.add_command(label="Nouveau")
menu_principal.add_command(label="Enregistrer sous ")
menu_principal.add_command(label="Quitter")



##########################################################################################################





parcourit_entry = Entry(win, font= ("castellar", 14) )
parcourit_entry.place(x=0, y = 40, width=230, height=50)
parcourit_button = Button(win, text="parcours", font= ("castellar", 14), bg = "blue")
parcourit_button.place(x=230, y= 40 )




# Ouvrir l'image et la redimensionner
with open("images/photos_eleve/profil_1.png", "rb") as f:
    image_profil = Image.open(f)
    new_width = 400
    new_height = 300
    image_profil_resized = image_profil.resize((new_width, new_height))

# Créer l'objet ImageTk avec l'image redimensionnée
mon_profil = ImageTk.PhotoImage(image_profil_resized)
# Créer le label avec l'image redimensionnée
label_mon_profil = Label(win, image=mon_profil)
label_mon_profil.place(x=0, y=80)






frame = Frame(win)



#Label(frame, image=img, bg="white").pack()


label =Label(frame, font=("arial", 12))
label.place(x=5, y=10)
time()



################################################################################

#creation de label
label1 = Label(frame, text="Nom :",  font= ("Elephant", 14), bg="#D8E7F0")
label1.place(x=50,y=70)
#le champ d'ebtreé de valeurs
entree1 = Entry(frame, border=0, font=("arial", 14), bg="#D8E7F0")
entree1.place(x=120, y=70, height=25)
Frame(frame, width=300, height=2, bg="black", ).place(x=52, y=92)
##############################################################################



#creation de label
label2 = Label(frame, text="Post Nom :" , font= ("Elephant", 14), bg = "#D8E7F0")
label2.place(x=50,y=110)
#le champ d'ebtreé de valeurs
entree2 = Entry(frame, border=0, font=("arial", 14), bg="#D8E7F0" )
entree2.place(x=160, y=110)
Frame(frame, width=300, height=2, bg="black", ).place(x=52, y=132)

###############################################################################


#creation de label
label3 = Label(frame, text="Prenom:", font= ("Elephant", 14), bg= "#D8E7F0")
label3.place(x=50,y=150)
#le champ d'ebtreé de valeurs
entree3 = Entry(frame, border=0, font=("arial", 14) , bg="#D8E7F0")
entree3.place(x=160, y=150)
Frame(frame, width=300, height=2, bg="black", ).place(x=52, y=172)
##############################################################################

#titre du combo box
label4= Label(frame, text="cycle : ", font= ("Elephant", 14), bg= "#D8E7F0")
label4.place(x=50, y=190)
#creation d'une combobox
list1 = [" 8ème", "7ème"] 
list_der1 = ttk.Combobox(frame, value=list1)
list_der1.place(x=50  ,y=220)

###############################################################################
#titre du combo box
label5= Label(frame, text="1ème: ", font= ("Elephant", 12), bg= "#D8E7F0")
label5.place(x=200, y=190)
#creation d'une combobox
list2 = ["1ere HP", "1ere BC", "1ere LIT", "1ere CG", "1ere SCIENTIF", "1ere TCC"] 
list_der2 = ttk.Combobox(frame, value=list2)
list_der2.place(x=200  ,y=220)
###################################################################################


#titre du combo box
label6= Label(frame, text="2ème: ", font= ("Elephant", 12), bg= "#D8E7F0")
label6.place(x=350, y=190)
#creation d'une combobox
list3 = ["2ème HP", "2ème BC", "2ème LIT", "2ème CG", "2ème SCIENTIF", "2ème TCC"] 
list_der3 = ttk.Combobox(frame, value=list3)
list_der3.place(x=350  ,y=220)

################################################################################


#titre du combo box
label7=Label(frame, text="3ème : ", font= ("ariElephantal", 14), bg= "#D8E7F0")
label7.place(x=120, y=243)
#creation d'une combobox
list4 =["3ème HP", "3ème BC", "3ème LIT", "3ème CG", "3ème SCIENTIF", "3ème TCC"]
list_der4 = ttk.Combobox(frame, value=list4, width=20)
list_der4.place(x=120  ,y=270)
###################################################################################

#titre du combo box
label8=Label(frame, text="4ème : ", font= ("ariElephantal", 14), bg= "#D8E7F0")
label8.place(x=270, y=243)
#creation d'une combobox
list5 =["4ème HP", "4ème BC", "4ème LIT", "4ème CG", "4ème SCIENTIF", "4ème TCC"]
list_der5 = ttk.Combobox(frame, value=list5, width=20)
list_der5.place(x=270  ,y=270)

#####################################################################################

#creation de label
label6 = Label(frame, text="Montant de frais:", font= ("Elephant", 14), bg="#D8E7F0")
label6.place(x=160,y=300)
#le champ d'ebtreé de valeurs
entree6 = Entry(frame, width=20,border=0, font=("arial", 14) , bg="#D8E7F0")
entree6.place(x=350, y=300)
Frame(frame, width=280, height=2, bg="black", ).place(x=163, y=323)


frame.pack()
frame.pack_propagate(False)
frame.configure(width= 650, height= 415, bg='#D8E7F0',  highlightthickness=2, highlightbackground="black" )
frame.place(x=370, y=35)

##############################################################################################""

bouton_valide_image = PhotoImage(file="images/boutons/valide.png")
bouton_suppr_image = PhotoImage(file="images/boutons/suppr.png")
bouton_update_image = PhotoImage(file="images/boutons/update.png")
bouton_cycle_image = PhotoImage(file="images/boutons/cycle_cours.png")
bouton_deuxieme_image = PhotoImage(file="images/boutons/deuxieme.png")
bouton_premier_image = PhotoImage(file="images/boutons/premiere.png")
bouton_quatrieme_image = PhotoImage(file="images/boutons/quatrieme.png")
bouton_troisieme_image = PhotoImage(file="images/boutons/troisieme.png")



###################################################################################################
bouton_cycle = Button(win, border = 0, image=bouton_cycle_image, command = cycle_toplevel)
bouton_cycle.place(x=1100, y=200)

bouton_premier = Button(win, border = 0, image=bouton_premier_image, command=ouvrir_toplevel)
bouton_premier.place(x=1100, y=300)


bouton_deuxieme = Button(win, border = 0, image=bouton_deuxieme_image, command = deuxieme_toplevel)
bouton_deuxieme.place(x=1100, y=400)


bouton_troisieme = Button(win, border = 0, image=bouton_troisieme_image, command = troisieme_toplevel)
bouton_troisieme.place(x=1100, y=500)


bouton_quatrieme = Button(win, border = 0, image=bouton_quatrieme_image, command = quatrieme_toplevel)
bouton_quatrieme.place(x=1100, y=600)


bout1= Button(frame, border = 5, image=bouton_valide_image,command=valide)
bout1.place(x=50, y=340)

bout1= Button(frame,border=5, image=bouton_update_image)
bout1.place(x=230, y=340)

bout1= Button(frame,border = 5, image=bouton_suppr_image, command = delete)
bout1.place(x=390, y=340)
##############################################################################################
frame1 = Frame(win)

#ajout d'un scroollnarr
scroll = Scrollbar(frame1)
scroll.pack(side =RIGHT, fill=Y)

#la creation de la liste de tout les identifiants de l'etudiants, placer dans la frame
Arbre = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show="headings", yscrollcommand=scroll.set)
Arbre.pack(fill=BOTH, expand=True)



Arbre.bind("<<TreeviewSelect>>", select_treeview)

frame1.pack()
frame1.pack_propagate(False)
frame1.configure(width= 660, height= 250, bg="#E4DEE4",  highlightthickness=2, highlightbackground="black")
frame1.place(x=370, y=450)



#configuration de scrollbar dans le treeiew
scroll.config(command = Arbre.yview)

#ajoute des entete
Arbre.heading(1, text="N°")
Arbre.heading(2, text="Noms")
Arbre.heading(3, text="Classe")
Arbre.heading(4, text="Montants")
Arbre.heading(5, text="Date")





#Redimensionnement de colonne
Arbre.column(1, width=20)
Arbre.column(2, width=180)
Arbre.column(3, width=100)
Arbre.column(4, width=100)
Arbre.column(5, width=100)



# inserer les donnée dans le treevievw
conn= sqlite3.connect("bases_des_donnees/mydatabase.db")
cur = conn.cursor()

req = "CREATE TABLE IF NOT EXISTS eleves (id INTEGER primary KEY AUTOINCREMENT,\
Noms TEXT NOT NULL, Classe TEXT NOT NULL, Montant TEXT NOT NULL,Date TEXT NOT NULL)"

cur.execute(req)
select=cur.execute("select * from eleves")
for row in select:
    Arbre.insert("", END, value = row)







# Créer une variable StringVar pour stocker la date sélectionnée
selected_date = StringVar()

# Fonction pour mettre à jour la valeur de la variable StringVar à partir du widget Calendar
def update_selected_date():
    selected_date.set(cal.get_date())
    top.destroy()

# Fonction pour afficher le widget Calendar dans une fenêtre contextuelle
def show_calendar():
    global top, cal
    top = Toplevel(win)
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(padx=10, pady=10)
    ok_button = Button(top, text="OK", command=update_selected_date)
    ok_button.pack(pady=10)

# Créer une Combobox pour sélectionner une date
date_combobox = ttk.Combobox(win, textvariable=selected_date, font= ("Elephant", 14))
date_combobox.place(x=1100, y=100, width=200, height=50)
date_combobox.bind("<Button-1>", lambda event: show_calendar())




win.config(menu=barreMenu)
win.mainloop() 