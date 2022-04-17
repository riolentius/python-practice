from fnmatch import translate
import string
from tkinter import *
from turtle import screensize
from translate import Translator

Screen = Tk()
Screen.title("Translator")

inputLanguageChoice = StringVar()
translateLanguageChoice = StringVar()

languageChoice = {'English', 'German', 'Japanese'}
inputLanguageChoice.set('English')
translateLanguageChoice.set('German')

# Function to translate Text


def Translate():
    translator = Translator(
        from_lang=inputLanguageChoice.get(), to_lang=translateLanguageChoice.get())
    translation = translator.translate(TextVar.get())
    outputVar.set(translation)


# Choice for input language
inputLanguageChoiceMenu = OptionMenu(
    Screen, inputLanguageChoice, *languageChoice)
Label(Screen, text="Choose a Language").grid(row=0, column=1)
inputLanguageChoiceMenu.grid(row=1, column=1)

# Choice in which language is translated
NewLanguageChoiceMenu = OptionMenu(
    Screen, translateLanguageChoice, *languageChoice)
Label(Screen, text="Translated Language").grid(row=0, column=2)
NewLanguageChoiceMenu .grid(row=1, column=2)

# Input and Output Text
Label(Screen, text="Enter Text").grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar).grid(row=2, column=1)

Label(Screen, text="Output Text").grid(row=2, column=2)
outputVar = StringVar()
TextBox = Entry(Screen, textvariable=outputVar).grid(row=2, column=3)
# Button for calling function
bButton = Button(Screen, text="Translate", command=Translate,
                 relief=GROOVE).grid(row=3, column=1, columnspan=3)

mainloop()
