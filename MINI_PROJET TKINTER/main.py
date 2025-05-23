from tkinter import *
import csv
from tkinter import messagebox
import login

def open_main():

    main=Tk() #create window
    main.title("Gestion d'étudiant") #window title
    main.geometry("1500x1400")
    main.config(bg="white")
    #function to add student into database/csv file 
    def add():
        n1=nom_input.get()
        p1=prenom_input.get()
        d1=age_input.get()
        g1=groupe_input.get()
        if(len(n1)>0 and len(p1)>0 and len(d1)>0 and len(g1)>0):
            with open ("etudiants.csv","a",newline='') as file:
                CSV_writer = csv.writer(file,delimiter=";")
                CSV_writer.writerow([n1,p1,d1,g1])
            messagebox.showinfo("Succès","Etudiant ajouté.")
        else:
            messagebox.showerror("Error","Please fill out all fields.")

        #show all students in csv file
    def afficher_tous():
        text.delete("1.0", "end")
        i=1
        with open ("etudiants.csv","r") as file:
            CSV_reader = csv.reader(file,delimiter=";")
            for line in CSV_reader:
                line_str="   ".join(line)
                text.insert("end",line_str+"\n")
                i+=1
        #clear the entry widgets from any texts
    def clear():
        nom_input.delete(0,END)
        prenom_input.delete(0,END)
        age_input.delete(0,END)
        groupe_input.delete(0,END)

        #delete a student from csv file    
    def effacer():
        n1=nom_input.get()
        p1=prenom_input.get()
        d1=age_input.get()
        g1=groupe_input.get()
        lignes_modifiees = [] #list to store students different to the one we want to delete
        if(len(n1)>0 and len(p1)>0 and len(d1)>0 and len(g1)>0):
            with open("etudiants.csv",'r') as file:
                reader = csv.reader(file,delimiter=';')
                for line in reader:
                    if not (n1==line[0] and p1==line[1] and d1==line[2] and g1==line[3]):
                        lignes_modifiees.append(line)
            with open("etudiants.csv","w",newline='') as file2:
                ecrivain=csv.writer(file2,delimiter=";")
                for line in lignes_modifiees:
                    ecrivain.writerow(line) 
            messagebox.showinfo("Succès","Etudiant supprimé.")
        else:
            messagebox.showerror("Error","Please fill out all fields.")

        #search for a student using (nom,prenom)
    def recherche():
        try:
            s1=search_entry.get().strip()
            parts=s1.split()
            n1 = parts[0]
            p1 = parts[1]
            reponse = False 
            text.delete("1.0","end")

            with open("etudiants.csv",'r') as file3:
                reader = csv.reader(file3,delimiter=';')
                for line in reader:
                    if line[0]==n1 or line[1]==p1:
                        text.insert(END, "   ".join(line) + "\n")
                        reponse = True
                if reponse==False:
                    messagebox.showwarning('Warning','Name or Last name can\'t be found')   
        except:
            messagebox.showwarning('Warning','Entrer nom et prenom')
    def Logout():
        main.destroy()
        login.open_login()


    #image
    image = PhotoImage(file="logo.png")  # Replace with your image file name
    resized_img = image.subsample(2, 2)

    label = Label(main, image=resized_img,bg="white")  # keep a reference
    label.place(x=900, y=50)
    #logout
    log_out = Button(main,text="Logout",command=Logout,bg="white",font=("Segoe UI", 16,"underline"), fg="blue")
    log_out.place(x=50,y=40)
    #Nom
    nom=Label(main,text="Nom",font=("Segoe UI", 16), fg="black",bg="white")
    nom_input = Entry(main,width=40,bd=2,font=("Segoe UI", 16))
    #Prenom
    prenom=Label(main,text="Prenom",font=("Segoe UI", 16), fg="black",bg="white")
    prenom_input = Entry(main,width=40,bd=2,font=("Segoe UI", 16))
    #Age
    age=Label(main,text="Age",font=("Segoe UI", 16), fg="black",bg="white")
    age_input=Entry(main,width=40,bd=2,font=("Segoe UI", 16))
    #Group
    groupe=Label(main,text="Groupe",font=("Segoe UI", 16), fg="black",bg="white")
    groupe_input=Entry(main,width=40,bd=2,font=("Segoe UI", 16))

    #Buttons
    add_etud = Button(main,text="Add",command=add,bg="#11c70e",font=("Segoe UI", 16), fg="black")
    show_all = Button(main,text="Afficher tous",command=afficher_tous,bg="#c9c9c9",font=("Segoe UI", 16), fg="black")
    delete_etud = Button(main,text="Delete",command=effacer,bg="#e30707",font=("Segoe UI", 16), fg="black")
    clear_etud = Button(main,text="Clear",command=clear,bg="#eef531",font=("Segoe UI", 16), fg="black")


    #Search
    search_entry = Entry(main,width=30,bd=2,font=("Segoe UI", 16))
    search = Button(main,text="Search",command=recherche,bg="#0dbbde",font=("Segoe UI", 12), fg="black")

    #Text
    text=Text(main,width=80,height=15,bd=2)

    #placement
    nom.place(x=190,y=50)
    nom_input.place(x=250,y=50)
    Frame(main, bg="black", height=2, width=250).place(x=250, y=85,width=445)

    prenom.place(x=165,y=100)
    prenom_input.place(x=250,y=100)
    Frame(main, bg="black", height=2, width=250).place(x=250, y=135,width=445)

    age.place(x=195,y=150)
    age_input.place(x=250,y=150)
    Frame(main, bg="black", height=2, width=250).place(x=250, y=185,width=445)

    groupe.place(x=165,y=200)
    groupe_input.place(x=250,y=200)
    Frame(main, bg="black", height=2, width=250).place(x=250, y=235,width=445)

    add_etud.place(x=150,y=275,width=80)
    show_all.place(x=250,y=275,width=160)
    delete_etud.place(x=435,y=275,width=100)
    clear_etud.place(x=565,y=275,width=100)

    search_entry.place(x=250,y=350)
    search.place(x=600,y=350,width=100)
    Frame(main, bg="black", height=2, width=250).place(x=250, y=385,width=335)

    text.place(x=100,y=400)
    Frame(main, bg="black", height=2, width=250).place(x=100, y=645,width=645)
    main.mainloop()

if __name__=="__main__":
    login.open_login()