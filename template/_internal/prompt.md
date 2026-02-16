# Konteks Proyek: Sistem Auto-Post WordPress

Repositori ini dirancang untuk mengotomatisasi publikasi postingan blog ke website **[NAMA WEBSITE]** menggunakan plugin **Git It Write**.

## 1. Ringkasan Proyek
- **Website:** [URL WEBSITE]
- **Tujuan:** Mengelola konten WordPress langsung dari repositori GitHub ini.
- **Mekanisme:** Menulis konten dalam format Markdown (.md), melakukan Push ke GitHub, yang kemudian memicu webhook untuk update ke website WordPress.
- **Plugin Utama:** [Git It Write](https://wordpress.org/plugins/git-it-write-github-to-wordpress/)

## 2. Struktur Direktori
```
/ (Root)       -> Berisi README.md dan file sistem.
/blog/         -> FOLDER UTAMA. Simpan semua artikel di sini.
/blog/_images/ -> Simpan semua gambar di sini. WAJIB agar terbaca oleh plugin.
/_internal/    -> File internal (prompt, data, laporan). Tidak akan terbit.
```

## 3. Cara Membuat Postingan Baru
1. **Buat file .md** di dalam folder `blog`.
2. **Tambahkan Front Matter** (Metadata) di bagian paling atas file:
    ```yaml
    ---
    title: "Judul Artikel Anda"
    date: YYYY-MM-DD
    categories: [Nama Kategori]
    tags: [tag1, tag2]
    status: publish  # Pilihan: publish, draft
    ---
    ```
3. **Tulis Konten** menggunakan format Markdown standar.

## 4. Cara Menambahkan Gambar
1. Upload file gambar ke folder `blog/_images` (contoh: `blog/_images/foto-baru.jpg`).
2. Panggil gambar tersebut di markdown menggunakan **relative path**:
    ```markdown
    ![Deskripsi Gambar](/_images/foto-baru.jpg)
    ```

## 5. Konfigurasi Teknis (Perlu Disetting)
- **Plugin:** Git It Write
- **Repository:** `[USERNAME_GITHUB]/[NAMA_REPOSITORY]`
- **Source:** Branch `master`, Folder `blog`.
- **Auth:** Menggunakan GitHub Personal Access Token.
- **Otomatisasi:** Setup Webhook di GitHub untuk trigger update saat ada Push.

## 6. Kategori yang Digunakan
Sesuaikan dengan kategori di WordPress Anda:
- [Nama Kategori 1]
- [Nama Kategori 2]
- [Nama Kategori 3]

## 7. Alat Admin
- **Daftar Topik:** Lihat `data.txt` untuk daftar topik artikel yang direncanakan.
- **Laporan:** Lihat `laporan_implementasi.md` untuk format laporan status.
- **Log:** Cek WordPress Admin > Posts untuk melihat konten yang sudah terbit.
