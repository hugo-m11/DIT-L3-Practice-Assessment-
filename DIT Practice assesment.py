from tkinter import *

class People:
    def __init__(self, name, age, phone):
        self.name = name 
        self.age = age
        self.phone = phone
        

class SimpleGUI:
    def __init__(self, parent):
        self.input_frame = Frame(parent, bg="pink")
        self.display_frame = Frame(parent, bg="blue")

        self.current_index = 0

        self.input_frame.pack()

        self.people = []

        b1 = Button(self.input_frame, text="Click", command=self.switch_frame_two)
        b1.pack()
        b2 = Button(self.display_frame, text="Click", command=self.switch_frame_one)
        b2.pack()

        self.display_name = Label(self.display_frame, text="")
        self.display_name.pack()

        self.display_age = Label(self.display_frame, text="")
        self.display_age.pack()

        self.display_phone = Label(self.display_frame, text="")
        self.display_phone.pack()

        self.next_button = Button(self.display_frame, text="Next")
        self.next_button.pack()

        self.prev_button = Button(self.display_frame, text="Previous")
        self.prev_button.pack()

        self.back_button = Button(self.display_frame, text="Add New Person")
        self.back_button.pack()







        self.name_thing = StringVar()
        self.age_thing = StringVar()

        self.name_label = Label(self.input_frame, text="Name")
        self.name_label.pack()
        self.name_entry = Entry(self.input_frame, textvariable=self.name_thing)
        self.name_entry.pack()

        self.age_label = Label(self.input_frame, text="Age")
        self.age_label.pack()
        self.age_entry = Entry(self.input_frame, textvariable=self.age_thing)
        self.age_entry.pack()

        self.phone_ownership = Label(self.input_frame, text="Do you have a phone?")
        self.phone_ownership.pack()

        self.v = StringVar()
        self.v.set("0")

        self.own_phone = Radiobutton(self.input_frame, variable=self.v, text="Yes", value="1")
        self.own_phone.pack()

        self.own_phone_one = Radiobutton(self.input_frame, variable=self.v, text="No", value="2")
        self.own_phone_one.pack()

        self.enter_data_button = Button(self.input_frame, text="enter data", command= self.enter_data)
        self.enter_data_button.pack()

        self.show_data_button = Button(self.input_frame, text="show data", command= self.show_all)
        self.show_data_button.pack()
    
    def switch_frame_one(self):
        self.display_frame.pack_forget()
        self.input_frame.pack()


    def switch_frame_two(self):
        self.input_frame.pack_forget()
        self.display_frame.pack()


    
    def enter_data(self):
        name = self.name_thing.get()
        age = self.age_thing.get()
        phone = self.v.get()
        new_person = People(name, age, phone)
        self.people.append(new_person)

    def show_all(self):
        if len(self.people) == 0:
            print("")
            return

        self.current_index = 0
        self.switch_frame_two()

        




if __name__ == "__main__":
    
    root = Tk()
    Thing = SimpleGUI(root)
    root.mainloop()