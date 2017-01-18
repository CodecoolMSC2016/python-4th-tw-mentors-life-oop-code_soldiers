class Device:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = int(price)
        self.is_broken = bool(False)

    def destroy(self):
        self.is_broken = True
