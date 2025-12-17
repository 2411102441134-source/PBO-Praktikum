# test_diskon_advanced.py

import unittest
from diskon_service import DiskonCalculator 
# Asumsi: diskon_service.py telah diperbaiki (bug logika awal dan bug PPN sudah dihapus)

class TestDiskonLanjut(unittest.TestCase):
    """
    Class baru untuk Laporan Pengujian Lanjutan (Tes 5 dan Tes 6)
    """
    
    def setUp(self):
        # Arrange: Siapkan instance Calculator sebelum setiap tes
        self.calc = DiskonCalculator()

    def test_uji_nilai_float_assertAlmostEqual(self):
        """
        Tes 5 (Boundary/Float): Uji nilai diskon 33% pada 999. 
        Memerlukan assertAlmostEqual karena hasil float 669.33.
        """
        # Act: 999 * (1 - 0.33) = 669.33
        hasil = self.calc.hitung_diskon(999.0, 33)
        
        # Assert: Menggunakan assertAlmostEqual untuk mengizinkan perbedaan kecil pada float
        harga_yang_diharapkan = 669.33
        # places=2 menunjukkan toleransi hingga 2 angka desimal
        self.assertAlmostEqual(hasil, harga_yang_diharapkan, places=2)

    def test_edge_case_harga_awal_nol(self):
        """
        Tes 6 (Edge Case): Memastikan harga awal 0 menghasilkan harga akhir 0.
        """
        # Act: Harga 0, Diskon 50%
        hasil = self.calc.hitung_diskon(0, 50)
        
        # Assert: Hasil seharusnya selalu 0.0
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()