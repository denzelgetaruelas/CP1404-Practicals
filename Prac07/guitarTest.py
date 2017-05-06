from Prac07.guitar import Guitar


def main():
    guitar_list = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(Guitar(name, year, cost), "added.")
        guitar_list.append(Guitar(name, year, cost))
        name = input("Name: ")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    count = 0
    for guitar in guitar_list:
        guitar.is_vintage()
        count += 1
        print("Guitar {}: {:>20} "
              "({}), worth $"
              "{:10.2f} {}".format(count, guitar.name, guitar.year, guitar.cost, guitar.vintage))


main()
