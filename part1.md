# Aljabar Linear Dasar untuk AI | Vektor, Dot Product, dan Cosine Similarity

Dalam dunia Artificial Intelligence (AI), komputer nggak bisa langsung paham bahasa manusia kayak kata-kata atau dokumen. Komputer cuma ngerti angka. Nah, untuk ngubah teks jadi angka biar bisa diproses AI, kita butuh konsep dasar aljabar linear.

## 1. Pengenalan Vektor
Vektor itu sesimpel **daftar angka** atau *array*. Semua data teks (satu kata atau satu kalimat) bakal diubah jadi deretan angka desimal untuk mewakili makna dari teks tersebut.

Contoh simpel (mendeskripsikan fisik orang [tinggi, berat]):
Budi = [170, 65]
Andi = [165, 60]

Di Python, vektor ini gampang banget dibikin pakai list biasa.

## 2. Dot Product
Dot product adalah cara awal buat ngecek seberapa "searah" dua vektor. 
Cara hitungnya: kalikan angka-angka yang posisinya sama di kedua vektor, lalu jumlahin semua hasil kalinya.

Contoh Vektor A = [1, 2] dan Vektor B = [3, 4]
- 1 x 3 = 3
- 2 x 4 = 8
- Total: 3 + 8 = 11 (Ini nilai dot product-nya)

*Kelemahan:* Angka dot product bisa jadi gede banget cuma karena angka di dalam vektornya emang gede, bukan karena maknanya beneran mirip.

## 3. Cosine Similarity
Ini versi "upgrade" dari dot product. Cosine similarity membuang faktor besaran angka dan murni cuma ngecek **arahnya** aja (di AI, arah = makna).

Rentang nilainya:
- **Mendekati 1**: Maknanya sangat mirip (searah).
- **Mendekati 0**: Nggak nyambung.
- **Mendekati -1**: Maknanya berlawanan.

**Rumus Manual:**
`Hasil Dot Product dibagi (Panjang Vektor A dikali Panjang Vektor B)`

*Cara hitung Panjang Vektor:* 
Kuadratkan tiap angka di vektor -> Jumlahkan semuanya -> Akar-kuadratkan hasilnya.

## 4. Kenapa Ini Penting di AI (RAG)?
Nanti pas bikin sistem RAG (AI yang bisa jawab berdasarkan dokumen), user bisa nanya "biaya makan", padahal di dokumen tertulis "pengeluaran konsumsi". Kalau cuma nyocokin teks biasa, nggak bakal ketemu. Tapi karena AI ngubah kata-kata itu jadi vektor, AI tau kalau arah vektor kedua kata itu searah. Lewat hitungan cosine similarity, AI bisa nemuin dokumen yang maknanya paling pas buat ngejawab pertanyaan.

## 5. Implementasi Code di Python
Berikut adalah cara menghitung Cosine Similarity secara manual tanpa library Machine Learning.

```python
import math

# 1. Definisikan vektor
vector_a = [2, 4, 6]
vector_b = [3, 6, 9]

# 2. Menghitung dot product
# zip() memasangkan angka di posisi yang sama, lalu dikali dan dijumlahkan
dot = sum([a * b for a, b in zip(vector_a, vector_b)])
print(f"Hasil Dot Product: {dot}")

# 3. Menghitung panjang vektor
panjang_vector_a = math.sqrt(sum([a**2 for a in vector_a]))
panjang_vector_b = math.sqrt(sum([b**2 for b in vector_b]))

# 4. Menghitung Cosine Similarity
cosine_similarity = dot / (panjang_vector_a * panjang_vector_b)
print(f"Hasil Cosine Similarity: {cosine_similarity}")
```
*(Ingat: Hati-hati saat looping list comprehension, pastikan memanggil variabel yang tepat supaya hasilnya tidak kelebihan/salah).*

***DIHARAPKAN KALIAN SELALU EXPLORE DAN SEARCHING SENDIRI KETIKA MENEMUKAN ERROR, KARENA PROGRAMMER SERING DITUNTUT MENYELESAIKAN MASALAHNYA SENDIRIAN***