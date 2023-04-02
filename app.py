from flask import Flask, render_template, request, redirect
import meeter

app = Flask(__name__)

global person # current person

# welcome page
@app.route('/')
def index():
    return render_template('index.html')

# get user inputs
@app.route('/start/', methods=['POST', 'GET'])
def inputs():
    if request.method == 'POST':
        global person # current person
        person = meeter.Person(str(request.form['name_input']), str(request.form['phone_input']), str(request.form['degree_input']), request.form.getlist('interests_input')) # assign inputs
        meeter.people.append(person) # add to database
        return redirect('/matches/')
    else:
        return render_template('input.html')

# view matches
@app.route('/matches/')
def matches():
        global person # current person
        matches:list[meeter.Person] = []
        matches = person.matches.get_matches()
        if matches != []: return render_template('matches.html', matches=matches)
        else: return render_template('matches.html', notice='No matches yet!')

if __name__ == '__main__':
    app.run(debug=True)