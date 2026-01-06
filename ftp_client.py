from ftplib import FTP

def main():
    # --- LANGKAH 1: KONEKSI [cite: 200] ---
    print("1. Menghubungkan ke server...")
    ftp = FTP('ftp.dlptest.com', timeout=60) # Inisialisasi koneksi FTP [cite: 33]
    ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
    print("   Status: Berhasil Login!")

    # --- LANGKAH 2: EKSPLORASI [cite: 201] ---
    print("\n2. Eksplorasi Direktori...")
    print("   Direktori saat ini:", ftp.pwd()) # Cetak direktori kerja [cite: 46]
    
    print("   Daftar file di server:")
    files = ftp.nlst() # Ambil daftar file [cite: 55]
    for f in files:
        print("   -", f)

    # --- LANGKAH 3: UNGGAH (UPLOAD)  ---
    # Pastikan file 'biodata.txt' sudah kamu buat di langkah 1 tadi!
    print("\n3. Mengunggah biodata.txt...")
    filename = 'biodata.txt'
    
    try:
        with open(filename, 'rb') as file_obj: # Buka mode read binary [cite: 99]
            ftp.storbinary(f'STOR {filename}', file_obj) # Perintah STOR [cite: 102]
        print(f"   Status: File {filename} berhasil diunggah.")
    except FileNotFoundError:
        print(f"   ERROR: File {filename} tidak ditemukan di laptopmu! Buat dulu file-nya.")

    # --- LANGKAH 4: VERIFIKASI [cite: 203] ---
    print("\n4. Verifikasi Upload...")
    files_baru = ftp.nlst() # Ambil daftar file terbaru
    if filename in files_baru:
        print(f"   Sukses! {filename} sudah ada di dalam server.")
    else:
        print(f"   Gagal! {filename} tidak terlihat di server.")

    # --- LANGKAH 5: UNDUH (DOWNLOAD) [cite: 204] ---
    # Kita coba download salah satu file, misalnya 'readme.txt'. 
    # Jika tidak ada readme.txt di server, kode ini akan error, jadi sesuaikan nama filenya.
    file_target = 'biodata.txt' 
    file_lokal_baru = 'downloaded_biodata.txt' # Nama file simpanan [cite: 205]

    print(f"\n5. Mengunduh {file_target}...")
    
    # Cek dulu apakah file target ada di server
    if file_target in files_baru:
        with open(file_lokal_baru, 'wb') as f: # Buka mode write binary [cite: 80]
            ftp.retrbinary(f'RETR {file_target}', f.write) # Perintah RETR [cite: 83]
        print(f"   Status: Berhasil diunduh sebagai {file_lokal_baru}")
    else:
        print(f"   Info: File '{file_target}' tidak ditemukan di server, lewati download.")

    # --- LANGKAH 6: PEMBERSIHAN [cite: 206] ---
    ftp.quit() # Tutup koneksi [cite: 139]
    print("\n6. Koneksi ditutup. Selesai.")

if __name__ == "__main__":
    main()