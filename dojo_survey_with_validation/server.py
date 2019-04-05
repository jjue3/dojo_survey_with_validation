from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/') #Surver Page
def survey_form():
    location = ['San Jose', 'Seattle', 'Los Angeles', 'Chicago', 'Online']
    language = ['Python', 'JavaScript', 'C++', 'Java', 'C#']
    return render_template('index.html', location = location, language = language)

@app.route('/result', methods=['POST']) #Results Page
def survey_complete():
    print('THIS WORKS')
    is_valid = True 
    # data = {
    #         "name": request.form["name"],
    #         "location": request.form["location"],
    #         "language": request.form["language"],
    #         "comment": request.form["comment"]
    #         } 
    # mysql = connectToMySQL('survey')
    # query = "INSERT INTO survey.users (name, location, language, comment) VALUES ('test2', 'test2', 'test2', 'test2');"
    if len(request.form['name']) < 5:
        is_valid = False
        flash("Please enter your name")
        print('false')
        return redirect('/')
    if len(request.form['comment']) < 10:
        is_valid = False
        flash("Please enter a comment")
        print('false')
        return redirect('/')
    if is_valid:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        data = {
                "name": request.form["name"],
                "location": request.form["location"],
                "language": request.form["language"],
                "comment": request.form["comment"]
                }
        mysql = connectToMySQL('survey')         
        query = "INSERT INTO survey.users (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        successful = mysql.query_db(query, data)
        print(successful)
        return render_template('result.html', name=request.form['name'], comment=request.form['comment'], location=request.form['location'], language=request.form['language']) #render template for results page

if __name__ == "__main__":
    app.run(debug=True)    

