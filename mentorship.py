from flask import Blueprint
mentor = Blueprint('mentor',__name__,url_prefix='/mentor')
mentee = Blueprint('mentee',__name__,url_prefix='/mentee')

#Mentors routes
@mentor.route('/mentor-1')
def Mentor1():
    return "<body style=background-color:mediumseagreen;><h2>This is Mentor 1</h2></body>"

@mentor.route('/mentor-2')
def Mentor2():
    return "<body style=background-color:mediumseagreen;><h2>This is Mentor 2</h2></body>"

@mentor.route('/mentor-3')
def Mentor3():
    return "<body style=background-color:mediumseagreen;><h2>This is  Mentor 3</h2></body>"



#Mentees Routes
@mentee.route('/mentee-1')
def mentee1():
    return "<body style=background-color:mediumseagreen;><h2> This is Mentee 1</h2></body>"

@mentee.route('/mentee-2') 
def mentee2():
    return   "<body style=background-color:mediumseagreen;><h2 > This is Mentee 2</h2></body>"

@mentee.route('/mentee-3') 
def mentee3():
    return   "<body style=background-color:mediumseagreen;><h2> This is Mentee 3</h2></body>"

@mentee.route('/mentee-4') 
def mentee4():
    return   "<body style=background-color:mediumseagreen;><h2> This is Mentee 4</h2></body>"


#  Error 404   Route 
@mentee.app_errorhandler(404)
def error(err):
    return "<body style=background-color:black;><h1 style=color:red;text-align:center >Sorry  Page not found !! Please Search for a specific Mentee / Mentor ,we have mentee-1 to mentee-4  and mentor-1 to mentor-3</h1></body>",404
