import pyttsx3
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import threading
from tkinter import messagebox

def cls1():
    textbox.delete(1.0, tk.END)

def cls2():
    textboxp.delete(1.0, tk.END)

def audio_():
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textboxp.get("1.0", tk.END))
    speaker.runAndWait()

def stop_audio():
    pyttsx3.init().stop()

def thread():
    x = threading.Thread(target=audio_)
    x.start()

def pdf_():
    p1_text = e1.get()
    p2_text = e2.get()

    if p1_text.strip() == '' or p2_text.strip() == '':
        messagebox.showerror("Error", "Please enter valid page numbers.")
        return

    p1 = int(p1_text)
    p2 = int(p2_text)

    filelocation = askopenfilename()
    book = open(filelocation, 'rb')
    pdf_reader = PdfReader(book)

    if p1 <= 0 or p2 <= 0 or p1 > len(pdf_reader.pages) or p2 > len(pdf_reader.pages):
        messagebox.showerror("Error", "Invalid page numbers.")
        return

    pages = len(pdf_reader.pages)
    plabel = tk.Label(tab2, text="Total pages: " + str(pages))
    plabel.grid(row=3)

    for x in range(p2 - 1, p1 - 2, -1):
        page = pdf_reader.pages[x]
        text = page.extract_text()
        textboxp.insert(1.0, text)
        plabel = tk.Label(window, text="Page num: " + str(x))
        plabel.grid(row=2)

def tpages():
    filelocation = askopenfilename()
    book = open(filelocation, 'rb')
    pdf_reader = PdfReader(book)
    pages = len(pdf_reader.pages)
    plabel = tk.Label(tab2, text="Total pages: " + str(pages))
    plabel.grid(row=3)

def text_():
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textbox.get("1.0", tk.END))
    speaker.runAndWait()

def rbutton(value):
    if value == 0:
        label1 = tk.Label(tab3, text="Voice: Male  ")
        label1.grid(row=12)
    else:
        label1 = tk.Label(tab3, text="Voice: Female")
        label1.grid(row=12)

def scale(s):
    label = tk.Label(tab3, text="Rate: " + str(range1.get()))
    label.grid(row=10, column=0)

def close_app():
    pyttsx3.init().stop()
    window.quit()

window = tk.Tk()
window.title("AudiobookAI")
window.geometry('390x540')

v = tk.IntVar()
v.set(0)

tab_control = ttk.Notebook(window)

tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)
tab3 = tk.Frame(tab_control)

tab_control.add(tab1, text='Text')
tab_control.add(tab2, text='PDF')
tab_control.add(tab3, text='Settings')

# tab1
label1 = tk.Label(tab1, text="\u2193Enter text here \u2193", font=("Arial", 15), background='white')
label1.grid(row=0, column=0, sticky=tk.E + tk.W)

scroll = tk.Scrollbar(tab1)
scroll.grid(row=1, column=1, sticky="ns")
textbox = tk.Text(tab1, height=20, width=41, wrap="word", yscrollcommand=scroll.set)
textbox.grid(row=1, column=0, sticky="nsew")

button1 = tk.Button(tab1, text="Convert", command=text_)
button1.grid(pady=20, row=2)
button1 = tk.Button(tab1, text="Clear", command=cls1)
button1.grid(pady=10, padx=10, row=3, column=0, sticky=tk.W)
button1 = tk.Button(tab1, text="Close", command=close_app)
button1.grid(pady=10, padx=10, row=3, column=0, sticky=tk.E)

# tab2
label1 = tk.Label(tab2, text="Select a pdf file", font=("Arial", 15), background='white')
label1.grid(row=0, column=0, sticky=tk.E + tk.W)

scroll = tk.Scrollbar(tab2)
scroll.grid(row=1, column=1, sticky="ns")
textboxp = tk.Text(tab2, height=15, width=41, wrap="word", yscrollcommand=scroll.set)
textboxp.grid(row=1, column=0, sticky="nsew")

plabel1 = tk.Label(tab2, text="First page")
plabel1.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)
plabel2 = tk.Label(tab2, text="page num:0")
plabel2.grid(row=2)
plabel3 = tk.Label(tab2, text="Last page")
plabel3.grid(row=2, padx=10, column=0, sticky=tk.E)
e1 = tk.Entry(tab2, width=10)
e1.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)
e2 = tk.Entry(tab2, width=10)
e2.grid(row=3, padx=10, column=0, sticky=tk.E)

button1 = tk.Button(tab2, text="Open", command=pdf_)
button1.grid(pady=10, row=4)

button1 = tk.Button(tab2, text="Convert", command=thread)
button1.grid(pady=10, row=5)

button1 = tk.Button(tab2, text="Clear", command=cls2)
button1.grid(pady=10, padx=10, row=6, column=0, sticky=tk.W)

button1 = tk.Button(tab2, text="Close", command=close_app)
button1.grid(pady=10, padx=10, row=6, column=0, sticky=tk.E)

button1 = tk.Button(tab2, text="Check No.of Pages", command=tpages)
button1.grid(pady=10, padx=10, row=6, column=0)

scroll.config(command=textboxp.yview)

# tab3
label1 = tk.Label(tab3, text="Select the setting you want to apply", font=("Arial", 15), background='white',
                foreground="black")
label1.grid(row=0, column=0, sticky=tk.E + tk.W)

label1 = tk.Label(tab3, text="Rate", font=("Arial", 15), background='white')
label1.grid(pady=10, row=1, column=0, sticky=tk.E + tk.W)
range1 = tk.Scale(tab3, from_=-200, to=200, orient=tk.HORIZONTAL, command=scale, length=300)
range1.grid(row=2, column=0, sticky=tk.W, padx=10)

label1 = tk.Label(tab3, text="Voice", font=("Arial", 15), background='white')
label1.grid(pady=10, row=3, column=0, sticky=tk.E + tk.W)
rbutton1 = tk.Radiobutton(tab3, text="Male", variable=v, value=0, command=lambda: rbutton(v.get()))
rbutton1.grid(row=4, sticky=tk.W)
rbutton2 = tk.Radiobutton(tab3, text="Female", variable=v, value=1, command=lambda: rbutton(v.get()))
rbutton2.grid(row=5, sticky=tk.W)

rlabel = tk.Label(tab3, text="Rate: 0")
rlabel.grid(row=10, column=0)
vlabel = tk.Label(tab3, text="Voice: Male")
vlabel.grid(row=12)

# Ver
label1 = tk.Label(tab3, text="Ver:0.1.0", font=("Arial", 8), background='white')
label1.grid(pady=190, row=20, column=0, sticky=tk.E + tk.W)

tab_control.grid(row=0, column=0)

window.mainloop()
