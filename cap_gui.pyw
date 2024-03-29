import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from csv import reader, writer

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

def classification(cap):
    if cap >= 4.50: return "Honours (Highest Distinction)"
    if cap >= 4: return "Honours (Distinction)"
    if cap >= 3.5: return "Honours (Merit)"
    if cap >= 3: return "Honours"
    if cap >= 2: return "Pass"
    return "DANGER"

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
    calculated = round(cap(results), 2)
    cap_label['text'] = f"CAP: {calculated}\n{classification(calculated)}"

def on_closing():
    global ADDITIONAL_WINDOWS
    EDIT_WINDOW.destroy()
    ADDITIONAL_WINDOWS = False    

def open_csv():
    ftypes = [('CSV files', '*.csv'), ('All files', '*')]
    dialog = filedialog.Open(filetypes = ftypes)
    fl = dialog.show()
    with open(fl) as f:
        read = reader(f)
        for row in read:
            if row:
                if row[0].startswith("#"):
                    continue
                else:
                    print(row)
                    module, grade, mc = row
                    if not mc:
                        mc = 4
                    else:
                        try:
                            mc = int(mc)
                        except ValueError:
                            raise ValueError(f"{fl}:{read.line_num}\n\t{mc} is not a digit")
                    if mc not in MC_LIST:
                        raise ValueError(f"{fl}:{read.line_num}\n\t{mc} is not valid MCs. Value must be in the range [0,8]")
                    if not grade:
                        raise ValueError(f"{fl}:{read.line_num}\n\tgrade is missing")
                    elif grade.upper() not in grade_points:
                        raise ValueError(f"{fl}:{read.line_num}\n\t{grade} is an invalid grade")
                    listbox_list.append((module, grade, mc))
        listvar.set(listbox_list)
        results = [i[1:] for i in listbox_list]
        calculated = round(cap(results), 2)
        cap_label['text'] = f"CAP: {calculated}\n{classification(calculated)}"

def save_csv():
    ftypes = [('CSV files', '*.csv')]
    file = filedialog.asksaveasfilename(filetypes = ftypes)
    with open(file + ".csv", 'w', newline='') as f:
        write = writer(f)
        for record in listbox_list:
            write.writerow(record)

def right_click(arg):
    print(arg)
    print("right click")

def shift_up(arg):
    i = listbox.curselection()[0]
    try:
        listbox_list[i-1], listbox_list[i] = listbox_list[i], listbox_list[i-1]
        listvar.set(listbox_list)
    except IndexError:
        pass    

def shift_down(arg):
    i = listbox.curselection()[0]
    try:
        listbox_list[i+1], listbox_list[i] = listbox_list[i], listbox_list[i+1]
        listvar.set(listbox_list)
    except IndexError:
        pass

def double_click(arg):
    global ADDITIONAL_WINDOWS, EDIT_WINDOW
    def edit():
        new_grade = (module_text_edit.get(), grade_text_edit.get(), int(mc_text_edit.get()))
        listbox_list[i] = new_grade
        listvar.set(listbox_list)
        results = [i[1:] for i in listbox_list]
        calculated = round(cap(results), 2)
        cap_label['text'] = f"CAP: {calculated}\n{classification(calculated)}"
        on_closing()
    if not ADDITIONAL_WINDOWS:
        ADDITIONAL_WINDOWS = True
        i = listbox.curselection()[0]
        module, grade, mc = listbox_list[i]
     
        EDIT_WINDOW = tk.Toplevel()
        EDIT_WINDOW.wm_title("Edit")

        module_label_edit = tk.Label(EDIT_WINDOW, text="Module Code")
        mc_label_edit = tk.Label(EDIT_WINDOW, text="MCs")
        grade_label_edit = tk.Label(EDIT_WINDOW, text="Grade")

        module_text_edit = tk.StringVar()
        module_entry_edit = tk.Entry(EDIT_WINDOW, textvariable=module_text_edit)
        module_entry_edit.insert(0, module)
        mc_text_edit = tk.StringVar(EDIT_WINDOW)
        mc_dropdown_edit = ttk.OptionMenu(EDIT_WINDOW, mc_text_edit, mc, *MC_LIST)
        grade_text_edit = tk.StringVar(EDIT_WINDOW)
        grade_dropdown_edit = ttk.OptionMenu(EDIT_WINDOW, grade_text_edit, grade, *GRADE_LIST)
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

def clear(arg=None):
    global cap_label
    listbox_list.clear()
    listvar.set(listbox_list)
    mc_text.set(4)
    grade_text.set("B")
    cap_label['text'] = "CAP:"

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
listbox.bind("<Control-Up>", shift_up)
listbox.bind("<Control-Down>", shift_down)

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
filemenu.add_command(label="Save to CSV", command=save_csv)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Clear all", command=clear)
menubar.add_cascade(label="Edit", menu=editmenu)
window.config(menu=menubar)

window.update()
offset_x = int(window.winfo_screenwidth()/2 - window.winfo_width()/2)
offset_y = int(window.winfo_screenheight()/2 - window.winfo_height()/2)
window.geometry(f"+{offset_x}+{offset_y}")
tk.mainloop()
