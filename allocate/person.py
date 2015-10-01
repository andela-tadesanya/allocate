import sqlite3 as lite


class Person(object):
    '''base class for a person at amity that requires rooms'''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.office_room = None


class Fellow(Person):
    '''class for a fellow person at amity that requires a office room
     and may or may not require a living room'''

    def __init__(self, first_name, last_name, living_required, gender=None):
        super(Fellow, self).__init__(first_name, last_name)
        self.living_required = living_required  # boolean if fellow requires living
        self.living_room = None  # name of living room fellow is allocated
        self.gender = gender

        # add object to database
        con = lite.connect('bin/amity.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO 'Fellow'('First_name','Last_name','Office_room','Living_required','Living_room','Gender') VALUES (?, ?, ?, ?, ?, ?);", (unicode(self.first_name), unicode(self.last_name), self.office_room, self.living_required, self.living_room, self.gender))

    def assign_office():
        pass


class Staff(Person):
    '''class for a staff person at amity that only requires
     office room allocation'''
    
    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)

        # add object to database
        con = lite.connect('bin/amity.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO 'Staff'('First_name','Last_name','Office_room') VALUES (?, ?, ?);", (unicode(self.first_name), unicode(self.last_name), self.office_room))