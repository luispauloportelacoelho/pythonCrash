from car import Car
from electric_car import ElectricCar as EC

if __name__ == "__main__":
    my_mercedes = Car('Mercedes', 'S350', 2018)
    print(my_mercedes.get_descriptive_name())
    my_mercedes.read_odometer()
    my_mercedes.odometer_reading = 23
    my_mercedes.read_odometer()
    my_mercedes.update_odometer(10)
    my_mercedes.update_odometer(40)
    my_mercedes.read_odometer()
    my_mercedes.increment_odometer(30)
    my_mercedes.read_odometer()
    my_mercedes.gas_in_tank()
    my_mercedes.fill_gas_tank()
    my_mercedes.gas_in_tank()

    
    my_tesla = EC('Tesla', 'Model S', 2020)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()