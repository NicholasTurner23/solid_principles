"""
A derived class can assume the place of its super class and everythin should work.

"""

class KitchenAppliance():
    def on(self):
        pass

    def off(self):
        pass


class KitchenApplianceWithTemp(KitchenAppliance):
    def set_temperature(self):
        pass


class Toaster(KitchenApplianceWithTemp):
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self):
        pass


class Juicer(KitchenAppliance):
    def on(self):
        pass

    def off(self):
        pass