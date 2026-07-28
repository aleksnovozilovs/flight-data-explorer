from flight import Flight

class FlightData:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def show_all_flights(self):
        for flight in self.flights:
            print(flight)

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number.casefold() == flight_number.casefold():
                return flight
        return None    