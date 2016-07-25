import Tkinter as tk
import ttk
import os
from PIL import Image, ImageTk
import dictionaries


class Description(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.desc_can = tk.Canvas(self,bg='white')
        self.desc_can.grid(sticky='news')

# self.row/column_configure is fucking mindblowing, holyshit!
# really great way to understand how class inheritance works

class Feats(tk.Frame):
    
    feat_list = []
    feat_check_list = []
    feat_butt_list = []
    feat_frame_list = []

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid_columnconfigure(0,weight=2)
        self.grid_rowconfigure(0,weight=2)
        self.LF_Feats = tk.LabelFrame(self, text='Feats')
        self.LF_Feats.grid(row=0, column=0, sticky='news')
        self.LF_Feats.grid_columnconfigure(2,weight=1)
        Feats.feat_frame_list.append(self.LF_Feats)

        page_label = tk.Label(self.LF_Feats, text='Page 1')
        page_label.grid(row=0, column=0, columnspan=3, sticky='NEW')

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25, 25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        for key, value in dictionaries.feats_dict.iteritems():
            self.feat_list.append(key)

        self.Butt_Add_Feat = tk.Button(self.LF_Feats,text='Add ',command=lambda: self.add_feat(self.Combo_Add_Feat))
        self.Butt_Add_Feat.grid(row=1,column=0,sticky='W',padx=2)

        self.Combo_Add_Feat = AutocompleteCombobox(self.LF_Feats,width=40)
        self.Combo_Add_Feat.set_completion_list(Feats.feat_list)
        self.Combo_Add_Feat.grid(row=1,column=1,sticky='W',padx=2)

    def add_feat(self,feat):
        if feat.get().lower() in (x.lower() for x in Feats.feat_list) \
            and feat.get().lower() not in (y.cget("text").lower() for y in Feats.feat_check_list):

            combo_info = feat.grid_info()
            current_frame = Feats.feat_frame_list[(len(Feats.feat_frame_list)-1)]

            checkvar = tk.IntVar()
            feat_check = tk.Checkbutton(current_frame, text=feat.get(), variable=checkvar)
            feat_check.grid(row=combo_info["row"],column=1,sticky='W',padx=2)
            Feats.feat_check_list.append(feat_check)

            Butt_Remove_Feat = tk.Button(current_frame,command = lambda: self.remove_feat(feat_check))
            Butt_Remove_Feat.grid(row=combo_info["row"],column=0,sticky='W',padx=2)
            Feats.feat_butt_list.append(Butt_Remove_Feat)

            row_shift = len(Feats.feat_check_list) % 5
            if row_shift == 0 and len(Feats.feat_check_list) != 0:
                self.new_frame()
                self.Butt_Add_Feat.grid_forget()
                self.Combo_Add_Feat.grid_forget()
                top_frame = Feats.feat_frame_list[(len(Feats.feat_frame_list) - 1)]

                self.Butt_Add_Feat = tk.Button(top_frame,text='Add ',command=lambda: self.add_feat(self.Combo_Add_Feat))
                self.Butt_Add_Feat.grid(row=row_shift+1,column=0,sticky='W',padx=2)
                self.Combo_Add_Feat = AutocompleteCombobox(top_frame,width=40)
                self.Combo_Add_Feat.set_completion_list(Feats.feat_list)
                self.Combo_Add_Feat.grid(row=1,column=1,sticky='W',padx=2)                
            else:
                self.Butt_Add_Feat.grid(row=row_shift+2,column=0,sticky='W', padx=2)
                feat.grid(row=row_shift+2,column=1,sticky='W', padx=2)
 
    def remove_feat(self,feat):
        feat_info = feat.grid_info()
        feat_index = Feats.feat_check_list.index(feat)
        feat_frame = feat_info["in"]
        feat_frame_index = Feats.feat_frame_list.index(feat_frame)

        for item in Feats.feat_check_list:
            item_info = item.grid_info()
            item_index = Feats.feat_check_list.index(item)
            item_frame = item_info["in"]
            item_frame_index = Feats.feat_frame_list.index(item_frame)
            button = Feats.feat_butt_list[item_index]
            button_info = button.grid_info()
            if item_index > feat_index:
                if item_index % 5 == 0:

                    item_frame = Feats.feat_frame_list[item_frame_index-1]
                    item_text = item.cget('text')
                    item_var = item.cget('variable')
                    button_command = button.cget('command')

                    item.grid_forget()
                    button.grid_forget()

                    new_item = tk.Checkbutton(item_frame, text=item_text, variable=item_var)
                    new_item.grid(row=6,column=1,sticky='W', padx=2)
                    new_button = tk.Button(item_frame,command=lambda: self.remove_feat(new_item))
                    new_button.grid(row=6,column=0,sticky='W',padx=2)

                    Feats.feat_check_list[item_index] = new_item
                    Feats.feat_butt_list[item_index] = new_button

                else:
                    button.grid(row=int(button_info['row'])-1,column=0,sticky='W',padx=2)
                    item.grid(row=int(item_info['row'])-1,column=1,sticky='W',padx=2)
       
        feat.grid_forget()
        Feats.feat_butt_list[feat_index].grid_forget()
        Feats.feat_check_list.remove(feat)
        Feats.feat_butt_list.remove(Feats.feat_butt_list[feat_index])

        row_shift = (len(Feats.feat_check_list) % 5)
        top_frame = Feats.feat_frame_list[(len(Feats.feat_frame_list) - 2)]
        if row_shift == 4:
            self.Combo_Add_Feat = AutocompleteCombobox(top_frame,width=40)
            self.Combo_Add_Feat.set_completion_list(Feats.feat_list)
            self.Combo_Add_Feat.grid(row=6,column=1,sticky='W',padx=2)
            self.Butt_Add_Feat = tk.Button(top_frame,text='Add ',command=lambda: self.add_feat(self.Combo_Add_Feat))
            self.Butt_Add_Feat.grid(row=6,column=0,sticky='W',padx=2)

            destroy_frame = Feats.feat_frame_list[len(Feats.feat_frame_list)-1]
            Feats.feat_frame_list.remove(destroy_frame)
            destroy_frame.destroy()
        else:
            self.Butt_Add_Feat.grid(row=row_shift+2,column=0,sticky='W', padx=2)
            self.Combo_Add_Feat.grid(row=row_shift+2,column=1,sticky='W', padx=2)

    def new_frame(self):
        current_frame = Feats.feat_frame_list[(len(Feats.feat_frame_list) - 1)]

        frame = tk.LabelFrame(self)
        frame.grid(row=0, column=0, sticky='news')
        frame.columnconfigure(2, weight=1)

        next_page_button = tk.Button(current_frame, image=self.next_image,
                                        command=lambda: self.next_frame(current_frame))
        next_page_button.grid(row=0, column=2, sticky='NE')

        page_label = tk.Label(frame, text='Page %r' % (len(Feats.feat_frame_list)+1))
        page_label.grid(row=0, column=0, columnspan=3, sticky='NEW')

        previous_page_button = tk.Button(frame, image=self.previous_image,
                                            command=lambda: self.previous_frame(current_frame))
        previous_page_button.grid(row=0, column=0, sticky='NW')

        Feats.feat_frame_list.append(frame)
        frame.lift()

    def previous_frame(self, current_frame):
        current_frame.lift()

    def next_frame(self, current_frame):
        try:
            frame = Feats.feat_frame_list.index(current_frame)
            next_frame = frame + 1
            Feats.feat_frame_list[next_frame].lift()
        except IndexError:
            pass


class Character(tk.Frame):

    stat_list = ['Str: ', 'Dex: ', 'Con : ', 'Int: ', 'Wis: ', 'Cha: ']
    stat_entry_list = []

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.LF_Character_Stats = tk.LabelFrame(self, text='Stats')
        self.LF_Character_Stats.grid(row=0, column=0, sticky='news')

        self.Class_Label = tk.Label(self.LF_Character_Stats, text='Class: ')
        self.Class_Label.grid(row=0, column=0, sticky='W')

        self.Class_Combobox_var = tk.StringVar(self.LF_Character_Stats)
        self.Class_Combobox_var.set(' ')

        self.Class_Combobox = ttk.Combobox(self.LF_Character_Stats)
        self.Class_Combobox.grid(row=0, column=1, columnspan=4, sticky='W', padx=2, pady=3)
        self.Class_Combobox.config(width=20)

        for i in range(6):
            self.Stat_Label = tk.Label(self.LF_Character_Stats, text=Character.stat_list[i])
            self.Stat_Label.grid(row=((i%3)+1), column=((i/3)*3), padx=2, pady=3)

            self.Stat_Entry = tk.Entry(self.LF_Character_Stats)
            self.Stat_Entry.grid(row=((i%3)+1), column=(((i/3)*3)+1), sticky='W',padx=2, pady=3)
            self.Stat_Entry.configure(width=5)

            Character.stat_entry_list.append(self.Stat_Entry)

class Abilities(tk.Frame):

    class_level = 20
    character_class = 'Barbarian'

    abilities_frame_list = []
    abilities_checkvar_list = []

    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.grid_columnconfigure(0,weight=3)
        self.grid_rowconfigure(0,weight=3)
        self.main_frame = tk.LabelFrame(self, text='Abilities')
        self.main_frame.grid(row=0, column=0, sticky='news')
        self.main_frame.grid_columnconfigure(0,weight=2)
        self.main_frame.grid_rowconfigure(0,weight=2)

        self.frame1 = tk.Frame(self.main_frame)
        self.frame1.grid(row=0, column=0, sticky='news')
        self.frame1.columnconfigure(2, weight=1)

        Abilities.abilities_frame_list.append(self.frame1)

        page_label = tk.Label(self.frame1, text='Page 1')
        page_label.grid(row=0, column=0, columnspan=3, sticky='NEW')

        self.next_image_path = os.path.join(os.getcwd(), 'Pictures/right_arrow.jpg')
        next_image = Image.open(self.next_image_path).resize((25, 25), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(next_image)

        self.previous_image_path = os.path.join(os.getcwd(), 'Pictures/left_arrow.jpg')
        previous_image = Image.open(self.previous_image_path).resize((25, 25), Image.ANTIALIAS)
        self.previous_image = ImageTk.PhotoImage(previous_image)

        for key, value in dictionaries.abilities_dict[Abilities.character_class]['Standard Abilities'].iteritems():
            if int(key) <= Abilities.class_level:
                for item in value:
                    ability_count = len(Abilities.abilities_checkvar_list) % 10

                    if ability_count == 0 and len(Abilities.abilities_checkvar_list) != 0:
                        self.new_frame()

                    top_frame = Abilities.abilities_frame_list[(len(Abilities.abilities_frame_list) - 1)]

                    checkvar = tk.IntVar()
                    ability_check = tk.Checkbutton(top_frame, text=item, variable=checkvar)

                    Abilities.abilities_checkvar_list.append(ability_check)
                    row_count = 2 + ((len(Abilities.abilities_checkvar_list)-1) % 5)
                    column_count = ((len(Abilities.abilities_checkvar_list)-1)/5) % 2

                    ability_check.grid(row=row_count, column=column_count, sticky='W')

        for path, key in dictionaries.abilities_dict[Abilities.character_class]['Paths'].iteritems():        
            for key, value in dictionaries.abilities_dict[Abilities.character_class]['Paths'][path].iteritems():
                if int(key) <= Abilities.class_level:
                    for item in value:
                        ability_count = len(Abilities.abilities_checkvar_list) % 10

                        if ability_count == 0 and len(Abilities.abilities_checkvar_list) != 0:
                            self.new_frame()

                        top_frame = Abilities.abilities_frame_list[(len(Abilities.abilities_frame_list) - 1)]

                        checkvar = tk.IntVar()
                        ability_check = tk.Checkbutton(top_frame, text=item, variable=checkvar)

                        Abilities.abilities_checkvar_list.append(ability_check)
                        row_count = 2 + ((len(Abilities.abilities_checkvar_list)-1) % 5)
                        column_count = ((len(Abilities.abilities_checkvar_list)-1)/5) % 2

                        ability_check.grid(row=row_count, column=column_count, sticky='W')

        self.frame1.lift()

    def new_frame(self):
        current_frame = Abilities.abilities_frame_list[(len(Abilities.abilities_frame_list) - 1)]

        frame = tk.Frame(self.main_frame)
        frame.grid(row=0, column=0, sticky='news')
        frame.columnconfigure(2, weight=1)

        next_page_button = tk.Button(current_frame, image=self.next_image,
                                        command=lambda: self.next_frame(current_frame))
        next_page_button.grid(row=0, column=2, sticky='NE')

        page_label = tk.Label(frame, text='Page %r' % (len(Abilities.abilities_frame_list)+1))
        page_label.grid(row=0, column=0, columnspan=3, sticky='NEW')

        previous_page_button = tk.Button(frame, image=self.previous_image,
                                            command=lambda: self.previous_frame(current_frame))
        previous_page_button.grid(row=0, column=0, sticky='NW')

        Abilities.abilities_frame_list.append(frame)
        frame.lift()

    def previous_frame(self, current_frame):
        current_frame.lift()

    def next_frame(self, current_frame):
        try:
            frame = Abilities.abilities_frame_list.index(current_frame)
            next_frame = frame + 1
            Abilities.abilities_frame_list[next_frame].lift()
        except IndexError:
            pass

class AutocompleteCombobox(ttk.Combobox):

    def set_completion_list(self, completion_list):
        """Use our completion list as our drop down selection menu, arrows move through menu."""
        self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list  # Setup our popup menu

    def autocomplete(self, delta=0):
        """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
        if delta: # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else: # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()): # Match case insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits=_hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0,tk.END)
            self.insert(0,self._hits[self._hit_index])
            self.select_range(self.position,tk.END)

    def handle_keyrelease(self, event):
        """event handler for the keyrelease event on this widget"""
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
        if event.keysym == "Left":
            if self.position < self.index(tk.END): # delete the selection
                self.delete(self.position, tk.END)
            else:
                self.position = self.position-1 # delete one character
                self.delete(self.position, tk.END)
        if event.keysym == "Right":
            self.position = self.index(tk.END) # go to end (no selection)
        if len(event.keysym) == 1:
            self.autocomplete()
        # No need for up/down, we'll jump to the popup
        # list at the position of the autocompletion