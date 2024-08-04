# register_user_menu.py

import smartscan_registration_module as srm

def display_menu():
    print("\nMenu:")
    print("1. Register User from SmartScan Code")
    print("2. View All Registered Users")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            smartscan_code = input("Enter the SmartScan Code (format: 'name,email'): ")
            srm.RegisterUserFromSmartScan(smartscan_code.encode('utf-8'))
        elif choice == '2':
            srm.view_all_registered_users()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
