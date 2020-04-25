# Greg Elgin
# Last Updated: 04/25/20
# Heat transfer simulation from solar panel to storage tank for Application Test

import SolarPanel
import WaterTank


def main():
    # Initialise pump strength in gallons per minute
    pump_flow = 2.0

    # Initialize the surface area of the solar panel in square feet
    surface_area = 10

    # Initialize capacity of solar panel in gallons
    capacity = 2.0

    # Initialize the temperature of the surface of the solar panel in degrees fahrenheit
    surface_temp = 80.0

    # Initialize the capacity of the tank in gallons
    capacity = 100.0

    # Initialize the initial temperature of the water in the tank
    tank_temp = 40.0

    # Create solar panel and water tank objects
    solar_panel = SolarPanel.SolarPanel(surface_temp, surface_area, capacity)
    water_tank = WaterTank.WaterTank(capacity, tank_temp)

    # Initialize time step in minutes
    time_step = 1

    # Run simulation for 60 time steps
    for i in range(1, 61):
        # Water in the solar panel is heated
        new_temp = solar_panel.heat_water(water_tank.get_temp(), pump_flow)

        # Warm water is pumped to tank, cold water is pumped from tank
        water_tank.recalculate_temp(pump_flow, time_step, new_temp)

        # Resulting temperature of tank is printed
        print("Temperature of tank after:", time_step * i, "minutes(degrees F): %3.1f" % (water_tank.get_temp()))


main()
