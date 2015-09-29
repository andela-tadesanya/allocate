import unittest
from allocate.room import Room, Office, Living


class RoomTestCase(unittest.TestCase):

    def setUp(self):
        self.room = Room('onyx')

    def tearDown(self):
        del self.room

    def test_class(self):
        self.assertTrue(isinstance(self.room, Room),
                        'is not an instance of Room')

    def test_roomname_set(self):
        self.assertGreater(len(self.room.room_name), 0,
                           'room_name not set')

    def test_roomname_correct(self):
        self.assertEqual(self.room.room_name, 'onyx',
                         'incorrect room name was set')

    def test_space_limit(self):
        self.assertEqual(self.room.space_limit, 0,
                         'space_limit not initially set to 0')

    def test_occupants(self):
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')


class OfficeTestCase(unittest.TestCase):

    def setUp(self):
        self.room = Office('gold', 6)

    def tearDown(self):
        del self.room

    def test_class(self):
        self.assertTrue(isinstance(self.room, Office),
                        'is not an instance of Office')

    def test_subclass(self):
        self.assertTrue(issubclass(type(self.room), Room),
                        'is not a subclass of Room')

    def test_roomname_correct(self):
        self.assertEqual(self.room.room_name, 'gold',
                         'incorrect room name was set')

    def test_space_limit(self):
        self.assertEqual(self.room.space_limit, 6,
                         'space_limit not set to 6')

    def test_occupants(self):
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')


class LivingTestCase(unittest.TestCase):

    def setUp(self):
        self.room = Living('crystal', 4)

    def tearDown(self):
        del self.room

    def test_class(self):
        self.assertTrue(isinstance(self.room, Living),
                        'is not an instance of Living')

    def test_subclass(self):
        self.assertTrue(issubclass(type(self.room), Room),
                        'is not a subclass of Room')

    def test_roomname_correct(self):
        self.assertEqual(self.room.room_name, 'crystal',
                         'incorrect room name was set')

    def test_space_limit(self):
        self.assertEqual(self.room.space_limit, 4,
                         'space_limit not set to 4')

    def test_occupants(self):
        self.assertEqual(len(self.room.occupants), 0,
                         'list of occupants not initially empty')

    def test_room_gender(self):
        self.assertIsNone(self.room.room_gender,
                          'room gender not initially None')


if __name__ == '__main__':
    unittest.main()
