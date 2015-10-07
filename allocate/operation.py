from cmd import Cmd
import os.path
from person import Fellow, Staff
from room import Living, Office
from pre_populate import populate
import csv
import sqlite3 as lite
try:
    import cPickle as pickle
except:
    import pickle
from os.path import expanduser
from reset import reset

class Operator(Cmd):

    def file_ext(self, source_file):
        '''determine type of file'''

        file_type = os.path.splitext(source_file)
        return file_type[1][1:]

    def get_person_status(self, index, fname, lname):
        '''called when an invalid syntax for employment status
(e.g staff or fellow) is found when processing a file'''

        print '''Error on line %d, for entry %s %s. Please type in "fellow"
or "staff" for the entry''' % (index, fname, lname)

        status = ''

        # get an input of either staff or fellow from the user
        while status != 'staff' and status != 'fellow':
            status = raw_input('> ')

        return status.lower()

    def process_txt(self, source_file):
        '''allocate people to rooms from a txt file'''

        with open(source_file, 'r') as f:
            # get the lines in the file
            lines = f.readlines()

            # loop over lines with enumerate to keep track of each iteration
            for index, line in enumerate(lines):
                words = line.split()

                # check to make sure the third word is either staff of fellow
                if words[2].lower() != 'staff' and words[2].lower() != 'fellow':
                    # make user input the correct value
                    correct_value = self.get_person_status(index + 1, words[0].lower(), words[1].lower())
                    # insert correct value into the list of words
                    words.insert(2, correct_value)

                # create objects with regard to employment status
                if words[2].lower() == 'staff':
                    # create an object of Staff
                    obj = Staff(words[0].lower(), words[1].lower())

                    # assign to an office
                    obj.assign_office('Staff')
                else:
                    # check if sex of fellow is given
                    if len(words) > 4:
                        # create an object of Fellow setting gender
                        obj = Fellow(words[0].lower(), words[1].lower(), words[3].lower(), words[4].lower())

                        # assign to an office
                        obj.assign_office('Fellow')

                        # assign to a living room if required
                        if obj.living_required == 'y':
                            obj.assign_living()
                    else:
                        # create an object of Fellow without setting gender
                        obj = Fellow(words[0].lower(), words[1].lower(), words[3].lower())

                        # assign to an office
                        obj.assign_office('Fellow')

                        # assign to a living room if required
                        if obj.living_required == 'y':
                            obj.assign_living()

        print "Finished processing..."

    def process_csv(self, source_file):
        '''allocate people to rooms from a txt file'''

        with open(source_file, 'r') as f:
            reader = csv.reader(f)

            # loop over rows with enumerate to keep track of each iteration
            for index, row in enumerate(reader):
                # check that third element in row is either staff of fellow
                if row[2].lower() != 'staff' and row[2].lower() != 'fellow':
                    # make user input the correct value
                    correct_value = self.get_person_status(index + 1, row[0].lower(), row[1].lower())
                    # insert correct value into the row list
                    row.insert(2, correct_value)

                # create objects with regard to employment status
                if row[2].lower() == 'staff':
                    # create an object of Staff
                    obj = Staff(row[0].lower(), row[1].lower())

                    # assign to an office
                    obj.assign_office('Staff')
                else:
                    # check if sex of fellow is given
                    if len(row) > 4 and len(row[4]) > 0:
                        # create an object of Fellow setting gender
                        obj = Fellow(row[0].lower(), row[1].lower(), row[3].lower(), row[4].lower())

                        # assign to an office
                        obj.assign_office('Fellow')

                        # assign to a living room if required
                        if obj.living_required == 'y':
                            obj.assign_living()
                    else:
                        # create an object of Fellow without setting gender
                        obj = Fellow(row[0].lower(), row[1].lower(), row[3].lower())

                        # assign to an office
                        obj.assign_office('Fellow')

                        # assign to a living room if required
                        if obj.living_required == 'y':
                            obj.assign_living()

        print "Finished processing..."

    def get_office_room(self, room):
        '''gets list of an office occupants from database'''

        con = lite.connect('bin/amity.db')
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

    def get_living_room(self, room):
        '''gets list of a living room occupants from database'''

        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            sql = "SELECT Occupants from Living where Room_name = '%s'" % room
            cur.execute(sql)
            result = cur.fetchone()

            if result is not None:
                # unpickle the data
                unpickled_result = pickle.loads(str(result['Occupants']))
            else:
                # return empty list
                unpickled_result = []
        return unpickled_result

    def is_name_vacant(self, room_name, room_type):
        '''check if the room name is already used'''

        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            sql = "SELECT * FROM %s WHERE Room_name = '%s'" % (room_type.capitalize(), room_name)
            cur.execute(sql)
            result = cur.fetchone()

            if result is not None:
                return False
            else:
                return True

    def create_room(self, room_name, room_type):
        '''creates a room'''

        occupants = pickle.dumps([])
        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            sql = "INSERT INTO '%s'('Room_name', 'Space_count', 'Occupants') VALUES('%s', 0, '%s')" % (room_type.capitalize(), room_name, occupants)
            cur.execute(sql)
        print "Room '%s' created." % (room_name)

    def do_batch_allocate(self, source):
        '''Allocate people to rooms via data from a file'''

        # format the filepath
        source = source.replace('\\', '/')

        # check if file exists
        if os.path.exists(source):
            file_type = self.file_ext(source)

            # call appropriate method for each type of file
            if file_type == 'txt':
                self.process_txt(source)
            elif file_type == 'csv':
                self.process_csv(source)
            else:
                print "Error: unsupported file format \n"
        else:
            print "Error: No such file '%s' exists \n" % (source)

    def do_pre_populate(self, *args):
        '''creates a database, tables and pre-polulates the tables
with data'''

        populate()

    def do_get_allocation(self, *args):
        '''displays room allocations'''

        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()

            # fetch and instantiate objects of Office from database
            cur.execute("SELECT * FROM Office")
            office_rows = cur.fetchall()
            for row in office_rows:
                # create an Office object call get_occupants method on each
                office = Office(row['Room_name'])
                office.space_count = row['Space_count']
                office.occupants = pickle.loads(str(row['Occupants']))
                office.get_occupants()

            # fetch and instantiate objects of Living from database
            cur.execute("SELECT * FROM Living")
            living_rows = cur.fetchall()
            for row in living_rows:
                # create an Living object call get_occupants method on each
                living = Living(row['Room_name'])
                living.space_count = row['Space_count']
                living.occupants = pickle.loads(str(row['Occupants']))
                living.get_occupants()

    def do_print_allocation(self, *args):
        '''prints room allocations into a txt or csv file'''
        # set home directory 
        home = expanduser('~')

        # set output file type
        file_type = ''
        filepath = ''
        while True:
            file_type = raw_input('> Please input \'txt\' or \'csv\' for output file format: ')
            if file_type == 'txt' or file_type == 'csv':
                break
            else:
                print "Invalid format."

        # fetch living and office room allocations
        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()

            # fetch office occupants
            cur.execute('SELECT Room_name, Space_count, Occupants FROM Office')
            office_rows = cur.fetchall()

            # fetch living occupants
            cur.execute("SELECT Room_name, Space_count, Occupants FROM Living")
            living_rows = cur.fetchall()

            if file_type == 'txt':
                # create file path
                filepath = os.path.join(home, 'allocation.txt')

                # open file to write to
                with open(filepath, 'w') as f:
                    for row in office_rows:
                        f.write('%s (OFFICE)\n' % (row['Room_name']))
                        if row['Space_count'] == 0:
                            f.write('Empty')
                        else:
                            room_occupants = pickle.loads(str(row['Occupants']))
                            line = ", ".join(room_occupants)
                            f.write(line + '\n\n')

                    for row in living_rows:
                        f.write('%s (LIVING)\n' % (row['Room_name']))
                        if row['Space_count'] == 0:
                            f.write('Empty')
                        else:
                            room_occupants = pickle.loads(str(row['Occupants']))
                            line = ", ".join(room_occupants)
                            f.write(line + '\n\n')
            else:
                # create file path
                filepath = os.path.join(home, 'allocation.csv')

                # open file to write to
                with open(filepath, 'w') as f:
                    writer = csv.writer(f)
                    for row in office_rows:
                        writer.writerow((row['Room_name'], 'OFFICE'))
                        if row['Space_count'] == 0:
                            writer.writerow(('Empty'))
                        else:
                            room_occupants = pickle.loads(str(row['Occupants']))
                            writer.writerow(room_occupants)

                    for row in living_rows:
                        writer.writerow((row['Room_name'], 'LIVING'))
                        if row['Space_count'] == 0:
                            writer.writerow(('Empty'))
                        else:
                            room_occupants = pickle.loads(str(row['Occupants']))
                            writer.writerow(room_occupants)

        print "Allocations outputted to %s" % filepath

    def do_get_unallocated(self, *args):
        '''display unallocated people'''

        con = lite.connect('bin/amity.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()

            # fetch unallocated staff
            cur.execute('SELECT * from staff where Office_room is null')
            unallocated_staff = cur.fetchall()

            # fetch unallocated fellows
            cur.execute("SELECT * from fellow where (Office_room is null) or (Living_room is null and Living_required = 'y')")
            unallocated_fellows = cur.fetchall()

            # display unallocated staff
            print "List of Unallocated people:\n"
            print "{0:25} {1:10} {2:15} {3:15}".format('Name of Person', 'Position', 'Office Room', 'Living Room')
            print "{0:25} {1:10} {2:15} {3:15}".format('-'*25, '-'*10, '-'*15, '-'*15)

            for staff in unallocated_staff:
                fullname = '%s %s' % (staff['First_name'], staff['Last_name'])
                print "{0:25} {1:10} {2:15}".format(fullname, 'staff', staff['Office_room'])

            for fellow in unallocated_fellows:
                fullname = '%s %s' % (fellow['First_name'], fellow['Last_name'])

                # format the Office_room variable
                if fellow['Office_room'] is not None:
                    office = ''
                else:
                    office = None

                # format the Living_room variable
                if fellow['Living_room'] is not None:
                    living = ''
                else:
                    living = None

                print "{0:25} {1:10} {2:15} {3:15}".format(fullname, 'fellow', office, living)

    def do_get_room(self, *args):
        '''displays occupants of a given room'''

        room = raw_input('> Input the name of the room: ')

        # check if the room is an office
        occu_list_office = self.get_office_room(room)

        # check if room is a living
        occu_list_living = self.get_living_room(room)

        if occu_list_office:
            print "Occupants in %s are: \n" % (room)
            print "\n".join(occu_list_office)
        elif occu_list_living:
            print "Occupants in %s are: \n" % (room)
            print "\n".join(occu_list_living)
        else:
            print "No result found."

    def do_add_room(self, *args):
        '''create an additional room'''

        room_name = raw_input('> Give the new room a name: ')
        room_type = raw_input("> What type of room is it 'office' or 'living': ").lower()

        while True:
            if room_type == 'office' or room_type == 'living':
                break
            else:
                print "Invalid entry."
                room_type = raw_input("> What type of room is it 'office' or 'living': ")

        # check if name is vacant
        if self.is_name_vacant(room_name, room_type):
            # create room
            self.create_room(room_name, room_type)
        else:
            print "Room with the name '%s' is already in use" % room_name

    def do_reset(self, *args):
        ''' reset database, truncate all tables'''
        reset()


    def do_quit(self, args):
        '''Quits the program.'''

        print "Quitting....."
        raise SystemExit

if __name__ == '__main__':
    prompt = Operator()
    prompt.prompt = '>>> '
    prompt.cmdloop('Starting program.....type \'help\' to get the list of available commands')
