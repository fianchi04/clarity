#search
import sqlite3
import re#use for string to digit splice


class search:
#individual search methods to compare criteria to that field of dbs
    def sTitle(title):
        print("SEARCH.PY search.sTitle REACHED")
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        title = '%' + title + '%' #add wildcard to search non exact fields
        #retrieve ID from main DBS
        c.execute("SELECT ID FROM JOB_LISTING WHERE jobTitle LIKE ?", (title,))        
        #store
        fetchJobTitle = c.fetchall()
        '''END CONNECTION'''
        connect.close()
        return fetchJobTitle

    def sEmployer(employer):
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sEmployer REACHED")
        employer = '%' + employer + '%'
        #retrieve ID and jobTitle from main DBS
        c.execute("SELECT ID FROM JOB_LISTING WHERE employer LIKE ?", (employer,))
        fetchEmployer = c.fetchall()
        #print("fetchEmployer = ", fetchEmployer)
        '''END CONNECTION'''
        connect.close()
        return fetchEmployer

    def sSalary(minsal):
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sSalary REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE salary>=?", (minsal,))
        fetchSalary = c.fetchall()
        '''END CONNECTION'''
        connect.close()
        return fetchSalary

    def sHPW(hpwMin, hpwMax):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.hpw REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE contractHours BETWEEN ? AND ?", (hpwMin, hpwMax,))
        fetchHPW = c.fetchall()
        '''END CONNECTION'''
        connect.close()
        return fetchHPW

    def sStartDate(startDate):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.startDate REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE startDate > ?", (startDate,))
        fetchStartDate = c.fetchall()
        print("start date results: ", fetchStartDate)

        '''END CONNECTION'''
        connect.close()
        return fetchStartDate


    #job type
    def sJobType(jobType):
        print("passedjobType is: ", jobType)
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sJobType REACHED")
        #retrieve ID and jobType from main DBS
        c.execute("SELECT ID FROM JOB_LISTING WHERE jobType = ?", (jobType,))
        fetchJobType = c.fetchall()
        
        '''END CONNECTION'''
        connect.close()
        return fetchJobType
        

                  
    def sContract(CLMin, CLMax):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sContract REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE contractLength BETWEEN ? AND ?", (CLMin, CLMax,))
        fetchContract = c.fetchall()
        '''END CONNECTION'''
        connect.close()

        return fetchContract

                  
    def sTraining(training):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sTraining REACHED")
        if training == 'on':
            training = 'Y'
        
        c.execute("SELECT ID FROM JOB_LISTING WHERE training = ?", (training,))
        fetchTraining = c.fetchall()
        '''END CONNECTION'''
        connect.close()

        return fetchTraining

        
    def sExpenses(expenses):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sExpenses REACHED")
        if expenses == 'on':
            expenses = 'Y'
        c.execute("SELECT ID FROM JOB_LISTING WHERE expenses = ?", (expenses,))
        fetchExpenses = c.fetchall()

        '''END CONNECTION'''
        connect.close()
        return fetchExpenses

    def sBenefits(benefits):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sBenefits REACHED")
        if benefits == 'on':
            benefits = 'Y'
        c.execute("SELECT ID FROM JOB_LISTING WHERE benefits = ?", (benefits,))
        fetchBenefits = c.fetchall()

        '''END CONNECTION'''
        connect.close()
        return fetchBenefits

        
    def sHoliday(holiday):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sHoliday REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE annualHolidayDays >= ?", (holiday,))
        fetchHoliday = c.fetchall()

        '''END CONNECTION'''
        connect.close()
        return fetchHoliday

        
    def sAbroad(abroad):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sAbroad REACHED")
        if abroad == 'on':
            abroad = 'Y'
        c.execute("SELECT ID FROM JOB_LISTING WHERE opportunitiesAbroad = ?", (abroad,))
        fetchAbroad = c.fetchall()

        '''END CONNECTION'''
        connect.close()
        return fetchAbroad

        
    def sDatePosted(datePosted):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db')
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sDatePosted REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE datePosted > date(?)", (datePosted,))
        fetchDatePosted = c.fetchall()
        '''END CONNECTION'''
        connect.close()
        return fetchDatePosted

    def sIndustry(industry):
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db')
        c = connect.cursor() #database cursor
        print("SEARCH.PY search.sIndustry REACHED")
        c.execute("SELECT ID FROM JOB_LISTING WHERE industry = ?", (industry,))
        fetchIndustry = c.fetchall()
        '''END CONNECTION'''
        connect.close()
        return fetchIndustry

    def compare(d, pTotal):
        connect = sqlite3.connect('jobListings.db') #connect to database
        c = connect.cursor() #database cursor

        #create temp database of all fields and priority
        c.execute('''DROP TABLE IF EXISTS TEMPMATCH''')
        c.execute('''CREATE TABLE IF NOT EXISTS TEMPMATCH(ID INTEGER,
jobTitle TEXT, employer TEXT, salary INT, contractHours INT, startDate DATE,
jobType TEXT, contractLength INT, qualifications TEXT, skillsUsed TEXT, training TEXT, expenses TEXT, 
benefits TEXT, annualHolidayDays INT, opportunitiesAbroad TEXT,
datePosted DATE, industry TEXT, priority INT);''')
        print("TEMP DBS initialised")

        #temp dbs of 100% matches
        c.execute('''DROP TABLE IF EXISTS TEMPMATCH100''')
        c.execute('''CREATE TABLE IF NOT EXISTS TEMPMATCH100(ID INTEGER,
jobTitle TEXT, employer TEXT, salary INT, contractHours INT, startDate DATE,
jobType TEXT, contractLength INT, qualifications TEXT, skillsUsed TEXT, training TEXT, expenses TEXT, 
benefits TEXT, annualHolidayDays INT, opportunitiesAbroad TEXT,
datePosted DATE, industry TEXT, priority INT);''')
        print("TEMPMATCH100 DBS initialised")
        
        #go through dictionary and add rows to database with priority
        for a in d.keys():
            tempP = d[a]
            #remove any non digit characters
            a = str(a)
            a = int(''.join(x for x in a if x.isdigit()))
            
            c.execute('''SELECT * FROM JOB_LISTING WHERE ID = ?''', [str(a)])
            Trow = c.fetchall()


            
            #assign tuples to actual vars
            #0 ID
            tid = Trow[0][0]
            #1 job title
            tjob = Trow[0][1]
            #2 employer
            templ = Trow[0][2]
            #3 salary
            tsal = Trow[0][3]
            #4 hours pw
            thour= Trow[0][4]
            #5 start date
            tstar = Trow[0][5]
            #6 job type
            ttyp = Trow[0][6]
            #7 length of contract
            tleng= Trow[0][7]
            #8 qualifications
            tqual= Trow[0][8]
            #9 skills
            tskil = Trow[0][9]
            #10 training
            ttra= Trow[0][10]
            #11 expenses
            texp= Trow[0][11]
            #12 benefits
            tben= Trow[0][12]
            #13 annual holiday
            tann= Trow[0][13]
            #14 opportunnities abroad
            tabr= Trow[0][14]
            #15 date posted
            tpos = Trow[0][15]
            #16 industry
            tind= Trow[0][16]


            #TWO LISTS TO ADD TO: 100% MATCHES AND EVERYTHING ELSE
            if tempP == pTotal:
                c.execute('''INSERT INTO TEMPMATCH100 (ID, jobTitle, employer, salary, contractHours, startDate, jobType, contractLength, qualifications, skillsUsed, training, expenses, \
        benefits, annualHolidayDays, opportunitiesAbroad, datePosted, industry, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',\
                          (tid, tjob, templ, tsal, thour, tstar, ttyp, tleng, tqual, tskil, ttra, texp, tben, tann, tabr, tpos, tind, tempP))    
            else:
                c.execute('''INSERT INTO TEMPMATCH (ID, jobTitle, employer, salary, contractHours, startDate, jobType,  contractLength, qualifications, contractLength, training, expenses, \
        benefits, annualHolidayDays, opportunitiesAbroad, datePosted, industry, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',\
                          (tid, tjob, templ, tsal, thour, tstar, ttyp, tleng, tqual, tskil, ttra, texp, tben, tann, tabr, tpos, tind, tempP))


        #order by priority
        c.execute("SELECT * FROM TEMPMATCH ORDER BY priority DESC")
        tData = c.fetchall()
        #get 100% matches
        c.execute("SELECT * FROM TEMPMATCH100")
        tData100 = c.fetchall()
            


        '''END CONNECTION'''
        connect.close()
        #return list
        return tData, tData100
                      

    



    def searchDBS(title, employer, minsal, hpwMin, hpwMax, startDate, jobType, CLMin, CLMax, training, expenses, benefits, holiday, abroad, datePosted,industry,
                s1, s2, s3, s4, s5, s6, s7, s10, s11, s12, s13, s14, s15, s16):
        print("SEARCH.PY search.searchDBS REACHED")
		#method passed user input and priority number from sliders

        
        '''START CONNECTION'''
        connect = sqlite3.connect('jobListings.db')
        c = connect.cursor() #database cursor
        

        titleP= int(s1)
        employerP = int(s2)
        salaryP = int(s3)
        hpwP = int(s4)
        startDateP = int(s5)
        jobTypeP = int(s6)
        contractP = int(s7)
        #qualifications s8
        #skills s9
        trainingP = int(s10)
        expensesP = int(s11)
        benefitsP = int(s12)
        holidayP = int(s13)
        


        
        abroadP = int(s14)
        datePostedP = int(s15)
        industryP = int(s16)
        
        #total priority to calculate which are 100% matches
        pTotal = 0
        
        #dictionary to store priority
        dIDs = {}
        #add all IDs
        c.execute("SELECT ID FROM JOB_LISTING")
        holdAll = c.fetchall()
        for row in holdAll:
            #print("SAVE ID TO dIDs: ", row)
            dIDs[row] = 0


        
        if title!="":
            pTotal = pTotal + titleP
            #fetchJobTitle = search.sTitle(title)
            #dJobs[titlePriority] = fetchJobTitle
            titleResults = search.sTitle(title)
            #print(titleResults)
            for a in titleResults:
                dIDs[a] = dIDs[a] + titleP


               
        if employer!="":
            pTotal = pTotal + employerP
            employerResults = search.sEmployer(employer)
            for a in employerResults:
                dIDs[a] = dIDs[a] + employerP

        if minsal!=None:
            if minsal!="":
                pTotal = pTotal + salaryP
                salResults = search.sSalary(minsal)
                for a in salResults:
                    dIDs[a] = dIDs[a] + salaryP



        if hpwMin!=None:
            if hpwMax!=None:
                if hpwMin != "":
                    pTotal = pTotal + hpwP
                    hpwResults = search.sHPW(hpwMin, hpwMax)
                    for a in hpwResults:
                        dIDs[a] = dIDs[a] + hpwP
                        

        #startDate
        if startDate!="":
            if startDate!=None:
                pTotal = pTotal + startDateP
                startDateResults = search.sStartDate(startDate)
                for a in startDateResults:
                    dIDs[a] = dIDs[a] + startDateP


        #jobType
        if jobType!=None:
            if jobType!="None":
                pTotal = pTotal + jobTypeP
                jTypeResults = search.sJobType(jobType)
                for a in jTypeResults:
                    dIDs[a] = dIDs[a] + jobTypeP
        
        if CLMin!=None:
            if CLMax!=None:
                if CLMin != "":
                    pTotal = pTotal + contractP
                    CLResults = search.sContract(CLMin, CLMax)
                    for a in CLResults:
                        dIDs[a] = dIDs[a] + contractP

        #qualifications

        #skills
                
        if training!=None:
            pTotal = pTotal + trainingP
            trainingResults = search.sTraining(training)
            for a in trainingResults:
                dIDs[a] = dIDs[a] + trainingP

                
        if expenses!=None:
            pTotal = pTotal + expensesP
            expensesResults = search.sExpenses(expenses)
            for a in expensesResults:
                dIDs[a] = dIDs[a] + expensesP
            
        if benefits!=None:
            pTotal = pTotal + benefitsP
            benefitsResults = search.sBenefits(benefits)
            for a in benefitsResults:
                dIDs[a] = dIDs[a] + benefitsP
                
        if holiday!=None:
            if holiday!= "":
                pTotal = pTotal + holidayP
                holidayResults = search.sHoliday(holiday)
                for a in holidayResults:
                    dIDs[a] = dIDs[a] + holidayP
            
        if abroad!=None:
            pTotal = pTotal + abroadP
            abroadResults = search.sAbroad(abroad)
            for a in abroadResults:
                dIDs[a] = dIDs[a] + abroadP
                
        #datePosted
        if datePosted!=None:
            if datePosted!= "":
                print("datePosted = ", datePosted)
                pTotal = pTotal + datePostedP
                datePostedResults = search.sDatePosted(datePosted)
                print("dateposted results: ", datePosted)
                for a in datePostedResults:
                    dIDs[a] = dIDs[a] + datePostedP

        #industry
        if industry!=None:
            if industry!="None":
                pTotal = pTotal + industryP
                industryResults = search.sIndustry(industry)
                for a in industryResults:
                    dIDs[a] = dIDs[a] + industryP

                
        #print("dIDs is: ", str(dIDs))
                  
        
        tData, tData100 = search.compare(dIDs, pTotal)

        '''END CONNECTION'''
        connect.close()
        return tData, tData100, pTotal	
            




