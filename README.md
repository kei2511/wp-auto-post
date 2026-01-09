# WP Auto Post Repository

Selamat datang di repositori sistem publikasi otomatis Blog Perusahaan.
Repositori ini berfungsi sebagai "Content Management System" (CMS) berbasis Git.

## :file_folder: Struktur Folder
Agar sistem berjalan lancar dan tidak error, harap patuhi struktur berikut:

- **`/blog/`** : **TEMPAT MENULIS ARTIKEL.** Semua file markdown (`.md`) dan folder `_images` ada di sini.
- **`/_internal/`** : Tempat menyimpan laporan, draft kasar, dan prompt AI. (Tidak akan terbit ke web).
- **`README.md`** : File panduan ini.

## :rocket: Cara Menggunakan

1.  Masuk ke folder `blog`.
2.  Buat file artikel baru dengan format Markdown.
3.  Pastikan ada **Front Matter** (Judul, Tanggal, Kategori) di paling atas file.
4.  Lakukan `git push`.
5.  Artikel akan otomatis terbit di WordPress.

## :warning: PENTING
Jangan menaruh file `.md` di halaman depan (root) ini, karena akan menyebabkan error pada plugin WordPress. Selalu simpan tulisan di dalam folder `blog`.
