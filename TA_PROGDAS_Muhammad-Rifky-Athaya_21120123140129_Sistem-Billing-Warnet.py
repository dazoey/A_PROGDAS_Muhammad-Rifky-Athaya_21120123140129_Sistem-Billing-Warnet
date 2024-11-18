import tkinter as tk
from tkinter import messagebox
from collections import deque

class Pelanggan:
    def __init__(self, nama, jam):
        self.nama = nama
        self.jam = jam
        self.tarif = 3000  
    def get_nama(self):
        return self.nama
    def set_nama(self, nama):
        self.nama = nama
    def get_jam(self):
        return self.jam
    def set_jam(self, jam):
        self.jam = jam
    def hitung_tagihan(self):
        return self.jam * self.tarif

class RentalWarnet:
    def __init__(self, root):
        self.root = root
        self.root.title("Rental Warnet Mamad Resing")
        
        self.antrian = deque()
        self.riwayat = []

        self.buat_widget()

    def buat_widget(self):
        self.label_nama = tk.Label(self.root, text="Nama Pelanggan")
        self.label_nama.pack()
        self.entri_nama = tk.Entry(self.root)
        self.entri_nama.pack()
        self.label_jam = tk.Label(self.root, text="Durasi Rental (jam)")
        self.label_jam.pack()
        self.entri_jam = tk.Entry(self.root)
        self.entri_jam.pack()
        self.tombol_tambah = tk.Button(self.root, text="Tambahkan ke Antrian", command=self.tambah_ke_antrian)
        self.tombol_tambah.pack()
        self.tombol_proses = tk.Button(self.root, text="Proses Antrian Berikutnya", command=self.proses_pelanggan)
        self.tombol_proses.pack()
        self.area_tampilan = tk.Text(self.root, height=10, width=50)
        self.area_tampilan.pack()

        self.perbarui_tampilan()

    def tambah_ke_antrian(self):
        nama = self.entri_nama.get()
        jam = self.entri_jam.get()

        if not nama or not jam:
            messagebox.showwarning("Kesalahan Input", "Mohon masukkan nama dan durasi rental.")
            return
        try:
            jam = int(jam)
        except ValueError:
            messagebox.showwarning("Kesalahan Input", "Durasi rental harus berupa angka.")
            return
        
        pelanggan = Pelanggan(nama, jam)
        self.antrian.append(pelanggan)
        self.perbarui_tampilan()

    def proses_pelanggan(self):
        if not self.antrian:
            messagebox.showinfo("Antrian Kosong", "Tidak ada pelanggan dalam antrian.")
            return

        pelanggan = self.antrian.popleft()
        tagihan = pelanggan.hitung_tagihan()
        messagebox.showinfo("Tagihan", f"Pelanggan: {pelanggan.get_nama()}\nDurasi: {pelanggan.get_jam()} jam\nTotal Tagihan: Rp{tagihan}")
        self.riwayat.append(f"{pelanggan.get_nama()}: Rp{tagihan}")
        self.perbarui_tampilan()

    def perbarui_tampilan(self):
        self.area_tampilan.delete(1.0, tk.END)
        self.area_tampilan.insert(tk.END, "Antrian:\n")
        for pelanggan in self.antrian:
            self.area_tampilan.insert(tk.END, f"{pelanggan.get_nama()} - {pelanggan.get_jam()} jam\n")
        
        self.area_tampilan.insert(tk.END, "\nRiwayat:\n")
        for catatan in reversed(self.riwayat):
            self.area_tampilan.insert(tk.END, f"{catatan}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalWarnet(root)
    root.mainloop()
