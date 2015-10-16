import mock
from mock import patch, MagicMock
import unittest
from allocate.operation import Operator, main
from allocate import pre_populate, reset

class OperatorTestCase(unittest.TestCase):

    def setUp(self):
        pre_populate.populate()
        self.prompt = Operator()
                
    def tearDown(self):
        del self.prompt
        reset.reset()

    def test_pre_populate(self):
        '''test pre_populate can be called'''

        self.prompt.do_pre_populate = MagicMock(name='do_pre_populate')
        self.prompt.do_pre_populate()
        self.prompt.do_pre_populate.assert_called_once_with()

    def test_batch_allocate(self):
        '''test batch allocate command'''

        self.prompt.do_batch_allocate = MagicMock(name='do_batch_allocate')
        source = 'C:/Users/Andela/test.txt'
        self.prompt.do_batch_allocate(source)
        self.prompt.do_batch_allocate.assert_any_call(source)
        self.prompt.do_batch_allocate.assert_called_once_with('C:/Users/Andela/test.txt')

    def test_get_allocation(self):
        '''test get allocation'''

        self.prompt.do_get_allocation = MagicMock(name='do_get_allocation')
        self.prompt.do_get_allocation()
        self.prompt.do_get_allocation.assert_called_with()

    def test_file_extension(self):
        '''test file extension'''

        ext = self.prompt.file_ext('C:/Users/Andela/test.txt')
        self.assertEqual(ext, 'txt')
        self.assertIsNotNone(self.prompt.file_ext('C:/Users/Andela/test.txt'))

    def test_get_person_status(self):
        '''test person status'''

        self.assertIsNotNone(self.prompt.get_person_status(2,'tosin','ade'))

    def test_process_txt(self):
        '''test process from txt file'''

        self.assertIsNone(self.prompt.process_txt('C:/Users/Andela/test.txt'))

    def test_process_csv(self):
        '''test process from csv file'''

        self.assertIsNone(self.prompt.process_csv('C:/Users/Andela/test.csv'))

    def test_get_office_room(self):
        '''test getting an office'''

        self.assertIsNotNone(self.prompt.get_office_room('gold'))

    def test_get_living_room(self):
        '''test getting an living'''

        self.assertIsNotNone(self.prompt.get_living_room('london'))

    def test_is_name_vacant(self):
        '''test getting an living'''

        self.assertIsNotNone(self.prompt.is_name_vacant('london', 'living'))        

    def test_create_room(self):
        '''test creating room'''

        self.assertIsNone(self.prompt.create_room('vegas', 'living'))

    def test_do_batch_allocate(self):
        '''test batch allocation'''

        self.assertIsNone(self.prompt.do_batch_allocate('C:/Users/Andela/test.txt'))

    def test_prepopulation(self):
        '''test pre population'''
        
        self.assertIsNone(self.prompt.do_pre_populate())

    def test_get_allocation(self):
        '''test to get allocation'''

        self.assertIsNone(self.prompt.do_get_allocation())

    def test_print_txt_allocation(self):
        '''test to print txt allocation'''

        self.assertIsNone(self.prompt.do_print_allocation())

    def test_print_csv_allocation(self):
        '''test to print csv allocation'''

        self.assertIsNone(self.prompt.do_print_allocation())

    def test_do_get_unallocated(self):
        '''test to get unallocated'''

        self.assertIsNone(self.prompt.do_get_unallocated())

    def test_do_get_room(self):
        '''test to get room'''

        self.assertIsNone(self.prompt.do_get_room())

    def test_add_room(self):
        '''test to add room'''

        self.assertIsNone(self.prompt.do_get_room())



    if __name__ == '__main__':
        unittest.main()
