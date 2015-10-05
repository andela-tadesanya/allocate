from cmd import Cmd
import os.path
from person import Fellow, Staff
from pre_populate import populate
import csv


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

    def do_quit(self, args):
        """Quits the program."""

        print "Quitting....."
        raise SystemExit

if __name__ == '__main__':
    prompt = Operator()
    prompt.prompt = '>>> '
    prompt.cmdloop('Starting program.....type \'help\' to get the list of available commands')
