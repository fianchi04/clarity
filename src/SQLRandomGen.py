import random
import sqlite3



def bittoStr(v1):
    if v1 == False:
        return "N"
    else:
        return "Y"

def GenJobListing():
    lang = ("Java ", "C++ ", "Web ", "HTML ", "Python ")
    extra = ("and C# ", "", "application ", "", "UI ")
    buzz = ("Administrator ", "Engineer ", "Technician ", "Support")

    title = lang[random.randint(0, len(lang)-1)] + extra[random.randint(0, len(extra)-1)] + buzz[random.randint(0, len(buzz)-1)]

    lang = ("Light", "Green", "Blue", "Smart", "Safe", "Red")
    extra = ("house", "room", "tech", "space")
    buzz = (" Inc.", " Industries", " Web", "", "")

    employer = lang[random.randint(0, len(lang)-1)] + extra[random.randint(0, len(extra)-1)] + buzz[random.randint(0, len(buzz)-1)]

    sal = random.randint(5, 35)*1000

    hours = random.randint(3,8)*5

    date = str(random.randint(2017,2018)) + "-" + str(random.randint(3,12)) + "-" + str(random.randint(1,28))
    
    lang = ("Grad Scheme", "Apprenticeship", "Full-Time")

    jobtype = ""
    if sal < 10000:
        jobtype = "Internship"
    else:
        jobtype = lang[random.randint(0, len(lang)-1)]

    length = random.randint(1,8)*3

    lang = ("BSC Computer Science", "None Listed", "GCSE English")
    qual = lang[random.randint(0, len(lang)-1)]

    lang = ("Coding", "Web Development", "Software Design", "HTML Development", "Java Development", "None Listed", "None Listed")
    skills = lang[random.randint(0, len(lang)-1)]

    training = bool(random.getrandbits(1))
    training = bittoStr(training)
    expenses = bool(random.getrandbits(1))
    expenses = bittoStr(expenses)
    benefits = bool(random.getrandbits(1))
    benefits = bittoStr(benefits)

    holiday = random.randint(1,3)*7
    
    abroad = bool(random.getrandbits(1))
    abroad = bittoStr(abroad)

    dateposted = str(2017) + "-" + str(random.randint(1,3)) + "-" + str(random.randint(1,28))
    #add job posting to dbs
    #try:

    industry = "Computing"
    
    c.execute("INSERT INTO JOB_LISTING (ID, jobTitle, employer, salary, contractHours, \
startDate, jobType, contractLength, qualifications, skills, training, expenses, benefits, \
annualHolidayDays, opportunitiesAbroad, datePosted, industry) \
VALUES (NULL, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
    (title, employer, sal, hours, date, jobtype, \
    length, qual, skills, training, expenses, \
    benefits, holiday, abroad, dateposted,industry) )
   # except:

#open database (previous)
connect = sqlite3.connect('jobListings.db')
c = connect.cursor()
 
#create job listings database
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
    print("DATABASE JOB_LISTING ALREADY INITIALISED")
print("CONNECTED TO JOB_LISTING DATABASE")
 
 
 


consoleoutput = input("END TO END")
while consoleoutput != "END":
    GenJobListing()
    consoleoutput = input("END TO END")


'''end'''
connect.commit()
connect.close()
