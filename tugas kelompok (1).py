import tkinter as tk  # Tkinter digunakan untuk membuat antarmuka pengguna (GUI)
from tkinter import Menu, messagebox  # Menu untuk navigasi, messagebox untuk menampilkan pesan
import random  # Library random untuk memilih kutipan motivasi secara acak

# Fungsi Timer Belajar
def timer_belajar():
    """
    Membuka jendela baru yang memungkinkan pengguna mengatur durasi waktu belajar 
    dan memberikan hitungan mundur hingga waktu habis.
    """

    def start_timer():
        """
        Memulai timer berdasarkan input pengguna (dalam menit) dan menangani kesalahan input.
        """
        try:
            durasi = int(entry_timer.get()) * 60  # Konversi input menit menjadi detik
            countdown(durasi)  # Mulai hitungan mundur
        except ValueError:  # Jika input tidak valid (bukan angka)
            messagebox.showerror("Input Error", "Masukkan angka dalam menit!")  # Tampilkan pesan error

    def countdown(durasi):
        """
        Mengatur hitungan mundur dan memperbarui label di layar setiap detik.
        """
        if durasi > 0:  # Jika durasi masih tersisa
            mins, secs = divmod(durasi, 60)  # Konversi detik menjadi format menit:detik
            timer_label.config(text=f"{mins:02}:{secs:02}")  # Tampilkan sisa waktu
            timer_window.after(1000, countdown, durasi - 1)  # Panggil fungsi ini kembali setelah 1 detik
        else:  # Jika waktu habis
            timer_label.config(text="Waktu Habis!")  # Perbarui label menjadi "Waktu Habis"
            messagebox.showinfo("Selesai", "Waktu belajar selesai!")  # Tampilkan pesan selesai

    # Membuat jendela baru untuk fitur Timer Belajar
    timer_window = tk.Toplevel(app)
    timer_window.title("Timer Belajar")  # Judul jendela baru

    # Menampilkan label untuk meminta input durasi waktu belajar
    tk.Label(timer_window, text="Masukkan waktu belajar (menit):").pack(pady=5)

    # Kolom input untuk durasi waktu belajar
    entry_timer = tk.Entry(timer_window)
    entry_timer.pack(pady=5)

    # Tombol untuk memulai timer
    tk.Button(timer_window, text="Mulai", command=start_timer).pack(pady=5)

    # Label untuk menampilkan waktu hitungan mundur
    timer_label = tk.Label(timer_window, text="00:00", font=("Helvetica", 16)) #untuk menampilkan waktu hitungan mundur
    timer_label.pack(pady=10)

# Fungsi Catatan Harian
def catatan_harian():
    """
    Membuka jendela baru untuk membuat, membaca, dan menyimpan catatan harian.
    """

    def simpan_catatan():
        """
        Menyimpan isi catatan dari area teks ke file bernama 'catatan_harian.txt'.
        """
        with open("catatan_harian.txt", "w") as file:
            file.write(text_area.get("1.0", tk.END))  # Simpan teks mulai dari awal hingga akhir
        messagebox.showinfo("Sukses", "Catatan berhasil disimpan!")  # Tampilkan pesan sukses

    def baca_catatan():
        """
        Membaca catatan dari file 'catatan_harian.txt' dan menampilkannya di area teks.
        """
        try:
            with open("catatan_harian.txt", "r") as file:
                text_area.delete("1.0", tk.END)  # Bersihkan area teks sebelum memuat catatan
                text_area.insert(tk.END, file.read())  # Masukkan isi file ke area teks
        except FileNotFoundError:  # Jika file tidak ditemukan
            messagebox.showerror("Error", "Tidak ada catatan yang ditemukan!")  # Tampilkan pesan error

    # Membuat jendela baru untuk fitur Catatan Harian
    catatan_window = tk.Toplevel(app)
    catatan_window.title("Catatan Harian")  # Judul jendela baru

    # Area teks untuk menulis catatan
    text_area = tk.Text(catatan_window, wrap="word")  # Bungkus kata secara otomatis
    text_area.pack(pady=5)

    # Tombol untuk menyimpan catatan
    tk.Button(catatan_window, text="Simpan", command=simpan_catatan).pack(pady=5)

    # Tombol untuk membaca catatan
    tk.Button(catatan_window, text="Baca", command=baca_catatan).pack(pady=5)

# Fungsi To-Do List
def todo_list():
    """
    Membuka jendela baru untuk mengelola daftar tugas harian.
    """

    def tambah_tugas():
        """
        Menambahkan tugas baru ke daftar tugas.
        """
        listbox.insert(tk.END, entry_tugas.get())  # Tambahkan tugas ke listbox
        entry_tugas.delete(0, tk.END)  # Bersihkan input setelah tugas ditambahkan

    def hapus_tugas():
        """
        Menghapus tugas yang dipilih dari daftar tugas.
        """
        selected = listbox.curselection()  # Ambil item yang dipilih
        for idx in reversed(selected):  # Hapus dari akhir ke awal untuk mencegah indeks bergeser
            listbox.delete(idx)

    def hapus_semua():
        """
        Menghapus semua tugas dari daftar.
        """
        listbox.delete(0, tk.END)  # Hapus semua item di listbox

    # Membuat jendela baru untuk fitur To-Do List
    todo_window = tk.Toplevel(app)
    todo_window.title("To-Do List")  # Judul jendela baru

    # Label dan input untuk menambah tugas
    tk.Label(todo_window, text="Masukkan Tugas:").pack(pady=5)
    entry_tugas = tk.Entry(todo_window)  # Input untuk tugas baru
    entry_tugas.pack(pady=5)

    # Tombol untuk menambah, menghapus, dan menghapus semua tugas
    tk.Button(todo_window, text="Tambah", command=tambah_tugas).pack(pady=5)
    tk.Button(todo_window, text="Hapus", command=hapus_tugas).pack(pady=5)
    tk.Button(todo_window, text="Hapus Semua", command=hapus_semua).pack(pady=5)

    # Listbox untuk menampilkan daftar tugas
    listbox = tk.Listbox(todo_window)
    listbox.pack(pady=5)

# Fungsi Kalkulator
def kalkulator():
    """
    Membuka jendela baru untuk melakukan perhitungan sederhana.
    """

    def masukkan_angka(angka):
        """
        Memasukkan angka atau operator ke dalam input kalkulator.
        """
        entry_calculator.insert(tk.END, angka)  # Tambahkan angka/operator ke input

    def hitung():
        """
        Menghitung hasil dari ekspresi matematika yang dimasukkan.
        """
        try:
            result = eval(entry_calculator.get())  # Evaluasi ekspresi matematika
            entry_calculator.delete(0, tk.END)  # Bersihkan input
            entry_calculator.insert(0, str(result))  # Tampilkan hasil
        except Exception:  # Jika ada error dalam evaluasi
            entry_calculator.delete(0, tk.END)
            entry_calculator.insert(0, "Error")  # Tampilkan pesan error

    def clear():
        """
        Membersihkan semua input di kalkulator.
        """
        entry_calculator.delete(0, tk.END)  # Bersihkan input

    # Membuat jendela baru untuk Kalkulator
    calc_window = tk.Toplevel(app)
    calc_window.title("Kalkulator Sederhana")  # Judul jendela baru

    # Input untuk ekspresi matematika
    entry_calculator = tk.Entry(calc_window, justify="right")  # Input rata kanan
    entry_calculator.grid(row=0, column=0, columnspan=4, pady=5)

    # Tombol angka dan operator untuk kalkulator
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]
    for text, row, col in buttons:  # Loop melalui daftar tombol
        if text == '=':
            tk.Button(calc_window, text=text, command=hitung).grid(row=row, column=col)
        elif text == 'C':
            tk.Button(calc_window, text=text, command=clear).grid(row=row, column=col)
        else:
            tk.Button(calc_window, text=text, command=lambda t=text: masukkan_angka(t)).grid(row=row, column=col)

# Fungsi Motivational Quote
def motivational_quote():
    """
    Menampilkan kutipan motivasi secara acak dalam kotak pesan.
    """
    quotes = [
        "Stay positive, work hard, make it happen!",
        "The future depends on what you do today.",
        "Don't stop until you're proud.",
        "Believe in yourself and all that you are.",
    ]
    quote = random.choice(quotes)  # Pilih kutipan secara acak
    messagebox.showinfo("Motivational Quote", quote)  # Tampilkan kutipan dalam kotak pesan

# Aplikasi Utama
app = tk.Tk()
app.title("Student Productivity Toolkit")  # Judul aplikasi utama

# Menu navigasi utama
menu_bar = Menu(app)  # Buat menu utama
app.config(menu=menu_bar)  # Tambahkan menu ke aplikasi

# Tambahkan menu untuk setiap fitur
menu_bar.add_command(label="Timer Belajar", command=timer_belajar)
menu_bar.add_command(label="Catatan Harian", command=catatan_harian)
menu_bar.add_command(label="To-Do List", command=todo_list)
menu_bar.add_command(label="Kalkulator", command=kalkulator)
menu_bar.add_command(label="Motivational Quote", command=motivational_quote)

# Menjalankan aplikasi
app.mainloop()  # Loop utama aplikasi GUI
