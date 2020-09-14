import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import csv

window = tk.Tk()
window.title("NUS CAP Calculator")
notebook = ttk.Notebook(window)
notebook.pack()
frames = {}
tab_id = -1
semesters, hidden = [], []
for year in range(1, 5):
    for sem in range(1, 5):
        tab_id += 1
        semester = f"Year {year} Sem {sem}"
        semesters.append(semester)
        frames[semester] = tk.Frame(notebook, width=500, height=500, bg="blue")
        frames[semester].pack(fill="both", expand="1")
        notebook.add(frames[semester], text=semester)
        if semester[-1] in {"3", "4"}:
            notebook.hide(tab_id)
            hidden.append(semester)



# solve_btn = tk.Button(window, text="Solve", command=get_puzzle, bg="green")
# solve_btn.grid(column=3, row=9)
# reset = tk.Button(window, text="Reset", command=clear_grid, bg="red")
# reset.grid(column=5, row=9)

def open_csv():
    pass

def save():
    pass

def exit():
    pass

def toggle_hide():
    dialog = tk.Tk()
    dialog.title("Toggle hidden semesters")

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Import from CSV", command=open_csv)
filemenu.add_command(label="Save to CSV", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

viewmenu = tk.Menu(menubar, tearoff=0)
viewmenu.add_command(label="Hide/Unhide semesters", command=toggle_hide)
menubar.add_cascade(label="View", menu=viewmenu)
window.config(menu=menubar)
window.mainloop()