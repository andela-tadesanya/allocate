import sqlite3 as lite
import random
try:
    import cPickle as pickle
except:
    import pickle


class Person(object):
    '''base class for a person at amity that requires rooms'''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.office_room = None
        self.id = None

    def assign_office(self, table):
        '''assign object to an office'''

        # get list of offices with available space
        con = lite.connect('amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM Office WHERE Space_count < 6')
            rows = cur.fetchall()

            # break if there is no available space in any office
            if not rows:
                print 'No more available office space'
                return
            else:
                # randomly select an office from returned list of offices
                office = rows[random.randint(0, len(rows) - 1)]

                # assign office name to object office_room property and update in database
                self.office_room = office['Room_name']
                if table == 'Staff':
                    cur.execute("UPDATE Staff set Office_room = ? where Id = ?", (self.office_room, self.id))
                else:
                    cur.execute("UPDATE Fellow set Office_room = ? where Id = ?", (self.office_room, self.id))

                # update space_count of the office by +1
                cur.execute("UPDATE Office set Space_count = ? where Id = ?", (office['Space_count'] + 1, office['Id']))

                # add object to list of occupants of the office
                # unpickle the data and append object name into occupants list
                occupants = pickle.loads(str(office['Occupants']))
                occupants.append('%s %s' % (self.first_name, self.last_name))

                # pickle updated occupants list and update entry in database
                pickled_occu = pickle.dumps(occupants)
                cur.execute("UPDATE Office set Occupants = ? where Id = ?", (pickled_occu, office['Id']))


class Fellow(Person):
    '''class for a fellow person at amity that requires a office room
     and may or may not require a living room'''

    def __init__(self, first_name, last_name, living_required, gender=None):
        super(Fellow, self).__init__(first_name, last_name)
        self.living_required = living_required  # if fellow requires living
        self.living_room = None  # name of living room fellow is allocated
        self.gender = gender

        # add object to database
        con = lite.connect('amity.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO 'Fellow'('First_name','Last_name','Office_room','Living_required','Living_room','Gender') VALUES (?, ?, ?, ?, ?, ?);", (self.first_name, self.last_name, self.office_room, self.living_required, self.living_room, self.gender))

            # set self.id from the Id of the row just created
            self.id = cur.lastrowid

    def assign_living(self):
        con = lite.connect('amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()

            # get available rooms based on gender
            if self.gender is not None:
                sql = "SELECT * FROM Living WHERE (Space_count < 4) AND (Room_gender = '%s' OR Room_gender IS NULL)" % (self.gender)
            else:
                sql = "SELECT * FROM Living WHERE (Space_count < 4) AND (Room_gender = 'mixed' OR Room_gender IS NULL)"
            cur.execute(sql)
            rows = cur.fetchall()

            # break if there is no available space in any living
            if not rows:
                print 'No more available living space'
                return
            else:
                # randomly select a living room from returned list of living rooms
                living = rows[random.randint(0, len(rows) - 1)]

                # set room gender if previously NULL
                if living['Room_gender'] is None:
                    if self.gender is not None:
                        cur.execute("UPDATE Living SET Room_gender = ? WHERE Id = ?", (self.gender, living['Id']))
                    else:
                        cur.execute("UPDATE Living SET Room_gender = ? WHERE Id = ?", ('mixed', living['Id']))

                # update space_count of the office by +1
                cur.execute("UPDATE Living SET Space_count = ? where Id = ?", (living['Space_count'] + 1, living['Id']))

                # assign living name to object living_room property and update in database
                self.living_room = living['Room_name']
                cur.execute("UPDATE Fellow SET Living_room = ? where Id = ?", (self.living_room, self.id))

                # add fellow into occupants list of living room
                # unpickle the data and append object name into occupants list
                occupants = pickle.loads(str(living['Occupants']))
                occupants.append('%s %s' % (self.first_name, self.last_name))

                # pickle updated occupants list and update entry in database
                pickled_occu = pickle.dumps(occupants)
                cur.execute("UPDATE Living set Occupants = ? where Id = ?", (pickled_occu, living['Id']))


class Staff(Person):
    '''class for a staff person at amity that only requires
    office room allocation'''

    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)

        # add object to database
        con = lite.connect('amity.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO 'Staff'('First_name','Last_name','Office_room') VALUES (?, ?, ?);", (self.first_name, self.last_name, self.office_room))

            # set self.id
            self.id = cur.lastrowid
