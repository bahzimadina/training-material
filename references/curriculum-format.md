# Format Kurikulum (curriculum.md)

## Nama File
`curriculum.md` — simpan di root direktori project training.

## Template Lengkap

```markdown
# {NAMA_TRAINING}

## Informasi Kurikulum
- **Target Peserta:** {jabatan/role, level pengalaman, organisasi}
- **Durasi Total:** {X jam / X hari}
- **Jumlah Sesi:** {N sesi}
- **Level Taksonomi Bloom yang Ditargetkan:**
  - Sesi 1: Remember & Understand (C1–C2)
  - Sesi 2: Apply (C3)
  - Sesi 3: Analyze & Evaluate (C4–C5)
  - Sesi 4: Create (C6)
- **Sumber Referensi:** {notebooklm notebook / dokumen referensi}

---

## Kurikulum

| Sesi | Materi & Aktivitas Utama |
| ---- | ------------------------ |
| Sesi 1: {Nama Sesi} | • {Topik 1}: {deskripsi singkat}<br><br>• {Topik 2}: {deskripsi singkat}<br><br>• {Topik N}: {deskripsi singkat}<br><br>**Aktivitas:** {jenis aktivitas, misal: diskusi, kuis, hands-on} |
| Sesi 2: {Nama Sesi} | • {Topik 1}: {deskripsi singkat}<br><br>• {Topik 2}: {deskripsi singkat}<br><br>**Aktivitas:** {jenis aktivitas} |
| Sesi N: {Nama Sesi} | • {Topik 1}: {deskripsi singkat}<br><br>**Aktivitas:** {jenis aktivitas} |

---

## Capaian Pembelajaran (Learning Outcomes)

Setelah menyelesaikan seluruh sesi, peserta mampu:
1. **[C1-C2]** {Menyebutkan/Menjelaskan} — {apa yang dipelajari}
2. **[C3]** {Menerapkan} — {apa yang bisa dilakukan}
3. **[C4-C5]** {Menganalisis/Mengevaluasi} — {kemampuan berpikir kritis}
4. **[C6]** {Merancang/Membuat} — {output yang bisa dihasilkan}

---

## Referensi Konten
{Daftar sumber yang digunakan, termasuk hasil query notebooklm-mcp}
```

---

## Panduan Pengisian

### Kolom "Sesi"
Format: `Sesi {N}: {Nama Tema Sesi}`

Contoh:
- `Sesi 1: Dasar & Cara "Ngobrol" dengan AI`
- `Sesi 2: Prompting Lanjutan untuk Produktivitas`

### Kolom "Materi & Aktivitas Utama"
- Gunakan bullet `•` untuk setiap topik/sub-topik
- Pisahkan antar bullet dengan `<br><br>`
- Gunakan indentasi (dash `-`) untuk sub-item dalam satu topik
- Sertakan jenis aktivitas di akhir kolom

### Contoh Baris Tabel Lengkap

```markdown
| Sesi 1: Dasar & Cara "Ngobrol" dengan AI | • Kenalan Antarmuka: Tombol penting, privasi data, & pilih model.<br><br>• The GenAI Shift: Memahami pergeseran ke AI generatif.<br><br>• Etika & Privasi: Perlindungan data & penggunaan yang bertanggung jawab.<br><br>• Logika Prompting Dasar:<br>    - Teknik Zero Shot & Few-Shot<br>    - Chain of Thought<br><br>• Framework PARTS: Workshop menyusun prompt presisi.<br><br>**Aktivitas:** Hands-on prompting workshop (30 menit) |
```

---

## Pengecekan Kualitas (Quality Checklist)

Sebelum finalisasi `curriculum.md`, pastikan:

- [ ] Jumlah sesi sesuai dengan durasi training
- [ ] Setiap sesi memiliki topik yang jelas dan terukur
- [ ] Ada progres level Taksonomi Bloom dari sesi awal ke akhir
- [ ] Capaian pembelajaran mencakup semua level yang ditargetkan
- [ ] Materi relevan dengan target peserta
- [ ] Sumber referensi dicantumkan
