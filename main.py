# https://github.com/asalnorouzzade/Practice-43-The-Gallery.git
class Vehicle:
    def __init__(self, vehicle_id, model, color, price, is_sold):
        self.id = vehicle_id
        self.model = model
        self.color = color
        self.price = int(price)
        self.is_sold = is_sold

    def get_info(self):
        sold_str = "Yes" if self.is_sold else "No"
        return f"Vehicle | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {sold_str}"

    def update_price(self, new_price):
        self.price = int(new_price)

    def update_sold_status(self, new_status):
        if isinstance(new_status, str):
            self.is_sold = (new_status == "True")
        else:
            self.is_sold = new_status

class Car(Vehicle):
    def __init__(self, vehicle_id, model, color, price, is_sold, number_of_doors):
        super().__init__(vehicle_id, model, color, price, is_sold)
        self.number_of_doors = int(number_of_doors)

    def get_info(self):
        sold_str = "Yes" if self.is_sold else "No"
        return f"Car | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {sold_str} | Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, model, color, price, is_sold, engine_capacity):
        super().__init__(vehicle_id, model, color, price, is_sold)
        self.engine_capacity = int(engine_capacity)

    def get_info(self):
        sold_str = "Yes" if self.is_sold else "No"
        return f"Motorcycle | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {sold_str} | Engine Capacity: {self.engine_capacity}"

class Truck(Vehicle):
    def __init__(self, vehicle_id, model, color, price, is_sold, cargo_capacity):
        super().__init__(vehicle_id, model, color, price, is_sold)
        self.cargo_capacity = int(cargo_capacity)

    def get_info(self):
        sold_str = "Yes" if self.is_sold else "No"
        return f"Truck | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {sold_str} | Cargo Capacity: {self.cargo_capacity}"

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    pointer = 0
    count = int(data[pointer]); pointer += 1
    vehicles = {}
    for i in range(count):
        Vehicle_type = data[pointer]; pointer += 1
        Vehicle_id = int(data[pointer]); pointer += 1
        model = data[pointer]; pointer += 1
        color = data[pointer]; pointer += 1
        price = data[pointer]; pointer += 1
        is_sold_string = data[pointer]; pointer += 1
        is_sold = (is_sold_string == "True")
        extra = data[pointer]; pointer += 1
        if Vehicle_type == "Car":
            Vehicle = Car(Vehicle_id, model, color, price, is_sold, extra)
        elif Vehicle_type == "Motorcycle":
            Vehicle = Motorcycle(Vehicle_id, model, color, price, is_sold, extra)
        elif Vehicle_type == "Truck":
            Vehicle = Truck(Vehicle_id, model, color, price, is_sold, extra)
        vehicles[Vehicle_id] = Vehicle
        
    queries = int(data[pointer]); pointer += 1
    for i in range(queries):
        command = data[pointer]; pointer += 1
        Vehicle_id = int(data[pointer]); pointer += 1
        vehicle = vehicles[Vehicle_id]
        if command == "INFO":
            print(vehicle.get_info())
        elif command == "PRICE":
            new_price = data[pointer]; pointer += 1
            vehicle.update_price(new_price)
        elif command == "SOLD":
            new_status = data[pointer]; pointer += 1
            vehicle.update_sold_status(new_status)

if __name__ == "__main__":
    main()
