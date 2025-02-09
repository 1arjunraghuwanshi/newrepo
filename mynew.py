import asyncio
from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import messagebox, ttk

async def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = await translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def on_translate():
    text_to_translate = text_input.get("1.0", "end-1c")  
    if text_to_translate.lower() == "exit":
        root.quit()
    else:
        src_lang_code = source_language.get()
        dest_lang_code = target_language.get()
        src_lang = lang_dict.get(src_lang_code, "en")
        dest_lang = lang_dict.get(dest_lang_code, "hi")
        translation = asyncio.run(translate_text(text_to_translate, src_lang, dest_lang))
        text_output.delete("1.0", "end")  
        text_output.insert(tk.END, translation)  

def on_exit():
    messagebox.showinfo("Goodbye", "Goodbye! Aaj ke liye bas itna hi.")
    root.quit()

root = tk.Tk()
root.title("ARJUN  KE TRANSLATER MEIN AAPKA SWAGAT HAI")
root.geometry("600x500")
root.config(bg="#D4AF37")

label = tk.Label(root, text="Text to Translate ", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=5)

text_input = tk.Text(root, height=5, width=50, font=("Arial", 12))
text_input.pack(pady=5)

# Language dictionary for full names
lang_dict = {v: k for k, v in LANGUAGES.items()}

# Language selection dropdowns
source_language_label = tk.Label(root, text="Select source language:", font=("Arial", 10), bg="#f0f0f0")
source_language_label.pack(pady=2)
source_language = ttk.Combobox(root, values=list(lang_dict.keys()), font=("Arial", 10))
source_language.set("English")  # Default: English
source_language.pack(pady=2)

target_language_label = tk.Label(root, text="Select target language:", font=("Arial", 10), bg="#f0f0f0")
target_language_label.pack(pady=2)
target_language = ttk.Combobox(root, values=list(lang_dict.keys()), font=("Arial", 10))
target_language.set("Hindi")  # Default: Hindi
target_language.pack(pady=2)

translate_button = tk.Button(root, text="Translate", font=("Arial", 12), bg="#f0f0f0", fg="black", command=on_translate)
translate_button.pack(pady=10)

text_output = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#f0f0f0")
text_output.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="#33FFFF", fg="black", command=on_exit)
exit_button.pack(pady=10)

root.mainloop()
