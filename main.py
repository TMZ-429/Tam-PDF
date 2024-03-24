#!/usr/bin/env python3
from PyPDF2 import PdfReader, PdfWriter
from tkinter import filedialog as fd
from tkinter import *
import os

CWD = os.getcwd()

WIDTH = 800
HEIGHT = 800

window = Tk()
window.title("TamPDF")
window.geometry(f"{WIDTH}x{HEIGHT}")

def extract(input_pdf, output_pdf, content):
    open(output_pdf, 'wb').truncate(0)
    reader = PdfReader(input_pdf, 'rb')
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_js(content)
    file_contents = open(output_pdf, "wb")
    writer.write(file_contents)

def main_menu():
    filename = ""
    def run_script():
        global filename
        script = script_input.get('1.0', 'end').strip()
        extract(filename, "output.pdf", script)
    def find_pdf():
        global filename
        filename = fd.askopenfilename()
        file_text = Label(window, text = filename)
        file_text.place(x = 200, y = 410)
    script_input = Text(
        window,
        height = 20,
        width = 60,
    )
    file_button = Button(
        window,
        text = "Open original PDF",
        command = find_pdf
    )
    script_input_button = Button(
        window,
        text = "Create modified PDF",
        command = run_script
    )
    Label(text = "Input your JS script here").pack()
    script_input.pack()
    file_button.place(x = 200, y = 430)
    script_input_button.place(x = 430, y = 430)
    window.mainloop()

main_menu()