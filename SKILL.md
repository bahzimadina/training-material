# Agentic Workflow Skills - Training Material Generator

Workflow ini dirancang untuk otomatisasi pembuatan materi training (kurikulum, slide, dan aktivitas) menggunakan `notebooklm-mcp` sebagai Source of Truth.

## Dasar Perintah (Workflows)

| Perintah        | Nama Alias           | Deskripsi                                                    |
| :-------------- | :------------------- | :----------------------------------------------------------- |
| `/e-plan`       | **The Orchestrator** | Validasi lingkungan, pembuatan folder, dan cek dependensi.   |
| `/e-curriculum` | **The Architect**    | Ekstraksi data dari MCP menjadi struktur `curriculum.md`.    |
| `/e-slide`      | **The Storyteller**  | Generasi slide per sesi secara granular ke folder `slides/`. |
| `/e-activity`   | **The Facilitator**  | Membuat latihan berbasis Bloom’s Taxonomy (C1-C6).           |

## Struktur Proyek

- `curriculum/`: Berisi file `curriculum.md` (roadmap).
- `slides/`: Folder per sesi (`Sesi1/`, etc.) berisi materi slide.
- `activities/`: Folder per sesi (`activity_1/`, etc.) berisi latihan peserta.
- `scripts/`: Berisi `merge_contents.py` untuk penggabungan file otomatis.
- `.agent/gemini.json`: Konfigurasi global persona dan batasan (config).
- `.agent/antigravity.json`: Identitas dan kapabilitas Antigravity agent (config).

## Pedoman Konten (Constraint)

1.  **Bloom's Taxonomy**: Aktivitas wajib mengikuti kode kognitif 1-6.
2.  **Slide Format**: Markdown kompatibel dengan *Marp* (`---` separator).
3.  **Source Grounding**: Semua informasi harus berasal dari `notebooklm-mcp`. Jika tidak ada, tandai dengan `[NEED_CONTEXT]`.
4.  **Bahasa**: Bahasa Indonesia yang profesional namun menarik.

---

## Cara Menjalankan

1.  Jalankan `/e-plan` untuk inisialisasi.
2.  Jalankan `/e-curriculum` untuk membuat kerangka materi.
3.  Gunakan `/e-slide` untuk meng-generate konten slide per sesi.
4.  Selesaikan dengan `/e-activity` untuk membuat bank soal/aktivitas.
