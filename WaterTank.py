# Greg Elgin
# Last Updated: 04/25/20
# Water tank used in heat transfer simulation for Application Test


class WaterTank:
    # Initialize the water tank with the size measured in gallons
    # and the temperature of it's contents measured in degrees fahrenheit
    def __init__(self, size, temp):
        self.size = size
        self.temperature = temp

    # Return the temperature of the contents of the tank
    def get_temp(self):
        return self.temperature

    # Recalculate the temperature of the tanks contents
    def recalculate_temp(self, pump_flow, time_step, heated_temp):
        gallons_transferred = pump_flow * time_step
        cold_quantity = self.size - gallons_transferred
        new_temp = (cold_quantity * self.temperature + gallons_transferred * heated_temp) / self.size
        self.temperature = new_temp
