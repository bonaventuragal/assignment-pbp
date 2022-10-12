# Todo List

[Deployment Link](https://assignment-bonaventuragal.herokuapp.com/todolist)

## Perbedaan Asynchronous Programming dan Synchronous Programming
Synchronous Programming menjalankan code secara berurutan, baris per baris. Ketika terjadi pemanggilan sebuah function, function tersebut harus diselesaikan terlebih dahulu sebelum melanjutkan ke baris code berikutnya. Pada synchronous programming, task-task yang ada harus dijalankan secara urut.

Asynchronous Programming tidak perlu menunggu baris code sebelumnya selesai. Ketika terjadi pemanggilan sebuah function asynchronous, baris code selanjutnya dapat dijalankan tanpa perlu menunggu function tersebut selesai. Dengan asynchronous programming, beberapa task dapat dijalankan secara bersamaan.

## Paradigma Event-Driven Programming
Event-Driven Programming adalah paradigma pemrograman yang berfokus pada terjadinya sebuah event. Alur program bukan dijalankan secara terurut, melainkan bergantung pada terjadinya sebuah event, misalnya ketika sebuah button diklik. Event-Driven Programming biasanya menerapkan konsep asynchronous programming.

Pada tugas ini, salah satu penerapan Event-Driven Programming adalah ketika melakukan AJAX POST pada saat membuat task baru. Ketika button pada form untuk membuat task diklik, sebuah function akan dipanggil dan menjalankan AJAX POST untuk mengirim data ke server.

## Penerapan Asynchronous Programming pada AJAX
Ketika sebuah event terjadi, event tersebut akan mengakibatkan sebuah fungsionalitas AJAX dijalankan. Misalnya ketika mengklik button pada form untuk membuat task baru, akan dilakukan AJAX POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, akan dijalankan callback function yang telah dibuat sebelumnya.

## Implementasi

### AJAX GET
Pada `views.py` ditambahkan sebuah function untuk mengembalikan `Task` yang sesuai dengan user logged in dalam bentuk JSON. Views tersebut dihubungkan dengan routing `/todolist/json` yang ditambahkan di `urls.py`. Ketika website selesai di-load, dilakukan pemanggilan AJAX GET untuk mendapatkan `Task` dalam bentuk JSON, kemudian dimasukkan ke dalam tabel.

### AJAX POST
Tombol buat task yang sebelumnya melakukan redirect ke `todolist/create_task` diubah menjadi tidak melakukan redirect, tetapi memunculkan sebuah modal. Modal tersebut dibuat dengan memanfaatkan class pada Tailwind, yaitu `hidden`. Ketika button buat task diklik, atribut `hidden` akan dihapus. Sebaliknya, ketika button untuk menutup modal diklik, atribut `hidden` akan ditambahkan.

Pada modal tersebut berisi sebuah form. Ketika form tersebut diisi dan button untuk tambah task diklik, akan dilakukan pemanggilan AJAX POST. Data pada fields form akan dikirim ke server dan kemudian diproses. Jika berhasil membuat task baru, callback function dari AJAX POST tersebut akan dipanggil dan menutup modal.