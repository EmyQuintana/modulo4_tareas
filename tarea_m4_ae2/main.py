from tdc import TarjetaCredito

tarjeta1 = TarjetaCredito (0, 5000, 0.02)
tarjeta2 = TarjetaCredito (500, 10000, 0.05)
tarjeta3 = TarjetaCredito (100, 3000, 0.01)


TarjetaCredito.total_tarjetas_aperturadas()
TarjetaCredito.tarjetas_info()

print("\n--- Operaciones en Tarjeta 1 ---")
tarjeta1.comprar(1000).comprar(500).pagar(200).charge_interest().get_balance()
print("\n--- Operaciones en Tarjeta 2 ---")
tarjeta2.comprar(2000).comprar(800).comprar(4000).pagar(1000).pagar(1200).charge_interest().get_balance()
print("\n--- Operaciones en Tarjeta 3 ---")
tarjeta3.comprar(200).comprar(500).comprar(100).comprar(1000).comprar(2000).charge_interest().get_balance()
