#Gui import
from tkinter import *
#message box
import tkinter.messagebox as mb
#Treeview
import tkinter.ttk as ttk

#import the database class
from Pokemon_database import Database

#list of pokemon types for option menu drop down
pokemon_types = ["Normal", "Fire", "Water", "Electric", 
                 "Grass", "Ice", "Fighting", "Poison", 
                 "Ground", "Flying", "Psychic", "Bug", 
                 "Rock", "Ghost", "Dragon", "Dark", 
                 "Steel", "Fairy"]

#list of pokemon natures for option menu drop down
pokemon_natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty",
                   "Bold", "Docile", "Relaxed", "Impish", "Lax",
                   "Timid", "Hasty", "Serious", "Jolly", "Naive",
                   "Modest", "Mild", "Quiet", "Bashful", "Rash",
                   "Calm", "Gentle", "Sassy", "Careful", "Quirky"]

db = Database("C:/Users/ernie/OneDrive/Desktop/Pokemon_CRUD/pokemon.db")

#create window object
root = Tk()

#add title to the window
root.title("Pokemon storage box")

#set the size of the window
root.geometry("800x650+351+174")



#for updating pokemon details
def update_pokemon():
    if not validate_entry_fields():
        return

    db.update(
        entrypokemonid.get(),
        entrypokemonname.get(),
        selected_type.get(),      # ✔ OptionMenu
        entrypokemonlevel.get(),
        legendary_var.get(),      # ✔ Radio button
        shiny_var.get(),          # ✔ Radio button
        selected_nature.get()     # ✔ OptionMenu
    )

    clear_fields()
    load_pokemon_data()


#for deleting pokemon details
def delete_pokemon():
    if entrypokemonid.get() == "":
        mb.showinfo("Information needed", "Please enter the Pokemon ID to delete")
        return
    MsgBox = mb.askquestion("Delete Pokemon", "Are you sure you want to delete this Pokemon?", icon='warning')
    if MsgBox == 'yes':
        db.remove(entrypokemonid.get())
        clear_fields()
        load_pokemon_data()
    return

#for clearing the entry fields
def clear_fields():
    entrypokemonid.delete(0, END)
    entrypokemonname.delete(0, END)
    entrypokemonlevel.delete(0, END)

    selected_type.set("Select Type")
    selected_nature.set("Select Nature")

    legendary_var.set("No")
    shiny_var.set("No")


#for showing all pokemon details
def show_all_pokemon():
    clear_fields()
    load_pokemon_data()
    return

#for exiting the application
def exit_application():
    MsgBox = mb.askquestion("Exit Application", "Are you sure you want to exit the application?", icon='warning')
    if MsgBox == 'yes':
        root.destroy()


#showing the selected pokemon details in the entry fields
def show_selected_pokemon(event):
    selected = tvStudent.focus()
    if not selected:
        return

    values = tvStudent.item(selected, "values")

    clear_fields()

    entrypokemonid.insert(0, values[0])
    entrypokemonname.insert(0, values[1])
    selected_type.set(values[2])
    entrypokemonlevel.insert(0, values[3])
    legendary_var.set(values[4])
    shiny_var.set(values[5])
    selected_nature.set(values[6])


#loading pokemon data into the treeview
def load_pokemon_data():
    # Clear the treeview
    tvStudent.delete(*tvStudent.get_children())

    # Load rows from the database
    for row in db.fetch():
        tvStudent.insert("", END, values=row)

        
    

#validdating entry fields
def validate_entry_fields():
    # Validate Pokémon Name
    if entrypokemonname.get() == "":
        mb.showerror("Error", "Pokemon name cannot be empty.")
        return False

    # Validate Type (OptionMenu)
    if selected_type.get() == "Select Type":
        mb.showerror("Error", "Please select a Pokemon type.")
        return False

    # Validate Level
    if entrypokemonlevel.get() == "":
        mb.showerror("Error", "Level cannot be empty.")
        return False

    if not entrypokemonlevel.get().isdigit():
        mb.showerror("Error", "Level must be a number.")
        return False

    # Validate Nature (OptionMenu)
    if selected_nature.get() == "Select Nature":
        mb.showerror("Error", "Please select a nature.")
        return False

    return True


#defining the functions for different events
def register_pokemon():
    if not validate_entry_fields():
        return

    db.insert(
        entrypokemonname.get(),
        selected_type.get(),
        entrypokemonlevel.get(),
        legendary_var.get(),
        shiny_var.get(),
        selected_nature.get()
    )

    clear_fields()
    load_pokemon_data()

    return


#label widget for the title
title_label = Label(root, text="Pokemon storage box", font=("Arial", 20))

#label widgets for each field
lblpokemonid = Label(root, text="Pokemon ID", font=("Arial", 10))
lblpokemonname = Label(root, text="Pokemon Name", font=("Arial", 10))
lblpokemontype = Label(root, text="Pokemon Type", font=("Arial", 10))
lblpokemonlevel = Label(root, text="Pokemon Level", font=("Arial", 10))
lblislegendary = Label(root, text="Is Legendary", font=("Arial", 10))
lblisshiny = Label(root, text="Is Shiny", font=("Arial", 10))
lblnature = Label(root, text="Nature", font=("Arial", 10))

#label for select and search
lblselect = Label(root, text="Select Pokemon", font=("Arial", 10))

#create entry widgets for each field
entrypokemonid = Entry(root, font=("Arial", 10))
entrypokemonname = Entry(root, font=("Arial", 10))
entrypokemonlevel = Entry(root, font=("Arial", 10))


# Variables for OptionMenus
selected_type = StringVar()
selected_type.set("Select Type")

selected_nature = StringVar()
selected_nature.set("Select Nature")

# OptionMenus for Type and Nature
type_menu = OptionMenu(root, selected_type, *pokemon_types)
nature_menu = OptionMenu(root, selected_nature, *pokemon_natures)

#Radio buttons for is_legendary
legendary_var = StringVar()
legendary_var.set("No")

legendary_yes = Radiobutton(root, text="Yes", variable=legendary_var, value="Yes")
legendary_no = Radiobutton(root, text="No", variable=legendary_var, value="No")

legendary_yes.place(x=300, y=210, height=25, width=90)
legendary_no.place(x=400, y=210, height=25, width=90)

#Radio buttons for is_shiny
shiny_var = StringVar()
shiny_var.set("No")

shiny_yes = Radiobutton(root, text="Yes", variable=shiny_var, value="Yes")
shiny_no = Radiobutton(root, text="No", variable=shiny_var, value="No")

shiny_yes.place(x=300, y=250, height=25, width=90)
shiny_no.place(x=400, y=250, height=25, width=90)

#create button widgets for Register, Update, Delete, , Clear, Show All, and Exit
btnregister = Button(root, text="Register", font=("Arial", 11), command=register_pokemon)
btnupdate = Button(root, text="Update", font=("Arial", 11), command=update_pokemon)
btndelete = Button(root, text="Delete", font=("Arial", 11), command=delete_pokemon)
btnclear = Button(root, text="Clear", font=("Arial", 11), command=clear_fields)
btnshowall = Button(root, text="Show All", font=("Arial", 11), command=show_all_pokemon)  
btnexit = Button(root, text="Exit", font=("Arial", 11), command=exit_application)

###Placing Widgets###
#specify a tuple columns
columns = ("Pokemon ID", "Pokemon Name", "Pokemon Type", "Pokemon Level", "Is Legendary", "Is Shiny", "Nature")

tvStudent = ttk.Treeview(root, columns=columns, show="headings", height="5")

tvStudent.heading('Pokemon ID', text='Pokemon ID', anchor='center')
tvStudent.column('Pokemon ID', width=60, anchor='center', stretch=False)

tvStudent.heading('Pokemon Name', text='Pokemon Name', anchor='center')
tvStudent.column('Pokemon Name', width=120, anchor='center', stretch=True)

tvStudent.heading('Pokemon Type', text='Pokemon Type', anchor='center')
tvStudent.column('Pokemon Type', width=100, anchor='center', stretch=True)

tvStudent.heading('Pokemon Level', text='Pokemon Level', anchor='center')
tvStudent.column('Pokemon Level', width=100, anchor='center', stretch=True)

tvStudent.heading('Is Legendary', text='Is Legendary', anchor='center')
tvStudent.column('Is Legendary', width=100, anchor='center', stretch=True)

tvStudent.heading('Is Shiny', text='Is Shiny', anchor='center')
tvStudent.column('Is Shiny', width=100, anchor='center', stretch=True)

tvStudent.heading('Nature', text='Nature', anchor='center')
tvStudent.column('Nature', width=100, anchor='center', stretch=True)    


#add a vertical scroll bar
vertical_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tvStudent.yview)

#place the vertical scroll bar
vertical_scrollbar.place(x=800 - 20, y=420, height=200)

#configure the treeview to use the vertical scroll bar
tvStudent.configure(yscrollcommand=vertical_scrollbar.set)

#create a horizontal scroll bar
horizontal_scrollbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=tvStudent.xview)

#place the horizontal scroll bar
horizontal_scrollbar.place(x=150, y=620, width=650)

#configure the treeview to use the horizontal scroll bar
tvStudent.configure(xscrollcommand=horizontal_scrollbar.set)

#bind the treeview to the function show_selected_pokemon
tvStudent.bind("<<TreeviewSelect>>", show_selected_pokemon)

# place the labels
title_label.place(x=270, y=5, height=30, width=300)

lblpokemonid.place(x=150, y=60, height=25, width=120)
lblpokemonname.place(x=150, y=100, height=25, width=120)
lblpokemontype.place(x=150, y=140, height=25, width=120)
lblpokemonlevel.place(x=150, y=180, height=25, width=120)
lblislegendary.place(x=150, y=220, height=25, width=120)
lblisshiny.place(x=150, y=260, height=25, width=120)
lblnature.place(x=150, y=300, height=25, width=120)
lblselect.place(x=150, y=340, height=25, width=120)


# place the entry widgets   
entrypokemonid.place(x=300, y=60, height=25, width=190)
entrypokemonname.place(x=300, y=100, height=25, width=190)
type_menu.place(x=300, y=140, height=25, width=190)
nature_menu.place(x=300, y=290, height=25, width=190)
entrypokemonlevel.place(x=300, y=180, height=25, width=190)


# place the button widgets
btnregister.place(x=150, y=360, height=30, width=100)
btnupdate.place(x=260, y=360, height=30, width=100)
btndelete.place(x=370, y=360, height=30, width=100)
btnclear.place(x=480, y=360, height=30, width=100)
btnshowall.place(x=590, y=360, height=30, width=100)
btnexit.place(x=700, y=360, height=30, width=100)




#place the treeview widget
tvStudent.place(x=150, y=420, height=200, width=650)


load_pokemon_data()

#call the main loop()
root.mainloop()

