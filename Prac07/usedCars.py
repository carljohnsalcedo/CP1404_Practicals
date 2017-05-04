from Prac07.car import Car


def main():
    bus = Car(180)
    bus.name = "Bus"
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100)
    limo.fuel += 20
    limo.name = "Limo"
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)


main()
