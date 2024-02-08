import tkinter as tk
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

class translateApp(tk.Tk):
    """This class encapsulates the main window"""
    def __init__(self):
        # main setup
        super().__init__() # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.title("Google Translate App") # name window
        self.geometry('1000x400') # change window size

        # widgets
        self.translate_frame = translateFrame(self)
        self.input_frame = inputFrame(self)
        self.middle_frame = middleFrame(self)

        # run
        self.mainloop()

# SET UP THREE FRAME CLASSES
# Each of the classes is an example of encapsultion. The data and methods working within each frame are encapsulated in a class.
class inputFrame(ttk.Frame):
    """This class is the frame for the left side, where the user inputs text to be translated"""
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of inheritance, because class is inheriting from superClass. 
        self.place(x=0, y=0, relwidth=0.4, relheight=1) # place frame in window.
        self.create_widgets()

    def create_widgets(self):     
        global original_combo, original_text
        text = ttk.Label(self, text = "Input Text",  font = "Times 15 bold") # title for original textbox
        text.grid(row=0, columnspan=2) # place in window

        text = ttk.Label(self, text = "Input Language") # label for input language drop down box
        text.grid(sticky='nsew', row=2, column=0, padx=15) # place in window

        original_text = tk.Text(self, height=10, width=45) # create box for user to input text into
        original_text.grid(row=1, columnspan=2, padx=15) # column span brings the box across 2 columns

        original_combo = ttk.Combobox(self, width=20, value=language_list) # this will create a drop down list of languages for user to choose from
        original_combo.grid(sticky='W', row=2, column=1, padx=0, pady=5) # place in window
        original_combo.current(21) # change default selection to English

class translateFrame(ttk.Frame):
    """This class is the frame for the right side, where the program outputs translated text"""
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of inheritance, because class is inheriting from superClass. 
        self.place(x=600, y=0, relwidth=0.4, relheight=1) # place frame in window
        self.create_widgets()

    def create_widgets(self): # this is an example of polymorphism. The create_widgets method has a different function depending which class it is in.    
        global translated_combo, translated_text # so variables exist outside of this class, to be accessed by other classes.
        text = ttk.Label(self, text = "Translated Text",  font = "Times 15 bold") # title for translated textbox
        text.grid(row=0, columnspan=2) # place in window

        text = ttk.Label(self, text = "Output Language") # label for output language drop down box
        text.grid(sticky='W', row=2, column=0, padx=15) # place in window

        translated_text = tk.Text(self, height=10, width=45) # create box for translated text to be displayed in
        translated_text.grid(row=1, columnspan=2, padx=15) # pady brings it down from the top and padx brings it from the left towards the middle

        translated_combo = ttk.Combobox(self, width=20, value=language_list) # this will create a drop down list of languages for user to choose from
        translated_combo.grid(sticky='W', row=2, column=1, padx=0, pady=5) # place in window
        translated_combo.current(26) # change default selection to English

class middleFrame(ttk.Frame):
    """This class encapsulates the buttons to translate and clear in the middle frame of the screen."""
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.place(x=400, y=0, relwidth=0.2, relheight=1) # place frame in window
        self.create_widgets()

    def create_widgets(self):
        translate_button = tk.Button(self, text="TRANSLATE", font="Times 20", command=self.translate_clicked) # button activates translation process
        translate_button.grid(row=0, column=0, pady=50) # place button in window

        clear_button = tk.Button(self, text="CLEAR", font="Times 20", command=self.clear_clicked) # button clears text boxes
        clear_button.grid(row=1, column=0) # place button in window

    @staticmethod # this is a decorator. this function does not need variables of the class, but makes sense to be encapsulated within this class.
    def get_languages():
        """This function retrieves the source and destination language and returns them in a tuple"""
        source_lang = original_combo.get() # global variables can be accessed
        dest_lang = translated_combo.get()
        return (source_lang, dest_lang)

    @staticmethod # this is a decorator. this function does not need variables of the class, but makes sense to be encapsulated within this class.
    def translate_clicked():
        source_lang, dest_lang = middleFrame.get_languages() # retrieve languages for translation
        translated_text.delete(1.0, tk.END) # clear text box prior to translation
        translator = Translator() # set up translator
        words = original_text.get(1.0, tk.END) # retrieve words for translation
        words = translator.translate(words, dest=dest_lang, src=source_lang)  # This function translates the text 
        words = words.text # extract the translated text which exists in the attribute text
        translated_text.insert(1.0, words) # This function is the output of the translated text to the screen  

    @staticmethod # this is a decorator. this function does not need variables of the class, but makes sense to be encapsulated within this class.
    def clear_clicked():
        original_text.delete(1.0, tk.END) # clear boxes when button is clicked
        translated_text.delete(1.0, tk.END) # global variables can be accessed

languages = googletrans.LANGUAGES
language_list = list(languages.values())
language_list =[x.title() for x in language_list] # list of all languages aquired
translateApp()
