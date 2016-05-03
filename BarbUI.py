from Tkinter import *
import ttk
import os
from PIL import Image, ImageTk
import dictionaries

class App:

    class_level = 20
    character_class = 'Barbarian'

    abilities_frame_list = []
    abilities_checkvar_list = []

    def __init__(self, master):
        self.main_frame = LabelFrame(master, text='Abilities', width=200, height=100)
        self.main_frame.grid(row=0, column=0, sticky=S+N+E+W)
        self.main_frame.columnconfigure(0, minsize=400)
        self.main_frame.rowconfigure(0, minsize=150)

        self.frame1 = Frame(self.main_frame)
        self.frame1.grid(row=0, column=0, sticky='news')
        self.frame1.columnconfigure(2, weight=1)

        App.abilities_frame_list.append(self.frame1)

        page_label = Label(self.frame1, text='Page 1')
        page_label.grid(row=0, column=1, sticky=N)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25, 25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)


        for key, value in dictionaries.abilities_dict[App.character_class].iteritems():
            if int(key) < App.class_level:
                for item in value:
                    ability_count = len(App.abilities_checkvar_list) % 10

                    if ability_count == 0 and len(App.abilities_checkvar_list) != 0:
                        current_frame = App.abilities_frame_list[(len(App.abilities_frame_list) - 1)]

                        frame = Frame(self.main_frame)
                        frame.grid(row=0, column=0, sticky='news')
                        frame.columnconfigure(2, weight=1)

                        next_page_button = Button(current_frame, image=self.next_image,
                                                      command=lambda: self.next_frame(current_frame))
                        next_page_button.grid(row=0, column=2, sticky=N + E)

                        page_label = Label(frame, text='Page %r' % (len(App.abilities_frame_list)+1))
                        page_label.grid(row=0, column=1, sticky=N)

                        previous_page_button = Button(frame, image=self.previous_image,
                                                          command=lambda: self.previous_frame(current_frame))
                        previous_page_button.grid(row=0, column=0, sticky=N + W)

                        App.abilities_frame_list.append(frame)
                        frame.lift()

                    top_frame = App.abilities_frame_list[(len(App.abilities_frame_list) - 1)]

                    checkvar = IntVar()
                    ability_check = Checkbutton(top_frame, text=item, variable=checkvar)

                    App.abilities_checkvar_list.append(ability_check)
                    row_count = 2 + ((len(App.abilities_checkvar_list)-1) % 5)
                    column_count = ((len(App.abilities_checkvar_list)-1)/5) % 2

                    ability_check.grid(row=row_count, column=column_count, sticky=W)

    def previous_frame(self, current_frame):
        current_frame.lift()

    def next_frame(self, current_frame):
        try:
            frame = App.abilities_frame_list.index(current_frame)
            next_frame = frame + 1
            App.abilities_frame_list[next_frame].lift()
        except IndexError:
            pass




root = Tk()
A = App(root)
root.mainloop()