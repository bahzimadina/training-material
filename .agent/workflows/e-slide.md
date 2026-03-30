---
description: Generasi slide per sesi secara granular (The Storyteller)
---

1. Baca `curriculum/curriculum.md` untuk menentukan jumlah sesi dan sub-topik.
2. Baca `references/slide-format.md`
// turbo
2. Buat folder `slides/Sesi{n}/` untuk sesi yang akan dikerjakan.
3. Untuk setiap sub-topik, gunakan `mcp_notebooklm-mcp_notebook_query` untuk mendapatkan detail materi.
4. Simpan hasil ke `slides/Sesi{n}/slide_topik{n}_{subtopik}.md` dengan format:
   - Cover.
   - Capaian Pembelajaran.
   - Diskusi Singkat (Trigger).
   - Isi Topik #1 (Pembahasan Mendalam).
   - Isi Topik #2 (Pembahasan Mendalam).
   - Isi Topik #3 (Pembahasan Mendalam).
   - Isi Topik #4 (Pembahasan Mendalam).
   - Isi Topik #n.. (Pembahasan Mendalam).
   - Real Life App #1 (Contoh Nyata).
   - Real Life App #2 (Contoh Nyata).
   - Do & Don'ts.
   - Kesimpulan.
5. Gunakan Markdown yang kompatibel dengan Marp (gunakan `---` sebagai separator slide) dan sesuaikan dengan format `references/slide-format.md`.
// turbo
6. Setelah semua topik sesi selesai, jalankan: 
   `python3 scripts/merge_contents.py slides/Sesi{n}/ SlideSesi{n}.md slide_topik`