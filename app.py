from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS
from person import Person

app = Flask(__name__)
CORS(app)
app.secret_key = "your_secret_key_here"  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get form values
            name = request.form.get("name")
            age = int(request.form.get("age"))
            height = float(request.form.get("height"))
            weight = float(request.form.get("weight"))
            sex = request.form.get("sex")

            # Create Person instance and calculate TMB
            person = Person(name, age, height, weight, sex)
            person.checks()
            tmb = round(person.evaluate())

            # Save values in session
            session["result"] = {"name": name, "tmb": tmb}

            # Redirect to the second route
            return redirect(url_for("tmb_info"))

        except ValueError as e:
            return render_template("index.html", error=str(e))
        except Exception as e:
            return render_template("index.html", error=f"Unexpected error: {e}")

    return render_template("index.html")


@app.route("/tmb")
def tmb_info():
    # Retrieve values from session
    result = session.get("result")
    if not result:
        return redirect(url_for("index"))  
    
    return render_template("result.html", result=result)


@app.route("/weight_goal", methods=["POST"])
def weight_goal():
    goal = request.form.get("goal")
    
    if goal == "maintain":
        return redirect(url_for("maintain_page")) # sets the url for maintain_page and then executes the maintain_page function
    elif goal == "lose":
        return redirect(url_for("lose_page")) # sets the url for lose_page and then executes the lose_page function
    elif goal == "gain":
        return redirect(url_for("gain_page")) # sets the url for gain_page and then executes the gain_page function
    else:
        return redirect(url_for("tmb_info")) 


@app.route("/maintain")
def maintain_page():
    result = session.get("result")
    if not result:
        return redirect(url_for("index"))
    return render_template("maintain.html", result=result)  # pass result to template

@app.route("/lose")
def lose_page():    
    result = session.get("result")
    if not result:
        return redirect(url_for("index"))
    return render_template("lose.html", result=result)  # pass result to template

@app.route("/gain")
def gain_page():
    result = session.get("result")
    if not result:
        return redirect(url_for("index"))
    return render_template("gain.html", result=result)  # pass result to template

app.route("/go_home")
def Home():    
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
