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

    def get_occupants(self):
        '''display lists of occupants'''
        print "%s (OFFICE)" % (self.room_name.upper())
        if self.space_count == 0:
            print "Empty."
        else:
            uppercase_occu = map(lambda x: x.upper(), self.occupants)
            print ", ".join(uppercase_occu)
        print "\n"


class Living(Room):
    '''a living room at amity'''

    def __init__(self, room_name):
        super(Living, self).__init__(room_name)
        self.room_gender = None

    def get_occupants(self):
        '''display lists of occupants'''
        print "%s (LIVING)" % (self.room_name.upper())
        if self.space_count == 0:
            print "Empty."
        else:
            uppercase_occu = map(lambda x: x.upper(), self.occupants)
            print ", ".join(uppercase_occu)
        print "\n"
