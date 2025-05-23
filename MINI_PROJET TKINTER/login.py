from tkinter import *
from tkinter import messagebox
import main

def open_login(): 
    login = Tk()
    login.title("Login page")
    login.geometry("1200x600")
    login.config(bg="white")

    def Submit():
        u1 = user_input.get()
        p1 = password_input.get()
        if u1 == "admin" and p1 == "0000":
            messagebox.showwarning("welcome", "success")
            login.destroy()
            main.open_main()
        else:
            messagebox.showwarning("erreur", "Incorrect user")

    #image
    image = PhotoImage(file="login.png")
    resized_img = image.subsample(2, 2)
    label = Label(login, image=resized_img,bg="white")  
    label.place(x=20, y=50)

    #title
    title = Label(login,text="Login",font=("Segoe UI", 25), fg="black",bg="white")
    # Username
    user = Label(login, text="Username: ",font=("Segoe UI", 16), fg="black",bg="white")
    user_input = Entry(login, font=("Segoe UI", 16), fg="black", bd=0, width=30)

    # Password
    password = Label(login, text="Password: ",font=("Segoe UI", 16), fg="black",bg="white")
    password_input = Entry(login, font=("Segoe UI", 16), fg="black", bd=0, width=30,show="*")

    # Login Button
    login_button = Button(login, text="Se connecter", font=("Segoe UI", 16), command=Submit,bg="#1591EA",fg="white",width=15,height=1)

    # Placement des widgets avec place
    title.place(x=775,y=90)
    user.place(x=595, y=145)
    user_input.place(x=700, y=150, width=250)
    password.place(x=600,y=195)
    password_input.place(x=700, y=200, width=250)
    login_button.place(x=725, y=250,height=40)
    Frame(login, bg="black", height=2, width=250).place(x=700, y=180)
    Frame(login, bg="black", height=2, width=250).place(x=700, y=230)

    login.mainloop()