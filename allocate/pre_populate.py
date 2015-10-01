import sqlite3 as lite


# tuple containing Office data to populate Office table
office_data = (
           (1, 'gold'),
           (2, 'silver'),
           (3, 'diamond'),
           (4, 'ruby'),
           (5, 'sapphire'),
           (6, 'emerald'),
           (7, 'opal'),
           (8, 'topaz'),
           (9, 'amethyst'),
           (10, 'amber'),
           )

# tuple containing Living data to populate Living table
living_data = (
           (1, 'london'),
           (2, 'tokyo'),
           (3, 'lagos'),
           (4, 'chicago'),
           (5, 'moscow'),
           (6, 'shangai'),
           (7, 'paris'),
           (8, 'rome'),
           (9, 'madrid'),
           (10, 'berlin'),
           )


def populate():
    '''
    creates a database, tables and pre-polulates the tables
    with data
    '''
    con = lite.connect('bin/amity.db')

    with con:
        cur = con.cursor()
        # drop tables Office and Living if it already exists
        cur.execute("DROP TABLE IF EXISTS Office")
        cur.execute("DROP TABLE IF EXISTS Living")

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
                      'First_name'  TEXT NOT NULL,
                      'Last_name' TEXT,
                      'Office_room' TEXT
                    );
                    ''')
        print 'Staff table created'

        # create Fellow table
        cur.execute('''
                    CREATE TABLE 'Fellow' (
                      'Id'  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      'First_name'  TEXT NOT NULL,
                      'Last_name' TEXT,
                      'Office_room' TEXT,
                      'Living_required' TEXT,
                      'Living_room' TEXT,
                      'Gender'  INTEGER
                    );
                    ''')
        print 'Fellow table created'

        # insert 10 rows in Office table
        cur.executemany("INSERT INTO Office VALUES(?, ?, 0, NULL)",
                        office_data)
        print 'Office table pre-populated with data'

        # insert 10 rows in Living table
        cur.executemany("INSERT INTO Living VALUES(?, ?, 0, NULL, NULL)",
                        living_data)
        print 'Living table pre-populated with data'

populate()
