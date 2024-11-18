import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
)
''')
conn.commit()

def predict_faculty(biology, physics, english):
    if biology > physics and biology > english:
        return "Kedokteran"
    elif physics > biology and physics > english:
        return "Teknik"
    elif english > biology and english > physics:
        return "Bahasa"
    else:
        return "Tidak Diketahui"

def submit_data():
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
    
    prediksi = predict_faculty(biologi, fisika, inggris)
    
    cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))
    conn.commit()
    
    messagebox.showinfo("Success", f"Data submitted successfully!\nPredicted Faculty: {prediksi}")
    
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = tk.Label(root, text="Nilai Biologi")
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = tk.Label(root, text="Nilai Fisika")
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = tk.Label(root, text="Nilai Inggris")
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2)

root.mainloop()

conn.close()
