from dataclasses import dataclass
from abc import ABC, abstractmethod 

@dataclass
class Mahasiswa:
    """Model sederhana untuk data mahasiswa."""
    nama: str
    nim: str
    sks_diambil: int
    prasyarat_lulus: bool = False
    is_valid: bool = False 

class ValidatorManager: 
    """Kelas monolitik yang menangani berbagai jenis validasi pendaftaran."""

    def validate_registration(self, mahasiswa: Mahasiswa, validation_type: str) -> bool:
        print(f"Memulai validasi '{validation_type}' untuk Mahasiswa: {mahasiswa.nama}")

        if validation_type == "sks":
            if mahasiswa.sks_diambil > 24:
                print("Validasi Gagal: SKS melebihi batas (Maks. 24).")
                return False
            print("Validasi SKS Sukses.")
            return True
        elif validation_type == "prasyarat":
            if not mahasiswa.prasyarat_lulus:
                print("Validasi Gagal: Prasyarat mata kuliah belum terpenuhi.")
                return False
            print("Validasi Prasyarat Sukses.")
            return True
        else:
            print(f"Tipe validasi '{validation_type}' tidak dikenal.")
            return False

class IValidator(ABC):
    """Kontrak: Semua validator harus punya method validate."""
    @abstractmethod
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        pass

class SKSValidator(IValidator):
    """Tanggung jawab Tunggal: Hanya mengurus validasi batas SKS."""
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.sks_diambil > 24:
            print(f"|SKS| GAGAL: SKS {mahasiswa.sks_diambil} melebihi batas 24.")
            return False
        print(f"|SKS| OK: SKS {mahasiswa.sks_diambil} valid.")
        return True

class PrasyaratValidator(IValidator):
    """Tanggung jawab Tunggal: Hanya mengurus validasi prasyarat mata kuliah."""
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if not mahasiswa.prasyarat_lulus:
            print(f"|Prasyarat| GAGAL: {mahasiswa.nama} belum lulus mata kuliah prasyarat.")
            return False
        print(f"|Prasyarat| OK: {mahasiswa.nama} telah memenuhi prasyarat.")
        return True

class RegistrationService:
    """Modul High-Level yang bergantung pada Abstraksi IValidator (DIP)."""
    def __init__(self, validator: IValidator):
        self.validator = validator

    def run_validation(self, mahasiswa: Mahasiswa) -> bool:
        print(f"\n--- Memulai proses validasi untuk {mahasiswa.nama} (Validator: {self.validator.__class__.__name__}) ---")
        validation_success = self.validator.validate(mahasiswa) 

        if validation_success:
            mahasiswa.is_valid = True
            print("Status: Validasi Sukses.")
            return True
        else:
            print("Status: Validasi Gagal.")
            return False

budi = Mahasiswa("Budi", "19041002", 20, False)
citra = Mahasiswa("Citra", "19041003", 24, True)

sks_validator = SKSValidator()
service_sks = RegistrationService(validator=sks_validator)
service_sks.run_validation(budi) 

prasyarat_validator = PrasyaratValidator()
service_prasyarat = RegistrationService(validator=prasyarat_validator)
service_prasyarat.run_validation(budi) 

class PembayaranValidator(IValidator):
    """Implementasi Konkrit Baru (Plug-in) untuk validasi status pembayaran."""
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if int(mahasiswa.nim[-1]) % 2 != 0:
            print(f"|Pembayaran| GAGAL: Mahasiswa {mahasiswa.nim} belum lunas (NIM ganjil).")
            return False
        print(f"|Pembayaran| OK: Mahasiswa {mahasiswa.nim} lunas/bebas biaya (NIM genap).")
        return True

dian = Mahasiswa("Dian", "19041004", 22, True) 
eko = Mahasiswa("Eko", "19041005", 22, True)  


pembayaran_validator_dian = PembayaranValidator()
service_pembayaran_dian = RegistrationService(validator=pembayaran_validator_dian)
service_pembayaran_dian.run_validation(dian)

pembayaran_validator_eko = PembayaranValidator()
service_pembayaran_eko = RegistrationService(validator=pembayaran_validator_eko)
service_pembayaran_eko.run_validation(eko)