"""
Simple in memory database
Obviously no SQL support :)
"""

class ThingToBook:
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return "ID is " + str(self._id)

class SimpleDb:
    def __init__(self):
        self.data = []

    def createTable(self, tableName, colDef):
        pass

    def listTables(self):
        pass

    def deleteTable(self, tableName):
        pass

    def get(self, tableName):
        pass

class SimpleDbTable:
    def __init__(self, name, colDef):
        self.__name = name

    def insert(self, key, data):
        pass

    def update(self, key, data):
        pass

    def delete(self, key):
        pass

    def exists(self, key):
        pass
