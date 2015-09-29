class Person(object):
    """base class for a person at amity that requires rooms"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.office_room = None


class Fellow(Person):
    """class for a fellow person at amity that requires a office room
     and may or may not require a living room"""

    def __init__(self, first_name, last_name, living_required, gender=None):
        super(Fellow, self).__init__(first_name, last_name, gender)
        self.living_required = living_required  # boolean if fellow requires living
        self.living_room = None  # name of living room fellow is allocated
        self.gender = gender


class Staff(Person):
    """class for a staff person at amity that only requires
     office room allocation"""
