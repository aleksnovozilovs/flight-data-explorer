from flight import Flight
from flight_data import FlightData

flight_data = FlightData()

flight_1 = Flight(
    "BA117",
    "British Airways",
    "London Heathrow LHR",
    "New York JFK",
    36000
)

flight_2 = Flight(
    "EK2",
    "Emirates",
    "London Heathrow LHR",
    "Dubai DXB",
    38000
)

flight_data.add_flight(flight_1)
flight_data.add_flight(flight_2)

search_number = input("Enter a flight number: ")

found_flight = flight_data.find_flight(search_number)

if found_flight:
    print("\n Flight found:")
    print(found_flight)
else:
    print("\nFlight not found")