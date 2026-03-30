# Format Slide (slide_topik_N.md & Slide_Sesi_N.md)

## Struktur File

```
Sesi_1/
├── slide_topik_1.md    ← Satu file per topik
├── slide_topik_2.md
└── slide_topik_N.md
Slide_Sesi_1.md         ← Gabungan semua topik + pembuka + penutup sesi
```

---

## Format Blok Slide

Setiap slide menggunakan template berikut:

```markdown
---

**Slide {N}: {Judul Slide}**
* **{Field 1}:** {isi}
* **{Field 2}:** {isi}

**Visualisasi:** {deskripsi visual yang disarankan, misal: diagram alur, ilustrasi, screenshot}

**Speaker Notes:**
{Catatan untuk presenter — apa yang harus diucapkan, konteks tambahan, pertanyaan pemantik}

---
```

> Pisahkan antar slide dengan garis `---`

---

## Template Lengkap Per Jenis Slide

### 1. Slide Cover/Judul Sesi
```markdown
---

**Slide 1: Judul Utama**
* **Judul Presentasi:** {Nama Sesi}
* **Sub-judul:** {Tagline atau deskripsi singkat sesi}
* **Pemateri/Tanggal:** {Nama Trainer} | {Tanggal}

**Visualisasi:** Gambar/ilustrasi representatif tema sesi, logo organisasi

**Speaker Notes:**
Sambut peserta, perkenalkan diri, dan berikan gambaran singkat apa yang akan dipelajari hari ini.
Sebutkan durasi sesi dan aturan dasar (boleh bertanya kapan saja, dll).

---
```

### 2. Slide Daftar Topik / Capaian Pembelajaran
```markdown
---

**Slide 2: Apa yang Akan Kita Pelajari Hari Ini**
* **Topik-topik:**
  1. {Topik 1}
  2. {Topik 2}
  3. {Topik N}
* **Capaian Pembelajaran:** Setelah sesi ini, peserta mampu {kata kerja Bloom} {hasil belajar}

**Visualisasi:** Roadmap visual atau daftar ikon per topik

**Speaker Notes:**
Jelaskan singkat setiap topik dan bagaimana topik-topik ini saling berkaitan.
Sebutkan level Taksonomi Bloom yang akan dicapai.

---
```

### 3. Slide Diskusi Pembuka (Pain Point)
```markdown
---

**Slide 3: Mari Kita Diskusi Dulu!**
* **Pertanyaan Diskusi:** {Pertanyaan terbuka yang relevan dengan topik sesi}
* **Contoh Pertanyaan:**
  - "{Pain point question 1}"
  - "{Pain point question 2}"

**Visualisasi:** Ikon diskusi/obrolan, atau gambar yang memancing percakapan

**Speaker Notes:**
Lemparkan pertanyaan ini ke peserta. Berikan 3–5 menit untuk diskusi kecil.
Catat poin-poin yang disebutkan peserta — ini akan jadi jembatan ke materi.
Gunakan jawaban peserta untuk memperkuat relevansi topik yang akan dibahas.

---
```

### 4. Slide Cover Topik
```markdown
---

**Slide {N}: Cover Topik — {Nama Topik}**
* **Judul Topik:** {Nama Topik}
* **Sub-judul:** {Deskripsi singkat atau pertanyaan kunci topik ini}
* **Level Bloom:** {C1 Remember / C2 Understand / C3 Apply / dst}

**Visualisasi:** Ikon atau ilustrasi representatif topik

**Speaker Notes:**
Transisi ke topik baru. Jelaskan mengapa topik ini penting dan apa kaitannya dengan topik sebelumnya.

---
```

### 5. Slide Pembahasan (berulang sebanyak sub-topik minimal 3 topik)
```markdown
---

**Slide {N}: {Judul Sub-Topik / Konsep Kunci}**
* **Konsep:** {Definisi atau penjelasan utama}
* **Poin Kunci:**
  - {Poin 1}
  - {Poin 2}
  - {Poin 3}
* **Contoh:** {Contoh konkret atau analogi}

**Visualisasi:** {Diagram, tabel perbandingan, screenshot, atau infografis sesuai konten}

**Speaker Notes:**
{Penjelasan mendalam untuk presenter. Sertakan analogi, cerita pendek, atau fakta menarik.
Sebutkan pertanyaan yang mungkin muncul dari peserta dan cara menjawabnya.}

---
```

### 6. Slide Real Life Application (berulang sebanyak minimal 2 real life)
```markdown
---

**Slide {N}: Penerapan Nyata — {Nama Topik}**
* **Skenario:** {Situasi nyata yang relevan dengan pekerjaan/kehidupan peserta}
* **Bagaimana {Topik} Membantu:**
  - {Manfaat/penerapan 1}
  - {Manfaat/penerapan 2}
* **Studi Kasus:** {Contoh kasus nyata atau hipotetis yang relevan}

**Visualisasi:** Foto atau screenshot penerapan nyata, atau diagram alur proses

**Speaker Notes:**
Hubungkan materi dengan konteks pekerjaan sehari-hari peserta.
Ajak peserta berbagi pengalaman mereka sendiri jika ada.

---
```

### 7. Slide Do and Don't
```markdown
---

**Slide {N}: Do & Don't — {Nama Topik}**

| ✅ LAKUKAN | ❌ JANGAN |
|---|---|
| {Do 1} | {Don't 1} |
| {Do 2} | {Don't 2} |
| {Do 3} | {Don't 3} |

**Visualisasi:** Tabel dua kolom dengan ikon centang hijau dan silang merah

**Speaker Notes:**
Tekankan kesalahan umum yang sering terjadi. Berikan alasan mengapa setiap "Don't" perlu dihindari.
Jika ada, ceritakan contoh nyata akibat mengabaikan poin-poin ini.

---
```

### 8. Slide Kesimpulan Topik
```markdown
---

**Slide {N}: Rangkuman — {Nama Topik}**
* **Poin Utama yang Dipelajari:**
  1. {Poin kunci 1}
  2. {Poin kunci 2}
  3. {Poin kunci N}
* **Kata Kunci:** {keyword-1}, {keyword-2}, {keyword-N}
* **Ingat Selalu:** {One-liner takeaway paling penting}

**Visualisasi:** Infografis ringkasan atau mind map mini

**Speaker Notes:**
Rangkum dengan mengulang 2–3 poin terpenting. Tanyakan apakah ada pertanyaan sebelum lanjut.
Berikan transisi ke topik berikutnya atau ke sesi penutup.

---
```

### 9. Slide Kesimpulan Sesi
```markdown
---

**Slide {N}: Kesimpulan Sesi {X}**
* **Hari Ini Kita Telah Mempelajari:**
  1. {Topik 1}: {satu kalimat ringkasan}
  2. {Topik 2}: {satu kalimat ringkasan}
  3. {Topik N}: {satu kalimat ringkasan}
* **Capaian Pembelajaran Tercapai:** ✅ {capaian yang sudah dicapai}
* **Next Steps:** {Apa yang perlu dilanjutkan / dipraktikkan / dipelajari sendiri}

**Visualisasi:** Checklist visual atau roadmap yang menandai progress peserta

**Speaker Notes:**
Tutup sesi dengan energi positif. Berikan apresiasi atas partisipasi peserta.
Ingatkan tentang tugas/aktivitas yang perlu diselesaikan sebelum sesi berikutnya.

---
```

---

## Panduan Kualitas Slide

### Prinsip Desain Konten
- **1 slide = 1 ide utama** — jangan paksakan terlalu banyak informasi
- **Bullet max 5 poin** per slide
- **Speaker Notes wajib ada** — ini panduan presenter, bukan ringkasan slide
- **Visualisasi selalu dideskripsi** — trainer bisa membuat visual berdasarkan deskripsi ini

### Query notebooklm-mcp per Topik
Saat membuat setiap file slide topik, selalu query notebooklm-mcp dengan:
```
"Berikan [3-5] poin kunci, contoh nyata, dan praktik terbaik tentang {NAMA_TOPIK}
dalam konteks {NAMA_TRAINING} untuk peserta {TARGET_PESERTA}.
Sertakan: definisi, manfaat utama, kesalahan umum yang harus dihindari,
dan satu skenario penerapan nyata."
```

### Pengecekan Kualitas
- [ ] Setiap topik memiliki semua jenis slide (cover → pembahasan → real life → do&don't → kesimpulan)
- [ ] Speaker notes cukup detail untuk presenter yang baru
- [ ] Visualisasi dideskripsi dengan jelas
- [ ] Konten relevan dengan level Bloom yang ditargetkan di sesi ini
- [ ] Ada koneksi antar topik dalam satu sesi
