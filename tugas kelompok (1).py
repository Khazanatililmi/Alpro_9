import tkinter as tk  # Import library Tkinter untuk membuat GUI
from tkinter import Menu, messagebox  # Import widget Menu dan messagebox dari Tkinter
import random  # Import library random untuk fitur kutipan motivasi

# Fungsi Timer Belajar
def timer_belajar():
    def start_timer():
        try:
            durasi = int(entry_timer.get()) * 60  # Konversi menit ke detik
            countdown(durasi)
        except ValueError:
            messagebox.showerror("Input Error", "Masukkan angka dalam menit!")

    def countdown(durasi):
        if durasi > 0:
            mins, secs = divmod(durasi, 60)
            timer_label.config(text=f"{mins:02}:{secs:02}")
            timer_window.after(1000, countdown, durasi - 1)
        else:
            timer_label.config(text="Waktu Habis!")
            messagebox.showinfo("Selesai", "Waktu belajar selesai!")

    # Membuat jendela baru untuk Timer Belajar
    timer_window = tk.Toplevel(app)
    timer_window.title("Timer Belajar")

    # Input untuk durasi
    tk.Label(timer_window, text="Masukkan waktu belajar (menit):").pack(pady=5)
    entry_timer = tk.Entry(timer_window)
    entry_timer.pack(pady=5)

    # Tombol untuk memulai timer
    tk.Button(timer_window, text="Mulai", command=start_timer).pack(pady=5)

    # Label untuk menampilkan hitungan mundur
    timer_label = tk.Label(timer_window, text="00:00", font=("Helvetica", 16))
    timer_label.pack(pady=10)

# Fungsi Catatan Harian
def catatan_harian():
    def simpan_catatan():
        with open("catatan_harian.txt", "w") as file:
            file.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Sukses", "Catatan berhasil disimpan!")

    def baca_catatan():
        try:
            with open("catatan_harian.txt", "r") as file:
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, file.read())
        except FileNotFoundError:
            messagebox.showerror("Error", "Tidak ada catatan yang ditemukan!")

    # Membuat jendela baru untuk Catatan Harian
    catatan_window = tk.Toplevel(app)
    catatan_window.title("Catatan Harian")
    text_area = tk.Text(catatan_window, wrap="word")
    text_area.pack(pady=5)
    tk.Button(catatan_window, text="Simpan", command=simpan_catatan).pack(pady=5)
    tk.Button(catatan_window, text="Baca", command=baca_catatan).pack(pady=5)

# Fungsi To-Do List
def todo_list():
    def tambah_tugas():
        listbox.insert(tk.END, entry_tugas.get())
        entry_tugas.delete(0, tk.END)

    def hapus_tugas():
        selected = listbox.curselection()
        for idx in reversed(selected):
            listbox.delete(idx)

    def hapus_semua():
        listbox.delete(0, tk.END)

    # Membuat jendela baru untuk To-Do List
    todo_window = tk.Toplevel(app)
    todo_window.title("To-Do List")
    tk.Label(todo_window, text="Masukkan Tugas:").pack(pady=5)
    entry_tugas = tk.Entry(todo_window)
    entry_tugas.pack(pady=5)
    tk.Button(todo_window, text="Tambah", command=tambah_tugas).pack(pady=5)
    tk.Button(todo_window, text="Hapus", command=hapus_tugas).pack(pady=5)
    tk.Button(todo_window, text="Hapus Semua", command=hapus_semua).pack(pady=5)
    listbox = tk.Listbox(todo_window)
    listbox.pack(pady=5)

# Fungsi Kalkulator
def kalkulator():
    def masukkan_angka(angka):
        entry_calculator.insert(tk.END, angka)

    def hitung():
        try:
            result = eval(entry_calculator.get())
            entry_calculator.delete(0, tk.END)
            entry_calculator.insert(0, str(result))
        except Exception:
            entry_calculator.delete(0, tk.END)
            entry_calculator.insert(0, "Error")

    def clear():
        entry_calculator.delete(0, tk.END)

    # Membuat jendela baru untuk Kalkulator
    calc_window = tk.Toplevel(app)
    calc_window.title("Kalkulator Sederhana")

    entry_calculator = tk.Entry(calc_window, justify="right")
    entry_calculator.grid(row=0, column=0, columnspan=4, pady=5)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]
    for text, row, col in buttons:
        if text == '=':
            tk.Button(calc_window, text=text, command=hitung).grid(row=row, column=col)
        elif text == 'C':
            tk.Button(calc_window, text=text, command=clear).grid(row=row, column=col)
        else:
            tk.Button(calc_window, text=text, command=lambda t=text: masukkan_angka(t)).grid(row=row, column=col)

# Fungsi Motivational Quote
def motivational_quote():
    quotes = [
        "Stay positive, work hard, make it happen!",
        "The future depends on what you do today.",
        "Don't stop until you're proud.",
        "Believe in yourself and all that you are.",
    ]
    quote = random.choice(quotes)
    messagebox.showinfo("Motivational Quote", quote)

# Aplikasi Utama
app = tk.Tk()
app.title("Student Productivity Toolkit")

# Menu navigasi utama
menu_bar = Menu(app)
app.config(menu=menu_bar)

# Tambahkan menu untuk setiap fitur
menu_bar.add_command(label="Timer Belajar", command=timer_belajar)
menu_bar.add_command(label="Catatan Harian", command=catatan_harian)
menu_bar.add_command(label="To-Do List", command=todo_list)
menu_bar.add_command(label="Kalkulator", command=kalkulator)
menu_bar.add_command(label="Motivational Quote", command=motivational_quote)

app.mainloop()
