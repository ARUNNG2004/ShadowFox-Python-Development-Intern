class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number}..."

    def receive_call(self, number):
        return f"Receiving call from {number}..."

    def take_picture(self):
        return f"Picture taken with {self.rear_camera}MP rear camera and {self.front_camera}MP front camera."
class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_model_info(self):
        return f"Apple Model: {self.model}"

class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_model_info(self):
        return f"Samsung Model: {self.model}"
# objects of Apple class
iphone14 = Apple("Touch Screen", "5G", False, 12, 48, "4GB", "128GB", "iPhone 14")
iphone15 = Apple("Touch Screen", "5G", False, 12, 48, "8GB", "256GB", "iPhone 15")

#  objects of Samsung class
galaxyS21 = Samsung("Touch Screen", "5G", True, 16, 108, "12GB", "128GB", "Galaxy S21")
galaxyNote20 = Samsung("Touch Screen", "5G", True, 10, 64, "8GB", "256GB", "Galaxy Note 20")

# Printing information
phones = [iphone14, iphone15, galaxyS21, galaxyNote20]
for phone in phones:
    print(phone.get_model_info())
    print(phone.make_call("1234567890"))
    print(phone.take_picture())
    print()
