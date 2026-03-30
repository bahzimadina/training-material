---
description: Ekstraksi data dari MCP menjadi struktur materi (The Architect)
---

1. Gunakan `mcp_notebooklm-mcp_notebook_list` untuk melihat daftar notebook yang tersedia.
2. Identifikasi notebook yang relevan dengan topik training.
3. Gunakan `mcp_notebooklm-mcp_notebook_query` dengan query: 
   "Rangkum seluruh materi dari notebook ini. Buat struktur kurikulum dalam format tabel Markdown dengan kolom | Sesi | Materi & Aktivitas Utama |. Pastikan pembagian sesi logis untuk durasi training yang standar (misal 1 hari = 4-6 sesi)."
4. Tulis hasil rangkuman tersebut ke `curriculum/curriculum.md` sesuaikan format dengan `references/activity-format.md`.
5. Pastikan `curriculum.md` memiliki satu H1 judul utama.