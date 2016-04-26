from Tkinter import *
import os
from PIL import Image, ImageTk

class App:

    frame_list = []
    spell_omvar_list = []
    spell_om_list = []


    def __init__(self, master):
        self.main_frame = Frame(master, width=200, height=100)
        self.main_frame.grid(row=0, column=0, sticky=S+N+E+W)
        self.main_frame.columnconfigure(0, minsize=400)
        self.main_frame.rowconfigure(0, minsize=150)

        self.frame1 = Frame(self.main_frame, bg='white')
        self.frame1.grid(row=0, column=0, sticky='news')

        self.frame2 = Frame(self.main_frame, bg='white')
        self.frame2.grid(row=1, column=0, sticky=E+W)

        App.frame_list.append(self.frame1)

        add_spell_button = Button(self.frame2, text='Add Spell', command=self.add_spell, bg='white')
        add_spell_button.pack(side=RIGHT)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25,25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        page_label = Label(self.frame1, text='Page 1', bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        spell_label = Label(self.frame1, text='Spell 1:')
        spell_label.grid(row=2,column=0, sticky=W)

        spell_optionmenu_var = StringVar(self.frame1)
        spell_optionmenu_var.set('one') # default value
        App.spell_omvar_list.append(spell_optionmenu_var)

        spell_optionmenu = OptionMenu(self.frame1, spell_optionmenu_var, 'one','two','three')
        spell_optionmenu.grid(row=2, column=1, sticky=W)
        spell_optionmenu.config(width=15)
        App.spell_om_list.append(spell_optionmenu)

    def add_spell(self):

        spell_number = 4 - (len(App.spell_omvar_list) % 4)

        if spell_number == 4:
            current_frame = App.frame_list[(len(App.frame_list) - 1)]
            frame = Frame(self.main_frame, bg='white')
            frame.grid(row=0, column=0, sticky=S+N+E+W)
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)
            frame.columnconfigure(2, weight=1)
            frame.rowconfigure(0, weight=1)
            frame.rowconfigure(1, weight=1)

            next_page_button = Button(current_frame, image=self.next_image, command= lambda: self.next_frame(current_frame))
            next_page_button.grid(row=0, column=2, sticky=N+E)

            page_label = Label(frame, text='Page %r' % (len(App.frame_list)+1), bg='white')
            page_label.grid(row=0, column=1, sticky=N)

            previous_page_button = Button(frame, image=self.previous_image, command= lambda: self.previous_frame(current_frame))
            previous_page_button.grid(row=0, column=0, sticky=N+W)

            App.frame_list.append(frame)
            frame.lift()

        current_frame = App.frame_list[(len(App.frame_list) - 1)]

        spell_label = Label(current_frame, text='Spell %r:' % (len(App.spell_omvar_list) + 1))
        spell_label.grid(row=(spell_number+1),column=0, sticky=W)

        spell_optionmenu_var = StringVar(current_frame)
        spell_optionmenu_var.set('one') # default value
        App.spell_omvar_list.append(spell_optionmenu_var)

        spell_optionmenu = OptionMenu(current_frame, spell_optionmenu_var, 'one','two','three')
        spell_optionmenu.grid(row=(spell_number+1), column=1, sticky=W)
        spell_optionmenu.config(width=15)
        App.spell_om_list.append(spell_optionmenu)

    def previous_frame(self, current_frame):
        frame = App.frame_list.index(current_frame)
        App.frame_list[frame].lift()


    def next_frame(self, current_frame):
        frame = App.frame_list.index(current_frame)
        next_frame = frame + 1
        App.frame_list[next_frame].lift()

root = Tk()
A = App(root)
root.mainloop()