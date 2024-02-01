import requests
from bs4 import BeautifulSoup as soup


def scrape_flights(source, destination, date):
    
    url = "https://www.skyscanner.co.in/transport/flights/{source}/{destination}/{date}/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=0"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all flight details
        flights = soup.find_all("section", class_="listing__contracts")
        
        flight_details = []
        for flight in flights:
            airline = flight.find("span", class_="trip__airline--name").text.strip()
           # departure_time = flight.find("div", class_="dep-time").text.strip()
           # arrival_time = flight.find("div", class_="arr-time").text.strip()
            price = flight.find("span", class_="fpamount").text.strip()
            
            flight_details.append({
                "airline": airline,
               # "departure_time": departure_time,
                #"arrival_time": arrival_time,
                "price": price
            })
        
        return flight_details
    else:
        print("Failed to retrieve data")


source = "DEL"  
destination = "BOM" 
date = "240131"  
flights = scrape_flights(source, destination, date)
if flights:
    for i, flight in enumerate(flights, 1):
        print(f"Flight {i}:")
        print(f"Airline: {flight['airline']}")
       # print(f"Departure Time: {flight['departure_time']}")
       # print(f"Arrival Time: {flight['arrival_time']}")
        print(f"Price: {flight['price']}")
        print()
else:
    print("No flights found.")
