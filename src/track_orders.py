class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.ordens = list()

    def __len__(self):
        return len(self.ordens)

    def add_new_order(self, customer, order, day):
        self.ordens.append([str(customer), str(order), str(day)])

    def get_most_ordered_dish_per_customer(self, customer):
        comidas_cliente = dict()
        for log in self.ordens:
            if log[0] == customer:
                if log[1] in comidas_cliente:
                    comidas_cliente[log[1]] += 1
                else:
                    comidas_cliente[log[1]] = 1
        return max(comidas_cliente, key=comidas_cliente.get)

    def get_never_ordered_per_customer(self, customer):
        comidas_res = set()
        costumeer_food = set()
        for log in self.ordens:
            comidas_res.add(log[1])
            if log[0] == customer:
                costumeer_food.add(log[1])
        return comidas_res.difference(costumeer_food)

    def get_days_never_visited_per_customer(self, customer):
        work_days = set()
        costumeer_days = set()
        for log in self.ordens:
            work_days.add(log[2])
            if log[0] == customer:
                costumeer_days.add(log[2])
        return work_days.difference(costumeer_days)

    def get_busiest_day(self):
        busy_days = dict()
        for log in self.ordens:
            if log[2] in busy_days:
                busy_days[log[2]] += 1
            else:
                busy_days[log[2]] = 1
        return max(busy_days, key=busy_days.get)

    def get_least_busy_day(self):
        busy_days = dict()
        for log in self.ordens:
            if log[2] in busy_days:
                busy_days[log[2]] += 1
            else:
                busy_days[log[2]] = 1
        return min(busy_days, key=busy_days.get)
