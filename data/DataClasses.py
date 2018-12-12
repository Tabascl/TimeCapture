import datetime

class Day:
    def __init__(self, date):
        assert isinstance(date, datetime.date)
        self.date = date
        self.arrive = datetime.time(8, 0)
        self.leave = datetime.time(17, 30)
        self.trips = []
        self.tasks = []

class Trip:
    def __init__(self, start, destination, distance):
        assert isinstance(start, Location)
        assert isinstance(destination, Location)
        self.start = start
        self.destination = destination
        self.distance = distance

class Task:
    def __init__(self, company, description):
        self.company = company
        self.description = description

class Location:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name, location):
        assert isinstance(location, Location)
        self.name = name
        self.location = location