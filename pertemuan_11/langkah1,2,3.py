from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

class OrderManager:  
    def process_checkout(self, order: Order, payment_method: str):
        print(f"Memulai checkout untuk {order.customer_name}...")

        if payment_method == "credit_card":
            print("Processing Credit Card...")
        elif payment_method == "bank_transfer":
            print("Processing Bank Transfer...")
        else:
            print("Metode tidak valid.")
            return False

        print(f"Mengirim notifikasi ke {order.customer_name}...")
        order.status = "paid"
        return True

class IPaymentProcessor(ABC):
    """Kontrak: Semua processor pembayaran harus punya method 'process'"""

    @abstractmethod
    def process(self, order: Order) -> bool:
        pass


class INotificationService(ABC):
    """Kontrak: Semua layanan notifikasi harus punya method 'send'"""

    @abstractmethod
    def send(self, order: Order):
        pass

class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Kartu Kredit.")
        return True


class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Mengirim email konfirmasi ke {order.customer_name}.")

class CheckoutService:
    def __init__(
        self,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order):
        payment_success = self.payment_processor.process(order)  

        if payment_success:
            order.status = "paid"
            self.notifier.send(order)  
            print("Checkout Sukses.")
            return True

        return False

andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

cc_processor = CreditCardProcessor()
checkout_cc = CheckoutService(
    payment_processor=cc_processor,
    notifier=email_service
)

print("=== Skenario 1: Credit Card ===")
checkout_cc.run_checkout(andi_order)

class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses QRIS.")
        return True


budi_order = Order("Budi", 100000)
qris_processor = QrisProcessor()

checkout_qris = CheckoutService(
    payment_processor=qris_processor,
    notifier=email_service
)

print("\n=== Skenario 2: Pembuktian OCP (QRIS) ===")
checkout_qris.run_checkout(budi_order)
