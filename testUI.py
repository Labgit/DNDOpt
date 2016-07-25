from Tkinter import *
import ttk
import os
from PIL import Image, ImageTk
import dictionaries
import frame_classes


class App:

# = Class Variables ================================================================================================== #

    spell_frame_list = []
    spell_label_list = []
    spell_combobox_list = []
    spell_om_list = []

# = Initial Construction ============================================================================================= #

    def __init__(self, master):
        self.main_frame = Frame(master)
        self.main_frame.pack()

        self.top_menu = Menu(master) # this can't be a frame, it has to be master window
        master.config(menu= self.top_menu)

        self.top_menu.add_cascade(label='File')
        self.top_menu.add_cascade(label='Edit')

# = Initial Sub-Frames =============================================================================================== #

# ===== Notebook Frames ============================================================================================== #
    
        self.NBook = ttk.Notebook(self.main_frame)
        self.NBook.grid(row=0, column=0)

        self.Ntab_Character = Frame(self.NBook)
        self.Ntab_Character.rowconfigure(0, minsize=175)
        self.Ntab_Character.rowconfigure(1, minsize=175)
        self.Ntab_Character.rowconfigure(2, minsize=175)
        self.Ntab_Character.columnconfigure(0, minsize=400)

        self.Ntab_Attacks= Frame(self.NBook)
        self.Ntab_Attacks.rowconfigure(0, minsize=175)
        self.Ntab_Attacks.rowconfigure(1, minsize=175)
        self.Ntab_Attacks.rowconfigure(2, minsize=175)
        self.Ntab_Attacks .columnconfigure(0, minsize=400)

        self.Ntab_Enemy = Frame(self.NBook)
        self.Ntab_Enemy.rowconfigure(0, minsize=175)
        self.Ntab_Enemy.rowconfigure(1, minsize=175)
        self.Ntab_Enemy.rowconfigure(2, minsize=175)
        self.Ntab_Enemy.columnconfigure(0, minsize=400)

        self.Ntab_Options = Frame(self.NBook)
        self.Ntab_Options.rowconfigure(0, minsize=175)
        self.Ntab_Options.rowconfigure(1, minsize=175)
        self.Ntab_Options.rowconfigure(2, minsize=175)
        self.Ntab_Options.columnconfigure(0, minsize=400)

        self.NBook.add(self.Ntab_Character, text='Character')
        self.NBook.add(self.Ntab_Enemy, text='Enemy')
        self.NBook.add(self.Ntab_Options, text='Options')

# ===== Sub-Tab Frames =============================================================================================== #

        self.character_frame = frame_classes.Character(self.Ntab_Character)
        self.character_frame.grid(row=0, column=0,sticky='news')

        self.abilities_frame = frame_classes.Abilities(self.Ntab_Character)        
        self.abilities_frame.grid(row=1, column=0,sticky='news')

        self.feats_frame = frame_classes.Feats(self.Ntab_Character)
        self.feats_frame.grid(row=2, column=0, sticky='news')
# = Mainloop ========================================================================================================= #

root = Tk()
A = App(root)
root.mainloop()