import os
from ics import Calendar, Event
from datetime import datetime

def load_calendar(filepath="schedule.ics"):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return Calendar(f.read())
    return Calendar()

def add_event():
    cal = load_calendar()

    e = Event()
    e.name        = os.environ["EVENT_NAME"]
    e.begin       = os.environ["START_TIME"]
    e.end         = os.environ["END_TIME"]
    e.location    = os.environ.get("LOCATION", "")
    e.description = os.environ.get("DESCRIPTION", "") + f" (Added by {os.environ['USER']})"

    cal.events.add(e)

    with open("schedule.ics", "w") as f:
        f.writelines(cal)

    print(f"Added event: {e.name}")

add_event()
