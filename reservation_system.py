"""Module for hotel, customer, and reservation management."""
import json
import os

class Hotel:
    """Hotel class for managing hotel data."""
    FILENAME = 'hotels.json'

    def __init__(self, hotel_id, name, location, rooms):
        """Initialize a hotel instance."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convert instance to dictionary."""
        return {"id": self.hotel_id, "name": self.name, "location": self.location,
                "rooms": self.rooms}

    @classmethod
    def load_hotels(cls):
        """Load hotels from JSON file."""
        if os.path.exists(cls.FILENAME):
            try:
                with open(cls.FILENAME, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error reading {cls.FILENAME}: {e}")
                return []
            except OSError as e:
                print(f"Unexpected error reading {cls.FILENAME}: {e}")
                return []
        return []

    @classmethod
    def save_hotels(cls, hotels):
        """Save hotels to JSON file."""
        try:
            with open(cls.FILENAME, 'w', encoding='utf-8') as f:
                json.dump(hotels, f)
        except OSError as e:
            print(f"Error writing to {cls.FILENAME}: {e}")

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Create a new hotel."""
        hotels = cls.load_hotels()
        hotel = Hotel(hotel_id, name, location, rooms)
        hotels.append(hotel.to_dict())
        cls.save_hotels(hotels)
        return hotel

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Delete a hotel by id."""
        hotels = cls.load_hotels()
        hotels = [h for h in hotels if h["id"] != hotel_id]
        cls.save_hotels(hotels)

    @classmethod
    def display_hotel(cls, hotel_id):
        """Display a hotel by id."""
        hotels = cls.load_hotels()
        for h in hotels:
            if h["id"] == hotel_id:
                print(h)
                return h
        return None

    @classmethod
    def modify_hotel(cls, hotel_id, name=None, location=None, rooms=None):
        """Modify a hotel's details."""
        hotels = cls.load_hotels()
        for h in hotels:
            if h["id"] == hotel_id:
                if name:
                    h["name"] = name
                if location:
                    h["location"] = location
                if rooms is not None:
                    h["rooms"] = rooms
        cls.save_hotels(hotels)

    @classmethod
    def reserve_room(cls, res_id, customer_id, hotel_id):
        """Reserve a room by delegating to Reservation."""
        return Reservation.create_reservation(res_id, customer_id, hotel_id)

    @classmethod
    def cancel_room_reservation(cls, res_id):
        """Cancel a room reservation."""
        Reservation.cancel_reservation(res_id)

class Customer:
    """Customer class for managing customer data."""
    FILENAME = 'customers.json'

    def __init__(self, customer_id, name):
        """Initialize a customer instance."""
        self.customer_id = customer_id
        self.name = name

    def to_dict(self):
        """Convert customer to dictionary."""
        return {"id": self.customer_id, "name": self.name}

    @classmethod
    def load_customers(cls):
        """Load customers from JSON file."""
        if os.path.exists(cls.FILENAME):
            try:
                with open(cls.FILENAME, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error reading {cls.FILENAME}: {e}")
                return []
            except OSError as e:
                print(f"Unexpected error reading {cls.FILENAME}: {e}")
                return []
        return []

    @classmethod
    def save_customers(cls, customers):
        """Save customers to JSON file."""
        try:
            with open(cls.FILENAME, 'w', encoding='utf-8') as f:
                json.dump(customers, f)
        except OSError as e:
            print(f"Error writing to {cls.FILENAME}: {e}")

    @classmethod
    def create_customer(cls, customer_id, name):
        """Create a new customer."""
        customers = cls.load_customers()
        customer = Customer(customer_id, name)
        customers.append(customer.to_dict())
        cls.save_customers(customers)
        return customer

    @classmethod
    def delete_customer(cls, customer_id):
        """Delete a customer by id."""
        customers = cls.load_customers()
        customers = [c for c in customers if c["id"] != customer_id]
        cls.save_customers(customers)

    @classmethod
    def display_customer(cls, customer_id):
        """Display a customer by id."""
        customers = cls.load_customers()
        for c in customers:
            if c["id"] == customer_id:
                print(c)
                return c
        return None

    @classmethod
    def modify_customer(cls, customer_id, name):
        """Modify a customer's name."""
        customers = cls.load_customers()
        for c in customers:
            if c["id"] == customer_id:
                c["name"] = name
        cls.save_customers(customers)

class Reservation:
    """Reservation class for managing reservations."""
    FILENAME = 'reservations.json'

    def __init__(self, reservation_id, customer_id, hotel_id):
        """Initialize a reservation instance."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convert reservation to dictionary."""
        return {"id": self.reservation_id, "customer_id": self.customer_id,
                "hotel_id": self.hotel_id}

    @classmethod
    def load_reservations(cls):
        """Load reservations from JSON file."""
        if os.path.exists(cls.FILENAME):
            try:
                with open(cls.FILENAME, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error reading {cls.FILENAME}: {e}")
                return []
            except OSError as e:
                print(f"Unexpected error reading {cls.FILENAME}: {e}")
                return []
        return []

    @classmethod
    def save_reservations(cls, reservations):
        """Save reservations to JSON file."""
        try:
            with open(cls.FILENAME, 'w', encoding='utf-8') as f:
                json.dump(reservations, f)
        except OSError as e:
            print(f"Error writing to {cls.FILENAME}: {e}")

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Create a new reservation."""
        reservations = cls.load_reservations()
        reservation = Reservation(reservation_id, customer_id, hotel_id)
        reservations.append(reservation.to_dict())
        cls.save_reservations(reservations)
        return reservation

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancel a reservation by id."""
        reservations = cls.load_reservations()
        reservations = [r for r in reservations if r["id"] != reservation_id]
        cls.save_reservations(reservations)

 