import unittest
from allocate.person import Person, Fellow, Staff


class PersonTestCase(unittest.TestCase):

    def setUp(self):
        self.me = Person('john', 'doe')

    def tearDown(self):
        del self.me

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


class FellowTestCase(unittest.TestCase):

    def setUp(self):
        self.me = Fellow('john', 'doe', True)
        self.her = Fellow('jane', 'doe', False, 'female')
        self.him = Fellow('joe', 'doe', False, 'male')

    def tearDown(self):
        del self.me
        del self.her
        del self.him

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


class StaffTestCase(unittest.TestCase):

    def setUp(self):
        self.me = Staff('john', 'doe')

    def tearDown(self):
        del self.me

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
