#main

import setup
import search
import newListing
import cherrypy
import os, os.path

#run database setup
init = setup.setUp()


#html for entry page
class startScreen(object):
    @cherrypy.expose
    def index(self):
        return """
    <html>
    <head>
    <link href="/static/css/style.css" rel="stylesheet">
    </head>
    <body>

    
    <div ID="banner">
    
    <div ID="Logo">
    <a href="/"><img src="/static/images/logo.jpeg" alt="logo"></a>
    <div ID="Slogan" >a priority ranked job search engine</div>
    </div>

    <div ID="Button">
    <h4>LOG IN</h4>
    </div>
    
    </div>

    <div ID="MainBody">
    <form method="post" action="search">

	<table style="text-align:left">
	<tr>
	<th></th>
        <th><p style="display:inline-table;width:33%">Low Priority</p>
		        <div class="box" style="display:inline-table;width:33%">
			<a class="popButton" href="#popup1">What is this?</a>
			</div>
		<p style="display:inline-table;text-align:right;width:32%">High Priority</p>

        


<div id="popup1" class="overlay">
	<div class="popup">
		<h2>Priority Sliders   </h2>
		<a class="close" href="#">×</a>
		<div class="content">
			Use the sliders to set what priority each search field is, after you click Submit, any results that don't match your input 100% will be ranked by what should be most important to you.
		</div>
	</div>
</div>
	</th></tr>



	<tr>
	<th>Job Title:</th>
	</tr>
	<tr ID="InputRow">
        <th><input type="text" name="title"></th>
		<th><input type="range" name="slider1" min="0", max="15"></th>
	</tr>	
	<tr>
        <th>Industry:</th>
    </tr>
	<tr ID="InputRow">	
		<th><select name="industry">
            <option value="None">      </option>
            <option value="Computing">Computing</option>
        </select></th>
		<th><input type="range" name="slider16" min="0", max="15"></th>
	</tr>
	<tr>
        <th>Employer name:</th>
    </tr>   
	<tr ID="InputRow">
		<th><input type="text" name="employer"></th>
		<th><input type="range" name="slider2" min="0", max="15"></th>
	</tr>	
	<tr>
        <th>Minimum Starting Salary:</th>
    </tr>
	<tr ID="InputRow">
		<th><input type="number" name="minsal"></th>
		<th><input type="range" name="slider3" min="0", max="15"></th>
	</tr>	
	<tr>
        <th>Contract Hours Per Week:</th>
    </tr>
	<tr ID="InputRow">
		<th><input type="number" name="hpwMin" placeholder="From">
        <input type="number" name="hpwMax" placeholder="Till"></th>
		<th><input type="range" name="slider4" min="0", max="15" ></th>
	</tr>	
	<tr>
        <th>Start Date:</th>
    </tr>    
	<tr ID="InputRow">	
		<th><input type="date" name="startDate"></th>
		<th><input type="range" name="slider5" min="0", max="15"></th>
	</tr>	
	<tr>
        <th>Job Type:</th>
    </tr>
	<tr ID="InputRow">	
		<th><select name="jobType">
            <option value="None">      </option>
            <option value="Internship">Internship</option>
            <option value="Apprenticeship">Apprenticeship</option>
            <option value="Grad Scheme">Graduate Scheme</option>
            <option value="Full-Time">Full-Time Employment</option>
            <option value="Part-Time">Part-Time Employment</option>
        </select></th>
		<th><input type="range" name="slider6" min="0", max="15"></th>
	</tr>
	<tr>
        <th>Contract Length (months):</th>
    </tr>    
	<tr ID="InputRow">
		<th><input type="number" name="CLMin" placeholder="Minimum">
        <input type="number" name="CLMax" placeholder="Maximum"></th>
		<th><input type="range" name="slider7" min="0", max="15" ></th>
	</tr>
    <tr>
		<th>Training Offered:</th>
    </tr>   
	<tr ID="InputRow">
		<th><input type="checkbox" name="training"></th>
		<th><input type="range" name="slider10" min="0", max="15"></th>
	</tr>	
    <tr>
		<th>Expenses covered:</th>
    </tr>
	<tr ID="InputRow">
		<th><input type="checkbox" name="expenses"></th>
		<th><input type="range" name="slider11" min="0", max="15"></th>
	</tr>
	<tr>
        <th>Job benefits:</th>
    </tr>    
	<tr ID="InputRow">
		<th><input type="checkbox" name="benefits"></th>
		<th><input type="range" name="slider12" min="0", max="15"></th>
	</tr>	
    <tr>
		<th>Number of days annual holiday: </th>
    </tr>    
	<tr ID="InputRow">
		<th><input type="number" name="holiday"></th>
		<th><input type="range" name="slider13" min="0", max="15"></th>
	</tr>	
    <tr>
		<th>Opportunities abroad:</th>
    </tr>    
	<tr ID="InputRow">
		<th><input type="checkbox" name="abroad"></th>
		<th><input type="range" name="slider14" min="0", max="15"></th>
	</tr>	
		
	<tr>
        <th>Date posted: </th>
	</tr>
    <tr ID="InputRow">
		<th><input type="date" name="datePosted"></th>
		<th><input type="range" name="slider15" min="0", max="15"></th>
    </tr>    

	</table>

        <div ID="Submit"> 
    	<button type="submit">Submit</button>
        </div>
        </form>

        </div>
        </body>
        </html>
        
        """
    @cherrypy.expose #needed for every page
    def search(self, **params):
        fields= ['title','employer','minsal', 'hpwMin', 'hpwMax', 'startDate', 'jobType', 'CLMin',
                 'CLMax', 'training','expenses', 'benefits', 'holiday', 'abroad', 'datePosted', 'industry',
                  'slider1', 'slider2', 'slider3', 'slider4', 'slider5', 'slider6', 'slider7',
                 'slider10', 'slider11', 'slider12','slider13', 'slider14','slider15', 'slider16']
        tData, tData100, pTotal = search.search.searchDBS(*[params.get(f, None) for f in fields])
        #params- set default data to none if nothing entered on webform
        tempString = """<html>
                    <head>
                    <link href="/static/css/style.css" rel="stylesheet">
                    </head>
                    <body>
                    <div ID="banner">
                     <div ID="Logo">
                    <a href="/"><img src="/static/images/logo.jpeg" alt="logo"></a>
                        <div ID="Slogan" >a priority ranked job search engine</div>
                    </div>
                    <div ID="Button">
                    <h4>LOG IN</h4>
                    </div>
                    </div>
                    <div ID="MainBody">
                        <h1> Search Results </h1><br>
                    <h3> 100% Matches </h3><br>
                    """
        #array to hold fields that i want to display as click link
        resultsSelect = (1,2,3,5)
        popUpSelect = (3,4,5,6,7,8,9,10,11,12,13,14,15,16)
        popUpLoc = (0,0,0,2,4,5,6,8,0,0,9,10,11,12,13,14,15,16,17)
        popUpText = ("","","","Starting Salary: ", "Hours Per Week: ", "Starting Date: ", "Job Type: ", "Contract Length (Months):" , "Qualifications Required: ", "Skills: ", "Training?: ", "Expenses?:", "Benefits?: ",
                     "Annual Holidays (Days): ", "Oppertunities Abroad: ", "Date Posted: ", "Industry: ")
        rowCounter = 0
        #for row in search results
        for row in tData100:
            counter = 0
            firstString = """<a href="#popup""" + str(rowCounter) + """"><div ID="ResultsBox"><div ID="ResultTextMain">"""
            secondString = """<div id="popup""" + str(rowCounter) + """" class="overlay">
	<div class="popup">
		<h2>"""
            secondString = secondString + str(row[1]) + " for " + str(row[2]) + """</h2>
		<a class="close" href="#/">×</a>
		<div class="content">"""
            secondString = secondString + """<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ "<b>Job Information</b>" + ""+ """</div><div ID="ResultText">"""+  "Your Search" + "</div></div>"
            rowCounter += 1
            #add only the numbers from the array
            for x in row:
                #
                if counter in popUpSelect:
                    if(counter==3):
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>£"+ str(x) + """</b></div><div ID="ResultText">£"""+  str(params.get(fields[popUpLoc[counter]], "")) + "</div></div>"
                    elif(counter == 8 or counter == 9):
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>"+ str(x) + """</b></div><div ID="ResultText">""""</div></div>"
                    else:
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>"+ str(x) + """</b></div><div ID="ResultText">"""+  str(params.get(fields[popUpLoc[counter]], "")) + "</div></div>"
                if counter in resultsSelect:
                    if(counter ==2):
                        firstString = firstString + "for "
                    if(counter == 3):
                        firstString = firstString + """</div><div ID="ResultText">    Annual Salary: <b>£</b>"""
                    if(counter == 5):
                        firstString = firstString + """</div><div ID="ResultText">  Starting on: """

                    firstString= firstString + "<b>" + str(x) + "</b> "
                    if(counter == 5):
                        firstString= firstString + "</div>"
                if counter == 17:
                    if(pTotal > 0):
                        firstString = firstString + """<div ID="ResultP"> """ + str(int((100/pTotal) * x)) + "%</div> "
                counter+=1
            tempString = tempString + firstString + "</div></a>" + secondString + """</div></div></div>"""

        tempString = tempString +  "<h3>Lesser Matches</h3><br>"
        for row in tData:
            counter = 0
            firstString = """<a href="#popup""" + str(rowCounter) + """"><div ID="ResultsBox"><div ID="ResultTextMain">"""
            secondString = """<div id="popup""" + str(rowCounter) + """" class="overlay">
	<div class="popup">
		<h2>"""
            secondString = secondString + str(row[1]) + " for " + str(row[2]) + """</h2>
		<a class="close" href="#/">×</a>
		<div class="content">"""
            secondString = secondString + """<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ "<b>Job Information</b>" + """</b></div><div ID="ResultText">"""+  "Your Search" + "</div></div>"
            rowCounter += 1
            #add only the numbers from the array
            for x in row:
                #
                if counter in popUpSelect:
                    if(counter==3):
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>£"+ str(x) + """</b></div><div ID="ResultText">£"""+  str(params.get(fields[popUpLoc[counter]], "")) + "</div></div>"
                    elif(counter == 8 or counter == 9):
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>"+ str(x) + """</b></div><div ID="ResultText">""""</div></div>"
                    else:
                        secondString = secondString +"""<div ID = "ResultsBox"><div ID="ResultTextMain"> """+ popUpText[counter] +"<b>"+ str(x) + """</b></div><div ID="ResultText">"""+  str(params.get(fields[popUpLoc[counter]], "")) + "</div></div>"

                if counter in resultsSelect:
                    if(counter ==2):
                        firstString = firstString + "for "
                    if(counter == 3):
                        firstString = firstString + """</div><div ID="ResultText">    Annual Salary: <b>£</b>"""
                    if(counter == 5):
                        firstString = firstString + """</div><div ID="ResultText">  Starting on: """

                    firstString= firstString + "<b>" + str(x) + "</b> "
                    if(counter == 5):
                        firstString= firstString + "</div>"
                if counter == 17:
                    if(pTotal > 0):
                        firstString = firstString + """<div ID="ResultP"> """ + str(int((100/pTotal) * x)) + "%</div> "
                counter+=1
            tempString = tempString + firstString + "</div></a>" + secondString + """</div></div></div>"""


        
        tempString = tempString + """</div></body>
        </html>"""
        return tempString





#set up for static content
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
          },
            '/static':{
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './public'
                }
        }
            
    cherrypy.quickstart(startScreen(), '/', conf)
