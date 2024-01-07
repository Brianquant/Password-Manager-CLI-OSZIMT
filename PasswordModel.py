import os
import csv
from prettytable import from_csv, PrettyTable


class PasswordModel:
    def __init__(self, databaseName):
        self.databaseName = databaseName

    def get_database_path(self):
        root_project_dir = os.path.abspath(os.curdir)
        return root_project_dir + "/databases/"

    def create_database(self):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        if os.path.exists(filepath):
            return "Database already exists"
        if not os.path.exists(filepath):
            open(filepath, "x")
            with open(filepath, 'w', newline="") as file:
                header = ['ID', 'Name', 'Password', 'URL', 'Note']
                csvwriter = csv.writer(file)
                csvwriter.writerow(header)
                file.close()
                return "Database created successfully"

    def add_new_password(self, password_id, name, password, url, note):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        new_data = [password_id, name, password, url, note]
        # 'a' stands for append
        with open(filepath, 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(new_data)
            file.close()
            return "Password " + name + " successfully added"

    def is_database_empty(self):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        rows = []
        with open(filepath, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
            if not rows:
                return True
            else:
                return False

    def enterExistingDatabase(self):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        if not os.path.exists(filepath):
            return "Database does not exist, please try again"

        if os.path.exists(filepath):
            print("############################")
            return "Selected database: " + self.databaseName

    def import_csv_into_table(self):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        with open(filepath) as fp:
            table = from_csv(fp)
            return table

    def list_databases(self):
        databases = []
        database_path = self.get_database_path()

        for item in os.listdir(database_path):

            item_path = os.path.join(database_path, item)

            if os.path.isfile(item_path):
                databases.append(item)

        processed_database_names = [filename.replace(".csv", "") for filename in databases]
        table = PrettyTable()
        table.field_names = ["Databases: "]
        table.add_rows([[name] for name in processed_database_names])

        return table

    def select_password_to_update(self, selected_id):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        tmp_password_set = []
        with open(filepath, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                tmp_password_set.append(row)

            for sublist in tmp_password_set[1:]:  # Skip the first sublist (header)
                if sublist[0] == selected_id:
                    selected_list = sublist

                    return selected_list

    def update_selected_database(self, selected_id, selected_list):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        with open(filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for i, sublist in enumerate(data):
            if sublist[0] == selected_id:
                data[i] = selected_list
                break
        else:
            print("ID not found.")

        # Write the updated data back to the CSV file
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            return "Updated successfully the password with the id " + selected_id

    def update_selected_password_set(self, selected_list):

        for i in range(len(selected_list)):
            response = input("Do you want to update " + "'" + selected_list[i] + "'" + " ? (yes/no): ").lower()

            if response == 'yes':
                # Get the new value from the user
                new_value = input("Edit Mode: ")
                # Update the item in the list
                selected_list[i] = new_value

        return selected_list

    def remove_password_from_database(self, selected_id):
        filepath = self.get_database_path() + self.databaseName + ".csv"

        with open(filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        new_data = []
        for sublist in data:
            if sublist[0] != selected_id:
                new_data.append(sublist)

        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
            return "Removed password with the id " + selected_id + " successfully"












