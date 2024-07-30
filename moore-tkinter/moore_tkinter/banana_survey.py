import tkinter as tk


# create root window
root = tk.Tk()

# set the title
root.title("Banana interest survey")

# set the root window size
root.geometry("640x480+300+300")
root.resizable(False, False)

# add title label
title = tk.Label(
    root,
    text="Please take the survey",
    font="Arial 16 bold",
    bg="brown",
    fg="#FF0"
)

# add name input
name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name")
name_inp = tk.Entry(root, textvariable=name_var)

# add checkbox
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
    root,
    variable=eater_var,
    text="Check this box if you eat bananas"
)

# add input for numbers (choose from predefined range and incrementation step)
num_var = tk.IntVar(value=3)
num_label = tk.Label(
    root,
    text="How many bananas do you eat per day?"
)
num_inp = tk.Spinbox(
    root,
    textvariable=num_var,
    from_=0,
    to=1000,
    increment=1
)

# add input for predefined options
color_var = tk.StringVar(value="Any")
color_label = tk.Label(
    root,
    text="What is the best color for banana?"
)
color_choices = (
    "Any", "Green", "Green-Yellow",
    "Yellow", "Brown Spotted", "Black"
)
color_inp = tk.OptionMenu(
    root, color_var, *color_choices
)

# add radiobutton choose options
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)

plantain_var = tk.BooleanVar()
plantain_yes_inp = tk.Radiobutton(plantain_frame, text="Yes", value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(plantain_frame, text="Ewww, no!", value=False, variable=plantain_var)

# add multiline text input
banana_haiku_label = tk.Label(
    root,
    text="Write a haiku about bananas"
)
banana_haiku_inp = tk.Text(root, height=3)

# add submit button
submit_btn = tk.Button(root, text="Submit Survey")

# add output
output_var = tk.StringVar(value="")
output_line = tk.Label(root, textvariable=output_var, anchor="w", justify="left")

# arrage app title
title.grid(columnspan=2)

# arrage name label and input
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)

# arrange checkbox
eater_inp.grid(row=2, columnspan=2, sticky="we")

# arrange number input
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

# arrange color choose
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=(tk.W + tk.E), padx=25)

# arrange radiobutton frame
plantain_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_no_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)

# arrange multiline input
banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky="NSEW")

# arrange submit button
submit_btn.grid(row=99)

# arrange output
output_line.grid(row=100, columnspan=2, sticky="NSEW")

# extra space occupation
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

# def callback func for submit event
def on_submit():
    """To be run when the user submits"""
    name = name_var.get()

    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000

    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()

    haiku = banana_haiku_inp.get("1.0", tk.END)

    message = f"Thanks for taking the survey, {name}.\n"
    
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f"Enjoy your {number} {color} bananas!\n"
    
    if plantain_eater:
        message += "Enjoy your plantains!"
    else:
        message += "May you successfully avoid plantains!"
    
    if haiku.strip():
        message += f"\n\nYour Haiku:\n{haiku}"

    output_var.set(message)

submit_btn.configure(command=on_submit)

root.mainloop()
