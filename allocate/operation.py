from cmd import Cmd
import os.path


class Operator(Cmd):

    def file_ext(self, source_file):
        '''determine type of file'''

        file_type = os.path.splitext(source_file)
        return file_type[1][1:]

    def get_person_status(self, index, fname, lname):
        '''
           called when an invalid syntax for employment status
            (e.g staff or fellow) is found when processing a file
           '''

        print '''
Error on line %d, for entry %s %s. Please type in "fellow"
or "staff" for the entry
''' % (index, fname, lname)

        status = ''

        # get an input of either staff or fellow from the user
        while status != 'staff' and status != 'fellow':
            status = raw_input('>>> ')

        return status.lower()

    def process_txt(self, source_file):
        '''allocate people to rooms from a txt file'''

        with open(source_file, 'r') as f:
            # get the lines in the file
            lines = f.readlines()

            for index, line in enumerate(lines):
                words = line.split()

                # check to make sure the third word is either staff of fellow
                if words[2].lower() != 'staff' and words[2].lower() != 'fellow':
                    words[2] = self.get_person_status(index + 1, words[0].lower(), words[1].lower())
                
                # create objects with regard to employment status
                if words[2].lower() == 'staff':
                    print 'Its a staff at %d' % (index + 1)
                else:
                    print 'Its a fellow at %d' % (index + 1)

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
                print "calling method to handle csv"
            else:
                print "Error: unsupported file format \n"
        else:
            print "Error: No such file '%s' exists \n" % (source)

    def do_quit(self, args):
        """Quits the program."""

        print "Quitting....."
        raise SystemExit

if __name__ == '__main__':
    prompt = Operator()
    prompt.prompt = '> '
    prompt.cmdloop('Starting program.....type \'help\' to get the list of available commands')
