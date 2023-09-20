import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")
language_data = lt.languages()
language_names = [lang['name'] for lang in language_data]
language_codes = {lang['name']: lang['code'] for lang in language_data}

app = tk.Tk()
app.geometry("700x400")
app.title('MO`s translator')
app.config(bg='white')

app_name = tk.Label(app, text='Hello', font='arial 15 bold')
app_name.place(x=230, y=0)

# input
input_label = tk.Label(app, text='Enter', font='arial 13 bold')

input_label.place(x=85, y=45)

input_text = tk.Text(app, font='arial 10', height=11, width=30, padx=5, pady=5)
input_text.place(x=15, y=100)

input_lang = ttk.Combobox(app, width=19, values=language_names)
input_lang.place(x=55, y=75)
input_lang.set("choose input language")
# ---------
# output
output_label = tk.Label(app, text='Output', font='arial 13 bold')

output_label.place(x=490, y=45)

output_text = tk.Text(app, font='arial 10', height=11, width=30, padx=5, pady=5)
output_text.place(x=400, y=100)

output_lang = ttk.Combobox(app, width=30, values=language_names)
output_lang.place(x=440, y=75)
output_lang.set("choose output language")

# -------
# translate button
def Translate():
    try:
        translated_text = lt.translate(input_text.get("1.0", tk.END), language_codes[input_lang.get()],
                                       language_codes[output_lang.get()])
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", translated_text)

    except KeyError as e:
        output_text.insert(tk.END, e)


trans_btn = tk.Button(app, text="Translate", font='arial 10 bold', padx=5, command=Translate)
trans_btn.place(x=305, y=180)
# --------
# clear button
def Clear():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


clear_btn = tk.Button(app, text="clrar", font='arial 10 bold', padx=5, width=8, command=Clear)
clear_btn.place(x=305, y=220)
app.mainloop()