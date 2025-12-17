Studi Kasus: Sistem Validasi Registrasi Mahasiswa

Kelas awal, ValidatorManager, merupakan contoh dari God Class yang melanggar prinsip desain karena memikul terlalu banyak tanggung jawab, membuat kode menjadi kaku dan rapuh.

Analisis Pelanggarn Prinsip SOLID (koode ValidatorManager)
1. Pelanggaran Single Responsibility Principle (SRP)

Penjelasan Singkat: Kelas ValidatorManager melanggar SRP karena ia memiliki lebih dari satu alasan untuk berubah. Di dalamnya terdapat logika untuk memvalidasi SKS dan logika untuk memvalidasi Prasyarat. Jika ada perubahan pada aturan SKS, kelas ini harus diubah. Jika ada perubahan pada aturan Prasyarat, kelas ini juga harus diubah. Solusinya adalah memecah kelas besar ini menjadi beberapa kelas kecil yang masing-masing memiliki tanggung jawab tunggal.



2. Pelanggaran Open/Closed Principle (OCP)

Penjelasan Singkat: OCP menyatakan bahwa kelas harus terbuka untuk ekstensi, tetapi tertutup untuk modifikasi. Kelas ValidatorManager melanggar ini karena ia menggunakan struktur if/elif untuk menangani setiap tipe validasi (misalnya, if validation_type == "sks"). Untuk menambahkan tipe validasi baru, seperti Validasi Pembayaran, Anda harus memodifikasi kode yang sudah ada di dalam metode validate_registration dengan menambahkan elif baru. Ini melanggar OCP. Solusinya adalah menggunakan Abstraksi (Interface) sebagai stopkontak universal untuk memungkinkan penambahan fitur baru tanpa mengubah kode inti.


3. Pelanggaran Dependency Inversion Principle (DIP)

Penjelasan Singkat: Kelas ValidatorManager adalah modul high-level (logika bisnis) yang secara langsung bergantung pada implementasi low-level (detail spesifik validasi SKS dan Prasyarat) yang hardcoded. Hal ini menciptakan keterikatan yang kuat (tight coupling). DIP menuntut agar modul high-level bergantung pada Abstraksi (Kontrak), bukan pada implementasi Konkret. Solusi yang diterapkan adalah menggunakan Dependency Injection, di mana objek high-level (seperti RegistrationService yang baru) akan menerima (disuntikkan) implementasi validasi melalui constructor, memastikan ketergantungan hanya pada kontrak (IValidator).