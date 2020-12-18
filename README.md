![Poster](/img/poster.jpeg)

Link Video: [Dashboard Loan Prediction](https://youtu.be/ETpeIdcJNuU)

# Dashboard Loan Prediction

Deva Hidayat, Gigas Taufan Arvyanto, Rachma Indira

Dashboard Loan Prediction merupakan sebuah implementasi data science berupa website untuk menemukan solusi permasalahan SDGs nomor 8. Permasalahan ini yaitu membuat regulasi individu atau kelompok mana saja yang dapat diberikan pinjaman. Berikut adalah tools, metode dan dataset yang digunakan:

## Dataset

Dataset yang digunakan merupakan prediksi pinjaman yang didapat dari Kaggle. Berikut adalah link dataset https://www.kaggle.com/ninzaami/loan-predication

## Metode Klasifikasi

Metode yang digunakan adalah Gaussian Naive-Bayes, Random Forest, dan Decision Tree. Berikut adalah akurasi dari setiap metode :

### Gaussian Naive-Bayes :

Accuracy: 0.7783783783783784
Precision: 0.7748344370860927
Recall: 0.9435483870967742
F1 Score: 0.8509090909090908
Cohens Kappa Score: 0.43509346838459817

### Random Forest

Accuracy : 0.8
Recall : 0.9354838709677419

### Decision Tree

Accuracy : 0.8698224852071006
Recall : 0.8745084269662922

## Cara Penggunaan Aplikasi Website

### Akses Website

Akses website pada link berikut: https://tubes-dti-kelompok6.herokuapp.com/
![Beranda](/img/beranda.jpeg)

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
![boxplot](/img/Eksplorasi/mean.png)

### Menu Uji Model & Prediksi

Menu Uji Prediksi & Prediksi berguna untuk melakukan pengujian metode machine learning yang akan digunakan untuk klasifikasi.

Pengguna mengunggah data melalui bagian Upload Dataset:
![ModelUpload](/img/UjiModel_Prediksi/upload.png)

#### Pilih Model

Pengguna dapat memilih target kelas yang dicari, memilih jumlah data test yang digunakan, dan memilih metode machine learning yang akan dipakai.
![model](/img/UjiModel_Prediksi/PilihModel.png)

#### Model Report

Setelah pengguna memilih target kelas, data test, dan metode maka akan dibawahnya akan muncul laporan terkait performa model yang digunakan.

![modelreport](/img/UjiModel_Prediksi/model1.png)

#### Prediksi

Pengguna dapat melakukan prediksi data baru dari model yang dibangun dengan memasukkan nilai-nilai pada atribut yang digunakan. Hasil keputusan akan ditampilkan setelah pengguna mengklik tombol "Keputusan".

![prediksi](/img/UjiModel_Prediksi/prediksi.png)
![prediksi](/img/UjiModel_Prediksi/prediksi1.png)
![prediksi](/img/UjiModel_Prediksi/prediksi2.png)
