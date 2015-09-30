import sqlite3 as lite


# tuple containing Office data to populate Office table
office_data = (
           (1, 'gold', 6,),
           (2, 'silver', 6,),
           (3, 'diamond', 6,),
           (4, 'ruby', 6,),
           (5, 'sapphire', 6,),
           (6, 'emerald', 6,),
           (7, 'opal', 6,),
           (8, 'topaz', 6,),
           (9, 'amethyst', 6,),
           (10, 'amber', 6,),
           )

# tuple containing Living data to populate Living table
living_data = (
           (1, 'london', 4,),
           (2, 'tokyo', 4,),
           (3, 'lagos', 4,),
           (4, 'chicago', 4,),
           (5, 'moscow', 4,),
           (6, 'shangai', 4,),
           (7, 'paris', 4,),
           (8, 'rome', 4,),
           (9, 'madrid', 4,),
           (10, 'berlin', 4,),
           )


def populate():
    '''
    creates a database, tables and pre-polulates the tables
    with data
    '''
    con = lite.connect('../bin/data.db')

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
                        'Space_limit'   INTEGER NOT NULL DEFAULT 6,
                        'Occupants' BLOB
                    );
                    ''')
        print 'Office table created.'

        # create Living table
        cur.execute('''
                    CREATE TABLE 'Living' (
                        'Id'    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        'Room_name' TEXT NOT NULL DEFAULT 'NO NAME' UNIQUE,
                        'Space_limit'   INTEGER DEFAULT 4,
                        'Room_gender'   TEXT,
                        'Occupants' BLOB
                    );
                    ''')
        print 'Living table created'

        # insert 10 rows in Office table
        cur.executemany("INSERT INTO Office VALUES(?, ?, ?, NULL)",
                        office_data)
        print 'Office table pre-populated with data'

        # insert 10 rows in Living table
        cur.executemany("INSERT INTO Living VALUES(?, ?, ?, NULL, NULL)",
                        living_data)
        print 'Living table pre-populated with data'

populate()
