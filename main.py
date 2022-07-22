from modules.mod_menu import Menu


class Main:

    def run(self):
        print("\n************ Welcome to Map Color Application **************")
        print()
        Menu.menu(self)


if __name__ == '__main__':
    Main().run()
