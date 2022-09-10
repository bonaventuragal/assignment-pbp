# Katalog

[Deployment Link](https://assignment2-bonaventuragal.herokuapp.com/)

## Bagan
![Bagan](../static/bagan.png?raw=true)
- Request dari user akan dihandle oleh URLConf untuk diarahkan ke views yang sesuai.
- Views akan menjalankan logic yang sudah dirancang sebelumnya, misalnya query database melalui models. Di akhir, views akan mengembalikan response kepada user. Response dapat berupa file HTML yang akan ditampilkan kepada user. File HTML yang ditampilkan diperoleh dari template yang sesuai.
- Models menjadi penghubung antara views dan database. Models akan menerima query dari views, mengakses database sesuai query tersebut, kemudian mengembalikan response dari query tersebut.
- Template menyediakan file HTML yang dapat dikirim oleh views kembali ke user dan kemudian ditampilkan ke user.

## Virtual Environment
### Mengapa menggunakan virtual environment?
Virtual Environment digunakan untuk mengisolasi packages dan dependencies yang digunakan pada project ini. Penginstalan packages dan dependencies yang digunakan pada project ini tidak akan mengganggu atau penginstalan packages dan dependencies lain yang ada di komputer atau project lain

### Apakah bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, packages dan dependencies yang dibutuhkan akan diinstall langsung di komputer dan bisa saja mengganggu packages dan dependencies project lain yang menggunakan packages dan dependencies yang sama dengan versi yang berbeda.

## Implementasi
### Poin 1
Pada `katalog/views.py` dibuat sebuah function `show_catalog(req)` yang menerima sebuah request sebagai parameter. Function ini akan mengambil semua data dari model `CatalogItem`. Kemudian function ini akan membuat sebuah `context` yang berisi `nama`, `npm`, dan `catalog_data`. Di akhir, function ini akan me-`render` file `katalog/index.html` dengan `context` sebagai template context.

### Poin 2
Pada `project_django/urls.py` ditambahkan `path('katalog/', include('katalog.urls'))` untuk menghubungkan `urlpatterns` pada `katalog/urls.py` dengan `urlpatterns` pada `project_django/urls.py`. Pada `katalog/urls.py` ditambahkan `path('', show_catalog, name='show_catalog')` untuk mengalihkan route `/katalog` ke function `show_catalog` pada `katalog/views.py`.

### Poin 3
Pada `katalog/templates/katalog/index.html` ditambahkan `{{nama}}` dan `{{npm}}` untuk menampilkan nama dan NPM sesuai dengan context. Kemudian, buat looping untuk menampilkan isi dari `catalog_data` satu per satu sebagai table row.

### Poin 4
Buat sebuah app pada akun Heroku, kemudian memasukkan app name dan Heroku API Key pada repository secrets `HEROKU_APP_NAME` dan `HEROKU_API_KEY`. Deployment akan berjalan otomatis sesuai dengan Github Actions yang sudah diatur oleh template tugas.
