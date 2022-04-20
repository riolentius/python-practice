from email import message
from tabnanny import check
from telnetlib import STATUS
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "asdfgce159"  # use your own password
mydatabase = "db"  # the database name

con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)
cur = con.cursor()

# table names
issueTable = "books_issued"
bookTable = "books"
allbid = []  # to store all the book id's


def issue():

    global issueBtn, labelFrame, lbl1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lbl1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from "+bookTable

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allbid.append(i[0])
            print(extractBid)

        if bid in allbid:
            checkAvail = "select status from "+bookTable+"where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            message.showinfo("Error", "Book id not present")
    except:
        messagebox.showinfo("Error", "Can't fetch book ids")

    issueSql = "insert into "+issueTable+" values ('"+bid+"', '"+issueto+"')"
    show = "select * from "+issueTable

    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allbid and status == True:
            cur.execute(issueSql)
            con.commit
            cur.execute(updateStatus)
            con.commit
            messagebox.showinfo('Success', "Book Isseud Successfully")
        else:
            allbid.clear()
            messagebox.showinfo('Message', "Book already issued")
            root.destroy()
            return
    except:
        messagebox.showinfo(
            "Search Error", "The Value entered is wrong, Try again")

    allbid.clear()


def issueBook():
    global issueBtn, labelFrame, lbl1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # book id
    lbl1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lbl1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # issued to student
    lbl2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lbl2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # issue button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0',
                      fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
