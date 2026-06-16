from .item import *

class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        cuenta = {}
        for bill in self.bills:
            for product in bill.products:
                if product in cuenta:
                    cuenta[product] +=1
                else:
                    cuenta[product] = 1
        clave = max(cuenta, key=cuenta.get)
        return (clave, cuenta[clave])

    def find_top_two_sellers(self) -> list:
        ventas = {}
        for bill in self.bills:
            seller = bill.seller:
            importe = bill.calculate_total()
            if seller in ventas:
                ventas[seller] += importe
            else:
                ventas[seller] = importe
        return sorted(ventas, key=ventas.get, reverse=True)[:2]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        compras = {}
        for bill in self.bills:
            buyer = bill.buyer
            importe = bill.calculate_total()
            if buyer in compras:
                compras[buyer] += importe
            else:
                compras[buyer] = importe
        clave = sorted(compras, key=compras.get)[0]      
        return (clave, compras[clave])
    
    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        pass

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
