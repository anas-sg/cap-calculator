import tkinter as tk
import tkinter.ttk as ttk

MC_LIST = list(range(9))
GRADE_LIST = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "D+", "D", "F", "F*", "S", "U"]

def select(arg):
    print("selected")

def add():
    global test
    grade = (module_text.get(), mc_text.get(), grade_text.get())
    listbox_list.append(grade)
    listvar.set(listbox_list)
    print("Adding", grade)

def open_csv():
    pass

def save():
    pass

window = tk.Tk()
window.title("CAP calculator")
window.call("wm", "attributes", ".", "-topmost", "1")

module_label = tk.Label(window, text="Module Code")
mc_label = tk.Label(window, text="MCs")
grade_label = tk.Label(window, text="Grade")

module_text = tk.StringVar()
module_entry = tk.Entry(window, textvariable=module_text)
mc_text = tk.StringVar(window)
mc_dropdown = ttk.OptionMenu(window, mc_text, 4, *MC_LIST, command=select)
grade_text = tk.StringVar(window)
grade_dropdown = ttk.OptionMenu(window, grade_text, "B", *GRADE_LIST, command=select)
add_button = tk.Button(window, text="Add", command=add)

listbox_list = []
listvar = tk.StringVar(value=listbox_list)
listbox = tk.Listbox(window, listvariable=listvar, height=10)
scrollbar = tk.Scrollbar(window, orient="vertical")
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

module_label.grid(column=0, row=0)
mc_label.grid(column=1, row=0)
grade_label.grid(column=2, row=0)

module_entry.grid(column=0, row=1)
mc_dropdown.grid(column=1, row=1)
grade_dropdown.grid(column=2, row=1)
add_button.grid(column=3, row=1)

listbox.grid(column=0, row=2, sticky='w')
scrollbar.grid(column=0, row=2, sticky='nse')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Import from CSV", command=open_csv)
filemenu.add_command(label="Save to CSV", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

window.update()
offset_x = int(window.winfo_screenwidth()/2 - window.winfo_width()/2)
offset_y = int(window.winfo_screenheight()/2 - window.winfo_height()/2)
window.geometry(f"+{offset_x}+{offset_y}")
tk.mainloop()