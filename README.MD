# Training Material Generator

Sistem otomatisasi pembuatan materi pelatihan (Kurikulum, Slide, dan Aktivitas) berbasis kurikulum menggunakan **NotebookLM MCP** sebagai sumber pengetahuan utama.

## 🚀 Fitur Utama

- **Source-Grounded**: Seluruh materi dihasilkan berdasarkan research dari NotebookLM.
- **Pedagogis**: Aktivitas belajar disusun menggunakan Bloom's Taxonomy (C1-C6).
- **Modular**: Pembuatan materi dilakukan per sesi untuk kontrol kualitas yang lebih baik.
- **Marp Compatible**: Slide dihasilkan dalam format Markdown yang siap dipresentasikan menggunakan Marp.

## 📁 Struktur Folder

```
.
├── .agent/
│   ├── workflows/        # Definisi perintah agen (/e-plan, etc.)
│   ├── gemini.json       # Konfigurasi persona dan batasan
│   └── antigravity.json  # Identitas dan kapabilitas agen
├── curriculum/           # Roadmap dan struktur pelatihan
├── slides/               # Konten slide per sesi (Markdown)
├── activities/           # Bank soal dan aktivitas peserta
├── scripts/              # Script utility (merge_contents.py)
├── references/           # Template dan referensi format
└── SKILL.md              # Dokumentasi teknis alur kerja agen
```

## 🛠️ Persiapan

1. **NotebookLM MCP**: Pastikan Anda telah memiliki akses ke `notebooklm-mcp`.
2. **Login**: Jalankan perintah `nlm login` jika belum terautentikasi.
3. **Environment**: Gunakan VS Code dengan ekstensi Antigravity untuk pengalaman terbaik.

## 📖 Alur Kerja (Workflows)

Gunakan perintah `/slash` berikut di chat Antigravity untuk memulai:

1.  **/e-plan** (The Orchestrator): Inisialisasi folder dan cek dependensi.
2.  **/e-curriculum** (The Architect): Membuat rencana kurikulum dari sumber data.
3.  **/e-slide** (The Storyteller): Menghasilkan slide materi per sesi secara detail.
4.  **/e-activity** (The Facilitator): Menghasilkan latihan dan kuis untuk peserta.

---
*Generated with 🤖 Antigravity Agent*
