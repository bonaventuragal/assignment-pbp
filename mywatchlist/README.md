# My Watchlist

[Deployment Link](https://assignment-bonaventuragal.herokuapp.com/mywatchlist)

## Perbedaan JSON, XML, HTML
Dalam merepresentasikan data, JSON (JavaScript Object Notation) menggunakan notasi objek JavaScript untuk merepresentasikan data, sedangkan XML (eXtensible Markup Language) merepresentasikan data dalam bentuk element tree, mirip seperti HTML. HTML merepresentasikan data dalam bentuk element tree, tetapi data yang direpresentasikan lebih ditujukan untuk ditampilkan pada web browser.

## Mengapa memerlukan data delivery
Dalam pengimplementasian sebuah platform tentu saja kita akan sering berurusan dengan pertukaran data. Penggunaan metode data delivery seperti akan membantu mempermudah proses pertukaran data menjadi lebih mudah. Selain itu, penggunaan metode data delivery seperti JSON, XML, dan HTML dapat mempermudah pekerjaan para developer karena JSON, XML, dan HTML mudah dibaca oleh manusia.

## Implementasi
### Poin 1
Pada repositori assignment yang sudah ada, membuat aplikasi `mywatchlist` dengan menjalankan command `python manage.py startapp mywatchlist`.

### Poin 2
Pada `project_django/urls.py` ditambahkan `path('mywatchlist/', include('mywatchlist.urls'))` untuk menghubungkan `urlpatterns` pada `mywatchlist/urls.py` dengan `urlpatterns` pada `project_django/urls.py`. Pada `mywatchilst/urls.py` ditambahkan pattern path-path yang diminta ke views yang sesuai.

### Poin 3
Pada `mywatchlist/models.py` dibuat model baru bernama `MyWatchList` dengan fields `watched`, `title`, `rating`, `release_date`, dan `review`. Setelah dibuat, dilakukan migrasi agak model tersebut dapat digunakan pada database dengan menjalankan command `python manage.py makemigrations` dan `python manage.py migrate`.

## Postman
### JSON
![JSON]("../../../static/postman_json.png?raw=true")
<br/><br/>

### XML
![XML]("../../../static/postman_xml.png?raw=true")
<br/><br/>

### HTML
![HTML]("../../../static/postman_html.png?raw=true")