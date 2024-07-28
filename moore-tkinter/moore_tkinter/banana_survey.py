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
name_label = tk.Label(root, text="What is your name")
name_inp = tk.Entry(root)

# add checkbox
eater_inp = tk.Checkbutton(
    root,
    text="Check this box if you eat bananas"
)

# add input for numbers (choose from predefined range and incrementation step)
num_label = tk.Label(
    root,
    text="How many bananas do you eat per day?"
)
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

# add input for predefined options
color_label = tk.Label(
    root,
    text="What is the best color for banana?"
)
color_inp = tk.Listbox(root, height=1)
color_choices = (
    "Any", "Green", "Green-Yellow",
    "Yellow", "Brown Spotted", "Black"
)
for choice in color_choices:
    color_inp.insert(tk.END, choice)

# add radiobutton choose options
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text="Yes")
plantain_no_inp = tk.Radiobutton(plantain_frame, text="Ewww, no!")

# add multiline text input
banana_haiku_label = tk.Label(
    root,
    text="Write a haiku about bananas"
)
banana_haiku_inp = tk.Text(root, height=3)

# add submit button
submit_btn = tk.Button(root, text="Submit Survey")

# add output
output_line = tk.Label(root, text="", anchor="w", justify="left")

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
    name = name_inp.get()
    number = num_inp.get()

    selected_idx = color_inp.curselection()
    if selected_idx:
        color = color_inp.get(selected_idx)
    else:
        color = ""
    haiku = banana_haiku_inp.get("1.0", tk.END)

    message = (
        f"Thanks for taking the survey, {name}. \n",
        f"Enjoy your {number} {color} bananas!"
    )
    output_line.configure(text=message)
    
    print(haiku)

submit_btn.configure(command=on_submit)


