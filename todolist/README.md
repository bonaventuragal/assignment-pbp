# Todo List

[Deployment Link](https://assignment-bonaventuragal.herokuapp.com/todolist)

## Kegunaan `{% csrf_token %}`
`{% csrf_token %}` berguna untuk melindungi dari CSRF (Cross Site Request Forgery) Attack. Tanpa `{% csrf_token %}`, form yang ada tetap dapat bekerja dengan baik, tetapi website lain yang tidak terpercaya bisa saja mengakses website kita dan mengisi form tersebut.

## Membuat `<form>` secara manual
Kita tetap dapat membuat form secara manual tanpa memanfaatkan generator. Caranya adalah membuat elemen `<form>`, kemudian mengisi form tersebut dengan elemen `<input>` yang sesuai dengan keinginan kita. Pastikan pula terdapat `<input type="submit">` untuk meng-submit form tersebut.

## Proses alur data
Ketika user mengklik tombol untuk submit form, data-data yang dimasukkan ke form akan diperiksa. Jika data yang dimasukkan tidak valid, user akan diarahkan untuk mengisi kembali form tersebut. Jika sudah valid, data tersebut akan diproses, misalnya dengan membuat Model sesuai dengan data yang diperoleh dan kemudian dimasukkan ke database. Ketika dibutuhkan, Model pada database dapat diambil dan ditampilkan pada template HTML.

## Implementasi

### Poin 1
Membuat aplikasi baru `todolist` dengan menjalankan program `python manage.py startapp todolist`.

### Poin 2
Menambahkan `path('todolist/', include('todolist.urls'))` pada file `project_django/urls.py`.

### Poin 3
Membuat sebuah model `Task` pada file `models.py` dengan fields sesuai dengan ketentuan pada soal.

### Poin 4
Membuat 2 buah template HTML, `login.html` dan `register.html` untuk ditampilkan ke user ketika akan login dan register. Pada file `views.py` ditambahkan 3 buah function `register`, `login_user`, dan `logout_user` untuk menghandle logic register, login, dan logout.

### Poin 5
Membuat sebuah template HTML, `todolist.html` untuk ditampilkan sebagai halaman utama. Pada file `views.py` ditambahkan sebuah function `todolist` untuk menghandle logic menampilkan data yang sesuai berdasarkan user yang login.

### Poin 6
Membuat sebuah template HTML, `add_task.html` untuk ditampilkan ke user ketika akan membuat task baru. Pada file `views.py` ditambahkan sebuah function `create_task` untuk menghandle logic pembuatan model `Task` yang baru.

### Poin 7
Pada file `urls.py` ditambahkan pola url yang tepat dan dihubungkan dengan function yang bersangkutan pada `views.py`.

### Poin 8
Deployment ke Heroku sudah berjalan secara otomatis dengan melakukan push ke repository GitHub.

### Poin 9
Pada deployment di Heroku dilakukan register 2 buah akun, dengan masing-masing akun dibuat pula 3 buah task.