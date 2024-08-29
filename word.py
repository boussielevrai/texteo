import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
import os

root = tk.Tk()
root.title("Texteo")
root.geometry("400x500")
# Vérifiez si le fichier existe avant de l'utiliser
icon_path = r'C:\Users\Toyger\Desktop\_a7a69b72-3906-4b4e-8049-c185187b87e6.jpeg'
if os.path.exists(icon_path):
    icon_image = ImageTk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon_image)
else:
    print(f"Le fichier {icon_path} n'existe pas.")

# Changer la couleur de fond de la fenêtre en bleu clair
root.configure(bg='light blue')

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def terminer():
    webbrowser.open("https://www.youtube.com/watch?v=GFq6wH5JR2A")

# Créer une zone de texte avec fond bleu clair et texte noir
text_area = tk.Text(root, wrap='word', bg='white', fg='black')
text_area.pack(expand=1, fill='both')

# Ajouter un menu
menu_bar = tk.Menu(root, bg='dark blue', fg='white')
file_menu = tk.Menu(menu_bar, tearoff=0, bg='white', fg='black')
file_menu.add_command(label="Ouvrir", command=open_file)
file_menu.add_command(label="Enregistrer", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="editeur de texte surement mieux que word", menu=file_menu)

root.config(menu=menu_bar)





root.mainloop()