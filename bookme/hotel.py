from simpledb import ThingToBook

class Hotel:
    def __init__(self, name, floor_count, rooms_per_floor):
        self._name = name
        self._residences = []
        self._floors = []

        for f in range(floor_count):
            floor_rooms = []
            for r in range(rooms_per_floor):
                residence_number = (f+1) * 100 + r
                residence = Residence( residence_number )
                floor_rooms.append(residence)
                self._residences[residence_number] = residence
                print("Add room number ", residence)

            self._floors.append(floor_rooms)
            print("Done with Floor", f)

        print(self)

    def __str__(self):
        return ("Hotel name " + self._name
            + " with total of "
            + len(self._residences)
            + " rooms")

class Residence(ThingToBook):
    def __init__(self, room_number):
        ThingToBook.__init__(self, room_number)

        self._bedrooms = []
        self._bathrooms = []
        self._half_bathrooms = []
        self._kitchens = []
        self._other_rooms = []
        self._living_area = []
        self._outdoor_space = []
        self._parking = []


    def __str__(self):
        return "I am Room number " + str(self._id)

class Room:
    def __init__(self, name, sqft):
        self.sqft = sqft
        self.name = name

class Bedroom(Room):
    def __init__(self, )