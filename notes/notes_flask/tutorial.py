from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #setting up what we're referencing, basically just the webpage. Establishing that it exists.

@app.route("/", methods=["POST", "GET"]) #Default homepages often just end with a backslash, tells the page that the thing below is the name of the page.
def home():
    if request.method == "POST": # url for our user function. "user" takes in a name 
        return redirect(url_for("user", name=request.form["name"])) #item in our form that has the class of name
    return render_template("index.html") # redirect tells the webpage to... go to a new webpage.

@app.route("/rain")
def rain():
    return "<h6>The rain is coming.</h6>"

@app.route("/<name>")
def user(name):
    return f"<p>Go away, {name}!!</p>"

if __name__ == "__main__": #checking to see if the code is being run on a file called main for it to work.
    app.run(debug=True) #running our app [webpage] and lets it refresh every time we make changes rather than us having to kill it and running it.

