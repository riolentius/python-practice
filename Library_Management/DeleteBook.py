from importlib.metadata import entry_points
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from cv2 import destroyAllWindows
import pymysql

mypass = "asdfgce159"
mydatabase = "db"
con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)
cur = con.cursor()

# enter tables name
issueTable = "books_issued"
bookTable = "books"


def deleteBook():

    bid = bookInfo1.get()

    deleteSql = "delete from "+bookTable+"where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+"where bid = '"+bid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showinfo("Please Check Book ID")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg='#006b38')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg='#ffbb00', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to delete
    lbl2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lbl2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # submit button
    submitBtn = Button(root, text="Submit", bg='#d1ccc0',
                       fg='black', command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
