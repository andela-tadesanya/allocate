import unittest
from allocate.room import Room, Office, Living
from allocate.person import Person, Fellow, Staff
from allocate import pre_populate
from allocate import reset
import sqlite3 as lite
try:
    import cPickle as pickle
except:
    import pickle

class RoomTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.room = Room('onyx')

    def tearDown(self):
        del self.room
        reset.reset()

    def test_class(self):
        '''test object is an instance of Room'''
        self.assertTrue(isinstance(self.room, Room),
                        'object is not an instance of Room')

    def test_roomname_set(self):
        '''test room name is set'''
        self.assertGreater(len(self.room.room_name), 0,
                           'room_name not set')

    def test_roomname_correct(self):
        '''test correct room name is set'''
        self.assertEqual(self.room.room_name, 'onyx',
                         'incorrect room name was set')

    def test_space_count(self):
        '''test space limit is set to 0 on instantiation'''
        self.assertEqual(self.room.space_count, 0,
                         'space_count not initially set to 0')

    def test_occupants(self):
        '''test occupants initially empty'''
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')


class OfficeTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.room = Office('gold')
        self.staff1 = Staff('tosin', 'ade')

    def tearDown(self):
        del self.room
        reset.reset()

    def test_class(self):
        '''test object is instance of Office'''
        self.assertTrue(isinstance(self.room, Office),
                        'is not an instance of Office')

    def test_subclass(self):
        '''test object is subclass of Room'''
        self.assertTrue(issubclass(type(self.room), Room),
                        'is not a subclass of Room')

    def test_roomname_correct(self):
        '''test correct room name is set'''
        self.assertEqual(self.room.room_name, 'gold',
                         'incorrect room name was set')

    def test_space_count(self):
        '''test space limit is only 6'''
        self.assertLessEqual(self.room.space_count, 6,
                             'office space_count exceeds 6')

    def test_occupants(self):
        '''test occupants initially empty'''
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')

    def test_get_occupants(self):
        '''test occupant list'''
        self.assertIsNone(self.room.get_occupants())


    def get_office_room(self, room):
        '''gets list of an office occupants from database'''

        con = lite.connect('amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            sql = "SELECT Occupants from Office where Room_name = '%s'" % room
            cur.execute(sql)
            result = cur.fetchone()

            if result is not None:
                # unpickle the data
                unpickled_result = pickle.loads(str(result['Occupants']))
            else:
                # return empty list
                unpickled_result = []
        return unpickled_result

    def test_occupants_in_room(self):
        '''test occupant added to office'''

        # assign staff to an ofiice
        self.staff1.assign_office('staff')
        # get office staff was assigned to
        staff_office = self.staff1.office_room

        # get occupants list of the office
        room_occupants = self.get_office_room(staff_office)

        # check staff is in office
        self.assertIn('tosin ade', room_occupants,
                      'Person not in occupants list of an office')




class LivingTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.room = Living('crystal')

    def tearDown(self):
        del self.room
        reset.reset()

    def test_class(self):
        '''test object is instance of Living class'''
        self.assertTrue(isinstance(self.room, Living),
                        'is not an instance of Living')

    def test_subclass(self):
        '''test object is a subclass of Room'''
        self.assertTrue(issubclass(type(self.room), Room),
                        'is not a subclass of Room')

    def test_roomname_correct(self):
        '''test correct room name set'''
        self.assertEqual(self.room.room_name, 'crystal',
                         'incorrect room name was set')

    def test_space_count(self):
        '''test space limit is only 4'''
        self.assertLessEqual(self.room.space_count, 4,
                             'living space_count exceeds 4')

    def test_occupants(self):
        '''test occupants is initially empty'''
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')
        
    def test_get_occupants(self):
        '''test occupant list'''
        self.assertIsNone(self.room.get_occupants())

    def test_room_gender(self):
        '''test room gender initially None'''
        self.assertIsNone(self.room.room_gender,
                          'room gender not initially None')


if __name__ == '__main__':
    unittest.main()
