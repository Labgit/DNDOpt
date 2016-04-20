from Tkinter import *


class ElliesButton:

    def __init__(self, master):
        main_frame = Frame(master)
        main_frame.pack()
        main_frame.columnconfigure(0, minsize=400)
        main_frame.rowconfigure(0, minsize=200)
        main_frame.rowconfigure(1, minsize=200)


        top_menu = Menu(master) # this can't be a frame, it has to be master window
        master.config(menu=top_menu)

        top_menu.add_cascade(label='File')
        top_menu.add_cascade(label='Edit')

#======= Initial Sub-Frames ===========================================================================================#

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

#======= Second Sub-Frames ============================================================================================#

        LF1_Frame1 = Frame(Lframe_1, padx=5, pady=5)
        LF1_Frame1.grid(row=0, column=0, sticky=N+W+E)

        LF2_Frame1 = Frame(Lframe_2, padx=5, pady=5)
        LF2_Frame1.grid(row=0, column=0, sticky=S+E+N+W)


        LF1_Frame2 = Frame(Lframe_1)
        LF1_Frame2.grid(row=1,column=0, sticky=N+S+E+W)

        LF2_Frame2 = Frame(Lframe_2)
        LF2_Frame2.grid(row=1,column=0, sticky=W+E)


# ======= Adding Widgets=========#

        LF1_Label1 = Label(LF1_Frame1, text='Class:')
        LF1_Label1.grid(row=0,column=0, sticky=W)

        LF1_OM1var = StringVar(master)
        LF1_OM1var.set('one') # default value
        LF1_OM1 = OptionMenu(LF1_Frame1, LF1_OM1var, 'one','two','three')
        LF1_OM1.grid(row=0, column=1, sticky=W)
        LF1_OM1.config(width=15)

        LF1_Label2 = Label(LF1_Frame2, text='Str: ')
        LF1_Label2.grid(row=0, column=0, sticky=N+W)
        LF1_Entry1 = Entry(LF1_Frame2)
        LF1_Entry1.config(width=10)
        LF1_Entry1.grid(row=0, column=1)

        LF2_Label1 = Label(LF2_Frame1, text='Spell:')
        LF2_Label1.grid(row=0,column=0, sticky=N+W)

        LF2_OM1var = StringVar(master)
        LF2_OM1var.set('one') # default value
        LF2_OM1 = OptionMenu(LF2_Frame1, LF2_OM1var, 'one','two','three')
        LF2_OM1.grid(row=0, column=1, sticky=N+W)
        LF2_OM1.config(width=15)

        LF2F2_AddSpell = Button(LF2_Frame2, text='Add Spell')
        LF2F2_AddSpell.pack(side=RIGHT)

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