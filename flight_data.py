import csv
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
    
    def search(self, field, value):
        search_results = [] 
        for flight in self.flights:
            flight_value = getattr(flight, field)
            if value.casefold() in flight_value.casefold():
                search_results.append(flight)
        return search_results

    def load_csv(self):
        with open("sample_flights.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                flight = Flight(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    int(row[4])
                )
                self.add_flight(flight)

