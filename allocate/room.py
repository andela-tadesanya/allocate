class Room(object):
    """ base class for rooms at amity """

    def __init__(self, room_name):
        self.room_name = room_name
        self.space_limit = 0
        self.occupants = []


class Office(Room):
    """ an office room at amity """

    def __init__(self, room_name, space_limit):
        super(Room, self).__init__(room_name)
        self.space_limit = 6


class Living(Room):
    """ a living room at amity """

    def __init__(self, room_name, space_limit):
        super(Room, self).__init__(room_name)
        self.space_limit = 4
        self.room_gender = None