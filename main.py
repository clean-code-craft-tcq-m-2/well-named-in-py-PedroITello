from modules.mod_menu import Menu


class Main:

    def __init__(self):
        self.menu = Menu()

    def run(self):
        print("\n************ Welcome to Map Color Application **************")
        print()
        self.menu.menu()


if __name__ == '__main__':
    Main().run()
