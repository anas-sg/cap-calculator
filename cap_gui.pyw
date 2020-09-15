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
semesters, hidden = [], {}
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
            hidden[semester] = 1

def open_csv():
    pass

def save():
    pass

def exit():
    pass

def toggle_hide(semester):
    if hidden[semester]:
        notebook.add(frames[semester], text=semester)
        hidden[semester] = 0
    else:
        year, sem = int(semester[5]), int(semester[11])
        tab_id = (year - 1) * 4 + (sem - 1)
        notebook.hide(tab_id)
        hidden[semester] = 1


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Import from CSV", command=open_csv)
filemenu.add_command(label="Save to CSV", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

viewmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)

togglemenu = tk.Menu(viewmenu)
togglemenu.add_checkbutton(label="Year 1 Sem 3", command=lambda: toggle_hide("Year 1 Sem 3"))
togglemenu.add_checkbutton(label="Year 1 Sem 4", command=lambda: toggle_hide("Year 1 Sem 4"))
togglemenu.add_checkbutton(label="Year 2 Sem 3", command=lambda: toggle_hide("Year 2 Sem 3"))
togglemenu.add_checkbutton(label="Year 2 Sem 4", command=lambda: toggle_hide("Year 2 Sem 4"))
togglemenu.add_checkbutton(label="Year 3 Sem 3", command=lambda: toggle_hide("Year 3 Sem 3"))
togglemenu.add_checkbutton(label="Year 3 Sem 4", command=lambda: toggle_hide("Year 3 Sem 4"))
togglemenu.add_checkbutton(label="Year 4 Sem 3", command=lambda: toggle_hide("Year 4 Sem 3"))
togglemenu.add_checkbutton(label="Year 4 Sem 4", command=lambda: toggle_hide("Year 4 Sem 4"))


viewmenu.add_cascade(label="Hide/Unhide semesters", menu=togglemenu)

window.config(menu=menubar)
window.mainloop()