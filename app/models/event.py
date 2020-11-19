class Event():

# should include Date, Name of Event, Number of guests, Room Location, Description

    def __init__(self, name, date, guests, location, description, recurring):
        self.name = name
        self.date = date
        self.guests = guests
        self.location = location
        self.description = description
        self.recurring = recurring
