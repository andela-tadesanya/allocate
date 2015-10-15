import unittest
from allocate.person import Person, Fellow, Staff
from allocate import pre_populate
from allocate import reset


class PersonTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.me = Person('john', 'doe')

    def tearDown(self):
        del self.me
        reset.reset()

    def test_class(self):
        '''test if object is of class Person'''
        self.assertTrue(isinstance(self.me, Person),
                        'object is not an instance of Person')

    def test_names(self):
        '''test first and last names set correctly'''
        self.assertEqual(self.me.first_name, 'john',
                         'object first name incorrect')
        self.assertEqual(self.me.last_name, 'doe',
                         'object last name incorrect')

    def test_office_room(self):
        ''' test office room initially set to None'''
        self.assertIsNone(self.me.office_room,
                          'office room not initially set to None')

    def test_assign_office(self):
        '''test person can be assigned an office'''
        self.me.assign_office('Staff')
        self.assertIsNotNone(self.me.office_room,
                             'office room cannot be assigned to person')

    def test_id(self):
        '''test Person object has no id'''
        self.assertIsNone(self.me.id,
                          'An Object of Person cannot have an id')


class FellowTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.me = Fellow('john', 'doe', True)
        self.her = Fellow('jane', 'doe', False, 'female')
        self.him = Fellow('joe', 'doe', False, 'male')

    def tearDown(self):
        del self.me
        del self.her
        del self.him
        reset.reset()

    def test_class(self):
        '''check is object is of class Fellow'''
        self.assertTrue(isinstance(self.me, Fellow),
                        'object is not an instance of Fellow')

    def test_subclass(self):
        '''check if object is a subclass of Person'''
        self.assertTrue(issubclass(type(self.me), Person),
                        'object is not a subclass of Person')

    def test_names(self):
        '''check if first and last name set correctly'''
        self.assertEqual(self.me.first_name, 'john',
                         'object first name incorrect')
        self.assertEqual(self.me.last_name, 'doe',
                         'object last name incorrect')

    def test_office_room(self):
        '''check if office is initially set to None'''
        self.assertIsNone(self.me.office_room,
                          'office room not initially set to None')

    def test_gender_none(self):
        '''test gender is either None, male or female'''
        self.assertIsNone(self.me.gender, 'gender not default None when not set in class instanciation')

    def test_gender_female(self):
        '''test gender is female when a female Fellow created'''
        self.assertEqual(self.her.gender, 'female', 'female fellow gender not female')

    def test_gender_male(self):
        '''test gender is female when a female Fellow created'''
        self.assertEqual(self.him.gender, 'male', 'male fellow gender not male')

    def test_living_required(self):
        '''test living required is either set to false or true'''
        self.assertTrue(self.me.living_required,
                        'living required not what was set in object')

    def test_living_room(self):
        '''test living room is initially set to None'''
        self.assertIsNone(self.me.living_room,
                          'living_room not initially set to None')

    def test_assign_living(self):
        '''test living room can be assigned'''
        self.me.assign_living()
        self.assertIsNotNone(self.me.living_room,
                             'assign_living failed to assign a living room')


class StaffTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.me = Staff('john', 'doe')

    def tearDown(self):
        del self.me
        reset.reset()

    def test_class(self):
        '''test if object is of class Staff'''
        self.assertTrue(isinstance(self.me, Staff),
                        'object is not an instance of Staff')

    def test_subclass(self):
        '''test object is a subclass of Person'''
        self.assertTrue(issubclass(type(self.me), Person),
                        'object is not a subclass of Person')

    def test_names(self):
        '''test first and last names set correctly'''
        self.assertEqual(self.me.first_name, 'john',
                         'object first name incorrect')
        self.assertEqual(self.me.last_name, 'doe',
                         'object last name incorrect')

    def test_assign_staff_livingroom(self):
        '''test staff cannot be assigned living rooms'''

        with self.assertRaises(AttributeError):
            self.me.assign_living()
