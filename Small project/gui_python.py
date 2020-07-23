# %%
from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
window.title('Hello Python')
window.geometry("1000x3000+10+10")
#var = StringVar()
#var.set("one")
lbl=Label(window, text="Select state", fg='Red', font=("Helvetica", 12))
lbl.place(x=60, y=100)
cb=Combobox(window)
cb['values']=["Maharashtra", "Gujarat", "Madhya Pradesh", "Chattisgarh"]
cb.place(x=60, y=125)
def check():
 #   value=cb.get()
 #   if value=="Maharashtra":
        lbl=Label(window, text="You selected Maharashtra", fg='Red', font=("Helvetica", 12))
        lbl.place(x=60, y=150)
        return
cb.after(10000,check())
window.mainloop()
# %%
import tkinter as tk

def change():
    my_string_var.set('Second Time')

root = tk.Tk()
my_string_var = tk.StringVar()
my_string_var.set('First Time')
tk.Label(root, textvariable=my_string_var).grid()
tk.Button(root, text='Change', command=change).grid(row=1)
root.mainloop()

# %%
print(type(data))
# %%
from tkinter import *
from tkinter.ttk import *

class Gui:

    def __init__(self):
        self.root = Tk()

        # Set up the Combobox
        self.selections = Combobox(self.root)
        self.selections['values'] = ['Apples', 'Oranges', 'Blueberries', 'Bananas', 'Custom']
        self.selections.pack()

        # The Entry to be shown if "Custom" is selected
        self.custom_field = Entry(self.root)
        self.show_custom_field = False

        # Check the selection in 100 ms
        self.root.after(100, self.check_for_selection)

    def check_for_selection(self):
        '''Checks if the value of the Combobox equals "Custom".'''


        # Get the value of the Combobox
        value = self.selections.get()

        # If the value is equal to "Custom" and show_field is set to False
        if value == 'Custom' and not self.show_custom_field:

            # Set show_field to True and pack() the custom entry field
            self.show_custom_field = True
            self.custom_field.pack()


        # If the value DOESNT equal "Custom"
        elif value != 'Custom':

            # Set show_field to False
            self.show_custom_field = False

            # Destroy the custom input
            self.custom_field.destroy()

            # Set up a new Entry object to pack() if we need it later.
            # Without this line, tkinter was raising an error for me.
            # This fixed it, but I don't promise that this is the
            # most efficient method to do this.
            self.custom_field = Entry(self.root)

        # If the value IS "Custom" and we're showing the custom_feild
        elif value == 'Custom' and self.show_custom_field:
            pass


        # Call this method again to keep checking the selection box
        self.root.after(100, self.check_for_selection)


app = Gui()
app.root.mainloop()

# %%
