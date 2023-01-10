from flask import Flask
from mentorship import mentor,mentee


app = Flask(__name__)
app.register_blueprint(mentor)
app.register_blueprint(mentee)

@app.route('/')
def index():
    return "<body style=background-color:mediumseagreen;><h1>This is the index Page</h1></body>"


if __name__ =='__main__':
    app.run(debug=True)
