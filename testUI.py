from Tkinter import *
import os
from PIL import Image, ImageTk

class App:

    frame_list = []

    def __init__(self, master):
        self.main_frame = Frame(master, width=200, height=100)
        self.main_frame.grid(row=0, column=0, sticky=S+N+E+W)
        self.main_frame.columnconfigure(0, minsize=400)
        self.main_frame.rowconfigure(0, minsize=150)

        self.frame1 = Frame(self.main_frame, bg='white')
        self.frame1.grid(row=0, column=0, sticky='news')

        self.frame2 = Frame(self.main_frame, bg='white')
        self.frame2.grid(row=0, column=0, stickcy=E+W)

        App.frame_list.append(self.frame1)

        add_page_button = Button(self.frame1, text='Add Page', command=self.add_page, bg='white')
        add_page_button.grid(row=1, columnspan=3, sticky=S)

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25,25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        page_label = Label(self.frame1, text='Page 1', bg='white')
        page_label.grid(row=0, column=1, sticky=N)

    def add_page(self):

        frame = Frame(self.main_frame, bg='white')
        frame.grid(row=0, column=0, sticky=S+N+E+W)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        current_frame = App.frame_list[(len(App.frame_list) - 1)]

        next_page_button = Button(current_frame, image=self.next_image, command= lambda: self.next_frame(current_frame))
        next_page_button.grid(row=0, column=2, sticky=N+E)

        add_page_button = Button(frame, text='Add Page', command=self.add_page, bg='white')
        add_page_button.grid(row=1, columnspan=3, sticky=S)

        page_label = Label(frame, text='Page %r' % (len(App.frame_list)+1), bg='white')
        page_label.grid(row=0, column=1, sticky=N)

        previous_page_button = Button(frame, image=self.previous_image, command= lambda: self.previous_frame(current_frame))
        previous_page_button.grid(row=0, column=0, sticky=N+W)

        App.frame_list.append(frame)
        frame.lift()

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