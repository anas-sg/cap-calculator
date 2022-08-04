import tkinter as tk
import tkinter.ttk as ttk

MC_LIST = list(range(9))
GRADE_LIST = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "D+", "D", "F", "F*", "S", "U"]
grade_points = {
    "A+": 5,
    "A":  5,
    "A-": 4.5,
    "B+": 4,
    "B":  3.5,
    "B-": 3,
    "C+": 2.5,
    "C":  2,
    "D+": 1.5,
    "D":  1,
    "F":  0
}
calculated = ""
ADDITIONAL_WINDOWS = False

def centre(win):
    win.update()
    offset_x = int(win.winfo_screenwidth()/2 - win.winfo_width()/2)
    offset_y = int(win.winfo_screenheight()/2 - win.winfo_height()/2)
    win.geometry(f"+{offset_x}+{offset_y}")

def cap(results: list) -> float:
    """Return CAP based on list of grades"""
    sum_credits = sum_product = 0
    if not results:
        return 0
    for grade, credits in results:
        sum_credits += credits
        sum_product += grade_points[grade] * credits
    return sum_product / sum_credits

def select(arg):
    print("selected")

def add():
    global test, calculated
    grade = (module_text.get(), grade_text.get(), int(mc_text.get()))
    listbox_list.append(grade)
    listvar.set(listbox_list)
    results = [i[1:] for i in listbox_list]
    print(calculated := round(cap(results), 2))
    cap_label['text'] = f"CAP: {calculated}"

def edit():
    print("editing...")
    on_closing()

def on_closing():
    global ADDITIONAL_WINDOWS
    print("destroying window")
    EDIT_WINDOW.destroy()
    ADDITIONAL_WINDOWS = False    

def open_csv():
    pass

def save():
    pass

def right_click(arg):
    print(arg)
    print("right click")

def double_click(arg):
    global ADDITIONAL_WINDOWS, EDIT_WINDOW
    print("enter double")
    print(ADDITIONAL_WINDOWS)
    if not ADDITIONAL_WINDOWS:
        print("enter additional")
        ADDITIONAL_WINDOWS = True
        i = listbox.curselection()
        print(i)
        # print(arg)
        # print("double_click")
#TODO: ADD IN EDIT        
        EDIT_WINDOW = tk.Toplevel()
        EDIT_WINDOW.wm_title("Edit")

        module_label_edit = tk.Label(EDIT_WINDOW, text="Module Code")
        mc_label_edit = tk.Label(EDIT_WINDOW, text="MCs")
        grade_label_edit = tk.Label(EDIT_WINDOW, text="Grade")

        module_text_edit = tk.StringVar()
        module_entry_edit = tk.Entry(EDIT_WINDOW, textvariable=module_text_edit)
        mc_text_edit = tk.StringVar(EDIT_WINDOW)
        mc_dropdown_edit = ttk.OptionMenu(EDIT_WINDOW, mc_text_edit, 4, *MC_LIST)
        grade_text_edit = tk.StringVar(EDIT_WINDOW)
        grade_dropdown_edit = ttk.OptionMenu(EDIT_WINDOW, grade_text_edit, "B", *GRADE_LIST)
        add_button_edit = tk.Button(EDIT_WINDOW, text="Edit", command=edit)

        module_label_edit.grid(column=0, row=0)
        mc_label_edit.grid(column=1, row=0)
        grade_label_edit.grid(column=2, row=0)

        module_entry_edit.grid(column=0, row=1)
        mc_dropdown_edit.grid(column=1, row=1)
        grade_dropdown_edit.grid(column=2, row=1)
        add_button_edit.grid(column=3, row=1)

        EDIT_WINDOW.withdraw()
        EDIT_WINDOW.grid()
        EDIT_WINDOW.transient(window)
        EDIT_WINDOW.grab_set()
        # EDIT_WINDOW.form.initial_focus()
        EDIT_WINDOW.update()
        offset_x = int(EDIT_WINDOW.winfo_screenwidth()/2 - EDIT_WINDOW.winfo_width()/2)
        offset_y = int(EDIT_WINDOW.winfo_screenheight()/2 - EDIT_WINDOW.winfo_height()/2)
        EDIT_WINDOW.geometry(f"+{offset_x}+{offset_y}")
        EDIT_WINDOW.deiconify()
        EDIT_WINDOW.protocol("WM_DELETE_WINDOW", on_closing)

def delete(arg):
    global cap_label
    if len(index := listbox.curselection()):
        print("Deleting", listbox_list.pop(index[0]))
    listvar.set(listbox_list)
    results = [i[1:] for i in listbox_list]
    print(calculated := round(cap(results), 2))
    cap_label['text'] = f"CAP: {calculated}"
    

window = tk.Tk()
window.title("CAP calculator")
window.call("wm", "attributes", ".", "-topmost", "1")

module_label = tk.Label(window, text="Module Code")
mc_label = tk.Label(window, text="MCs")
grade_label = tk.Label(window, text="Grade")

module_text = tk.StringVar()
module_entry = tk.Entry(window, textvariable=module_text)
mc_text = tk.StringVar(window)
mc_dropdown = ttk.OptionMenu(window, mc_text, 4, *MC_LIST)
grade_text = tk.StringVar(window)
grade_dropdown = ttk.OptionMenu(window, grade_text, "B", *GRADE_LIST)
add_button = tk.Button(window, text="Add", command=add)

listbox_list = []
listvar = tk.StringVar(value=listbox_list)
listbox = tk.Listbox(window, listvariable=listvar, height=10)
scrollbar = tk.Scrollbar(window, orient="vertical")
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
listbox.bind("<Button-3>", right_click)
listbox.bind("<Delete>", delete)
listbox.bind("<Double-Button-1>", double_click)

cap_label = tk.Label(window, text="CAP:")

module_label.grid(column=0, row=0)
mc_label.grid(column=1, row=0)
grade_label.grid(column=2, row=0)

module_entry.grid(column=0, row=1)
mc_dropdown.grid(column=1, row=1)
grade_dropdown.grid(column=2, row=1)
add_button.grid(column=3, row=1)

listbox.grid(column=0, row=2, sticky='w')
scrollbar.grid(column=0, row=2, sticky='nse')
cap_label.grid(column=1, row=2, columnspan=2)

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