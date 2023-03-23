class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.compra_de_ingredientes = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.costumer_orders = list()

    def add_new_order(self, customer, order, day):
        self.costumer_orders.append([str(customer),
                                     str(order), str(day)])
        for food in self.INGREDIENTS[order]:
            if self.compra_de_ingredientes[food] >= self.MINIMUM_INVENTORY[food]:
                return False                                                    
            self.compra_de_ingredientes[food] += 1

    def get_quantities_to_buy(self):
        return self.compra_de_ingredientes
    
    def get_available_dishes():
        # retorno: um conjunto de pratos que ainda têm ingredientes disponíveis no estoque
        ...
