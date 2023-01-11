from flask import Flask, render_template, request, redirect
import meeter

app = Flask(__name__)

global person # current person

# get user inputs
@app.route("/", methods=["POST", "GET"])
def inputs():
    if request.method == "POST":
        global person # current person
        person = meeter.Person(request.form["name_input"], request.form["degree_input"], request.form.getlist('interests_input')) # assign inputs
        meeter.people.append(person) # add to database
        return redirect("/matches/")
    else:
        return render_template("input.html")

# view matches
@app.route("/matches/")
def troubleshooting():
        global person # current person
        return render_template("matches.html", first_match=person.matches.get_first(), second_match=person.matches.get_second(), third_match=person.matches.get_third())

if __name__ == '__main__':
    app.run(debug=True)