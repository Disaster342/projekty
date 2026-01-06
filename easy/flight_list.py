import uuid
import datetime

current_time = datetime.datetime.now()

class Airplane:
    def __init__(self, flight_number, origin, destination , start_time, landing_time):
        all_flights = []
        self.flight_id = uuid.uuid4()
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.start_time = start_time
        self.landing_time = landing_time

        Airplane.all_flights.append(self)

    def flight_duration(self):
        lasted = self.landing_time - self.start_time
        return (lasted)
    
    def status(self):
        if current_time < self.start_time:
            return "planned"
        if self.start_time < current_time < self.landing_time:
            return "in air"
        # if current_time > self.landing_time:
        return "arrived"
    
    def all_flights(x):
        return 
    
a1 = Airplane("LO123", "Warsaw", "London", datetime.datetime(2025, 1, 15, 10, 30), datetime.datetime(2026, 1, 15, 12, 20))
a2 = Airplane("LH456", "Frankfurt", "Mexico", datetime.datetime(2025, 2, 3, 14, 10), datetime.datetime(2026, 1, 3, 17, 45))
a3 = Airplane("AF789", "Moscow", "New York", datetime.datetime(2025, 3, 20, 22, 0), datetime.datetime(2025, 12, 11, 17, 30))
a4 = Airplane("DN128", "Lublin", "Malta", datetime.datetime(2025, 4, 11, 6, 50), datetime.datetime(2025, 4, 11, 9, 15))
a5 = Airplane("XZ615", "Tokyo", "Madrit", datetime.datetime(2026, 5, 8, 9, 0), datetime.datetime(2027, 5, 8, 11, 40))

#print(a1.flight_duration())
#print(a5.status)
print(Airplane.all_flights())



#setter i getter