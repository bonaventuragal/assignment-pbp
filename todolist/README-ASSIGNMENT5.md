# Todo List

[Deployment Link](https://assignment-bonaventuragal.herokuapp.com/todolist)

## Perbedaan Inline, Internal, dan External CSS
Inline, Internal, dan External CSS berbeda dalam cara penggunaan CSS pada dokumen HTML. Inline CSS dituliskan sebagai attribute dari sebuah tag HTML, misalnya `<div style="display:block;"></div>`. Internal CSS dituliskan di dalam tag khusus, yaitu `<style>`. Di dalam tag ini, kita dapat menuliskan CSS secara normal. External CSS menggunakan file CSS external yang diimport ke file HTML, biasanya menggunakan `<link>`. File CSS external tersebut berisi style-style yang dapat digunakan dalam file HTML.

Inline CSS cocok untuk menambahkan sedikit style pada sebuah tag dan meng-override style lain yang ada. Namun, jika style yang ditambahkan cukup banyak, Inline CSS akan membuat file HTML sulit untuk dibaca. Internal CSS cocok untuk menambahkan banyak style pada satu buah dokumen HTML saja karena tidak perlu mengimport file lain. Internal CSS tidak cocok untuk menambahkan banyak style pada banyak dokumen HTML karena tiap file perlu menambahkan style-nya masing-masing. Selain itu, Internal CSS juga dapat membuat ukuran file HTML menjadi besar. External CSS cocok untuk menambahkan style yang banyak dan kompleks ke beberapa file HTML. Kekurangannya adalah tiap file HTML perlu mengimport file CSS yang akan digunakan sehingga menambah waktu agar browser me-load website.

## Tag HTML5
- `<div>`, sebuah tag yang merepresentasikan container/section. `<div>` dapat digunakan untuk mengelompokkan beberapa tag dan mengatur layout.
- `<p>`, sebuah tag yang merepresentasikan sebuah paragraf.
- `<title>`, tag yang digunakan untuk mengatur title pada tab browser.
- `<link>`, tag yang digunakan untuk menginclude dari path/link eksternal.
- `<a>`, tag yang digunakan untuk menambahkan link pada dokumen.

## CSS Selector
- Tag selector, untuk menambahkan style pada sebuah tag. Penggunaannya cukup menuliskan tag yang ingin diberikan style, misalnya `div {`
- Class selector, untuk menambahkan style pada elemen dengan class tertentu. Penggunaannya dengan menuliskan titik/dot (`.`) diikuti dengan nama classnya, misalnya `.class1 {`
- ID selector, untuk menambahkan style pada elemen dengan ID tertentu. Penggunaannya dengan menuliskan hashtag (`#`) diikuti dengan nama ID, misalnya `#id1 {`

## Implementasi
Pada tugas 5 ini saya menggunakan library Tailwind untuk menambahkan style pada app todolist. Saya menambahkan link Tailwind CDN pada `base.html` untuk menginclude Tailwin. Selain itu saya juga menggunakan Tailwind CLI untuk menginisialisasi dan membuat `tailwind.config.js`.

Pada `login.html` dan `register.html`, form login dan register ditampilkan ditengah layar. Pada bagian `todolist.html` saya menambahkan navbar dan menampilkan task dalam bentuk card. Navbar dibuat pada file `navbar.html` dan kemudian diinclude pada file yang menggunakan navbar. Card dibuat pada file `task_card.html` dan kemudian diinclude pada file `todolist.html` ketika looping menampilkan task satu per satu. Pada `add_task.html` saya menambahkan navbar dan mengatur peletakan form pembuatan task agar ditampilkan di tengah layar. Setelah semua style dibuat, saya menambahkan style responsive dengan memanfaatkan breakpoints yang disediakan oleh Tailwind.