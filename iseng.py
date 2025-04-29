
import os
import csv

FILENAME = ('C:\\Users\Lenovo\OneDrive\Documents\Data\data_nilai.txt')

def tampilkan_data():
    if not os.path.exists(FILENAME):
        print("Belum ada data yang disimpan.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        print("NIS, Nama Siswa, Kelas, Mata Pelajaran, Nilai Akhir")
        for row in reader:
            print(", ".join(row))

def tambah_data():
    nis = input("Masukkan NIS: ")
    nama = input("Masukkan Nama Siswa: ")
    kelas = input("Masukkan Kelas: ")
    mata_pelajaran = input("Masukkan Mata Pelajaran: ")
    nilai = float(input("Masukkan Nilai Akhir (0-100): "))

    if 0 <= nilai <= 100:
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nis, nama, kelas, mata_pelajaran, nilai])
        print("Data berhasil ditambahkan.")
    else:
        print("Error: Nilai harus antara 0 dan 100.")

def edit_data():
    if not os.path.exists(FILENAME):
        print("Belum ada data yang disimpan.")
        return

    nis = input("Masukkan NIS siswa yang ingin diedit: ")
    found = False
    rows = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nis:
                found = True
                print("Data ditemukan:", row)
                nama = input("Masukkan Nama Siswa baru: ")
                kelas = input("Masukkan Kelas baru: ")
                mata_pelajaran = input("Masukkan Mata Pelajaran baru: ")
                nilai = float(input("Masukkan Nilai Akhir baru (0-100): "))

                if 0 <= nilai <= 100:
                    rows.append([nis, nama, kelas, mata_pelajaran, nilai])
                    print("Data berhasil diedit.")
                else:
                    print("Error: Nilai harus antara 0 dan 100.")
                    rows.append(row)  # Simpan data lama jika nilai tidak valid
            else:
                rows.append(row)

    if not found:
        print("Data dengan NIS tersebut tidak ditemukan.")

    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def hapus_data():
    if not os.path.exists(FILENAME):
        print("Belum ada data yang disimpan.")
        return

    nis = input("Masukkan NIS siswa yang ingin dihapus: ")
    found = False
    rows = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nis:
                found = True
                print("Data ditemukan dan akan dihapus:", row)
            else:
                rows.append(row)

    if found:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Data berhasil dihapus.")
    else:
        print("Data dengan NIS tersebut tidak ditemukan.")

def main():
    while True:
        print("\nMenu Pengelolaan Data Nilai Siswa")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            edit_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
