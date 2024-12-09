from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def saleslist_1():
    return render_template("saleslist.html") # templates folder for html and static for static and css
# chrome may cache css changes so changes are not instant
# to hard restart chrome you must shift + restart button
@app.route("/7-9") # if the user typed this url in instead
def sales_list_2():
    return render_template("saleslist2.html")
@app.route("/10-16")
def sales_list_3():
    return render_template("saleslist3.html")
@app.route("/dairy")
def dairy_list():
    return render_template("dairysaleslist.html")

if __name__ == "__main__":
    app.run(debug=True)