import sqlite3 as lite
try:
    import cPickle as pickle
except:
    import pickle


def reset():
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

        # create Staff table
        cur.execute('''
                    CREATE TABLE 'Staff' (
                      'Id'  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      'First_name'  TEXT,
                      'Last_name' TEXT,
                      'Office_room' TEXT
                    );
                    ''')

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

    print "Database reset completed."
    print "Run pre_populate to create create initial data."

if __name__ == '__main__':
    reset()
