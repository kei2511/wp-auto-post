# [NAMA WEBSITE] - Auto Post Repository

Repositori ini berfungsi sebagai "Content Management System" (CMS) berbasis Git untuk website **[NAMA WEBSITE]**.
Konten ditulis dalam format Markdown dan otomatis terbit ke WordPress melalui plugin **Git It Write**.

## :file_folder: Struktur Folder

Agar sistem berjalan lancar dan tidak error, harap patuhi struktur berikut:

- **`/blog/`** : **TEMPAT MENULIS ARTIKEL.** Semua file markdown (`.md`) dan folder `_images` ada di sini.
- **`/_internal/`** : Tempat menyimpan laporan, draft kasar, dan prompt AI. (Tidak akan terbit ke web).
- **`README.md`** : File panduan ini.

## :gear: Setup Awal

1. Buat repository baru di GitHub.
2. Install plugin **[Git It Write](https://wordpress.org/plugins/git-it-write-github-to-wordpress/)** di WordPress.
3. Konfigurasi plugin:
   - **Repository:** `[USERNAME_GITHUB]/[NAMA_REPOSITORY]`
   - **Branch:** `master`
   - **Folder:** `blog`
   - **Authentication:** Gunakan GitHub Personal Access Token.
4. Aktifkan Webhook di GitHub agar auto-sync saat Push.

## :rocket: Cara Menggunakan

1. Masuk ke folder `blog`.
2. Buat file artikel baru dengan format Markdown (`.md`).
3. Pastikan ada **Front Matter** (Judul, Tanggal, Kategori) di paling atas file:
   ```yaml
   ---
   title: "Judul Artikel Anda"
   date: YYYY-MM-DD
   categories: [Nama Kategori]
   tags: [tag1, tag2]
   status: publish
   ---
   ```
4. Lakukan `git add`, `git commit`, dan `git push`.
5. Artikel akan otomatis terbit di WordPress.

## :framed_picture: Cara Menambahkan Gambar

1. Upload file gambar ke folder `blog/_images/`.
2. Panggil gambar di markdown menggunakan relative path:
   ```markdown
   ![Deskripsi Gambar](/_images/nama-gambar.jpg)
   ```

## :warning: PENTING

- Jangan menaruh file `.md` di root (halaman depan), karena akan menyebabkan error pada plugin WordPress.
- Selalu simpan tulisan di dalam folder `blog/`.
- Pastikan Front Matter menggunakan format YAML yang benar (perhatikan tanda `-`, spasi, dan kutip).
