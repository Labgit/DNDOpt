from Tkinter import *
import ttk
import os
from PIL import Image, ImageTk

class App:

    spell_frame_list = []
    spell_label_list = []
    spell_combobox_list = []
    spell_om_list = []


    def __init__(self, master):
        self.main_frame = Frame(master, width=200, height=100)
        self.main_frame.grid(row=0, column=0, sticky=S+N+E+W)
        self.main_frame.columnconfigure(0, minsize=400)
        self.main_frame.rowconfigure(0, minsize=150)

        self.frame1 = Frame(self.main_frame, bg='white')
        self.frame1.grid(row=0, column=0, sticky='news')
        self.frame1.columnconfigure(1, weight=1)

        self.frame2 = Frame(self.main_frame, bg='white')
        self.frame2.grid(row=1, column=0, sticky=E+W)

        App.spell_frame_list.append(self.frame1)

        add_spell_button = Button(self.frame2, text='Add Spell', command=self.add_spell, bg='white')
        add_spell_button.pack(side=RIGHT)

        remove_spell_button = Button(self.frame2, text='Remove Last Spell', command=self.remove_spell, bg='white')
        remove_spell_button.pack(side=LEFT)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25,25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        page_label = Label(self.frame1, text='Page 1', bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        spell_label = Label(self.frame1, text='Spell 1:', bg='white')
        spell_label.grid(row=2, column=0, sticky=W)
        App.spell_label_list.append(spell_label)

        spell_combobox_var = StringVar(self.frame1)
        spell_combobox_var.set(' ') # default value
        App.spell_combobox_list.append(spell_combobox_var)

        spell_combobox = ttk.Combobox(self.frame1, textvariable= spell_combobox_var)
        spell_combobox.grid(row=2, column=1, sticky=E+W)
        App.spell_om_list.append(spell_combobox)

        print_var = Button(self.frame2, text='print variables', command= self.print_var)
        print_var.pack()

    def add_spell(self):

        spell_number = (len(App.spell_combobox_list) % 4) + 1
        current_frame = App.spell_frame_list[(len(App.spell_frame_list) - 1)]

        if spell_number == 1:
            frame = Frame(self.main_frame, bg='white')
            frame.grid(row=0, column=0, sticky='news')
            frame.columnconfigure(1, weight=1)

            next_page_button = Button(current_frame, image=self.next_image, command= lambda: self.next_frame(current_frame))
            next_page_button.grid(row=0, column=2, sticky=N+E)

            page_label = Label(frame, text='Page %r' % (len(App.spell_frame_list) + 1), bg='white')
            page_label.grid(row=0, column=1, sticky=N)

            previous_page_button = Button(frame, image=self.previous_image, command= lambda: self.previous_frame(current_frame))
            previous_page_button.grid(row=0, column=0, sticky=N+W)

            App.spell_frame_list.append(frame)
            frame.lift()

        top_frame = App.spell_frame_list[(len(App.spell_frame_list) - 1)]

        spell_label = Label(top_frame, text='Spell %r:' % (len(App.spell_combobox_list) + 1), bg='white')
        spell_label.grid(row=(spell_number+1), column=0, sticky=W)
        App.spell_label_list.append(spell_label)

        spell_combobox_var = StringVar(top_frame)
        spell_combobox_var.set(' ') # default value
        App.spell_combobox_list.append(spell_combobox_var)

        spell_combobox = ttk.Combobox(top_frame, textvariable= spell_combobox_var)
        spell_combobox.grid(row=(spell_number+1), column=1, sticky=E+W)
        App.spell_om_list.append(spell_combobox)

    def previous_frame(self, current_frame):
        frame = App.spell_frame_list.index(current_frame)
        App.spell_frame_list[frame].lift()


    def next_frame(self, current_frame):
        frame = App.spell_frame_list.index(current_frame)
        next_frame = frame + 1
        App.spell_frame_list[next_frame].lift()

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

root = Tk()
A = App(root)
root.mainloop()