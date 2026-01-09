# Konteks Proyek: Sistem Auto-Post WordPress

Repositori ini dirancang untuk mengotomatisasi publikasi postingan blog ke website WordPress menggunakan plugin **Git It Write**.

## 1. Ringkasan Proyek
- **Tujuan:** Mengelola konten WordPress (Artikel) langsung dari repositori GitHub ini.
- **Mekanisme:** Menulis konten dalam format Markdown (.md), melakukan Push ke GitHub, yang kemudian memicu webhook untuk update ke website WordPress.
- **Plugin Utama:** [Git It Write](https://wordpress.org/plugins/git-it-write-github-to-wordpress/)

## 2. Struktur Direktori
```
/ (Root)      -> Berisi README.md dan file sistem.
/blog/        -> FOLDER UTAMA. Simpan semua artikel di sini.
/blog/_images/ -> Simpan semua gambar di sini. WAJIB agar terbaca oleh plugin.
```

## 3. Cara Membuat Postingan Baru
1.  **Buat file .md** di dalam folder `blog`.
2.  **Tambahkan Front Matter** (Metadata) di bagian paling atas file:
    ```yaml
    ---
    title: Judul Artikel Anda
    date: YYYY-MM-DD
    categories: [Nama Kategori]
    tags: [tag1, tag2]
    status: publish  # Pilihan: publish, draft
    ---
    ```
3.  **Tulis Konten** menggunakan format Markdown standar.

## 4. Cara Menambahkan Gambar
1.  Upload file gambar ke folder `blog/_images` (contoh: `blog/_images/foto-baru.jpg`).
2.  Panggil gambar tersebut di markdown menggunakan **relative path**:
    ```markdown
    ![Deskripsi Gambar](/_images/foto-baru.jpg)
    ```

## 5. Konfigurasi Teknis (Sudah Disetting)
- **Plugin:** Git It Write
- **Source:** Branch `master`, Folder `blog`.
- **Auth:** Menggunakan GitHub Personal Access Token.
- **Otomatisasi:** Webhook sudah diatur di GitHub untuk trigger update saat ada Push.

## 6. Alat Admin
- **Laporan:** Lihat `laporan_implementasi.md` untuk format laporan status harian.
- **Log:** Cek WordPress Admin > Posts untuk melihat konten yang sudah terbit.