---
description: Validasi lingkungan dan pembuatan blueprint (The Orchestrator)
---

1. Periksa apakah `notebooklm-mcp` tersedia dengan menggunakan `list_resources` atau `mcp_server_info`.
2. Jika tidak tersedia, informasikan pengguna untuk menjalankan `nlm login`.
// turbo
3. Buat struktur folder utama jika belum ada: `curriculum/`, `slides/`, `activities/`, `scripts/`.
4. Jika file `curriculum.md` tidak ditemukan di folder `curriculum/`, berikan peringatan bahwa langkah selanjutnya (`e-curriculum`) diperlukan.
5. Verifikasi keberadaan `scripts/merge_contents.py`, `.agent/gemini.json`, dan `.agent/antigravity.json`. Jika tidak ada, buat file tersebut.
