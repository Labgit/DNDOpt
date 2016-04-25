from Tkinter import *
import os

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

        add_page_button = Button(self.frame1, text='Add Page', command=self.add_page, bg='white')
        add_page_button.grid(row=1, columnspan=3, sticky=S)

        next_page_button = Button(self.frame1)
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

        next_page_button = Button(frame)
        next_page_button.grid(row=0, column=2, sticky=N + E)

        page_label = Label(frame, text='Page %r' % App.page_number, bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        previous_page_button = Button(frame)
        previous_page_button.grid(row=0, column=0, sticky=N + W)

        frame.lift()

root = Tk()
A = App(root)
root.mainloop()