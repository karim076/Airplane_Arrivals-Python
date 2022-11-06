import csv
# opening arrivals.csv in reading modus.convert into dictionary list
myArrival = open("arrivals.csv", "r", encoding = "UTF-8")
reader = csv.DictReader(myArrival, delimiter=",")
arrivalList = list(reader)

#
for flight in arrivalList:
    print(f"At {flight['arrival']} a {flight['airline']} flight from the city of {flight['origin']} has landed, carrying {flight['passengers']} passengers")
print('----------------------------------------------------------------------------------------------------------------------------------------')
totalPassengers = 0
vluchten = 0
for flight in arrivalList:
    vluchten += 1
    totalPassengers += int(flight['passengers'])
averageFlights = totalPassengers / vluchten

print(f"Aantal vluchten: {vluchten}\nTotaal hoeveelheid passagiers: {totalPassengers}\nGemiddeld aantal passagiers: {averageFlights}")

airline =  input("Voer een vliegmaatschappijin:")
numFlightsX = 0
forflightinflightList:print(f"...")
if flight["airline"]==airline:
    numFlightsX += 1
