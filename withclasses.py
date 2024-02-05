from tkinter import*
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

class Buttons():
    """This class contains the methods that are common to all subclass buttons"""
    def __init__(self, root):
        self.root = root # all buttons have the same root

    def place(self, row, column, padx, pady):
        """This method is common for all buttons. It allows the user to place the button on a location on the screen."""
        self.button.grid(row=row, column=column, padx=padx, pady=pady)

class translateButton(Buttons): # this is a subclass of the superclass Buttons
    """This class is for the button that commands the translation of text"""
    def __init__(self, root, font, text):
        Buttons.__init__(self, root) # multiple inheritance. calling superclass method.
        self.font = font
        self.text = text
        self.button = Button(self.root, text = self.text, font = self.font, command = self.clicked)
    
    def clicked(self):
        source_lang, dest_lang = get_languages()
        translated_text.delete(1.0, END) # Delete any previous translations
        translator = Translator()
        words = original_text.get(1.0, END)
        words = translator.translate(words, dest=dest_lang, src=source_lang)  # This function translates the text 
        words = words.text
        translated_text.insert(1.0, words) # This function is the output of the translated text to the screen  


class chooseLanguage(Buttons): # this is a subclass of the superclass Buttons
    """This class is for the drop down boxes where the suer can choose language source and destination"""
    def __init__(self, root, current, list):
        Buttons.__init__(self, root) # multiple inheritance. calling superclass method
        self.current = current
        self.list = list
        self.button = ttk.Combobox(self.root, width = 20, value = self.list)
        self.button.current(current)
    
    def place(self, row, column, padx, pady): # this is an example of method overiding. This place() method will be called for chooseLanguage objects
        self.button.grid(sticky=E, row=row, column=column, padx=padx, pady=pady)
        

class refreshButton(Buttons): # this is a subclass of the superclass Buttons
    """This class is for the button that clears all textboxes"""
    def __init__(self, root, font, text):
        Buttons.__init__(self, root) # multiple inheritance. calling superclass method
        self.font = font
        self.text = text
        self.button = Button(self.root, text= self.text, font = self.font, command = self.clicked)
    
    def clicked(self):
        original_text.delete(1.0, END)
        translated_text.delete(1.0, END)        

def get_languages():
    """"""
    global original_combo, dest_lang
    source_lang = original_combo.button.get()
    dest_lang = translated_combo.button.get()
    return (source_lang, dest_lang)


# **************** SET UP WINDOW ********************
root = Tk() # This command opens the the tkinter pop up box
root.title('Assignment 3 - Question 1')
root.geometry("1000x320") # size of the pop up box

# **************** AQUIRE LANGUAGES ********************
languages = googletrans.LANGUAGES
language_list = list(languages.values())
language_list =[x.title() for x in language_list]

#**************** ADD OBJECTS ***********************
text = Label(root, text = "Translated Text",  font = "Times 15 bold")
text.grid(row =0, column=3)

text = Label(root, text = "Input Text",  font = "Times 15 bold")
text.grid(row=0, columnspan=2)

text = Label(root, text = "Input Language")
text.grid(sticky=W, row=2, column=0, padx=15)

text = Label(root, text = "Output Language")
text.grid(sticky=W, row=2, column=3, padx=15)

original_text = Text(root, height=10, width=40) # change box sizes to suit what we want to do
original_text.grid(row=1, columnspan=2, padx= 15) # column span brings the box across 2 columns

translated_text = Text(root, height=10, width=40) # change box sizes to suit what we want to do
translated_text.grid(row=1, column=3, padx= 15, pady= 5) # pady brings it down from the top and padx brings it from the left towards the middle

translate_button = translateButton(root, ("Times", 24), "Translate")
translate_button.place(1, 2, 5, 5)

clear_button = refreshButton(root, ("Times", 24), "Clear")
clear_button.place(3, 2, 0, 20)

original_combo = chooseLanguage(root, 21, language_list)
original_combo.place(2,1,0,5)

translated_combo = chooseLanguage(root, 21, language_list)
translated_combo.place(2,3,25,5)

root.mainloop()