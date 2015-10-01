class Room(object):
    '''base class for rooms at amity'''

    def __init__(self, room_name):
        self.room_name = room_name
        self.space_count = 0
        self.occupants = []


class Office(Room):
    '''an office room at amity'''

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)


class Living(Room):
    '''a living room at amity'''

    def __init__(self, room_name):
        super(Living, self).__init__(room_name)
        self.room_gender = None
