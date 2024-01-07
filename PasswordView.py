class PasswordView:
    def show_start_menu(self):
        print("############################")
        print("Password manager")
        print("############################")
        print("Enter 1 for create new database")
        print("Enter 2 for select existing database")
        print("Enter 3 for showing existing databases")

    def show_logged_in_menu(self):
        print("Password manager")
        print("############################")
        print("Enter 1 => Show existing passwords")
        print("Enter 2 => Add new password")
        print("Enter 3 => Update a password")
        print("Enter 4 => Delete password")
        print("Enter 5 => Exit")

    def get_user_choice(self):
        return input("What do you want to do?")

    def get_password_id(self):
        return input("Please give the password a unique Id: ")

    def get_name(self):
        return input("Please enter the name of the password: ")

    def get_password(self):
        return input("Please enter a strong password: ")

    def get_url(self):
        return input("Please enter the url to the matching password: ")

    def get_note(self):
        return input("Please enter a note if you want: ")

    def get_new_database_name(self):
        return input("Enter database name please: ")

    def get_selected_database(self):
        return input("Select database name: ")

    def get_selected_password_to_update(self):
        return input("Please enter the id of your password you want to update/remove: ")
