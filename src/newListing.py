import sqlite3


#this was the original 'add a new listing' function to the database, from prototype 1 and 2. Is no longer compatible with system. 
class newListingM:
    
    def addPost():
        connect = sqlite3.connect('jobListings.db')
        c = connect.cursor()

        
        xjobTitle = input("enter job title:")
        xemployer = input("enter employer name:")
        xsalary = input("enter annual salary (£):")
        xcontractHours = input("enter contract hours per week: ):")
        xstartDateYY = input("enter start date YY:")
        xstartDateMM = input("enter start date MM:")
        xstartDateDD = input("enter start date DD:")
        xjobType = input("enter job type (internship, grad scheme etc):")
        xcontractLength = input("enter length of contract (in months):")
        xqualifications = input("list qualifications required:")
        xskills = input("list key skills utilised:")
        xtraining = input("Is any training offered? Y/N:")
        xexpenses = input("Will expenses be covered? Y/N (e.g. travel):")
        xbenefits = input("are there any job benefits? Y/N (e.g. job car):")
        xannualHoliday = input("enter number of days annual holiday:")
        xopportunitiesAbroad = input("are there any opportunities abroad? Y/N:")
        xdatePostedYY = input("enter date posted YY: ")
        xdatePostedMM = input("enter date posted MM: ")
        xdatePostedDD = input("enter date posted DD: ")

        #add to dbs
        c.execute("INSERT INTO JOB_LISTING (ID, jobTitle, employer, salary, contractHours, \
        startDateYY, startDateMM, startDateDD, jobType, contractLength, qualifications, skills, training, expenses, benefits, \
        annualHolidayDays, opportunitiesAbroad, datePostedYY, datePostedMM, datePostedDD) \
        VALUES (NULL, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
        (xjobTitle, xemployer, xsalary, xcontractHours, xstartDateYY, xstartDateMM, xstartDateDD, xjobType, \
        xcontractLength, xqualifications, xskills, xtraining, xexpenses, \
        xbenefits, xannualHoliday, xopportunitiesAbroad, xdatePostedYY, xdatePostedMM, xdatePostedDD) )

        connect.commit()
        print("newlisting.py: JOB LISTING SUCCESSFUL")

        connect.close()
        return
    
