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

def open_csv():
    pass

def save():
    pass

def exit():
    pass

def toggle_hide(semester):
    print(semester)
    # dialog = tk.Tk()
    # dialog.title("Toggle hidden semesters")

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
for semester in hidden:
    togglemenu.add_command(label=semester, command=lambda: toggle_hide(semester))
viewmenu.add_cascade(label="Hide/Unhide semesters", menu=togglemenu)

window.config(menu=menubar)
window.mainloop()

print(hidden)