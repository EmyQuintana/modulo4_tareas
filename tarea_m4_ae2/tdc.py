class TarjetaCredito:
    tarjetas_aperturadas = []
    _next_id = 1
    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.balancetopay = saldo_pagar
        self.creditlimit = limite_credito
        self.interest = intereses
        self.id_tarjeta = TarjetaCredito._next_id
        TarjetaCredito._next_id += 1 
        TarjetaCredito.tarjetas_aperturadas.append(self)
        print(f"Tarjeta #{self.id_tarjeta} creada con límite de ${self.creditlimit:.2f} y saldo inicial de ${self.balancetopay:.2f}")

    def comprar (self, monto):
            if self.balancetopay + monto > self.creditlimit:
                print(f"tarjeta # {self.id_tarjeta} Ha superado el límite de crédito, no puede hacer la compra")
            else: 
                self.balancetopay += monto
            return self
    
    def pagar (self, monto):
        self.balancetopay -= monto
        return self
    
    def get_balance (self):
        print (f"El saldo a pagar es: {self.balancetopay}")
        return self.balancetopay
    
    def charge_interest (self):
        self.balancetopay += (self.balancetopay * self.interest)
        return self
    
    @classmethod
    def tarjetas_info (cls):
        print ("Informacion de todas las tarjetas:")
        for tarjeta in cls.tarjetas_aperturadas:
            print(f"\n--- Tarjeta #{tarjeta.id_tarjeta} ---") 
            print (f"El saldo a pagar es: {tarjeta.balancetopay}")
            print (f"El limite de crédito es: {tarjeta.creditlimit}")
            print (f"El interes es: {tarjeta.interest}")

        return cls  
    
    @classmethod
    def total_tarjetas_aperturadas(cls):
        total = len(cls.tarjetas_aperturadas)
        print(f"\nTotal de tarjetas de crédito aperturadas: {total}")
        return total