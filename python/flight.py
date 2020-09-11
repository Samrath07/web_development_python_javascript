class Flight:
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    
    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Sud","Oshin","George","Ron","Harry","Ginny"]
for i in people:
    if flight.add_passengers(i):
        print(f"Added {i} to flight successfully")
    else:
        print(f"No available seats for {i}")
