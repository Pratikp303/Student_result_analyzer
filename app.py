
from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_grade(percentage):
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B+"
    elif percentage >= 60: return "B"
    elif percentage >= 50: return "C"
    else: return "F"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        name = request.form.get("name")
        roll_no = request.form.get("roll_no")
        marks = [int(request.form.get(f"sub{i}")) for i in range(1, 6)]
        
        total = sum(marks)
        perc = (total / 500) * 100
        status = "PASS" if all(m >= 35 for m in marks) and perc >= 35 else "FAIL"
        
        return render_template("results.html", 
                               name=name, roll_no=roll_no, 
                               total_marks=total, percentage=round(perc, 2),
                               highest_mark=max(marks), lowest_mark=min(marks),
                               grade=calculate_grade(perc), status=status)
    except:
        return "Please ensure all marks are valid numbers."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
