from tkinter import *
from tkinter.ttk import *


class ElliesButton:

    def __init__(self, master):
        main_frame = Frame(master)
        main_frame.pack()

        top_menu = Menu(master) # this can't be a frame, it has to be master window
        master.config(menu=top_menu)

        top_menu.add_cascade(label='File')
        top_menu.add_cascade(label='Edit')

#======= Initial Sub-Frames ========================================================================================== #

    # ===== Notebook Frames ========================================================================================== #
    
        NBook = Notebook(main_frame)
        NBF1_Character = Frame(NBook)
        NBF2_Enemy = Frame(NBook)
        
        NBook.add(NBF1_Character, text='Character', width=400, height=400)
        NBook.add(NBF1_Enemy, text='Enemy', width=400, height=400)
    
        Lframe_1 = LabelFrame(main_frame, text = 'Frame 1', relief=SUNKEN, borderwidth=3, padx=5, pady=5)
        Lframe_1.grid(row=0,column=0, sticky=S+E+N+W)
        Lframe_1.columnconfigure(0, weight=1)
        Lframe_1.rowconfigure(1,weight=1) #edit, take a look at later 4/20

        Lframe_2 = LabelFrame(main_frame, text = 'Frame 2', relief=SUNKEN, borderwidth= 3, padx=5, pady=5)
        Lframe_2.grid(row=1, column=0, sticky=S+E+N+W)
        Lframe_2.columnconfigure(0, weight=1)
        Lframe_2.rowconfigure(0, weight=1)

        Lframe_3 = LabelFrame(main_frame, text = 'Frame 3', relief=SUNKEN, borderwidth= 3, padx=5, pady=5)
        Lframe_3.grid(row=2, column=0, sticky=S+E+N+W)

        Lframe_4 = LabelFrame(main_frame, text = 'Frame 4', width=800, height=400, relief=SUNKEN, borderwidth= 3, padx=5, pady=5)
        Lframe_4.grid(row=0, column=1, columnspan=4, rowspan=3, sticky=S+E+N+W)

# ===== Second Sub-Frames ============================================================================================#

        LF1_Frame1 = Frame(Lframe_1, padx=5, pady=5)
        LF1_Frame1.grid(row=0, column=0, sticky=N+W+E)

        LF2_Frame1 = Frame(Lframe_2, padx=5, pady=5)
        LF2_Frame1.grid(row=0, column=0, sticky=S+E+N+W)


        LF1_Frame2 = Frame(Lframe_1)
        LF1_Frame2.grid(row=1,column=0, sticky=N+S+E+W)

        LF2_Frame2 = Frame(Lframe_2)
        LF2_Frame2.grid(row=1,column=0, sticky=W+E)


# ===== Adding Widgets ================================================================================================== #

    # ===== Class OptionMenu / LF1_Frame1 stuff ========================================================================= #
    
        LF1_Label1 = Label(LF1_Frame1, text='Class:')
        LF1_Label1.grid(row=0,column=0, sticky=W)

        LF1_OM1var = StringVar(master)
        LF1_OM1var.set('one') # default value
        LF1_OM1 = OptionMenu(LF1_Frame1, LF1_OM1var, 'one','two','three')
        LF1_OM1.grid(row=0, column=1, sticky=W)
        LF1_OM1.config(width=15)
        
        LF1_RandomStats = Button(LF1_Frame1, text='Randomize Stats')
        LF1_RandomStats.grid(row=0, column=2, sticky=E)
        
        LF1_DefaultStats = Button(LF1_Frame1, text='Default Stats')
        LF1_DefaultStats.grid(row=0, column=3, sticky=E)
    
    # ===== Stats Frame 1 =============================================================================================== #
    
        LF1_Label_Str = Label(LF1_Frame2, text='Str: ')
        LF1_Label_Str.grid(row=0, column=0, sticky=N+W)
        LF1_Entry_Str = Entry(LF1_Frame2)
        LF1_Entry_Str.config(width=5)
        LF1_Entry_Str.grid(row=0, column=1)

        LF1_Label_Dex = Label(LF1_Frame2, text='Dex: ')
        LF1_Label_Dex.grid(row=1, column=0, sticky=N+W)
        LF1_Entry_Dex = Entry(LF1_Frame2)
        LF1_Entry_Dex.config(width=5)
        LF1_Entry_Dex.grid(row=1, column=1)

        LF1_Label_Con = Label(LF1_Frame2, text='Con: ')
        LF1_Label_Con.grid(row=2, column=0, sticky=N+W)
        LF1_Entry_Con = Entry(LF1_Frame2)
        LF1_Entry_Con.config(width=5)
        LF1_Entry_Con.grid(row=2, column=1)
        
        LF1_Label_Int = Label(LF1_Frame2, text='Int: ')
        LF1_Label_Int.grid(row=3, column=0, sticky=N+W)
        LF1_Entry_Int = Entry(LF1_Frame2)
        LF1_Entry_Int.config(width=5)
        LF1_Entry_Int.grid(row=3, column=1)

        LF1_Label_Wis = Label(LF1_Frame2, text='Wis: ')
        LF1_Label_Wis.grid(row=4, column=0, sticky=N+W)
        LF1_Entry_Wis = Entry(LF1_Frame2)
        LF1_Entry_Wis.config(width=5)
        LF1_Entry_Wis.grid(row=4, column=1)

        LF1_Label_Cha = Label(LF1_Frame2, text='Cha: ')
        LF1_Label_Cha.grid(row=5, column=0, sticky=N+W)
        LF1_Entry_Cha = Entry(LF1_Frame2)
        LF1_Entry_Cha.config(width=5)
        LF1_Entry_Cha.grid(row=5, column=1)
        
    # ===== Spell OptionMenu (Frame2) ================================================================================== #
        
        LF2_Label_Spell = Label(LF2_Frame1, text='Spell:')
        LF2_Label_Spell.grid(row=0,column=0, sticky=N+W)
    
        LF2_OM_Spellvar = StringVar(master)
        LF2_OM_Spellvar.set('one') # default value
        LF2_OMSpell = OptionMenu(LF2_Frame1, LF2_OMSpellvar, 'one','two','three')
        LF2_OMSpell.grid(row=0, column=1, sticky=N+W)
        LF2_OMSpell.config(width=15)

        LF2F2_AddSpell = Button(LF2_Frame2, text='Add Spell')
        LF2F2_AddSpell.pack(side=RIGHT)

    # ===== Third LabelFrame Options =================================================================================== #
        # This will most likely become a Frame for Physical attacks.
        
        LF3_C1var = IntVar()
        LF3_C1button = Checkbutton(Lframe_3, text='Option 1', variable=LF3_C1var)
        LF3_C1button.grid(row=0,column=0)

        LF3_C2var = IntVar()
        LF3_C2button = Checkbutton(Lframe_3, text='Option 2', variable=LF3_C2var)
        LF3_C2button.grid(row=1,column=0)

        LF3_C3var = IntVar()
        LF3_C3button = Checkbutton(Lframe_3, text='Option 3', variable=LF3_C3var)
        LF3_C3button.grid(row=2,column=0)

        LF3_C4var = IntVar()
        LF3_C4button = Checkbutton(Lframe_3, text='Option 4', variable=LF3_C4var)
        LF3_C4button.grid(row=4,column=0)

        LF3_C5var = IntVar()
        LF3_C5button = Checkbutton(Lframe_3, text='Option 5', variable=LF3_C5var)
        LF3_C5button.grid(row=5,column=0)

        LF3_C6var = IntVar()
        LF3_C6button = Checkbutton(Lframe_3, text='Option 6', variable=LF3_C6var)
        LF3_C6button.grid(row=0,column=1)

    def printMessage(self):
        print 'This is a message'


root = Tk()
E = ElliesButton(root) #root is treated as master, also, anytime we want to use anything
                       # from a class, we have to create an object for it.
root.mainloop()
