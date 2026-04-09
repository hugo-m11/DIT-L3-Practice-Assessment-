from tkinter import *

class SimpleGUI:
    def __init__(self, parent):
        self.input_frame = Frame(parent)
        self.display_frame = Frame(parent)

        self.input_frame.pack()

        name_thing = StringVar()
        age_thing = StringVar()

        self.name_label = Label(self.input_frame, text="Name")
        self.name_label.pack()
        self.name_entry = Entry(self.input_frame, textvariable=name_thing)
        self.name_entry.pack()

        self.age_label = Label(self.input_frame, text="Age")
        self.age_label.pack()
        self.age_entry = Entry(self.input_frame, textvariable=age_thing)
        self.age_entry.pack()

        self.phone_ownership = Label(self.input_frame, text="Do you have a phone?")
        self.phone_ownership.pack()

        self.v = StringVar()
        self.v.set("0")

        self.own_phone = Radiobutton(self.input_frame, variable=self.v, text="Yes", value="1")
        self.own_phone.pack()

        self.own_phone_one = Radiobutton(self.input_frame, variable=self.v, text="No", value="2")
        self.own_phone_one.pack()


if __name__ == "__main__":
    root = Tk()
    Thing = SimpleGUI(root)
    root.mainloop()