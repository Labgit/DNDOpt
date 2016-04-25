from Tkinter import *
import os
from PIL import Image, ImageTk

class App:

    frame_list = []
    page_number = 1

    def __init__(self, master):
        self.main_frame = Frame(master, width=200, height=100)
        self.main_frame.grid(row=0, column=0, sticky=S+N+E+W)
        self.main_frame.columnconfigure(0, minsize=200)
        self.main_frame.rowconfigure(0, minsize=100)

        self.frame1 = Frame(self.main_frame, bg='white')
        self.frame1.grid(row=0, column=0, sticky='news')
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)

        App.frame_list.append(self.frame1)

        add_page_button = Button(self.frame1, text='Add Page', command=self.add_page, bg='white')
        add_page_button.grid(row=1, columnspan=3, sticky=S)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25,25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        next_page_button = Button(self.frame1, image=self.next_image, command=lambda: self.frame_index(self.frame1))
        next_page_button.grid(row=0, column=2, sticky=N+E)

        page_label = Label(self.frame1, text='Page 1', bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        previous_page_button = Button(self.frame1)
        previous_page_button.grid(row=0, column=0, sticky=N+W)

    def add_page(self):
        App.page_number += 1

        frame = Frame(self.main_frame, bg='white')
        frame.grid(row=0, column=0, sticky=S+N+E+W)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        add_page_button = Button(frame, text='Add Page', command=self.add_page, bg='white')
        add_page_button.grid(row=1, columnspan=3, sticky=S)

        next_page_button = Button(frame, image=self.next_image)
        next_page_button.grid(row=0, column=2, sticky=N + E)

        page_label = Label(frame, text='Page %r' % App.page_number, bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        previous_page_button = Button(frame, image=self.previous_image)
        previous_page_button.grid(row=0, column=0, sticky=N + W)

        frame.lift()

    def frame_index(self, frame_var):
        print App.frame_list.index(frame_var)

root = Tk()
A = App(root)
root.mainloop()