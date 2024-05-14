class BookingSystem:
    def __init__(self):
        self.rooms = {"101": None, "102": None, "103": None, "104": None}
        self.clients = {}

    def book_room(self):
        room_number = input("Enter room number to book (101, 102, 103, 104): ")

        if room_number not in self.rooms:
            print("Invalid room number. Please try again.")
            return self.book_room()

        if self.rooms[room_number] is not None:
            print(f"Room {room_number} is already booked. Please choose another room.")
            return self.book_room()

        name = input("Enter client's name: ")
        booking_id = input("Enter booking Code(4 digits): ")

        while True:
            try:
                number_of_guests = int(input("Enter number of guests: "))
                if number_of_guests > 0:
                    break
                else:
                    print("Number of guests must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        self.rooms[room_number] = {"name": name, "booking_id": booking_id, "number_of_guests": number_of_guests}
        self.clients[booking_id] = {"room_number": room_number, "name": name, "number_of_guests": number_of_guests}

        print(f"Room {room_number} has been successfully booked by {name}.")
        self.another_booking()

    def another_booking(self):
        more = input("Do you want to book another room? (yes/no): ").strip().lower()
        if more == 'yes':
            self.book_room()
        elif more == 'no':
            print("Thank you for using our booking system.")
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            self.another_booking()

    def display_bookings(self):
        print("\nCurrent bookings:")
        for room, details in self.rooms.items():
            if details:
                print(
                    f"Room {room} - {details['name']} (Booking ID: {details['booking_id']}), Number of Guests: {details['number_of_guests']}")
            else:
                print(f"Room {room} is available.")
        print("\n")


if __name__ == "__main__":
    system = BookingSystem()
    system.book_room()
    system.display_bookings()
