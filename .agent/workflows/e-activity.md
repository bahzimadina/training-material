---
description: Membuat latihan berbasis Bloom’s Taxonomy (The Facilitator)
---

1. Baca `slides/Sesi{n}/SlideSesi{n}.md` (atau file-file topik individual).
2. Baca `references/activity-format.md` dan `references/bloom-taxonomy-guide.md`
// turbo
3. Buat folder `activities/activity_{n}/` untuk sesi yang dikerjakan.
4. Gunakan `mcp_notebooklm-mcp_notebook_query` dengan query: 
   "Berdasarkan materi pada slide [Slide Content], buat 12 aktivitas yang mencakup seluruh level Taxonomy Bloom:
    - C1-C2 (Pemahaman): 4 aktivitas.
    - C3-C4 (Analisis): 4 aktivitas.
    - C5-C6 (Evaluasi/Kreasi): 4 aktivitas.
   Format: Bahasa Indonesia, bergaya Trainer Professional."
5. Tulis hasil per kategori ke sesuai dengan format `references/activity-format.md`:
   - `activities/activity_{n}/activity_taxC1C2-n.md`
   - `activities/activity_{n}/activity_taxC3C4-n.md`
   - `activities/activity_{n}/activity_taxC5C6-n.md`
// turbo
6. Setelah selesai, jalankan: 
   `python3 scripts/merge_contents.py activities/activity_{n}/ ActivitySesi{n}.md activity_tax`