from Prac07.programminglanguage import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(vb)

    program_list = [ruby, python, vb]
    print("The dynamically typed languages are:")
    for program in program_list:
        if program.is_dynamic() == True:
            print(program.name)


main()
