# Matematika
**Deskrip**
Package ini dibuat untuk menyediakan fungsi matematika sederhana

## Perlengkapan
- Python 3.10++ 
- Virtual Environment (untuk mencegah error)
- GitBash (untuk windows)
- PIP 

## Cara Install
1. Pada terminal (linux/mac) atau gitbash (windows) masukkan perintah berikut:
```
git clone https://github.com/najikh2002/math-package.git
```

2. Buka folder *math-package* :
```
cd math-package
```
3. Buat virtual environment-nya :
```
python3.10 -m venv venv
```

4. Aktifkan virtual environment-nya :
```
source venv/bin/activate
```

5. Buka folder *dist* :
```
cd dist
```

6. Cari file yang memiliki eksitensi *.whl* (file wheel) dengan menggunakan perintah `ls`

7. Setelah menemukan file wheel-nya lalu masukkan perintah berikut:
```
pip install <nama_file_wheel>.whl
```


## Cara Penggunaan

Berikut adalah panduan penggunaan untuk setiap fungsi yang terdapat pada modul `operasi` dan `hello`:

#### Modul `operasi`

1. **`penjumlahan(a, b)`**
   - **Deskripsi**: Fungsi ini melakukan penjumlahan dua bilangan.
   - **Penggunaan**:
     ```python
     from matematika import operasi

     result = operasi.penjumlahan(3, 3)
     print(result)  # Output: 6
     ```

2. **`pengurangan(a, b)`**
   - **Deskripsi**: Fungsi ini melakukan pengurangan dua bilangan.
   - **Penggunaan**:
     ```python
     from matematika import operasi

     result = operasi.pengurangan(5, 2)
     print(result)  # Output: 3
     ```

3. **`perkalian(a, b)`**
   - **Deskripsi**: Fungsi ini melakukan perkalian dua bilangan.
   - **Penggunaan**:
     ```python
     from matematika import operasi

     result = operasi.perkalian(3, 3)
     print(result)  # Output: 9
     ```

4. **`pembagian(a, b)`**
   - **Deskripsi**: Fungsi ini melakukan pembagian dua bilangan.
   - **Penggunaan**:
     ```python
     from matematika import operasi

     result = operasi.pembagian(12, 3)
     print(result)  # Output: 4.0
     ```

#### Modul `hello`

5. **`hello()`**
   - **Deskripsi**: Fungsi ini mengembalikan pesan sapaan "Hello World!".
   - **Penggunaan**:
     ```python
     from matematika import hello

     result = hello.hello()
     print(result)  # Output: Hello World!
     ```

#### Catatan

- Pastikan modul `matematika` dapat diakses dari lokasi tempat Anda mengimpor modul. Jika modul berada dalam direktori yang sama, pengimporan seperti contoh di atas harus berfungsi.
- Gunakan perintah `pip list` untuk memastikan modul sudah terinstall.
- Sesuaikan argumen fungsi sesuai kebutuhan Anda.
- Perbarui hasil pengujian jika Anda merubah implementasi fungsi-fungsi ini.
  
Selamat menggunakan fungsi-fungsi matematika dan sapaan "Hello World!" pada proyek Anda!



