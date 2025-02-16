"""Pruebas del sistema de reservas."""

import unittest
import os
import json
from reservation_system import Hotel, Customer, Reservation

class TestHotel(unittest.TestCase):
    """Pruebas de la clase Hotel."""
    TEST_FILE = 'test_hotels.json'

    def setUp(self):
        """Configuración."""
        Hotel.FILENAME = self.TEST_FILE
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def tearDown(self):
        """Limpieza."""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_create_hotel(self):
        """Crea un hotel y verifica la persistencia."""
        hotel = Hotel.create_hotel('h1', 'Hotel Uno', 'Ciudad Uno', 10)
        self.assertEqual(hotel.hotel_id, 'h1')
        self.assertEqual(hotel.name, 'Hotel Uno')
        self.assertEqual(hotel.location, 'Ciudad Uno')
        self.assertEqual(hotel.rooms, 10)
        with open(self.TEST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 'h1')

    def test_display_hotel(self):
        """Muestra un hotel existente."""
        Hotel.create_hotel('h2', 'Hotel Dos', 'Ciudad Dos', 20)
        hotel_data = Hotel.display_hotel('h2')
        self.assertIsNotNone(hotel_data)
        self.assertEqual(hotel_data['name'], 'Hotel Dos')

    def test_modify_hotel(self):
        """Modifica los datos de un hotel."""
        Hotel.create_hotel('h3', 'Hotel Tres', 'Ciudad Tres', 15)
        Hotel.modify_hotel('h3', name='Hotel Tres Modificado', location='Ciudad Modificada', rooms=25)
        hotel_data = Hotel.display_hotel('h3')
        self.assertEqual(hotel_data['name'], 'Hotel Tres Modificado')
        self.assertEqual(hotel_data['location'], 'Ciudad Modificada')
        self.assertEqual(hotel_data['rooms'], 25)

    def test_delete_hotel(self):
        """Elimina un hotel."""
        Hotel.create_hotel('h4', 'Hotel Cuatro', 'Ciudad Cuatro', 30)
        Hotel.delete_hotel('h4')
        hotel_data = Hotel.display_hotel('h4')
        self.assertIsNone(hotel_data)

class TestCustomer(unittest.TestCase):
    """Pruebas de la clase Customer."""
    TEST_FILE = 'test_customers.json'

    def setUp(self):
        """Configuración."""
        Customer.FILENAME = self.TEST_FILE
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def tearDown(self):
        """Limpieza."""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_create_customer(self):
        """Crea un cliente y verifica la persistencia."""
        customer = Customer.create_customer('c1', 'Cliente Uno')
        self.assertEqual(customer.customer_id, 'c1')
        self.assertEqual(customer.name, 'Cliente Uno')
        with open(self.TEST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 'c1')

    def test_display_customer(self):
        """Muestra un cliente existente."""
        Customer.create_customer('c2', 'Cliente Dos')
        cust_data = Customer.display_customer('c2')
        self.assertIsNotNone(cust_data)
        self.assertEqual(cust_data['name'], 'Cliente Dos')

    def test_modify_customer(self):
        """Modifica los datos de un cliente."""
        Customer.create_customer('c3', 'Cliente Tres')
        Customer.modify_customer('c3', 'Cliente Tres Modificado')
        cust_data = Customer.display_customer('c3')
        self.assertEqual(cust_data['name'], 'Cliente Tres Modificado')

    def test_delete_customer(self):
        """Elimina un cliente."""
        Customer.create_customer('c4', 'Cliente Cuatro')
        Customer.delete_customer('c4')
        cust_data = Customer.display_customer('c4')
        self.assertIsNone(cust_data)

class TestReservation(unittest.TestCase):
    """Pruebas de la clase Reservation."""
    TEST_FILE = 'test_reservations.json'

    def setUp(self):
        """Configuración."""
        Reservation.FILENAME = self.TEST_FILE
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def tearDown(self):
        """Limpieza."""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_create_reservation(self):
        """Crea una reserva y verifica la persistencia."""
        reservation = Reservation.create_reservation('r1', 'c1', 'h1')
        self.assertEqual(reservation.reservation_id, 'r1')
        self.assertEqual(reservation.customer_id, 'c1')
        self.assertEqual(reservation.hotel_id, 'h1')
        with open(self.TEST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 'r1')

    def test_cancel_reservation(self):
        """Cancela una reserva."""
        Reservation.create_reservation('r2', 'c2', 'h2')
        Reservation.cancel_reservation('r2')
        with open(self.TEST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()
