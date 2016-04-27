from Tkinter import *
import ttk
import os
from PIL import Image, ImageTk

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

# ========= Character Stats Label Frame ============================================================================== #

        self.LF_Character_Stats = LabelFrame(self.Ntab_Character, text='Stats')
        self.LF_Character_Stats.grid(row=0, column=0, sticky='news')

        self.Class_Label = Label(self.LF_Character_Stats, text='Class: ')
        self.Class_Label.grid(row=0, column=0, sticky=W)

        self.Class_Combobox_var = StringVar(self.LF_Character_Stats)
        self.Class_Combobox_var.set(' ')

        self.Class_Combobox = ttk.Combobox(self.LF_Character_Stats)
        self.Class_Combobox.grid(row=0, column=1, columnspan=4, sticky=W, padx=2, pady=3)
        self.Class_Combobox.config(width=20)

        self.Str_Stat_Label = Label(self.LF_Character_Stats, text='Str: ')
        self.Str_Stat_Label.grid(row=1, column=0, padx=2, pady=3)

        self.Dex_Stat_Label = Label(self.LF_Character_Stats, text='Dex: ')
        self.Dex_Stat_Label.grid(row=2, column=0, padx=2, pady=3)

        self.Con_Stat_Label = Label(self.LF_Character_Stats, text='Con: ')
        self.Con_Stat_Label.grid(row=3, column=0, padx=2, pady=3)

        self.Int_Stat_Label = Label(self.LF_Character_Stats, text='Int: ')
        self.Int_Stat_Label.grid(row=1, column=3, padx=2, pady=3)

        self.Wis_Stat_Label = Label(self.LF_Character_Stats, text='Wis: ')
        self.Wis_Stat_Label.grid(row=2, column=3, padx=2, pady=3)

        self.Cha_Stat_Label = Label(self.LF_Character_Stats, text='Cha: ')
        self.Cha_Stat_Label.grid(row=3, column=3, padx=2, pady=3)

        self.Str_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Str_Stat_Entry.grid(row=1, column=1, sticky=W, padx=2, pady=3)
        self.Str_Stat_Entry.configure(width=5)

        self.Dex_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Dex_Stat_Entry.grid(row=2, column=1, sticky=W, padx=2, pady=3)
        self.Dex_Stat_Entry.configure(width=5)

        self.Con_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Con_Stat_Entry.grid(row=3, column=1, sticky=W, padx=2, pady=3)
        self.Con_Stat_Entry.configure(width=5)

        self.Int_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Int_Stat_Entry.grid(row=1, column=4, sticky=W, padx=2, pady=3)
        self.Int_Stat_Entry.configure(width=5)

        self.Wis_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Wis_Stat_Entry.grid(row=2, column=4, sticky=W, padx=2, pady=3)
        self.Wis_Stat_Entry.configure(width=5)

        self.Cha_Stat_Entry = Entry(self.LF_Character_Stats)
        self.Cha_Stat_Entry.grid(row=3, column=4, sticky=W, padx=2, pady=3)
        self.Cha_Stat_Entry.configure(width=5)

# ========= Spells Label Frame ======================================================================================= #

        self.LF_Spells = LabelFrame(self.Ntab_Character, text='Spells')
        self.LF_Spells.grid(row=1, column=0, sticky='news')
        self.LF_Spells.rowconfigure(0, weight=1)
        self.LF_Spells.columnconfigure(0, weight=1)

        self.Spell_Subframe1 = Frame(self.LF_Spells)
        self.Spell_Subframe1.grid(row=0, column=0, sticky='news')
        self.Spell_Subframe1.columnconfigure(1, weight=1)

        self.Spell_Subframe2 = Frame(self.LF_Spells)
        self.Spell_Subframe2.grid(row=1, column=0, sticky=E + W)

        App.spell_frame_list.append(self.Spell_Subframe1)

        add_spell_button = Button(self.Spell_Subframe2, text='Add Spell', command=self.add_spell)
        add_spell_button.pack(side=RIGHT)

        remove_spell_button = Button(self.Spell_Subframe2, text='Remove Last Spell', command=self.remove_spell)
        remove_spell_button.pack(side=LEFT)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25, 25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        page_label = Label(self.Spell_Subframe1, text='Page 1')
        page_label.grid(row=0, column=1, sticky=N)

        spell_label = Label(self.Spell_Subframe1, text='Spell 1:')
        spell_label.grid(row=2, column=0, sticky=W)
        App.spell_label_list.append(spell_label)

        spell_combobox_var = StringVar(self.Spell_Subframe1)
        spell_combobox_var.set(' ')  # default value
        App.spell_combobox_list.append(spell_combobox_var)

        spell_combobox = ttk.Combobox(self.Spell_Subframe1, textvariable=spell_combobox_var)
        spell_combobox.grid(row=2, column=1, sticky=E + W)
        App.spell_om_list.append(spell_combobox)

        print_var = Button(self.Spell_Subframe2, text='print variables', command=self.print_var)
        print_var.pack()

# = User Interface Functions ========================================================================================= #

# ===== Spell Frame Functions ======================================================================================== #

    def add_spell(self):

        spell_number = (len(App.spell_combobox_list) % 4) + 1
        current_frame = App.spell_frame_list[(len(App.spell_frame_list) - 1)]

        if spell_number == 1:
            frame = Frame(self.LF_Spells)
            frame.grid(row=0, column=0, sticky='news')
            frame.columnconfigure(1, weight=1)

            next_page_button = Button(current_frame, image=self.next_image,
                                      command=lambda: self.next_frame(current_frame))
            next_page_button.grid(row=0, column=2, sticky=N + E)

            page_label = Label(frame, text='Page %r' % (len(App.spell_frame_list) + 1))
            page_label.grid(row=0, column=1, sticky=N)

            previous_page_button = Button(frame, image=self.previous_image,
                                          command=lambda: self.previous_frame(current_frame))
            previous_page_button.grid(row=0, column=0, sticky=N + W)

            App.spell_frame_list.append(frame)
            frame.lift()

        top_frame = App.spell_frame_list[(len(App.spell_frame_list) - 1)]

        spell_label = Label(top_frame, text='Spell %r:' % (len(App.spell_combobox_list) + 1))
        spell_label.grid(row=(spell_number + 1), column=0, sticky=W)
        App.spell_label_list.append(spell_label)

        spell_combobox_var = StringVar(top_frame)
        spell_combobox_var.set(' ')  # default value
        App.spell_combobox_list.append(spell_combobox_var)

        spell_combobox = ttk.Combobox(top_frame, textvariable=spell_combobox_var)
        spell_combobox.grid(row=(spell_number + 1), column=1, sticky=E + W)
        App.spell_om_list.append(spell_combobox)

    def previous_frame(self, current_frame):
        frame = App.spell_frame_list.index(current_frame)
        App.spell_frame_list[frame].lift()

    def next_frame(self, current_frame):
        try:
            frame = App.spell_frame_list.index(current_frame)
            next_frame = frame + 1
            App.spell_frame_list[next_frame].lift()
        except IndexError:
            pass

    def remove_spell(self):
        frame = App.spell_frame_list[-1]
        spell_label = App.spell_label_list[-1]
        spell_om = App.spell_om_list[-1]
        spell_omvar = App.spell_combobox_list[-1]
        spell_number = (len(App.spell_combobox_list) % 4)

        if len(App.spell_combobox_list) > 1:
            spell_label.destroy()
            spell_om.destroy()

            if spell_number == 1 and len(App.spell_frame_list) > 1:
                frame.destroy()
                App.spell_frame_list.pop()

            App.spell_label_list.pop()
            App.spell_om_list.pop()
            App.spell_combobox_list.pop()

        topframe = App.spell_frame_list[-1]
        topframe.lift()

    def print_var(self):
        for var in App.spell_combobox_list:
            print var.get()


# = Mainloop ========================================================================================================= #

root = Tk()
A = App(root)
root.mainloop()