# Format Activity (activity_taxN-N.md & Activity_Sesi_N.md)

## Struktur File

```
activity_1/
├── activity_tax1-1.md    ← C1 Remember, aktivitas ke-1
├── activity_tax1-2.md    ← C1 Remember, aktivitas ke-2
├── activity_tax2-1.md    ← C2 Understand, aktivitas ke-1
├── activity_tax2-2.md    ← C2 Understand, aktivitas ke-2
├── activity_tax3-1.md    ← C3 Apply, aktivitas ke-1
├── activity_tax3-2.md    ← C3 Apply, aktivitas ke-2
├── activity_tax4-1.md    ← C4 Analyze, aktivitas ke-1
├── activity_tax4-2.md    ← C4 Analyze, aktivitas ke-2
├── activity_tax5-1.md    ← C5 Evaluate, aktivitas ke-1
├── activity_tax5-2.md    ← C5 Evaluate, aktivitas ke-2
├── activity_tax6-1.md    ← C6 Create, aktivitas ke-1
└── activity_tax6-2.md    ← C6 Create, aktivitas ke-2
Activity_Sesi_1.md        ← File gabungan semua aktivitas sesi 1
```

> **Catatan:** Jumlah level Bloom yang digunakan bisa disesuaikan dengan durasi sesi.
> Untuk sesi pendek (1–2 jam), fokus ke 2–3 level. Untuk sesi penuh (4+ jam), gunakan semua 6 level.

---

## Format File Activity

### Template Standar

```markdown
---

ACTIVITY #{NUMBER_ACTIVITY} : {JUDUL AKTIVITAS}

TOPIK       : {Topik dari slide yang menjadi dasar aktivitas ini}
LEVEL BLOOM : {C1 - Remember / C2 - Understand / C3 - Apply / C4 - Analyze / C5 - Evaluate / C6 - Create}
DURASI      : {estimasi waktu, misal: 10 menit / 20 menit / 30 menit}
MEDIA       : {alat yang dibutuhkan: laptop, kertas, whiteboard, dll}

TUJUAN
{Satu atau dua kalimat yang menjelaskan apa yang peserta akan capai setelah aktivitas ini.
Gunakan kata kerja operasional Taksonomi Bloom yang sesuai dengan level.}

LANGKAH-LANGKAH
1. {Langkah pertama — deskripsi jelas dan spesifik}
2. {Langkah kedua}
3. {Langkah ketiga}
4. {Langkah selanjutnya, tambahkan sebanyak yang diperlukan}
{Ulangi sesuai kompleksitas aktivitas}

CODE_TAXONOMY : {C1 / C2 / C3 / C4 / C5 / C6}

PERTANYAAN REFLEKSI
1. {Pertanyaan refleksi pertama — mendorong peserta memikirkan kembali apa yang telah dilakukan}
2. {Pertanyaan refleksi kedua — mengaitkan pengalaman dengan konteks nyata}
3. {Pertanyaan refleksi ketiga — opsional, dorong peserta ke level berpikir lebih tinggi}

---
```

---

## Contoh Aktivitas per Level Bloom

### C1 — Remember (Mengingat)

```markdown
---

ACTIVITY #1 : KARTU KILAT TERMINOLOGI AI

TOPIK       : Dasar-Dasar AI Generatif
LEVEL BLOOM : C1 - Remember
DURASI      : 10 menit
MEDIA       : Kartu fisik atau dokumen digital

TUJUAN
Peserta mampu menyebutkan dan mengenali minimal 10 istilah kunci dalam AI Generatif
beserta definisi singkatnya.

LANGKAH-LANGKAH
1. Trainer membagikan kartu/daftar berisi 10 istilah AI (Prompt, LLM, Token, dll).
2. Peserta membaca kartu selama 3 menit tanpa mencatat.
3. Trainer mengambil kartu dan meminta peserta menuliskan sebanyak mungkin istilah yang diingat.
4. Bandingkan hasilnya berpasangan, lengkapi yang terlewat.
5. Diskusikan bersama: istilah apa yang paling sulit diingat dan mengapa?

CODE_TAXONOMY : C1

PERTANYAAN REFLEKSI
1. Istilah mana yang sudah familiar sebelum training dan mana yang baru pertama kali kamu dengar?
2. Apa strategi yang kamu gunakan untuk mengingat istilah-istilah baru?
3. Mengapa penting memahami terminologi dasar sebelum masuk ke praktik?

---
```

### C2 — Understand (Memahami)

```markdown
---

ACTIVITY #3 : JELASKAN DENGAN BAHASAMU SENDIRI

TOPIK       : Cara Kerja Large Language Model
LEVEL BLOOM : C2 - Understand
DURASI      : 15 menit
MEDIA       : Kertas atau sticky note

TUJUAN
Peserta mampu menjelaskan konsep cara kerja LLM menggunakan analogi atau bahasa
sehari-hari yang mudah dipahami orang awam.

LANGKAH-LANGKAH
1. Trainer menampilkan 3 konsep kunci: Token, Probabilitas, Context Window.
2. Peserta secara individu menulis penjelasan masing-masing konsep TANPA menggunakan
   istilah teknis (gunakan analogi, perumpamaan, atau cerita pendek).
3. Peserta berbagi penjelasannya dengan pasangan dan saling memberikan umpan balik.
4. Beberapa peserta dipilih untuk mempresentasikan penjelasan terbaik ke kelas.
5. Trainer memberikan klarifikasi dan penguatan.

CODE_TAXONOMY : C2

PERTANYAAN REFLEKSI
1. Analogi apa yang kamu gunakan dan mengapa kamu merasa itu paling tepat?
2. Apakah ada miskonsepsi yang kamu temukan saat menjelaskan ke pasangan?
3. Bagaimana cara kamu menjelaskan ini ke rekan kerja yang tidak punya latar belakang teknologi?

---
```

### C3 — Apply (Menerapkan)

```markdown
---

ACTIVITY #5 : HANDS-ON PROMPTING CHALLENGE

TOPIK       : Teknik Prompting dengan Framework PARTS
LEVEL BLOOM : C3 - Apply
DURASI      : 25 menit
MEDIA       : Laptop/HP dengan akses AI tool

TUJUAN
Peserta mampu menyusun prompt yang efektif menggunakan framework PARTS untuk
menyelesaikan minimal 3 tugas nyata dari pekerjaan sehari-hari mereka.

LANGKAH-LANGKAH
1. Trainer menampilkan template framework PARTS di layar.
2. Peserta memikirkan 3 tugas berulang dalam pekerjaan mereka yang bisa dibantu AI.
3. Untuk setiap tugas, peserta menyusun prompt menggunakan framework PARTS.
4. Peserta menjalankan prompt di tool AI yang tersedia dan mencatat hasilnya.
5. Bandingkan: prompt mana yang menghasilkan output paling relevan dan mengapa?
6. Peserta memperbaiki satu prompt yang hasilnya kurang memuaskan dan mencoba lagi.

CODE_TAXONOMY : C3

PERTANYAAN REFLEKSI
1. Elemen PARTS mana yang paling sering kamu lupakan dan apa dampaknya pada hasil?
2. Tugas mana yang paling cocok dibantu AI dan mana yang masih lebih baik dikerjakan sendiri?
3. Apa satu perubahan kecil yang akan kamu buat pada cara kamu menggunakan AI besok pagi?

---
```

---

## Panduan Menulis Aktivitas Berkualitas

### Prinsip Utama
1. **Kontekstual** — Aktivitas harus relevan dengan pekerjaan/kehidupan nyata peserta
2. **Aktif** — Peserta melakukan sesuatu, bukan hanya mendengar atau membaca
3. **Terukur** — Ada output yang bisa dievaluasi (tulisan, hasil kerja, presentasi)
4. **Progresif** — Level Bloom meningkat dari aktivitas awal ke akhir
5. **Reflektif** — Selalu ada pertanyaan refleksi untuk memperdalam pemahaman

### Kata Kerja Operasional per Level Bloom

| Level | Kode | Kata Kerja yang Tepat |
|---|---|---|
| Remember | C1 | Sebutkan, Daftarkan, Kenali, Identifikasi, Hapalkan, Temukan |
| Understand | C2 | Jelaskan, Rangkum, Klasifikasi, Terjemahkan, Parafrase, Contohkan |
| Apply | C3 | Gunakan, Demonstrasikan, Selesaikan, Terapkan, Jalankan, Hitung |
| Analyze | C4 | Bandingkan, Bedakan, Uraikan, Kategorikan, Temukan pola, Kritisi |
| Evaluate | C5 | Nilai, Justifikasi, Rekomendasikan, Pertahankan, Putuskan, Timbang |
| Create | C6 | Rancang, Buat, Susun, Kembangkan, Formulasikan, Hasilkan |

### Pertanyaan Refleksi yang Baik
- Level C1–C2: "Apa yang kamu pelajari? Apa yang mengejutkan?"
- Level C3: "Bagaimana kamu menerapkan ini? Apa yang berhasil/tidak?"
- Level C4: "Apa perbedaan/persamaan yang kamu temukan? Mengapa itu terjadi?"
- Level C5: "Apa penilaianmu? Apa yang akan kamu ubah?"
- Level C6: "Apa yang kamu ciptakan? Bagaimana ini bisa dikembangkan lebih jauh?"

### Query notebooklm-mcp untuk Activity
```
"Berikan 2 ide aktivitas pembelajaran praktis untuk topik {NAMA_TOPIK} di level
Taksonomi Bloom {NAMA_LEVEL} ({KODE}). Setiap aktivitas harus:
- Relevan dengan konteks {TARGET_PESERTA}
- Bisa diselesaikan dalam {DURASI} menit
- Menghasilkan output yang terukur
- Sertakan langkah-langkah detail dan pertanyaan refleksi yang mendorong pemikiran kritis."
```

### Pengecekan Kualitas
- [ ] Setiap aktivitas memiliki tujuan yang jelas dengan kata kerja Bloom yang tepat
- [ ] Langkah-langkah cukup detail untuk diikuti tanpa panduan tambahan
- [ ] Durasi realistis untuk jumlah langkah yang ada
- [ ] Pertanyaan refleksi mendorong pemikiran lebih dalam, bukan sekadar "ya/tidak"
- [ ] Ada variasi jenis aktivitas (individu, berpasangan, kelompok, pleno)
- [ ] Aktivitas C3 ke atas menggunakan tool/media nyata yang tersedia peserta
