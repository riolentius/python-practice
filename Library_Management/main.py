from tkinter import *
from PIL import ImageTk, Image  # PIL --> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *

mypass = "asdfgce159"  # use your own password
mydatabase = "db"  # the database name

con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)
# root is the username here

cur = con.cursor()  # cur --> cursor

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25

# adding bg image
background_img = Image.open("SMJfWsT.jpg")
[imageSizeW, imageSizeH] = background_img.size

newImageSizeW = int(imageSizeW*n)
if same:
    newImageSizeH = int(imageSizeH*n)
else:
    newImageSizeH = int(imageSizeH/n)

background_img = background_img.resize(
    (newImageSizeW, newImageSizeH), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_img)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeW, height=newImageSizeH)
Canvas1.pack(expand=True, fill=BOTH)

# setting head frame
headingFrame1 = Frame(root, bg='#ffbb00', bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Library",
                     bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# add buttons
btn1 = Button(root, text="Add Book Details",
              bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book",
              bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List",
              bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Issue Book to Student",
              bg='black', fg='white', command=issueBook)
btn3.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Return book", bg='black',
              fg='white', command=returnBook)
btn4.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
mainloop()
