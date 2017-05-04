from Prac07.guitarthing import Guitar


def main():
    print("My guitars!")
    name = ""
    while name == "":
        name = input("Name: ")
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print("{} ({}) : ${} added.".format(name, year, cost))
    print("... snip ...")
    print("These are my guitars:")
    guitar1 = Guitar(name, year, cost)
    print("Guitar 1: ", guitar1)
    guitar2 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("Guitar 2: ", guitar2)
    guitar3 = Guitar("Line 6 JTV-59", 2010, 1512.9)
    print("Guitar 3: ", guitar3)


main()
