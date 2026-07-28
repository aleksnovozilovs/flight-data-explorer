from flight_data import FlightData

flight_data = FlightData()
flight_data.load_csv()

search_airline = input("Enter an Airline: ")

found_airline = flight_data.find_airline(search_airline)

if found_airline:
    print ("\nFlights Found:")
    for flight in found_airline:
        print (flight)
else:
    print ("\nFlight not found")

#search_number = input("Enter a flight number: ")

#found_flight = flight_data.find_flight(search_number)

#if found_flight:
 #   print("\n Flight found:")
  #  print(found_flight)
#else:
 #   print("\nFlight not found")