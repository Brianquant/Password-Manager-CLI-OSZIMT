from PasswordModel import *
from PasswordView import *


class PasswordController:
    def __init__(self):
        self.model = PasswordModel(self)
        self.view = PasswordView()

    def run(self):
        while True:
            self.view.show_start_menu()
            choice = self.view.get_user_choice()
            if choice == '1':
                self.model.databaseName = self.view.get_new_database_name()
                print(self.model.create_database())
            elif choice == '2':
                self.model.databaseName = self.view.get_selected_database()
                print(self.model.enterExistingDatabase())
                self.view.show_logged_in_menu()
                choice = self.view.get_user_choice()
                if choice == '1':
                    print(self.model.import_csv_into_table())
                elif choice == '2':
                    password_id = self.view.get_password_id()
                    name = self.view.get_name()
                    password = self.view.get_password()
                    url = self.view.get_url()
                    note = self.view.get_note()
                    print(self.model.add_new_password(password_id, name, password, url, note))
                elif choice == '3':
                    selected_id = self.view.get_selected_password_to_update()
                    selected_list = self.model.select_password_to_update(selected_id)
                    print(selected_list)
                    updated_selected_list = self.model.update_selected_password_set(selected_list)
                    print(self.model.update_selected_database(selected_id, updated_selected_list))
                elif choice == '4':
                    selected_id = self.view.get_selected_password_to_update()
                    print(self.model.remove_password_from_database(selected_id))
                elif choice == '5':
                    return self.run()
            elif choice == '3':
                print(self.model.list_databases())
