# Hotel Management System in Python

class HotelManagementSystem:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = {1: "Available", 2: "Available", 3: "Available", 4: "Available"}
        self.menu = {
            "Pasta": 100,
            "Burger": 50,
            "Pizza": 150,
            "Coke": 30,
            "Ice Cream": 60
        }
        self.orders = []
        self.room_booking = {}

    def show_hotel_name(self):
        print(f"Welcome to {self.hotel_name}!\n")

    def show_rooms(self):
        print("Rooms Availability:")
        for room, status in self.rooms.items():
            print(f"Room {room}: {status}")
        print()

    def book_room(self):
        room_number = int(input("Enter the room number you want to book (1-4): "))
        if self.rooms.get(room_number) == "Available":
            self.rooms[room_number] = "Booked"
            self.room_booking["Room"] = room_number
            print(f"Room {room_number} successfully booked!\n")
        else:
            print(f"Room {room_number} is already booked.\n")

    def show_menu(self):
        print("Menu Card:")
        for dish, price in self.menu.items():
            print(f"{dish}: Rs. {price}")
        print()

    def take_order(self):
        print("Please enter your orders (Enter 'done' to finish):")
        while True:
            order = input("Enter item: ").capitalize()
            if order == 'Done':
                break
            if order in self.menu:
                self.orders.append(order)
                print(f"Added {order} to your order.")
            else:
                print("Invalid item. Please select from the menu.")
        print()

    def calculate_bill(self):
        total_bill = 0
        print("Your Orders:")
        for item in self.orders:
            total_bill += self.menu[item]
            print(f"{item}: Rs. {self.menu[item]}")
        print(f"\nTotal bill for food: Rs. {total_bill}")

        room_charge = 500  # Example charge for room booking
        print(f"Room charge: Rs. {room_charge}")
        total_bill += room_charge
        print(f"\nTotal amount due: Rs. {total_bill}\n")

    def show_options(self):
        print("1. Show Hotel Name")
        print("2. Show Available Rooms")
        print("3. Book Room")
        print("4. Show Menu Card")
        print("5. Take Order")
        print("6. Calculate Bill")
        print("7. Exit\n")

    def run(self):
        while True:
            self.show_options()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.show_hotel_name()
            elif choice == 2:
                self.show_rooms()
            elif choice == 3:
                self.book_room()
            elif choice == 4:
                self.show_menu()
            elif choice == 5:
                self.take_order()
            elif choice == 6:
                self.calculate_bill()
            elif choice == 7:
                print("Exiting the system. Have a nice day!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    hotel = HotelManagementSystem("Dreamy destiny Hotel")
    hotel.run()
