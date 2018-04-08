from simpledb import ThingToBook

class Hotel:
    def __init__(self, name, floor_count, rooms_per_floor):
        self._name = name
        self._floor_count = floor_count
        self._rooms_per_floor = rooms_per_floor
        self._rooms = []
        self._floors = []

        for f in range(floor_count):
            floor_rooms = []
            self._floors.append(floor_rooms)
            for r in range(rooms_per_floor):
                room = Room( (f+1) * 100 + r)
                floor_rooms.append(room)

                print("Add room number ", room)

            print("Done with Floor", f)

        print(self)

    def __str__(self):
        return ("Hotel name " + self._name
            + " with total of "
            + str(self._floor_count*self._rooms_per_floor)
            + " rooms")

class Room(ThingToBook):
    def __init__(self, roomNumber):
        ThingToBook.__init__(self, roomNumber)

    def __str__(self):
        return "I am Room number " + str(self._id)
