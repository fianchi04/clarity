#database setup

import sqlite3

class setUp:
    '''setup'''
    #open database as c
    connect = sqlite3.connect('jobListings.db')
    c = connect.cursor()

    #create job listing dbs
    try:
         c.execute('''CREATE TABLE IF NOT EXISTS JOB_LISTING(ID INTEGER PRIMARY KEY,
              jobTitle TEXT,
              employer TEXT,
              salary INT,
              contractHours INT,
              startDate DATE,
              jobType TEXT,
              contractLength INT,
              qualifications TEXT,
              skills TEXT,
              training TEXT,
              expenses TEXT,
              benefits TEXT,
              annualHolidayDays INT,
              opportunitiesAbroad TEXT,
              datePosted Date,
              industry TEXT);''')
    except:
        c.execute('''DELETE FROM JOB_LISTING''')
        connect.commit()
        print("SETUP.PY: DATABASE JOB_LISTING ALREADY INITIALISED")
    print("SETUP.PY: CONNECTED TO JOB_LISTING DATABASE")



    '''end'''
    connect.commit()
    connect.close()
