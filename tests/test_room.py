import unittest
from allocate.room import Room, Office, Living


class RoomTestCase(unittest.TestCase):

    def setUp(self):
        self.room = Room('onyx')

    def tearDown(self):
        del self.room

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
        self.room = Office('gold')

    def tearDown(self):
        del self.room

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


class LivingTestCase(unittest.TestCase):

    def setUp(self):
        self.room = Living('crystal')

    def tearDown(self):
        del self.room

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

    def test_room_gender(self):
        '''test room gender initially None'''
        self.assertIsNone(self.room.room_gender,
                          'room gender not initially None')


if __name__ == '__main__':
    unittest.main()
