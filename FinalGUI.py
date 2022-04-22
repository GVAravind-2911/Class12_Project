import hashlib
import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
import pyperclip
from PIL import Image, ImageTk

mydb = mysql.connector.connect(host="localhost", user="root", passwd="sairam123")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS forpython")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="sairam123", database="forpython")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(255) PRIMARY KEY ,password VARCHAR(255))")


def images():
    global backButton, showPassword, SignUpPage, hidePassword, mainPage, forgotPage, addPword, updatePword, deletePword, mainPage1, home1, genrand
    backButton = Image.open(r'backbutton.jpg')
    showPassword = Image.open(r'showPassword (2).jpg')
    showPassword = showPassword.resize((35, 23))
    hidePassword = Image.open(r'hidePassword (2).jpg')
    hidePassword = hidePassword.resize((35, 25))
    SignUpPage = Image.open('SignUp-01.png')
    SignUpPage = SignUpPage.resize((600, 400))
    mainPage = Image.open(r'Main-01.png')
    mainPage = mainPage.resize((800, 600))
    forgotPage = Image.open(r'forgotpage-01.png')
    forgotPage = forgotPage.resize((400, 300))
    addPword = Image.open(r'AddPword-01.png')
    addPword = addPword.resize((420, 320))
    updatePword = Image.open(r'updatePage-01-01.png')
    updatePword = updatePword.resize((400, 300))
    deletePword = Image.open(r'deletePword-01.png')
    deletePword = deletePword.resize((300, 200))
    mainPage1 = Image.open(r'mainPage-01.png')
    mainPage1 = mainPage.resize((300, 300))
    home1 = Image.open(r'home-01.png')
    home1 = home1.resize((35, 22))
    genrand = Image.open(r'GenPass.png')
    genrand = genrand.resize((125, 25))


root = Tk()
root.title("Password Manager")
root.geometry("300x300+520+220")
root.iconbitmap(r"password-manager.ico")


def randompg(x):
    x.delete("0", 'end')
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    res = messagebox.askquestion("PASSWORD GENERATOR", "Do You Want to use special \n symbols such as @#$")
    if res == "yes":
        comblist = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS
        maxlen = 12
        psswd = ""
        for i in range(maxlen):
            psswd += random.choice(comblist)
        print(psswd)
        x.insert(0, psswd)
    else:
        comblist = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS
        maxlen = 12
        psswd = ""
        for i in range(maxlen):
            psswd += random.choice(comblist)
        print(psswd)
        x.insert(0, psswd)


def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()


def removewindow(r):
    r.destroy()


def hashingpassword(text):
    hash = hashlib.blake2b(text).hexdigest()
    return hash


def copy_from_treeviewuap(tree, event):
    selection = tree.selection()
    value = []
    for each in selection:
        try:
            value = tree.item(each)["values"]
        except:
            pass
    copy_string = "\n".join(value[1:])
    pyperclip.copy(copy_string)


def copy_from_treeviewcol(tree, event):
    selection = tree.selection()
    column = tree.identify_column(event.x)
    column_no = int(column.replace("#", "")) - 1

    copy_values = []
    for each in selection:
        try:
            value = tree.item(each)["values"][column_no]
            copy_values.append(str(value))
        except:
            pass

    copy_string = "\n".join(copy_values)
    pyperclip.copy(copy_string)


def showp(x, y, z):
    x.configure(show='')
    y['state'] = 'normal'
    z['state'] = 'disabled'


def hidep(x, y, z):
    x.configure(show='*')
    y['state'] = 'normal'
    z['state'] = 'disabled'


def signup():
    root.title('SecureVault-SignUp')
    for widget in root.winfo_children():
        widget.destroy()
    global backButton, SignUpPage, hpforall, spforall, showPassword, hidePassword
    backButton = backButton.resize((35, 22))
    backButton = ImageTk.PhotoImage(backButton)
    SignUpPage = ImageTk.PhotoImage(SignUpPage)
    showPassword = ImageTk.PhotoImage(showPassword)
    hidePassword = ImageTk.PhotoImage(hidePassword)
    root.geometry("600x400+400+125")
    lblb = Label(root, image=SignUpPage)
    lblb.place(x=0, y=0)
    username1 = Entry(root, font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3', width=10)
    username1.place(x=257, y=121)
    password1 = Entry(root, width=10, show='*', font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3')
    password1.place(x=257, y=210)
    showpbtn1 = Button(root, image=showPassword, state='normal')
    showpbtn1.place(x=209, y=210)
    hidepbtn1 = Button(root, image=hidePassword, state='disabled')
    hidepbtn1.place(x=367, y=207)
    showpbtn1.configure(command=lambda: [showp(password1, hidepbtn1, showpbtn1)])
    hidepbtn1.configure(command=lambda: [hidep(password1, showpbtn1, hidepbtn1)])
    password2 = Entry(root, width=10, show='*', font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3')
    password2.place(x=257, y=290)
    showpbtn2 = Button(root, image=showPassword, state='normal')
    showpbtn2.place(x=209, y=287)
    hidepbtn2 = Button(root, image=hidePassword, state='disabled')
    hidepbtn2.place(x=367, y=287)
    showpbtn2.configure(command=lambda: [showp(password2, hidepbtn2, showpbtn2)])
    hidepbtn2.configure(command=lambda: [hidep(password2, showpbtn2, hidepbtn2)])
    lbl = Label(root, bg='#ED2124')
    lbl.place(x=245, y=15)
    entries = [child for child in root.winfo_children() if isinstance(child, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

    def credentialcheck():
        global funcstocall
        a = username1.get().lower()
        b = hashingpassword(password1.get().encode('utf-8'))
        c = hashingpassword(password2.get().encode('utf-8'))
        sqlFormula = 'SELECT username FROM login'
        mycursor.execute(sqlFormula)
        myresult = mycursor.fetchall()
        if myresult != []:
            if (a,) not in myresult:
                if b == c:
                    details1 = (a, b)
                    sqlFormula = "INSERT INTO login(username,password) VALUES(%s,%s)"
                    try:
                        mycursor.execute(sqlFormula, details1)
                        mycursor.execute(
                            "CREATE TABLE IF NOT EXISTS " + a + " (sitename VARCHAR(255),mailID VARCHAR(255),password VARCHAR(255))")
                        mydb.commit()
                        lbl['text'] = 'SUCCESSFULLY SIGNED UP'
                        lbl['font'] = ('BentonSans Comp Black', 12)
                    except mysql.connector.errors.IntegrityError:
                        lbl["text"] = "INVALID USERNAME"
                        lbl['font'] = ('BentonSans Comp Black', 12)
                elif b != c:
                    lbl["text"] = "PASSWORDS DON'T MATCH"
                    lbl['font'] = ('BentonSans Comp Black', 12)
            elif (a,) in myresult:
                lbl["text"] = "INVALID USERNAME"
                lbl['font'] = ('BentonSans Comp Black', 12)
        elif myresult == []:
            if b == c:
                details1 = (a, b)
                sqlFormula = "INSERT INTO login(username,password) VALUES(%s,%s)"
                mycursor.execute(sqlFormula, details1)
                mycursor.execute(
                    "CREATE TABLE IF NOT EXISTS " + a + " (sitename VARCHAR(255),mailID VARCHAR(255),password VARCHAR(255))")
                mydb.commit()
                lbl['text'] = 'SUCCESSFULLY SIGNED UP'
                lbl['font'] = ('BentonSans Comp Black', 12)

    button1 = Button(root, text="SIGN UP", command=lambda: [credentialcheck()], fg='White', bg='#ed2024',
                     font=('BentonSans Comp Black', 14))
    button1.place(x=275, y=330)
    button3 = Button(root, command=lambda: {start_menu()}, image=backButton)
    button3.place(x=30, y=35)


def login():
    images()
    global backButton, showPassword1, hidePassword1
    showPassword = Image.open(r'showPassword (2).jpg')
    showPassword = showPassword.resize((33, 21))
    hidePassword = Image.open(r'hidePassword (2).jpg')
    hidePassword = hidePassword.resize((33, 23))
    backButton = backButton.resize((35, 22))
    backButton = ImageTk.PhotoImage(backButton)
    j = 1
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600+275+50")
    root.title("SecureVault Password Manager Login")
    img = Image.open(r"D:\Aravind\Class 12th Project\LoginPage-01.png")
    img = img.resize((800, 600))
    labl = Label(root)
    labl.img = ImageTk.PhotoImage(img)
    labl['image'] = labl.img
    labl.place(x=0, y=0)
    username1 = Entry(root, width=12, font=("BentonSans Comp Black", 18), justify='center')
    username1.place(x=325, y=243)
    password1 = Entry(root, width=12, show='*', font=("BentonSans Comp Black", 18), justify='center')
    password1.place(x=325, y=347)
    showPassword1 = Image.open(r'showPassword (2).jpg')
    showPassword1 = showPassword.resize((33, 21))
    hidePassword1 = Image.open(r'hidePassword (2).jpg')
    hidePassword1 = hidePassword.resize((33, 23))
    showPassword1 = ImageTk.PhotoImage(showPassword1)
    hidePassword1 = ImageTk.PhotoImage(hidePassword1)
    showpbtn = Button(root, image=showPassword1, state='normal')
    showpbtn.place(x=280, y=349)
    hidepbtn = Button(root, image=hidePassword1, state='disabled')
    hidepbtn.place(x=478, y=349)
    showpbtn.configure(command=lambda: [showp(password1, hidepbtn, showpbtn)])
    hidepbtn.configure(command=lambda: [hidep(password1, showpbtn, hidepbtn)])
    entries = [child for child in root.winfo_children() if isinstance(child, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))
    button3 = Button(root, command=lambda: {start_menu()}, image=backButton)
    button3.place(x=30, y=35)

    def forgotpassword():
        global forgotPage, showPassword, hidePassword
        forgotPage = Image.open(r'forgotpage-01.png')
        forgotPage = forgotPage.resize((400, 300))
        forgotPage = ImageTk.PhotoImage(forgotPage)
        showPassword = Image.open(r'showPassword (2).jpg')
        showPassword = showPassword.resize((33, 21))
        hidePassword = Image.open(r'hidePassword (2).jpg')
        hidePassword = hidePassword.resize((33, 23))
        showPassword = ImageTk.PhotoImage(showPassword)
        hidePassword = ImageTk.PhotoImage(hidePassword)
        root4 = Toplevel(root)
        root4.resizable(False, False)
        root4.title('Forgot Password')
        root4.iconbitmap(r"password-manager.ico")
        root4.geometry('400x300+470+150')
        root4.grab_set()
        lbl1 = Label(root4, image=forgotPage)
        lbl1.place(x=0, y=0)
        enrt = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center')
        enrt.place(x=140, y=70)
        enrt1 = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center', show='*')
        enrt1.place(x=140, y=145)
        enrt2 = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center', show='*')
        enrt2.place(x=140, y=220)
        enrt1['state'] = 'disabled'
        enrt2['state'] = 'disabled'
        showpbtn = Button(root4, image=showPassword, state='normal')
        showpbtn.place(x=97, y=143)
        hidepbtn = Button(root4, image=hidePassword, state='disabled')
        hidepbtn.place(x=279, y=143)
        showpbtn.configure(command=lambda: [showp(enrt1, hidepbtn, showpbtn)])
        hidepbtn.configure(command=lambda: [hidep(enrt1, showpbtn, hidepbtn)])
        showpbtn1 = Button(root4, image=showPassword, state='normal')
        showpbtn1.place(x=97, y=218)
        hidepbtn1 = Button(root4, image=hidePassword, state='disabled')
        hidepbtn1.place(x=279, y=218)
        showpbtn1.configure(command=lambda: [showp(enrt2, hidepbtn1, showpbtn1)])
        hidepbtn1.configure(command=lambda: [hidep(enrt2, showpbtn1, hidepbtn1)])

        def chk():
            chk1 = enrt.get().lower()
            mycursor.execute("SELECT username FROM login")
            myresult = mycursor.fetchall()
            if (chk1,) in myresult:
                enrt1['state'] = 'normal'
                enrt2['state'] = 'normal'
                btn5.destroy()
                entries = [child for child in root4.winfo_children() if isinstance(child, Entry)]
                for idx, entry in enumerate(entries):
                    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                def chkfinal():
                    nonlocal chk1
                    q = enrt1.get()
                    r = enrt2.get()
                    if q == r:
                        q = hashingpassword(q.encode('utf-8'))
                        sqlFormula = f"UPDATE login SET password='{q}' WHERE username='{chk1}'"
                        mycursor.execute(sqlFormula)
                        mydb.commit()
                        removewindow(root4)
                    else:
                        btsn.configure(command=lambda: [chkfinal()])
                        messagebox.showinfo("Password Error", "Passwords Dont Match")

                btsn = Button(root4, text="DONE", command=lambda: [chkfinal()],
                              font=('BentonSans Comp Black', 12))
                btsn.place(x=180, y=255)

            else:
                messagebox.showinfo("Invalid Username", "User Doesn't Exist")

        btn5 = Button(root4, text="Check", command=chk, font=('BentonSans Comp Black', 10))
        btn5.place(x=300, y=69)

    butn9 = Button(root, text="FORGOT PASSWORD", command=forgotpassword, bg="#820814",
                   font=("BentonSans Comp Black", 12), fg="White", width=17)
    butn9.place(x=340, y=525)

    def credentialcheck():
        username = username1.get().lower()
        password = hashingpassword(password1.get().encode('utf-8'))
        det = (username, password)
        mycursor.execute("SELECT * FROM login")
        myresult = mycursor.fetchall()
        global showPassword, hidePassword, mainPage, home1
        if det in myresult:
            for widget in root.winfo_children():
                widget.destroy()
            root.title("SecureVault Password Manager")
            mainPage = ImageTk.PhotoImage(mainPage)
            label1 = Label(root, image=mainPage)
            label1.place(x=0, y=0)
            label2 = Label(root, text="Welcome!", font=("American Captain", 40), bg='#ed2124', fg='Black')
            label2.place(x=330, y=25)
            mycursor.execute('SELECT * FROM ' + username)
            myresult = mycursor.fetchall()
            global mytree
            style = ttk.Style(root)
            # set ttk theme to "clam" which support the fieldbackground option
            style.theme_use("clam")
            style.configure("Treeview", background="#a3a3a3",
                            fieldbackground='#a3a3a3', foreground="black", font=('BentonSans Cond Regular', 10), )
            mytree = ttk.Treeview(root)
            mytree['columns'] = ("Site Name", "Mail ID", "Password")
            mytree.column("#0", width=0, minwidth=25)
            mytree.column("Site Name", anchor=CENTER, width=200)
            mytree.column("Mail ID", anchor=CENTER, width=200)
            mytree.column("Password", anchor=CENTER, width=200)
            mytree.heading("#0", text=" ", anchor=CENTER)
            mytree.heading("Site Name", text="Site Name", anchor=CENTER)
            mytree.heading("Mail ID", text="Mail ID", anchor=CENTER)
            mytree.heading("Password", text="Password", anchor=CENTER)
            i = 0
            for result in myresult:
                result = list(result)
                result[2] = '*' * len(result[2])
                mytree.insert(parent="", index='end', iid=i, text="", values=result)
                i += 1
            mytree.place(x=95, y=210)
            mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
            mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))
            home1 = ImageTk.PhotoImage(home1)

            def suremain():
                x = messagebox.askquestion('Exit', 'Do you Want to go back\n to Home Page?')
                if x == 'yes':
                    start_menu()
                else:
                    pass

            def surelog():
                x = messagebox.askquestion('Exit', 'Do you Want to go back\n to Login Page?')
                if x == 'yes':
                    login()
                else:
                    pass

            button3 = Button(root, command=lambda: {suremain()}, image=home1)
            button3.place(x=25, y=15)
            button4 = Button(root, command=lambda: {surelog()}, image=backButton)
            button4.place(x=75, y=15)
            showPassword = Image.open(r'showPassword (2).jpg')
            showPassword = showPassword.resize((35, 23))
            hidePassword = Image.open(r'hidePassword (2).jpg')
            hidePassword = hidePassword.resize((35, 25))
            showPassword = ImageTk.PhotoImage(showPassword)
            hidePassword = ImageTk.PhotoImage(hidePassword)

            def hidepassword():
                global mytree
                nonlocal username
                mycursor.execute('SELECT * FROM ' + username)
                myresult = mycursor.fetchall()
                mytree.destroy()
                mytree = ttk.Treeview(root)
                mytree['columns'] = ("Site Name", "Mail ID", "Password")
                mytree.column("#0", width=0, minwidth=25)
                mytree.column("Site Name", anchor=CENTER, width=200)
                mytree.column("Mail ID", anchor=CENTER, width=200)
                mytree.column("Password", anchor=CENTER, width=200)
                mytree.heading("#0", text=" ", anchor=CENTER)
                mytree.heading("Site Name", text="Site Name", anchor=CENTER)
                mytree.heading("Mail ID", text="Mail ID", anchor=CENTER)
                mytree.heading("Password", text="Password", anchor=CENTER)
                i = 0
                for result in myresult:
                    result = list(result)
                    result[2] = '*' * len(result[2])
                    mytree.insert(parent="", index='end', iid=i, text="", values=result)
                    i += 1
                mytree.place(x=95, y=210)
                mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))
                btn5['state'] = 'disabled'
                btn4['state'] = 'active'

            def showpassword():
                mycursor.execute('SELECT * FROM ' + username)
                myresult = mycursor.fetchall()
                global mytree
                mytree.destroy()
                mytree = ttk.Treeview(root)
                mytree['columns'] = ("Site Name", "Mail ID", "Password")
                mytree.column("#0", width=0, minwidth=25)
                mytree.column("Site Name", anchor=CENTER, width=200)
                mytree.column("Mail ID", anchor=CENTER, width=200)
                mytree.column("Password", anchor=CENTER, width=200)
                mytree.heading("#0", text=" ", anchor=CENTER)
                mytree.heading("Site Name", text="Site Name", anchor=CENTER)
                mytree.heading("Mail ID", text="Mail ID", anchor=CENTER)
                mytree.heading("Password", text="Password", anchor=CENTER)
                i = 0
                for result in myresult:
                    mytree.insert(parent="", index='end', iid=i, text="", values=result)
                    i += 1
                mytree.place(x=95, y=210)
                mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))
                btn4['state'] = 'disabled'
                btn5['state'] = 'active'

            btn4 = Button(root, image=showPassword, command=showpassword)
            btn4.place(x=730, y=250)
            btn5 = Button(root, image=hidePassword, command=hidepassword)
            btn5.place(x=730, y=290)
            btn5['state'] = 'disabled'

            def refresh():
                global passwords
                global mytree
                mytree.destroy()
                mytree = ttk.Treeview(root)
                if btn5['state'] == 'disabled':
                    mytree['columns'] = ("Site Name", "Mail ID", "Password")
                    mytree.column("#0", width=0, minwidth=25)
                    mytree.column("Site Name", anchor=CENTER, width=200)
                    mytree.column("Mail ID", anchor=CENTER, width=200)
                    mytree.column("Password", anchor=CENTER, width=200)
                    mytree.heading("#0", text=" ", anchor=CENTER)
                    mytree.heading("Site Name", text="Site Name", anchor=CENTER)
                    mytree.heading("Mail ID", text="Mail ID", anchor=CENTER)
                    mytree.heading("Password", text="Password", anchor=CENTER)
                    mycursor.execute('SELECT * FROM ' + username)
                    myresult = mycursor.fetchall()
                    i = 0
                    for result in myresult:
                        result = list(result)
                        result[2] = '*' * len(result[2])
                        mytree.insert(parent="", index='end', iid=i, text="", values=result)
                        i += 1

                    mytree.place(x=95, y=210)
                    mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                    mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))
                else:
                    mytree['columns'] = ("Site Name", "Mail ID", "Password")
                    mytree.column("#0", width=0, minwidth=25)
                    mytree.column("Site Name", anchor=CENTER, width=200)
                    mytree.column("Mail ID", anchor=CENTER, width=200)
                    mytree.column("Password", anchor=CENTER, width=200)
                    mytree.heading("#0", text=" ", anchor=CENTER)
                    mytree.heading("Site Name", text="Site Name", anchor=CENTER)
                    mytree.heading("Mail ID", text="Mail ID", anchor=CENTER)
                    mytree.heading("Password", text="Password", anchor=CENTER)
                    mycursor.execute('SELECT * FROM ' + username)
                    myresult = mycursor.fetchall()
                    i = 0
                    for result in myresult:
                        mytree.insert(parent="", index='end', iid=i, text="", values=result)
                        i += 1

                    mytree.place(x=95, y=210)
                    mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                    mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))

            butn2 = Button(root, text="REFRESH", command=refresh, width=20, font=("Agency FB", 15), bg='#cec4c5')
            butn2.place(x=230, y=110)

            def add_pword():
                global addPword
                root1 = Toplevel(root)
                root1.resizable(False, False)
                root1.title('Add Password')
                root1.iconbitmap(r"password-manager.ico")
                root1.geometry("420x320+472+215")
                root1.grab_set()
                addPword = Image.open(r'AddPword-01.png')
                addPword = addPword.resize((420, 320))
                addPword = ImageTk.PhotoImage(addPword)
                lab1 = Label(root1, image=addPword)
                lab1.place(x=0, y=0)
                sitename = Entry(root1, width=16, font=("BentonSans Comp Black", 13), justify='center')
                sitename.place(x=140, y=69)
                mail = Entry(root1, width=16, font=("BentonSans Comp Black", 13), justify='center')
                mail.place(x=140, y=131)
                password2 = Entry(root1, width=16, font=("BentonSans Comp Black", 13), justify='center', show='*')
                password2.place(x=140, y=195)
                showpbtn1 = Button(root1, image=showPassword, state='normal')
                showpbtn1.place(x=97, y=194)
                hidepbtn1 = Button(root1, image=hidePassword, state='disabled')
                hidepbtn1.place(x=292, y=194)
                showpbtn1.configure(command=lambda: [showp(password2, hidepbtn1, showpbtn1)])
                hidepbtn1.configure(command=lambda: [hidep(password2, showpbtn1, hidepbtn1)])
                entries = [child for child in root1.winfo_children() if isinstance(child, Entry)]
                for idx, entry in enumerate(entries):
                    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                def credadd():
                    a1 = ''
                    nonlocal j
                    a = sitename.get()
                    b = mail.get()
                    c = password2.get()
                    det = (a, b, c)
                    sqlFormula = f"SELECT * FROM {username}"
                    mycursor.execute(sqlFormula)
                    myresult = mycursor.fetchall()
                    for result in myresult:
                        if result[0] == a and result[0][-1].isdigit() is False:
                            a1 = f'{j}'
                            j += 1
                        elif result[0] == a and result[0][-2].isdigit():
                            j = int(result[0][-1]) + 1
                            a1 = f'{j}'
                    a = a + a1
                    det = (a, b, c)
                    if det != ('', '', ''):
                        sqlFormula = "INSERT INTO " + username + " (sitename,mailID,password) VALUES(%s,%s,%s)"
                        mycursor.execute(sqlFormula, det)
                        mydb.commit()
                    else:
                        pass

                btnn = Button(root1, text="Generate Random Password", command=lambda: [randompg(password2)],
                              font=("BentonSans Comp Black", 10), bg='Black', fg='White')
                btnn.place(x=145, y=230)
                buton1 = Button(root1, text="DONE", command=lambda: [credadd(), refresh(), removewindow(root1)],
                                font=("BentonSans Comp Black", 10), bg='#820814', fg='White')
                buton1.place(x=198, y=260)

            butn1 = Button(root, text="ADD PASSWORD", command=add_pword, width=20, font=("Agency FB", 15),
                           bg='#cec4c5')
            butn1.place(x=60, y=110)

            def update_pword():
                global updatePword, genrand
                root2 = Toplevel(root)
                root2.resizable(False, False)
                root2.title('Update Details')
                root2.iconbitmap(r"password-manager.ico")
                updatePword = Image.open(r'updatePage-01-01.png')
                updatePword = updatePword.resize((400, 300))
                genrand = Image.open(r'GenPass.png')
                genrand = genrand.resize((130, 25))
                genrand = ImageTk.PhotoImage(genrand)
                root2.geometry('400x300+472+215')
                root2.grab_set()
                l = []
                sqlFormula = f'SELECT * FROM {username}'
                mycursor.execute(sqlFormula)
                myresult = mycursor.fetchall()
                for result in myresult:
                    l.append(result[0])
                b = StringVar()
                updatePword = ImageTk.PhotoImage(updatePword)
                lbls1 = Label(root2, image=updatePword)
                lbls1.place(x=0, y=0)
                menu1 = ttk.Combobox(root2, textvariable=b, values=l, font=('BentonSans Comp Black', 11),
                                     justify='center')
                menu1.place(x=115, y=60)
                ent4 = Entry(root2, width=20, font=('BentonSans Comp Black', 11), justify='center')
                ent4.place(x=119, y=125)
                ent6 = Entry(root2, width=20, font=('BentonSans Comp Black', 11), justify='center', show='*')
                ent6.place(x=119, y=185)
                showpbtn1 = Button(root2, image=showPassword, state='normal')
                showpbtn1.place(x=73, y=182)
                hidepbtn1 = Button(root2, image=hidePassword, state='disabled')
                hidepbtn1.place(x=289, y=182)
                showpbtn1.configure(command=lambda: [showp(ent6, hidepbtn1, showpbtn1)])
                hidepbtn1.configure(command=lambda: [hidep(ent6, showpbtn1, hidepbtn1)])
                entries = [child for child in root2.winfo_children() if isinstance(child, Entry)]
                for idx, entry in enumerate(entries):
                    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                def update1():
                    a = b.get()
                    a = "'" + a + "'"
                    d = ent4.get()
                    d = "'" + d + "'"
                    f = ent6.get()
                    f = "'" + f + "'"
                    sqlFormula1 = ("UPDATE " + username + " SET mailID=" + d + " WHERE sitename=" + a)
                    sqlFormula2 = ("UPDATE " + username + " SET password=" + f + " WHERE sitename=" + a)
                    mycursor.execute(sqlFormula1)
                    mycursor.execute(sqlFormula2)
                    mydb.commit()

                btnn = Button(root2, image=genrand, command=lambda: [randompg(ent6)], borderwidth=-0,
                              background='Black')
                btnn.place(x=135, y=225)
                btn1 = Button(root2, text="DONE", command=lambda: [update1(), refresh(), removewindow(root2)],
                              font=('BentonSans Comp Black', 10))
                btn1.place(x=180, y=260)

            butn3 = Button(root, text="UPDATE", command=update_pword, width=20, font=("Agency FB", 15),
                           bg='#cec4c5')
            butn3.place(x=400, y=110)

            def confirm(x, y):
                res = messagebox.askquestion("DELETE SITE", "Do You Want to Remove The Entered Site")
                if res == "yes":
                    x()
                    refresh()
                    y.destroy()
                else:
                    pass

            def delete_pword():
                global deletePword
                root3 = Toplevel(root)
                root3.resizable(False, False)
                root3.title('Delete Details')
                root3.iconbitmap(r"password-manager.ico")
                root3.geometry('300x200+540+280')
                root3.grab_set()
                l = []
                sqlFormula = f'SELECT * FROM {username}'
                mycursor.execute(sqlFormula)
                myresult = mycursor.fetchall()
                for result in myresult:
                    l.append(result[0])
                deletePword = Image.open(r'deletePword-01.png')
                deletePword = deletePword.resize((300, 200))
                deletePword = ImageTk.PhotoImage(deletePword)
                lbl = Label(root3, image=deletePword)
                lbl.place(x=0, y=0)
                b = StringVar()
                menu1 = ttk.OptionMenu(root3, b, 'SELECT ', *l)
                menu1.place(x=105, y=80)
                entries = [child for child in root3.winfo_children() if isinstance(child, Entry)]
                for idx, entry in enumerate(entries):
                    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                def delete2():
                    a = b.get()
                    sqlFormula = f"DELETE FROM {username} WHERE sitename='{a}'"
                    mycursor.execute(sqlFormula)
                    mydb.commit()

                btn1 = Button(root3, text="DONE", command=lambda: [confirm(delete2, root3)],
                              font=("BentonSans Comp Black", 15))
                btn1.place(x=130, y=150)

            btn1 = Button(root, text="DELETE", command=delete_pword, width=20, font=("Agency FB", 15), bg='#cec4c5')
            btn1.place(x=570, y=110)

            def savefiles():
                import csv
                file2 = filedialog.asksaveasfilename(defaultextension='.csv',
                                                     filetypes=[("Comma Separated Values", '.csv'),
                                                                ("Excel Sheet", '.xlsx')])
                print(file2)
                if file2 is None or file2 == '':
                    import os
                    file2 = os.getcwd()
                    file2 += f'\\{username}.csv'
                    file1 = open(file2, 'w', newline='')
                    writetofile = csv.writer(file1)
                    mycursor.execute("SELECT * FROM " + username)
                    myresult = mycursor.fetchall()
                    for result in myresult:
                        print(result)
                        writetofile.writerow(result)
                    file1.close()
                else:
                    file1 = open(file2, 'w', newline='')
                    writetofile = csv.writer(file1)
                    mycursor.execute("SELECT * FROM " + username)
                    myresult = mycursor.fetchall()
                    writetofile.writerows(myresult)
                    for result in myresult:
                        print(result)
                    file1.flush()

            btn2 = Button(root, text="EXPORT", command=savefiles, width=20, font=("Agency FB", 12), bg='#cec4c5')
            btn2.place(x=670, y=50)

            def importfromcsvfile():
                import csv
                file = filedialog.askopenfilename(defaultextension='.csv',
                                                  filetypes=[("Comma Separated Values", '.csv')])
                if file is not None and file != '':
                    file1 = open(file, 'r', newline='')
                    readed = csv.reader(file1)
                    sqlformula = "INSERT INTO " + username + " (sitename,mailID,password) VALUES(%s,%s,%s)"
                    for i in readed:
                        mycursor.execute(sqlformula, i)
                        mydb.commit()
                    file1.close()
                else:
                    pass

            btn3 = Button(root, text='IMPORT', command=lambda: [importfromcsvfile(), refresh()], width=20,
                          font=('Agency FB', 12), bg='#cec4c5')
            btn3.place(x=20, y=60)
        else:
            lblb = Label(root, text='INVALID USERNAME OR PASSWORD', font=("BentonSans Comp Black", 14), bg='#ed2124')
            lblb.place(x=270, y=25)

    button1 = Button(root, text="LOGIN", bg="#777071", font=("BentonSans Comp Black", 14), fg="Black",
                     command=credentialcheck, width=13)
    button1.place(x=340, y=475)


def start_menu():
    images()
    global mainPage1
    if root:
        for widget in root.winfo_children():
            widget.destroy()
        else:
            pass
    root.geometry("300x300+520+220")
    root.iconbitmap(r"password-manager.ico")
    root.title('SecureVault Password Manager')
    mainPage1 = ImageTk.PhotoImage(mainPage1)
    lbl = Label(root, image=mainPage1)
    lbl.place(x=0, y=0)
    button2 = Button(text="LOGIN", width=15, command=login, font=('BentonSans Comp Black', 14), bg='#bcbcbc',
                     fg='Black')
    button2.place(x=75, y=80)
    button1 = Button(text="SIGN UP", width=15, command=signup, font=('BentonSans Comp Black', 14), bg='#bcbcbc',
                     fg='Black')
    button1.place(x=75, y=130)


start_menu()
root.resizable(False, False)
root.mainloop()
