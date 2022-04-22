import hashlib
import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="sairam123")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS forpython")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="sairam123", database="forpython")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(255) PRIMARY KEY ,password VARCHAR(255))")


def images():
    global backButton, showPassword, SignUpPage, hidePassword, mainPage, forgotPage
    backButton = Image.open(r'D:\Aravind\Class 12th Project\backbutton.jpg')
    showPassword = Image.open(r'D:\Aravind\Class 12th Project\showPassword (2).jpg')
    showPassword = showPassword.resize((35, 23))
    hidePassword = Image.open(r'hidePassword (2).jpg')
    hidePassword = hidePassword.resize((35, 27))
    SignUpPage = Image.open('SignUp-01.png')
    SignUpPage = SignUpPage.resize((600, 400))
    mainPage = Image.open(r'Main-01.png')
    mainPage = mainPage.resize((800, 600))
    forgotPage = Image.open(r'forgotpage-01.png')
    forgotPage = forgotPage.resize((400, 300))


root = Tk()
root.title("Password Manager")
root.geometry("300x300+520+220")
root.iconbitmap(r"password-manager.ico")


def randompg(x):
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


def signup():
    root.title('SecureVault-SignUp')
    for widget in root.winfo_children():
        widget.destroy()
    global backButton, SignUpPage
    backButton = backButton.resize((35, 22))
    backButton = ImageTk.PhotoImage(backButton)
    SignUpPage = ImageTk.PhotoImage(SignUpPage)
    root.geometry("600x400+400+125")
    lblb = Label(root, image=SignUpPage)
    lblb.place(x=0, y=0)
    username1 = Entry(root, font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3', width=10)
    username1.place(x=257, y=121)
    password1 = Entry(root, width=10, show='*', font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3')
    password1.place(x=257, y=210)
    password2 = Entry(root, width=10, show='*', font=('BentonSans Comp Black', 14), justify='center', bg='#A3A3A3')
    password2.place(x=257, y=290)
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
        sqlFormula = 'SELECT * FROM login'
        mycursor.execute(sqlFormula)
        myresult = mycursor.fetchall()
        if myresult != []:
            for result in myresult:
                if result[0] != a:
                    if b == c:
                        details1 = (a, b)
                        sqlFormula = "INSERT INTO login(username,password) VALUES(%s,%s)"
                        try:
                            mycursor.execute(sqlFormula, details1)
                            mycursor.execute(
                                "CREATE TABLE IF NOT EXISTS " + a + " (sitename VARCHAR(255),mailID VARCHAR(255),password VARCHAR(255))")
                            mydb.commit()
                            break
                        except mysql.connector.errors.IntegrityError:
                            lbl["text"] = "INVALID USERNAME"
                            lbl['font'] = ('BentonSans Comp Black', 12)
                            break
                    elif b != c:
                        lbl["text"] = "PASSWORDS DON'T MATCH"
                        lbl['font'] = ('BentonSans Comp Black', 12)
                        break
                elif result[0] == a:
                    lbl["text"] = "INVALID USERNAME"
                    lbl['font'] = ('BentonSans Comp Black', 12)
                    break
        elif myresult == []:
            if b == c:
                details1 = (a, b)
                sqlFormula = "INSERT INTO login(username,password) VALUES(%s,%s)"
                mycursor.execute(sqlFormula, details1)
                mycursor.execute(
                    "CREATE TABLE IF NOT EXISTS " + a + " (sitename VARCHAR(255),mailID VARCHAR(255),password VARCHAR(255))")
                mydb.commit()

    button1 = Button(root, text="SIGN UP", command=lambda: [credentialcheck()], fg='White', bg='#ed2024',
                     font=('BentonSans Comp Black', 14))
    button1.place(x=275, y=330)
    button3 = Button(root, command=lambda: {start_menu()}, image=backButton)
    button3.place(x=30, y=35)


def login():
    images()
    global backButton
    backButton = backButton.resize((35, 22))
    backButton = ImageTk.PhotoImage(backButton)
    j = 1
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600+275+50")
    root.title("SecureVault Password Manager")
    img = Image.open(r"D:\Aravind\Class 12th Project\LoginPage-01.png")
    img = img.resize((800, 600))
    labl = Label(root)
    labl.img = ImageTk.PhotoImage(img)
    labl['image'] = labl.img
    labl.place(x=0, y=0)
    # label1=Label(root,text="ENTER YOUR USERNAME")
    # label1.place(x=345,y=175)
    username1 = Entry(root, width=12, font=("BentonSans Comp Black", 18), justify='center')
    username1.place(x=325, y=243)
    # label2=Label(root,text="ENTER YOUR PASSWORD")
    # label2.place(x=345,y=230)
    password1 = Entry(root, width=12, show='*', font=("BentonSans Comp Black", 18), justify='center')
    password1.place(x=325, y=347)
    entries = [child for child in root.winfo_children() if isinstance(child, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))
    button3 = Button(root, command=lambda: {start_menu()}, image=backButton)
    button3.place(x=30, y=35)

    def forgotpassword():
        global forgotPage
        forgotPage = Image.open(r'forgotpage-01.png')
        forgotPage = forgotPage.resize((400, 300))
        forgotPage = ImageTk.PhotoImage(forgotPage)
        root4 = Toplevel(root)
        root4.geometry('400x300')
        root4.grab_set()
        lbl1 = Label(root4, image=forgotPage)
        lbl1.place(x=0, y=0)
        enrt = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center')
        enrt.place(x=140, y=70)
        enrt1 = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center')
        enrt1.place(x=140, y=145)
        enrt2 = Entry(root4, width=16, font=('BentonSans Comp Black', 12), justify='center')
        enrt2.place(x=140, y=220)
        enrt1['state'] = 'disabled'
        enrt2['state'] = 'disabled'

        def chk():
            chk1 = enrt.get().lower()
            enrt1['state'] = 'normal'
            enrt2['state'] = 'normal'
            mycursor.execute("SELECT * FROM login")
            myresult = mycursor.fetchall()
            for result in myresult:
                if result[0] == chk1:
                    btn5.destroy()
                    entries = [child for child in root4.winfo_children() if isinstance(child, Entry)]
                    for idx, entry in enumerate(entries):
                        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                    def chkfinal():
                        nonlocal chk1
                        q = enrt1.get()
                        chk1 = "'" + chk1 + "'"
                        r = enrt2.get()
                        if q == r:
                            q = hashingpassword(q.encode('utf-8'))
                            q = "'" + q + "'"
                            sqlFormula = f"UPDATE login SET password={q} WHERE username={chk1}"
                            mycursor.execute(sqlFormula)
                            mydb.commit()

                    btsn = Button(root4, text="DONE", command=lambda: [chkfinal(), removewindow(root4)],
                                  font=('BentonSans Comp Black', 12))
                    btsn.place(x=180, y=255)

                    break
                else:
                    messagebox.showerror("ERROR", "ENTER A VALID USERNAME")
                    break

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
        global showPassword, hidePassword, mainPage
        for result in myresult:
            if det == result:
                for widget in root.winfo_children():
                    widget.destroy()
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
                                fieldbackground='#a3a3a3', foreground="black", font=('BentonSans Comp Black', 14),)
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
                mytree.place(x=95, y=200)
                mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))
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
                    mytree.place(x=95, y=200)
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
                    mytree.place(x=95, y=200)
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

                        mytree.place(x=95, y=200)
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

                        mytree.place(x=95, y=200)
                        mytree.bind("<Control-Key-c>", lambda x: copy_from_treeviewuap(mytree, x))
                        mytree.bind('<Control-Key-x>', lambda x: copy_from_treeviewcol(mytree, x))

                butn2 = Button(root, text="REFRESH", command=refresh, width=20, font=("Agency FB", 15), bg='#cec4c5')
                butn2.place(x=230, y=100)

                def add():
                    root1 = Toplevel(root)
                    root1.geometry("250x180+575+290")
                    root1.grab_set()
                    lab1 = Label(root1, text="Enter The Name of The Site", bg='#ed2124', fg='White',
                                 font=('BentonSans Comp Black', 12))
                    lab1.pack()
                    sitename = Entry(root1, width=20)
                    sitename.pack()
                    lab2 = Label(root1, text="Enter The Mail ID", bg='#ed2124', fg='White',
                                 font=('BentonSans Comp Black', 12))
                    lab2.pack()
                    mail = Entry(root1, width=20)
                    mail.pack()
                    lab3 = Label(root1, text="Enter The Password", bg='#ed2124', fg='White',
                                 font=('BentonSans Comp Black', 12))
                    lab3.pack()
                    password2 = Entry(root1, width=20)
                    password2.pack()
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

                    btnn = Button(root1, text="Generate Random Password", command=lambda: [randompg(password2)])
                    btnn.pack()
                    buton1 = Button(root1, text="Done", command=lambda: [credadd(), refresh(), removewindow(root1)])
                    buton1.pack()

                butn1 = Button(root, text="ADD PASSWORD", command=add, width=20, font=("Agency FB", 15), bg='#cec4c5')
                butn1.place(x=60, y=100)

                def update():
                    root2 = Toplevel(root)
                    root2.geometry('200x200+575+290')
                    root2.grab_set()
                    l = []
                    sqlFormula = f'SELECT * FROM {username}'
                    mycursor.execute(sqlFormula)
                    myresult = mycursor.fetchall()
                    for result in myresult:
                        l.append(result[0])
                    b = StringVar()
                    menu1 = ttk.Combobox(root2, textvariable=b, values=l)
                    menu1.pack()
                    label4 = Label(root2, text="Enter The New Email")
                    label4.pack()
                    ent4 = Entry(root2, width=20)
                    ent4.pack()
                    label6 = Label(root2, text="Enter The New Password")
                    label6.pack()
                    ent6 = Entry(root2, width=20)
                    ent6.pack()
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

                    btnn = Button(root2, text="Generate Random Password", command=lambda: [randompg(ent6)])
                    btnn.pack()
                    btn1 = Button(root2, text="DONE", command=lambda: [update1(), refresh(), removewindow(root2)])
                    btn1.pack()

                butn3 = Button(root, text="UPDATE", command=update, width=20, font=("Agency FB", 15), bg='#cec4c5')
                butn3.place(x=400, y=100)

                def confirm(x, y):
                    res = messagebox.askquestion("DELETE SITE", "Do You Want to Remove The Entered Site")
                    if res == "yes":
                        x()
                        refresh()
                        y.destroy()
                    else:
                        pass

                def delete1():
                    root3 = Toplevel(root)
                    root3.geometry('200x100+575+290')
                    root3.grab_set()
                    labl1 = Label(root3, text="Choose The Site Name \nFor which you want to \nRemove the Password")
                    labl1.pack()
                    l = []
                    sqlFormula = f'SELECT * FROM {username}'
                    mycursor.execute(sqlFormula)
                    myresult = mycursor.fetchall()
                    for result in myresult:
                        l.append(result[0])
                    b = StringVar()
                    menu1 = ttk.OptionMenu(root3, b, 'Select ', *l)
                    menu1.pack()
                    entries = [child for child in root3.winfo_children() if isinstance(child, Entry)]
                    for idx, entry in enumerate(entries):
                        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

                    def delete2():
                        a = b.get()
                        a = "'" + a + "'"
                        sqlFormula = f"DELETE FROM {username} WHERE sitename={a}"
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                    btn1 = Button(root3, text="DONE", command=lambda: [confirm(delete2, root3)])
                    btn1.pack()

                btn1 = Button(root, text="DELETE", command=delete1, width=20, font=("Agency FB", 15), bg='#cec4c5')
                btn1.place(x=570, y=100)

                def savefiles():
                    import csv
                    data = []
                    file2 = filedialog.asksaveasfilename(defaultextension='.csv',
                                                         filetypes=[("Comma Separated Values", '.csv'),
                                                                    ("Excel Sheet", '.xlsx')])
                    # print(type(file2),file2)
                    if file2 != None or file2 != '':
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
                        pass

                btn2 = Button(root, text="EXPORT", command=savefiles, width=20, font=("Agency FB", 12), bg='#cec4c5')
                btn2.place(x=670, y=40)

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
                btn3.place(x=20, y=50)

    button1 = Button(root, text="LOGIN", bg="#777071", font=("BentonSans Comp Black", 14), fg="Black",
                     command=credentialcheck, width=13)
    button1.place(x=340, y=475)


def start_menu():
    images()
    if root:
        for widget in root.winfo_children():
            widget.destroy()
        else:
            pass
    root.geometry("300x300+520+220")
    root.iconbitmap(r"password-manager.ico")
    root.title('SecureVault Password Manager')
    button2 = Button(text="LOGIN", width=15, command=login, font=('BentonSans Comp Black', 14))
    button2.place(x=75, y=50)
    button1 = Button(text="SIGN UP", width=15, command=signup, font=('BentonSans Comp Black', 14))
    button1.place(x=75, y=100)


start_menu()
root.resizable(False, False)
root.mainloop()
