from app.models.event import *



event1 = Event("Christmas market", "24 Dec", "12", "Town Hall", "A fun time for the socially distanced small crowd",  True)
event2 = Event("Hogmanay Hootenany", "31 Dec", "24", "Town Hall", "Celebrate the end of 2020", False)
events = [event1, event2]


def add_new_event(event):
    events.append(event)
