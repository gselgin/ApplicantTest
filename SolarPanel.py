# Greg Elgin
# Last Updated: 04/25/20
# Solar panel used in heat transfer simulation for Application Test

# Convection heat transfer coefficient
h = .01

# Weight in pounds of one gallon of water
weight_of_water = 8.34


class SolarPanel:
    # Initialize the solar panel with the temperature of its surface in degrees fahrenheit
    def __init__(self, temp, surface_area, water_capacity):
        self.surface_temp = temp
        self.area = surface_area
        self.capacity = water_capacity

    # Change the surface temperature of the solar panel
    def set_surface_temperature(self, temp):
        self.surface_temp = temp

    # Heat the water in the solar panel by convection for the
    # amount of time that its spends in the panel
    def heat_water(self, water_temp, pump_flow):
        # Calculate by how much the temperature of the water changes in BTU/hr
        increase_rate = h * self.area * (self.surface_temp - water_temp)

        # Calculate how much time the water spends in the solar panel in minutes
        time = self.capacity / pump_flow

        # Calculate the weight of the water that passes through the panel in the time-step
        weight = (pump_flow * time) * weight_of_water

        # Calculate how many BTU are being added to the water using how much time the water spends in the panel
        increase_amount = increase_rate * (time * 60)

        # Convert the BTUs added to the water to degrees fahrenheit and calculate new temp
        new_water_temp = water_temp + (increase_amount / weight)

        return new_water_temp
