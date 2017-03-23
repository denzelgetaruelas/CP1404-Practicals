"""Denzel Getaruelas"""
def main():
    name = input("Name: ")
    count = 0
    for i in name:
        if count % 2 == 0:
            print(i)

        count += 1
main()