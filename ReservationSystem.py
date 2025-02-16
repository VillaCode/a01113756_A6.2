import json
import os

# Hotel
class Hotel:
    FILENAME = 'hotels.json' 


    def __init__(self, id, name, location, rooms):
        self.id = id
        self.name = name
        self.location = location
        self.rooms = rooms  
        

    #metodos auxiliares para guardar y leer el archivo
    def to_dict(self):
        return {"id": self.id, "name": self.name, "location": self.location, "rooms": self.rooms}
    
    @classmethod
    def load_hotels(cls):
        if os.path.exists(cls.FILENAME):
            with open(cls.FILENAME, 'r') as f:
                return json.load(f)
        return []

    @classmethod
    def save_hotels(cls, hotels):
        with open(cls.FILENAME, 'w') as f:
            json.dump(hotels, f)


    #Métodos de requerimiento
    @classmethod
    def create_hotel(cls, id, name, location, rooms):
        hotels = cls.load_hotels()
        hotel = Hotel(id, name, location, rooms)
        hotels.append(hotel.to_dict())
        cls.save_hotels(hotels)
        return hotel

    @classmethod
    def delete_hotel(cls, id):
        hotels = cls.load_hotels()
        hotels = [h for h in hotels if h["id"] != id]
        cls.save_hotels(hotels)

    @classmethod
    def display_hotel(cls, id):
        hotels = cls.load_hotels()
        for h in hotels:
            if h["id"] == id:
                print(h)
                return h
        return None

    @classmethod
    def modify_hotel(cls, id, name=None, location=None, rooms=None):
        hotels = cls.load_hotels()
        for h in hotels:
            if h["id"] == id:
                if name:
                    h["name"] = name
                if location:
                    h["location"] = location
                if rooms is not None:
                    h["rooms"] = rooms
        cls.save_hotels(hotels)

    @classmethod
    def reserve_room(cls, res_id, customer_id, hotel_id):
        return Reservation.create_reservation(res_id, customer_id, hotel_id)

    @classmethod
    def cancel_room_reservation(cls, res_id):
        Reservation.cancel_reservation(res_id)





# Customer
class Customer:
    FILENAME = 'customers.json' 

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def load_customers(cls):
        if os.path.exists(cls.FILENAME):
            with open(cls.FILENAME, 'r') as f:
                return json.load(f)
        return []

    @classmethod
    def save_customers(cls, customers):
        with open(cls.FILENAME, 'w') as f:
            json.dump(customers, f)

   
   
   
   
   # Métodos requerimientos
    @classmethod
    def create_customer(cls, id, name):
        customers = cls.load_customers()
        customer = Customer(id, name)
        customers.append(customer.to_dict())
        cls.save_customers(customers)
        return customer

    @classmethod
    def delete_customer(cls, id):
        customers = cls.load_customers()
        customers = [c for c in customers if c["id"] != id]
        cls.save_customers(customers)

    @classmethod
    def display_customer(cls, id):
        customers = cls.load_customers()
        for c in customers:
            if c["id"] == id:
                print(c)
                return c
        return None

    @classmethod
    def modify_customer(cls, id, name):
        customers = cls.load_customers()
        for c in customers:
            if c["id"] == id:
                c["name"] = name
        cls.save_customers(customers)


# Reservation
class Reservation:
    FILENAME = 'reservations.json'  
    def __init__(self, id, customer_id, hotel_id):
        self.id = id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        return {"id": self.id, "customer_id": self.customer_id, "hotel_id": self.hotel_id}

    @classmethod
    def load_reservations(cls):
        if os.path.exists(cls.FILENAME):
            with open(cls.FILENAME, 'r') as f:
                return json.load(f)
        return []

    @classmethod
    def save_reservations(cls, reservations):
        with open(cls.FILENAME, 'w') as f:
            json.dump(reservations, f)





    # Métodos requerimientos
    @classmethod
    def create_reservation(cls, id, customer_id, hotel_id):
        reservations = cls.load_reservations()
        reservation = Reservation(id, customer_id, hotel_id)
        reservations.append(reservation.to_dict())
        cls.save_reservations(reservations)
        return reservation

    @classmethod
    def cancel_reservation(cls, id):
        reservations = cls.load_reservations()
        reservations = [r for r in reservations if r["id"] != id]
        cls.save_reservations(reservations)
