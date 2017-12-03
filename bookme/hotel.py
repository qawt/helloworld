from simpledb import *

class Hotel:
    def __init__(self, name, floorCount, roomsPerFloor):
        self.name = name
        self.floorCount = floorCount
        self.roomsPerFloor = roomsPerFloor
        self.rooms = []
        self.floors = []

        for f in range(floorCount):
            floorRooms = []
            self.floors.append(floorRooms)
            for r in range(roomsPerFloor):
                room = Room( (f+1) * 100 + r)
                floorRooms.append(room)

                print("Add room number ", room)

            print("Done with Floor", f)

        print(self)

    def __str__(self):
        return ("Hotel name " + self.name
            + " with total of "
            + str(self.floorCount*self.roomsPerFloor)
            + " rooms")


class Room(ThingToBook):
    def __init__(self, roomNumber):
        ThingToBook.__init__(self, roomNumber)

    def __str__(self):
        return "I am Room number " + str(self.id)
