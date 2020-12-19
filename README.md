# Dashboard Loan Prediction

![Poster](/img/posterFinal.jpeg)

Link Video: [Dashboard Loan Prediction](https://youtu.be/ETpeIdcJNuU)

Dashboard Loan Prediction adalah sebuah web application ayng merupakan hasil dari project ahir yang kami selesaikan pada Digital Talent Incubator (DTI) 2020 yang ditujukan untuk membantu permasalahan pemberian bantuan pinjamanan apakah orang yang diberi pinjaman layak untuk mendapatkan bantuan pinjaman.

Berikut adalah anggota dalam project ini:

- Muhammad Apriandito (Mentor)
- Deva Hidayat,
- Gigas Taufan Arvyanto,
- Rachma Indira

## Latar Belakang

Dilansir dari CNBC Indonesia, menurut Menteri Koordinator Bidang Kemaritiman dan Investasi Luhut Binsar Pandjaitan mengatakan bahwa akses permodalan menjadi tantangan utama bagi pelaku UMKM dalam menjalankan usahanya. Pelaku UMKM masih kesulitan mendapatkan bantuan pinjaman dari badan-badan pemberi pinjaman dari bank maupun koperasi.

Untuk dapat membantu menyelesaikan permasalahan tersebut kami berinisiatif untuk mengolah data yang terkait dengan pemberian modal yang tersedia dan meluncurkan aplikasi yang dapat membantu badan pemberi pinjaman modal untuk dapat mengambil keputusan yang lebih cepat dalam memberikan bantuan pinjaman kepada pemohon pinjaman.

## Konsep Aplikasi

Aplikasi adalah sebuah website yang dapat melakukan prediksi apakah seseorang dapat diberikan pinjaman atau tidak. Pengguna aplikasi dapat mengunggah dataset yang dimiliki ke website. Pengguna juga dapat melakukan analisis sederhana terhadap dataset. Terdapat menu Eksplorasi yang berguna untuk melihat visualisasi sederhana terhadap dataset. Lalu untuk melakukan prediksi terdapat pada Menu Uji Model & Prediksi di mana dataset yang diunggah dapat dijadikan model machine learning untuk dapat membantu mengambil keputusan.

terdapat 3 model machine learning yang dapat digunakan yakni Naive Bayes, Decision Tree, dan Random Forest.

## Tujuan

Pembangunan aplikasi ini guna mendukung usaha dalam mencapai UN Sustainable Development Goals 2030 (SDG) yang ditetapkan oleh PBB. Aplikasi yang dibangun sesuai dengan Goal ke-8: Pekerjaan Layak dan Pertumbuhan Ekonomi. Diharapkan aplikasi yang dibangun dapat membantu dalam usaha mencapai tujuan tersebut sebagai kontribusi data scientist untuk Sustainable Development Goals 2030.

## Pengembangan Lanjut

Aplikasi yang dibangun bersifat opensource. Kode dapat digunakan dan dimodifikasi untuk kepentingan lain yang memiliki model permasalahan yang mirip seperti Klasifikasi atau untuk permasalahn lainnya yang membutuhkan data science dan machine learning.

## Cara Penggunaan Aplikasi Website

### Akses Website

Akses website pada link berikut:

```bash
https://tubes-dti-kelompok6.herokuapp.com/
```

### Beranda

Tampilan Beranda:
![Beranda](/img/beranda.png)

Pada beranda terdapat penjelasan singkat terkait dengan aplikasi dan tatacara penggunaannya

### Menu

Dibagian kiri aplikasi terdapat sidebar berupa dropdown yang berisi menu-menu dari aplikasi
![Beranda](/img/menu.png)

### Menu Eksplorasi

Menu Eksplorasi berguna untuk menampilkan visualisasi sederhana dari data yang diunggah. Visualisasi seperti correlation heatmap, boxplot, pairplot, serta countplot tersedia.

Pengguna mengunggah data melalui bagian Upload Dataset:

![EksplorasiUpload](/img/Eksplorasi/eksplorasi_upload_file.png)

#### Pairplot dan Countplot

Pengguna dapat memilih kolom bertipe kategorikal atau object pada dropdown yang disediakan. Untuk dapat melihat visualisasi pairplot yang dipisahkan berdasarkan kolom yang dipilih:

![EksplorasiDataKategorikal](/img/Eksplorasi/eksplorasi_data_kategorikal.png)

#### Correlation Table

Berikut adalah correlation table dan heatmap dari dataset:

![Correlation](/img/Eksplorasi/correlation_map.png)

#### Describe Dataset

Pengguna dapat melihat deskripsi terkait dataset yang diunggahnya, dan juda dapat memilih satu kolom untuk melihat deskripsi data yang digrouping berdasarkan kolom yang dipilih:

![Describe1](/img/Eksplorasi/Desckripsi_dataset.png)

![Describe2](/img/Eksplorasi/Desckripsi_visualisasi.png)

#### Boxplot

Pengguna dapat melakukan visualisasi boxplot dengan memilih dua kolom yang masing-masing bertipe kategorikal dan numerik.

![boxplot](/img/Eksplorasi/boxplot.png)

#### Mean

Pengguan dapat melihat rata-rata dari kolom bertipe numerik yang dipilih.

![mean](/img/Eksplorasi/mean.png)

### Menu Uji Model & Prediksi

Menu Uji Prediksi & Prediksi berguna untuk melakukan pengujian metode machine learning yang akan digunakan untuk klasifikasi.

Pengguna mengunggah data melalui bagian Upload Dataset:

![ModelUpload](/img/UjiModel_Prediksi/upload.png)

#### Pilih Model

Pengguna dapat memilih target kelas yang dicari, memilih jumlah data test yang digunakan, dan memilih metode machine learning yang akan dipakai.

![model](/img/UjiModel_Prediksi/PilihModel.jpg)

#### Model Report

Setelah pengguna memilih target kelas, data test, dan metode maka akan dibawahnya akan muncul laporan terkait performa model yang digunakan.

![modelreport](/img/UjiModel_Prediksi/model1.png)

#### Prediksi

Pengguna dapat melakukan prediksi data baru dari model yang dibangun dengan memasukkan nilai-nilai pada atribut yang digunakan. Hasil keputusan akan ditampilkan setelah pengguna mengklik tombol "Keputusan".

![prediksi](/img/UjiModel_Prediksi/prediksi.png)

![prediksi](/img/UjiModel_Prediksi/prediksi1.png)

![prediksi](/img/UjiModel_Prediksi/prediksi2.png)
