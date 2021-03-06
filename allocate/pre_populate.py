import sqlite3 as lite
try:
    import cPickle as pickle
except:
    import pickle


# pickle an empty list that will act as occupants in rooms
occupants = []
occupants = pickle.dumps(occupants)

# tuple containing Office data to populate Office table
office_data = (
           (1, 'gold', occupants),
           (2, 'silver', occupants),
           (3, 'diamond', occupants),
           (4, 'ruby', occupants),
           (5, 'sapphire', occupants),
           (6, 'emerald', occupants),
           (7, 'opal', occupants),
           (8, 'topaz', occupants),
           (9, 'amethyst',occupants),
           (10, 'amber', occupants),
           )

# tuple containing Living data to populate Living table
living_data = (
           (1, 'london', occupants),
           (2, 'tokyo', occupants),
           (3, 'lagos', occupants),
           (4, 'chicago', occupants),
           (5, 'moscow', occupants),
           (6, 'shangai', occupants),
           (7, 'paris', occupants),
           (8, 'rome', occupants),
           (9, 'madrid', occupants),
           (10, 'berlin', occupants),
           )


def populate():
    '''
    creates a database, tables and pre-polulates the tables
    with data
    '''
    con = lite.connect('amity.db')

    with con:
        cur = con.cursor()
        # drop tables Office, Living, Staff and Fellow if it already exists
        cur.execute("DROP TABLE IF EXISTS Office")
        cur.execute("DROP TABLE IF EXISTS Living")
        cur.execute("DROP TABLE IF EXISTS Staff")
        cur.execute("DROP TABLE IF EXISTS Fellow")

        # create Office table
        cur.execute('''
                    CREATE TABLE 'Office' (
                        'Id'    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        'Room_name' TEXT NOT NULL DEFAULT 'NO NAME' UNIQUE,
                        'Space_count'   INTEGER NOT NULL DEFAULT 0,
                        'Occupants' BLOB
                    );
                    ''')
        print 'Office table created.'

        # create Living table
        cur.execute('''
                    CREATE TABLE 'Living' (
                        'Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        'Room_name' TEXT NOT NULL DEFAULT 'NO NAME' UNIQUE,
                        'Space_count'   INTEGER DEFAULT 0,
                        'Room_gender'   TEXT,
                        'Occupants' BLOB
                    );
                    ''')
        print 'Living table created'

        # create Staff table
        cur.execute('''
                    CREATE TABLE 'Staff' (
                      'Id'  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      'First_name'  TEXT,
                      'Last_name' TEXT,
                      'Office_room' TEXT
                    );
                    ''')
        print 'Staff table created'

        # create Fellow table
        cur.execute('''
                    CREATE TABLE 'Fellow' (
                      'Id'  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      'First_name'  TEXT,
                      'Last_name' TEXT,
                      'Office_room' TEXT,
                      'Living_required' TEXT,
                      'Living_room' TEXT,
                      'Gender'  INTEGER
                    );
                    ''')
        print 'Fellow table created'

        # insert 10 rows in Office table
        cur.executemany("INSERT INTO Office VALUES(?, ?, 0, ?)",
                        office_data)
        print 'Office table pre-populated with data'

        # insert 10 rows in Living table
        cur.executemany("INSERT INTO Living VALUES(?, ?, 0, NULL, ?)",
                        living_data)
        print 'Living table pre-populated with data'
        print '\n'

if __name__ == '__main__':
    populate()
