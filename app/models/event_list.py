from app.models.event import *



event1 = Event("Christmas market", "12-24 Dec", "12 tickets", "Town Hall", "A fun time for the socially distanced small crowd",  True)
event2 = Event("Hogmanay Hootenanny", "31 Dec", "24 tickets", "Town Hall", "Celebrate the start of 2021 and new beginnings!", False)
events = [event1, event2]


def add_new_event(event):
    events.append(event)
