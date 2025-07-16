# Website Portofolio

Website portofolio profesional dibuat dengan Flask, dengan desain modern menggunakan kombinasi warna putih, oranye, dan hitam, serta animasi scroll yang unik.

## Fitur
- Desain responsif yang cocok untuk semua perangkat
- Animasi fade-in dan slide-in saat scroll
- Tampilan profesional dengan font Poppins
- Mudah di-deploy ke platform seperti Render atau Heroku

## Cara Menjalankan Website Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan website di komputer Anda:

1. **Pastikan Python Terinstall**  
   - Pastikan Anda sudah menginstall Python versi 3.11 atau lebih baru. Cek dengan perintah:
     ```bash
     python --version
     ```
   - Jika belum terinstall, unduh dan install Python dari [python.org](https://www.python.org/downloads/).

2. **Unduh Kode Proyek**  
   - Jika kode dalam bentuk zip, ekstrak ke folder tertentu, misalnya `portfolio_website`.
   - Atau, jika menggunakan Git, jalankan:
     ```bash
     git clone <url-repositori>
     cd portfolio_website
     ```

3. **Buat dan Aktifkan Virtual Environment**  
   - Buat virtual environment untuk mengisolasi dependensi:
     ```bash
     python -m venv venv
     ```
   - Aktifkan virtual environment:
     - Untuk Windows:
       ```bash
       venv\Scripts\activate
       ```
     - Untuk Mac/Linux:
       ```bash
       source venv/bin/activate
       ```
     - Setelah aktif, Anda akan melihat `(venv)` di terminal.

4. **Install Dependensi**  
   - Install semua dependensi yang diperlukan:
     ```bash
     pip install -r requirements.txt
     ```

5. **Jalankan Website**  
   - Jalankan aplikasi Flask:
     ```bash
     python app.py
     ```
   - Jika berhasil, Anda akan melihat pesan bahwa server berjalan di `http://localhost:5000`.

6. **Akses Website**  
   - Buka browser (Chrome, Firefox, dll.) dan ketik:
     ```
     http://localhost:5000
     ```
   - Website akan muncul, dan Anda bisa menjelajahi halaman Home, About, Projects, dan Contact.

7. **Hentikan Server**  
   - Untuk menghentikan server, tekan `Ctrl+C` di terminal.

## Deployment
Untuk deploy ke Render atau Heroku:
1. Push kode ke GitHub.
2. Buat layanan web baru di Render/Heroku.
3. Gunakan perintah build: `pip install -r requirements.txt`.
4. Gunakan `Procfile` dan `runtime.txt` untuk konfigurasi.
5. Deploy dan akses situs yang sudah live.

## Kustomisasi
- Ganti gambar di `static/images/placeholder.jpg` dengan gambar proyek Anda.
- Edit konten di `templates/index.html` (nama, email, proyek).
- Sesuaikan warna atau gaya di `static/css/style.css`.