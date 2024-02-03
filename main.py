# pip install googletrans - this is used to install google translate
# pip install textblob - this is to ensure pyou have textblob, is required for this code

from tkinter import*
import googletrans
from googletrans import Translator
from tkinter import ttk,messagebox

root = Tk() # This command opens the the tkinter pop up box
root.title('Assignment 3 - Question 1')
#root.iconbitmap('') #insert the icon of charles darwin university if possible
root.geometry("1000x320") # size of the pop up box

# Below is how we have defined the functions of the buttons
def clear(): 
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

def get_languages():
    global original_combo, dest_lang
    source_lang = original_combo.get()
    dest_lang = translated_combo.get()
    return (source_lang, dest_lang)

def translate_it():
    source_lang, dest_lang = get_languages()
    # Delete any previous translations
    translated_text.delete(1.0, END)
    # We had to add a try box (add the reason why)
    try:
        translator = Translator()

        # This turns original text into a text blob
        words = original_text.get(1.0, END)

        # This function translates the text 
        words = translator.translate(words, dest=dest_lang, src=source_lang)
        words = words.text

        # This function is the output of the translated text to the screen  
        translated_text.insert(1.0, words)

        # This is for the error of the translator if the translator cant translate a sentence 
    except Exception as e:
        messagebox.showerror("Translator", e)
                             

languages = googletrans.LANGUAGES

language_list = list(languages.values())
language_list =[x.title() for x in language_list]

# Below is how we have added labels to the text boxes
text = Label(root, text = "Translated text",  font = "Times 15 bold")
text.grid(row =0, column=3)

text = Label(root, text = "Language input text",  font = "Times 15 bold")
text.grid(row=0, columnspan=2)

text = Label(root, text = "Select Input Language")
text.grid(sticky=W, row=2, column=0, padx=15)

text = Label(root, text = "Select Output Language")
text.grid(sticky=W, row=2, column=3, padx=15)

# text boxes
original_text = Text(root, height=10, width=40) # change box sizes to suit what we want to do
original_text.grid(row=1, columnspan=2, padx= 15) # column span brings the box across 2 columns

translated_text = Text(root, height=10, width=40) # change box sizes to suit what we want to do
translated_text.grid(row=1, column=3, padx= 15, pady= 5) # pady brings it down from the top and padx brings it from the left towards the middle

# activation button
translate_button = Button(root, text = "Translate", font= ("Times", 24 ), command=translate_it) # customise the font and size for the button
translate_button.grid(row=1, column=2, padx=5, pady= 5)

# combo boxes of both the original or input and the translated or output
original_combo = ttk.Combobox(root, width=20, value=language_list)
original_combo.current(21) # this brings up english as the first language as this is the most spoken language therefore we want it to be the default
original_combo.grid(sticky = W,row=2, column=1, pady= 5)

translated_combo = ttk.Combobox(root, width=20, value=language_list)
translated_combo.current(24) # this brings up the default language 
translated_combo.grid(sticky=E, row=2, column=3, padx= 25, pady= 5)

# refresh button to clear the text in the text boxes
Clear_button = Button(root, text="Refresh" , command=clear, width = 15) # properties of the clear button 
Clear_button.grid(row = 3, column = 2, pady = 20)

root.mainloop() # This command closes the the tkinter pop up box